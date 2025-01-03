import random
import string

# comment
def funky_method():

    funky_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    print(f"Here's your funky string: {funky_string}")

funky_method()