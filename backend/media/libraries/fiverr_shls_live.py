from sklearn.preprocessing import MinMaxScaler
from email.message import EmailMessage
from keras.models import load_model
import yfinance as yf
import numpy as np
import smtplib
import time


model = load_model('shls_model.h5')


def week_day(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return int(dayOfWeek)


def alert():
    data = yf.download(tickers='SHLS', period='30d', interval='1d')
    date = list(data.index)
    day_of_the_week = []
    month = []
    day = []
    for i in date:
        i = str(i).split('-')
        dow = week_day(int(i[0]), int(i[1]), int(str(i[2]).split(' ')[0]))
        day_of_the_week.append(dow)
        month.append(int(i[1]))
        day.append(int(str(i[2]).split(' ')[0]))
    data['DoW'] = day_of_the_week
    data['month'] = month
    data['day'] = day
    dataset = data.loc[:, ['Open', 'High', 'Low', 'Close', 'Volume', 'DoW', 'month', 'day']]
    dataframe = dataset.tail(10)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataframe)
    x_test = [scaled_data[:, :]]
    x_test = np.array(x_test)
    predict = model.predict(x_test)
    prediction = scaler.inverse_transform(predict)
    open_price = round(float(prediction[:, 0]), 2)
    high = round(float(prediction[:, 1]), 2)
    low = round(float(prediction[:, 2]), 2)
    close = round(float(prediction[:, 3]), 2)
    message = f'Open: {open_price}\nHigh: {high}\nLow: {low}\nClose: {close}'

    """
    df_close_list = data['Close'].tolist()

    df_old_close = round(df_close_list[-2], 2)
    df_new_close = round(df_close_list[-1], 2)
    difference = round((df_new_close - df_old_close), 2)

    if difference < 0:
        return (f'The Close price of ES has fallen from {df_old_close} to '
                f'{df_new_close} with the difference of {difference}.')
    elif difference > 0:
        return (f'The Close price of ES has risen from {df_old_close} to '
                f'{df_new_close} with the difference of {difference}.')
    else:
        return f'Price is stable at old: {df_old_close}\nnew: {df_new_close}'
    """
    return message


def send_email(message, subject, sender, sender_password, receiver):
    try:
        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("seawajdavid@gmail.com", "15micheald")
        server.send_message(msg)
        server.quit()
        print('successful')
    except:
        print('not successful')


def main():
    while True:
        send_email(alert(), 'Price Alert')
        time.sleep(3600)
        break


print(alert())
