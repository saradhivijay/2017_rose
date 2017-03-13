# # This is a print statement, single line comments
# print("It is working!")
#
# """
# This is for multi line comments
# """
#
# # variable definition
# # variable convention:
# #   - lower case
# student_no = 123332
# temperature = 37.2
# # X Temp = 123128
# studentGroup = "A"
# # x 1231AVC = "acd"
# # python is CASE VERY SENSITIVE
# print(student_no)

def greeting(): #function definition
    print("Hello, how are you?")

def data_types():
    student_name = "John" #string
    student_id = "12321312" #string
    student_names = [student_name, "Alice", "Jenny"] #list, a collection of data
    print(student_names[2])
    student_info = {"Alice": "1233212"} # a record of dictionary, key is Alice, value is 1233212
    print(student_info["Alice"])
    print(student_name.upper())
    x = 100
    print(x + 100)

def maths_operation(x, y):
    print("addition -> ", x + y)
    print("minus -> ", x - y)
    product = x * y
    print("product -> ", product)
    print("divide -> ", x / y)
    print("int divide ->", x // y)
    print("modulo -> ", x % y)
    print("power -> ", x ** y)

#greeting() # function calling
#data_types()
maths_operation(3, 2)