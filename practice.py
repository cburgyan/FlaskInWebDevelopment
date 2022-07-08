import time

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculate(foo_func, n1, n2):
    return foo_func(n1, n2)

print(calculate(multiply, 3, 9))


#Functions can be nested in other functions
def outer_function():
    print("outer function")
    def nested_func():
        print('nested func')

    nested_func()

outer_function()

#Functions can return other functions
def outer_function2():
    print("outer function")
    def nested_func():
        print('nested func')

    return nested_func

bob = outer_function2()
print("howdy")
bob()


#Python Decorator Function
def decorator_func_foo(funcky_foo):
    def wrapper_func():
        funcky_foo()
    return wrapper_func


def say_hello():
    print("Hello")

def say_bye():
    print("Bye.")

def say_greeting():
    print('How are you? ')

def delay_function(funky):
    def wrapper_func():
        #Do something before running the function
        time.sleep(2)
        funky()
        #And/or do something after running the function
    return wrapper_func
time.sleep(1)
say_hello()
delayed_hello = delay_function(say_hello)
delayed_hello()

time.sleep(1)
say_bye()
delayed_bye = delay_function(say_bye)
delayed_bye()

time.sleep(1)
say_greeting()
delayed_greeting = delay_function(say_greeting)
delayed_greeting()

print('*************')


#'@delay_function' is syntactic sugar to 'delay_function(say_weather)()'
# with no '@delay_function' above the function definition
@delay_function
def say_weather():
    print("The weather looks nice.")


print("does the weather look good?")
say_weather()


#'@delay_function' is syntactic sugar to 'delay_function(say_fine)()'
# with no '@delay_function' above the function definition
@delay_function
def say_fine():
    print('I feel fine.')


time.sleep(1)
print('How do you feel? ')
say_fine()

time.sleep(1)
print("hello, again!")
delay_function(say_hello)()

time.sleep(1)
print('How are you doing, again?')
delay_function(say_fine)()


def my_name_is(name):
    print(f'hi, I am {name}')


def print_input(funcky, *args):
    def wrapper_func():
        print(args[0])
        funcky(args[0])
    return wrapper_func


time.sleep(1)
print_input(my_name_is, 'bob')()
time.sleep(1)


# Create the logging_decorator() function
def logging_decorator(function):
    def wrapper_function(*argies):
        print(f'You called {function.__name__}{argies}')
        print(f'It returned: {function(*argies)}')
    return wrapper_function


# Use the decorator
@logging_decorator
def a_function(a, b, c):
    return a + b + c


time.sleep(1)
a_function(1, 2, 3)
time.sleep(1)

print('before class User')

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


print("at User:")
useful_user = User('Zareck')
print(type(useful_user))
print(useful_user)
create_blog_post(useful_user)
print("First Attempt:")
create_blog_post(useful_user)
print("********")
print("Second Attempt")
useful_user.is_logged_in = True
create_blog_post(useful_user)
