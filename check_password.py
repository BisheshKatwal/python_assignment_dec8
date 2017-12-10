def read_password():
    return input('Please input the password: ')
    """Asking the user for password"""

def check_password(pw):
    """ Function to check password"""
    if (pw == password):
        print('welcome password match')

    else:
        print('Wrong password')

"""Global variable """
password="bishesh"
pw= read_password()
check_password(pw)