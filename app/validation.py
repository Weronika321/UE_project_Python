from const import username, user_password

def validate(login, password):
    return login == username and password == user_password
