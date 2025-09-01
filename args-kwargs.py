# Args -> hanya positional argumen

def say_name(*args):
    name1, name2, name3 = args # destructure dari tuple
    print(f"Say Hello to {name3}")

say_name("Jamil", "Moe", "Miell") 

# Kwargs = Keyword Arguments -> gampangnya ada Key ada Value beda dengan args
"""
The *args parameter allows a function to accept any
number of keywords arguments:
"""

def filter_products(**kwargs):
    # category = kwargs["Font"]
    category = kwargs.get("category", "All")
    print(f"result : {category}")

filter_products(category="Font")

