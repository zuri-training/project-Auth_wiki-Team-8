// Register form validation
document.getElementById("registerForm").addEventListener("submit", (e) => {
    e.preventDefault();
    let firstName = document.getElementById("firstName").value;
    let lastName = document.getElementById("lastName").value;
    let email = document.getElementById("email").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;
    if (
        firstName == "" ||
        lastName == "" ||
        email == "" ||
        password == "" ||
        confirmPassword == ""
    ) {
        alert("Please fill all the fields");
    } else if (password != confirmPassword) {
        alert("Password and confirm password does not match");
    } else {
        const data = {
            firstname: firstName,
            lastname: lastName,
            email: email,
            username: username,
            password: password,
        };
        // console.log(data);
        axios
            .post("http://127.0.0.1:8000/account/signup/", data)
            .then((response) => {
                console.log(response);
                const addedUser = response.data;
                console.log(`POST: user is added`, addedUser);
            })
            .catch((error) => {
                let err = JSON.parse(error.request.response);
                console.log(err.errors[0]);
            });
    }
});