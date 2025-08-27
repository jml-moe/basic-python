# function -> reusable unit of code

# Function to say hello - Simple function without parameters that prints a greeting
def say_hello():
    print("hello")

say_hello()

# Function to display student name and age - Demonstrates basic parameter usage
def name_student(name, age):
    print(f"my name is {name} my age is {age}")

name_student("jamil", 20)
name_student(age=21, name="jamil") #positional argumen

# Function to greet with optional hobbies parameter - Shows optional parameter with default value
def greeting(name, hobbies = None): # kalau argumen sifatnya opsional pastikan ada fallback value
    print(f"hello my name is {name}, and my hobbies are {hobbies}")

greeting("Jamil")

# Function to calculate math grade average - Returns a value instead of just printing
def mtk_grade(sem1, sem2):
    return(sem1 + sem2)  
result = mtk_grade(80, 90)

print(result)
print("------------------------------")

# *args and **kwargs

# *args (Arbitrary Arguments) -> bentuknya tuple biasanya digunakan dalam sebuah function yang jumlah dari inputnya tidak tertentu, biasanya buat looping

# *args memungkinkan function menerima jumlah parameter yang tidak terbatas. Parameter disimpan sebagai tuple.

def sum(*args):
    print(args)

sum(1,2,3,4,5)

# **kwargs (Keyword Arguments) -> dict -> biasanya dlm SDK AI yg biasanya ada extra value yg tidak menentu

#**kwargs memungkinkan function menerima jumlah parameter bernama yang tidak terbatas. Parameter disimpan sebagai dictionary.

def my_fn(model="GPT-4.1", **kwargs):
    additional_config = kwargs.get("additional_config", None)
    if additional_config:
        print(f"using additional config: {additional_config}")

# With additional_config parameter
my_fn(additional_config="high performance")  # Prints: using additional config: high performance

# fleksibel function
def default(arg, default_arg = None, *args, **kwargs):
    pass

# 1. Accepting arg
# 1. Accepting arg, default arg
# 1. Accepting *args (tuple) 
# 1. Accepting **kwargs (dict)

def configure_database(**config):
    default_config = {
        "username": "postgres", 
        "database": "postgres" 
    }
    
    default_config.update(config)
    return default_config

result = configure_database(password="postgress")
print(result)