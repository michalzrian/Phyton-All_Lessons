import datetime
import logging


def decorator(my_func):
    def wrapper():
        print("khkjh")
        now = datetime.datetime.now()
        print(f"During func {now} ")
    return wrapper

@decorator
def my_func():
    now = datetime.datetime.now()
    print(f"time{now}")
my_func()

formater = logging.Formatter('%(asctimes)s - %(message)s')
logging.basicConfig(level=logging.DEBUG)
def logginDecorator(loggin):
    def wrapper():
        print("in loggin")
        logging.debug("this is debuger loggin")
    return wrapper
@logginDecorator
def loggin():
    print("loggin function")

loggin()
