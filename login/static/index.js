function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    var passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

    if (password !== confirmPassword) {
        alert("Passwords do not match");
        return false;
    }

    if (!passwordPattern.test(password)) {
        alert("Password must be at least 8 characters long and include letters, numbers, and symbols");
        return false;
    }

    return true;
}