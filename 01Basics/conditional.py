# if elif else

# age = int(input("Enter age: "))

# cond: age >= 18 -> can vote
# can not vote

# if age >= 18:
#     print("You can vote")
# else:
#     print("You can not vote")


# color = input("Enter traffic color: ")

# if color == "green":
#     print("Move")
# elif color == "yellow":
#     print("Look")
# else:
#     print("Stop")

# Existing
# username: admin
# password: pass

# username = input("Username: ").lower()
# password = input("Password: ").lower()

# # Admin
# # Pass

# if (username == "admin" and password == "pass"):
#     print("User loggedin successfully")
# else:
#     print("Invlid credentials")


# Nested if else


# if username == "admin" and password == "pass":
#     print("User loggedin successfully")
# else:
#     # check whether username is incorrect or pass
#     if username != "admin":
#         print("Wrong username")
#     else:
#         print("wrong password")


color = input("Enter traffic color: ")

# if color == "green":
#     print("Move")
# elif color == "yellow":
#     print("Look")
# else:
#     print("Stop")

match color:
    case "green":
        print("Move")
    case "yellow":
        print("Look")
    case "red":
        print("stop")
    case _:
        print("Invalid color")
        
            
