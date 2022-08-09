from sklearn.preprocessing import MinMaxScaler
from email.message import EmailMessage
from keras.models import load_model
import yfinance as yf
import numpy as np
import smtplib
import time


model = load_model('ES_stock_model.h5')


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
    data = yf.download(tickers='ES=F', period='300d', interval='1d')
    data1 = yf.download(tickers='^VIX', period='300d', interval='1d')
    date = list(data.index)
    date1 = list(data1.index)
    choice_es = []
    for i in date:
        if i in date1:
            choice_es.append(True)
        else:
            choice_es.append(False)
    data['choice'] = choice_es
    es_data = data.loc[data['choice'] == True]
    new_es_date = list(es_data.index)
    choice_vix = []
    for i in date1:
        if i in new_es_date:
            choice_vix.append(True)
        else:
            choice_vix.append(False)
    data1['choice'] = choice_vix
    vix_data = data1.loc[data1['choice'] == True]

    k = vix_data['Open'].tolist()
    l1 = vix_data['High'].tolist()
    l2 = vix_data['Low'].tolist()
    l3 = vix_data['Close'].tolist()

    es_data['es_open'] = k
    es_data['es_high'] = l1
    es_data['es_low'] = l2
    es_data['es_close'] = l3
    a = list(es_data.index)
    day_of_the_week = []
    month = []
    day = []
    for i in a:
        i = str(i).split('-')
        dow = week_day(int(i[0]), int(i[1]), int(str(i[2]).split(' ')[0]))
        day_of_the_week.append(dow)
        month.append(int(i[1]))
        day.append(int(str(i[2]).split(' ')[0]))
    es_data['DoW'] = day_of_the_week
    es_data['month'] = month
    es_data['day'] = day
    dataset = es_data.loc[:, ['Open', 'High', 'Low', 'Close',
                              'Volume', 'es_open', 'es_high', 'es_low',
                              'es_close', 'DoW', 'month', 'day']]
    dataset.to_csv('live_data.csv')
    dataframe = dataset.tail(200)

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


def pattern():
    data = yf.download(tickers='ES=F', period='200d', interval='1d')
    data1 = yf.download(tickers='^VIX', period='100d', interval='1d')
    date = list(data.index)
    high = data['High'].tolist()
    low = data['Low'].tolist()
    highest = max(high)
    lowest = min(low)
    index_highest = high.index(highest)
    index_lowest = low.index(lowest)
    date_time_for_highest = str(date[index_highest])
    date_time_for_lowest = str(date[index_lowest])
    time_highest = date_time_for_highest.split(' ')[1]
    date_highest = date_time_for_highest.split(' ')[0]
    time_lowest = date_time_for_lowest.split(' ')[1]
    # date_lowest = date_time_for_lowest.split(' ')[0]
    max_high = round(highest, 2)
    max_high_date = date_highest
    max_high_time = time_highest
    min_low = round(lowest, 2)
    # min_low_date = date_lowest
    min_low_time = time_lowest
    return f'The maximum high ({max_high}) of  {max_high_date} happened at {max_high_time} and the minimum low ' \
           f'({min_low}) happened at {min_low_time}'

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
    send_email(pattern(), 'Pattern Alert')
    while True:
        send_email(alert(), 'Price Alert')
        time.sleep(3600)
        break


print(alert())
