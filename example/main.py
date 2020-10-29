from project.config import Config
from project.functionality import Example

# Random function to demonstrate we can pass _anything_ to 'make_config' inside 'Config'.
def uppercase(words):
    return words.upper()

# We create our custom configuration without saving it.
Config(arg="hello world", func=uppercase)

# We initialize our Example object without passing the 'Config' object to it.
example = Example()
print(example.arg) 
# >>> "HELLO WORLD"
