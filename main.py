# ---------------------------------------------------------------
# decoratorlar

# def test_decoration(func):
#     print("Nimadir ish qilinadi")
#     return func
#
# @test_decoration
# def say_hello(name):
#     return f"Assalomu alaykum {name}"
#
# print(say_hello("Murodjon"))


# ---------------------------------------------------------------

# def test_decoration(func):
#     def wrapper():
#         print("Nimadir ish qilinadi")
#         print(func())
#         print("Yana nimadir qilinadi")
#     return wrapper
#
# def say_hello():
#     return f"Assalomu alaykum"
#
# hello = test_decoration(say_hello)
#
# hello()

# ---------------------------------------------------------------

# def test_decoration(func):
#     def wrapper(*args, **kwargs):
#         print("Nimadir ish qilinadi")
#         print(func(*args, **kwargs))
#         print("Yana nimadir qilinadi")
#     return wrapper
#
# @test_decoration
# def say_hello(name):
#     return f"Assalomu alaykum {name}"
#
#
# say_hello("Murodjon")

# ---------------------------------------------------------------
# import time
#
# def calculate(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         print(f"{time.time() - start} vaqt ketdi!")
#         return res
#     return wrapper
#
#
# @calculate
# def multiplay(x, y):
#     for i in range(5000000000000):
#         pass
#     return x * y
#
# # print(multiplay(4, 5))
#
#
# @calculate
# def start():
#     users = []
#     while True:
#         username = input("Username: ")
#         if username == 'stop':
#             break
#         users.append(username)
#     return users
#
# print(start())


# ---------------------------------------------------------------
# git va github

# print("Hello World")
#
# for i in range(5):
#     print("Hello World")