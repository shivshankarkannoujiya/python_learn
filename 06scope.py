"""
L → Local
E → Enclosing
G → Global
B → Built-in
"""


# def test():
#     x = 30  # local variable
#     print(x)

# test() #30

# x = 100

# def show():
#     print(x)

# show() # 100
# print(x)  # NameError: name 'x' is not defined


x = 100

def change():
    global x
    x = 200
    print(x)

# change()
# print(x)




