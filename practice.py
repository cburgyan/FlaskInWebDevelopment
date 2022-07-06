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

@delay_function #this is syntactic sugar
def say_weather():
    print("The weather looks nice.")

print("does the weather look good?")
say_weather()

@delay_function
def say_fine():
    print('I feel fine.')

time.sleep(1)
print('How do you feel? ')
say_fine()
