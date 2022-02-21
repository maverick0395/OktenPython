# First task

def decor(func):
    def wrapper():
        func()
        wrapper.counter += 1
        print('count: ', wrapper.counter)

    wrapper.counter = 0
    return wrapper

@decor
def myfunc1():
    print('My func1')

@decor
def myfunc2():
    print('My func2')

myfunc1()
myfunc1()
myfunc1()
myfunc2()
myfunc1()


# Second task

def make_decorator():
    def decorator(func):
        def wrapper():
            func()
            decorator.counter += 1
            print('count: ', decorator.counter)
        return wrapper
    decorator.counter = 0
    return decorator

decor2 = make_decorator()

@decor2
def func3():
    print('this is func3')

@decor2
def func4():
    print('This is func 4')

func3()
func3()
func3()
func4()
func3()