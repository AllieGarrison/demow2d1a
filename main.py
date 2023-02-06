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

def multiply(a=12, b=12):
    return a * b


r = multiply(6, 7)
print(r)
print(r)

r2 = multiply(16, 17)
print(r2)
print(r2)

r3 = multiply()  # 144?
print(r3)
print(r3)
