# def shout(text):
#     return text.upper()


# print(shout("Hello"))
# yell=shout
# print(yell("Hello"))

# def whisper(text):
#     return text.lower()


# def greet(func):
#     greeting=func("Hello world!")
#     print(greeting)


# greet(shout)
# greet(whisper)


def create_adder(x):
    def adder(y):
        return x+y

    return adder


add_15=create_adder(15)
print(add_15(10))


def func1(name):
    return f"Hello{name}"


def func2(name):
    return f"{name}, how're you doing ?"


def func3(func4):
    return func4("dear learner")

print(func3(func1))
print(func3(func2))




