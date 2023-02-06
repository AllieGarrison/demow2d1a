#
# # DEFINE THE FUNCTION
# def do_it():
#     print("Done")
#
#
# # call the function by name
# do_it()
#
#
# def hello(username):
#     print(f"Hello {username}.")
#
#     # + CONCATENATE OPERATOR
#     print("Hello " + username + ".")
#
#     print("Hello", username, ".")
#
#     # old-school ??
#     print("Hello %s." % username)
#
#
# hello("Class")
#

# def get_greeting(username="World"):
#     return f"Hello {username}."
#
#
# g = get_greeting("World")
# print(g)
# print(g)
#
# DRY Don't Repeat Yourself

"""
THIS MULTIPLIES TWO NUMBERS A AND B
"""
# def multiply(a=12, b=12):
#     return a * b
#
#
# r = multiply(6, 7)
# print(r)
# print(r)
#
# r2 = multiply(16, 17)
# print(r2)
# print(r2)
#
# r3 = multiply()  # 144?
# print(r3)
# print(r3)
#

# SCOPE
# x = 123
#
#
# def show_it():
#     global x
#     y = 456
#     print(x)
#
#
# show_it()

# print(y)

# NAMES PARAMETERS
# def pizza(cheese=True, meat=True):
#     print(cheese, meat)
#
#
# pizza(meat=False)
#


# def add_many(*numbers): # one star for read only list
#     # numbers[0] = 11 # WONT WORK AS ITS READ ONLY
#     print(sum(numbers))
#
#
# add_many(10, 20, 30, 20, 30, 20, 30, 20, 30)
#
# def f(**kwargs):  # Two stars for writable dict of key words
#     kwargs["extra"] = "bob"
#     print(kwargs)
#
#
# f(k1="v1", k2="v2")

# ALTERNATE WITHOUT **KWARGS
# def f(kwargs):  # Two stars for writable dict of key words
#     kwargs["extra"] = "bob"
#     print(kwargs)
#
#
# f({"k1":"v1", "k2":"v2"})
#RECURSION
# def call_me(n):
#     print(n)
#     if(n < 1000):
#         return call_me(n+10)
#     return n
#
# print(call_me(1))

# def power(x):
#     return x * x

# data = [2, 3, 4, 5]
# result = map(lambda x: x * x, data)
# # result = map(power, data)
# print(list(result))

# from functools import reduce
#
# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print(result)
#
# data = [
#     {"username": "Kevin", "age": 55},
#     {"username": "Bob", "age": 15},
#     {"username": "Carol", "age": 22},
# ]
# data2 = sorted(data, key=lambda o: o["age"])
# print(data2)

# power = lambda x: x * x


def power(x):
    return x * x


print(power(3))
