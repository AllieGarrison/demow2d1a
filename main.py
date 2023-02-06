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


# def power(x):
#     return x * x
#
#
# print(power(3))

"""
Online shopping is a form of electronic commerce which allows consumers to directly buy goods or services from
 a seller over the Internet using a web browser or a mobile app. Consumers find a product of interest by visiting
  the website of the retailer directly or by searching among alternative vendors using a shopping search engine, 
  which displays the same product's availability and pricing at different e-retailers. As of 2020, customers can 
  shop online using a range of different computers and devices, including desktop computers, laptops, tablet 
  computers and smartphones.

An online shop evokes the physical analogy of buying products or services at a regular "bricks-and-mortar"
 retailer or shopping center; the process is called business-to-consumer (B2C) online shopping. When an online 
 store is set up to enable businesses to buy from another businesses, the process is called business-to-business
  (B2B) online shopping. A typical online store enables the customer to browse the firm's range of products and 
  services, view photos or images of the products, along with information about the product specifications, 
  features and prices.

Online stores usually enable shoppers to use "search" features to find specific models, brands or items.
 Online customers must have access to the Internet and a valid method of payment in order to complete a 
 transaction, such as a credit card, an Interac-enabled debit card, or a service such as PayPal. For physical
  products (e.g., paperback books or clothes), the e-tailer ships the products to the customer; for digital 
  products, such as digital audio files of songs or software, the e-tailer usually sends the file to the 
  customer over the Internet. The largest of these online retailing corporations are Alibaba, Amazon.com, 
  and eBay.[1] 
  
  NOUN (Person place or thing): Service, Customer, Product, Cart, Items
  VERBS (Action word like Run): Find, Buy("AddToCart")
  ADJECTIVE (Color, Shape  Size): Model, Brand, Price
"""


class Customer:
    def __init__(self, name, number, order_history=[]):
        self.name = name
        self.number

    def get_lifetime_value(self):
        # return sum or all orders in history
        return 0


class Product:
    def __init__(self, name, price, **props):
        self.name = name
        self.price = price
        self.props = props  # size color


class Store:
    def __init__(self, name, products=[], customers=[], transactions=[], id=0):
        pass


class Transaction:
    def __init__(self, product={name:"", price:0}, quantity=1, id=0):
        pass


class Cart:
    def __init__(self, transactions=[], paymentMethod="VISA", card_number="", id=0):
        pass

    def total(self):
        pass

    def get_number_of_products(self):
        pass


if __name__ == "__main__":
    s = Store("Amzone");
    c = Customer("Bob")
    products = [
        Product("pencil", 1.00),
        Product("paper", 2.00)
    ]
    
    order = Cart()
    
    print(order.receipt()) # all customer info + all line items + total
    
    