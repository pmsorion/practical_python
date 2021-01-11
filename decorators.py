PASSWORD = '12345abcde'


def password_require(func):
    def wrapper():
        password = input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('Password is incorect')

    return wrapper

@password_require
def needs_password():
    print('The password is correct:')



def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return 'Hello, {}'.format(name)





if __name__ == '__main__':
    print(say_my_name('Frank'))
    #needs_password()