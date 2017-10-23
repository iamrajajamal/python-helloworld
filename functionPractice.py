# Arguments

def my_function():
    print("this is function")
    print("second print")

my_function()



def my_function_param(str1,str2):
    print("By Argument")
    print(str1)
    print(str2)

my_function_param("First Argument","Second Argument")

# Default Arguments

def print_str_int(name = "Anyone" ,age = "Unknown"):
    print("By Default Argument")
    print( "My Name is " + name + " and my age is " + str(age))
    # seperate them with comma
    print("My Name is",name,"and my age is",age)

print_str_int("Jamal")

# Keyword Arguments

def print_str_int(name = "Anyone" ,age = "Unknown"):
    print ("By Keyword Argument")
    print( "My Name is " + name + " and my age is " + str(age))
    # seperate them with comma
    print("My Name is",name,"and my age is",age)

print_str_int(age=24, name="Jamal")


# Infinite Arguments

def print_people(*people):
    print("Infinte Argument")
    for person in people:
        print("This person is", person)

print_people("Jamal","Ali","Murtaza","Mustafa","Zulfeqar")