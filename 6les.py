# try:
#     print("Hello")
# except:
#     print("We have problems")
# else:
#     print("no problems")
#
#
# try:
#     print("start code")
#     print("No errors")
# except NameError as error:
#     print(error)
# else:
#     print("I am ELSE")
# finally:
#     print("Finally code")
#
# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f"Sorry, we can't work with {type(var_1)},"
#                         f"we need class str")
#     else:
#         return print(var_1)
# first_var = "10"
# checker(first_var)
#
# import warnings
# warnings.warn("Warning, no code here", SyntaxWarning)

# import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always", ImportWarning)
#
# warnings.warn("Warning, no code here", SyntaxWarning)
# warnings.warn("Warning, module not import", ImportWarning)
# try:
#     a = int(input("Enter the number"))
#     d = int(input("Enter the number"))
#     print(a*d)
# except ValueError as error:
#     print("Only numbers")