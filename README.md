# 🤖 Auto Config

Memory-based global configuration for Python projects -- in 10 lines of code (including empty lines). Made with the intention of ridding the need to pass `Config` objects everywhere. Option to use [`namedtupled`](https://namedtupled.readthedocs.io/en/latest/) if wanted.

## Installing

```
pip install aconf
```

## Why?

Honestly? Because why not. Was tired of having to pass `Config` objects left and right in small personal projects, so created this.

## Using

This module comes with three main functions:

* `make_config(**kwargs)`: Creates the configuration in memory.
* `config()`: Loads configuration from memory as standard dictionary.
* `conf()`: Loads configuration from memory as namedtuple object for cleaner access.

```python
from aconf import make_config, config, conf

# Creates a global configuration that can be accessed by any other portion of the runtime.
make_config(database={"user": "admin", "password": "db_password", "host": "localhost", "port": "3306"}, method="GET")

# Accessing the global configuration as a dictionary.
print(config()['database']['user'])
# >>> admin

# Accessing the global configuration as a namedtuple object.
print(conf().database.user)
# >>> admin
```

A single file example doesn't encapsulate the usefulness of this module. Instead, imagine the following project:

```
.
├── project
│   ├── __init__.py
│   ├── config.py
│   └── functionality.py
└── main.py
```

### `config.py`

```python
""" 'Config' class to hold our desired configuration parameters. 

Note:
    This is technically not needed. We do this so that the user knows what he/she should pass 
    as a config for the specific project. Note how we also take in a function object - this is
    to demonstrate that one can have absolutely any type in the global config and is not subjected
    to any limitations.
"""

from aconf import make_config

class Config:
    def __init__(self, arg, func):
        make_config(arg=arg, func=func)
```

### `functionality.py`

```python
""" Use of the global configuration through the `conf` function. """

from aconf import conf

class Example:
    def __init__(self):
        func = conf().func
        arg = conf().arg

        self.arg = func(arg)
```

### `main.py`

```python
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
```

# Performance

Absolutely no idea. I wrote this for small projects that I don't intend on releasing and so I have not bothered to benchmark it. If anyone runs the number it would be lovely if you reported either as an Issue, or directly by shooting a pull request with this portion of the `README.md` updated. The project in essence does the following:

* `make_config(**kwargs)`: Pickles the `kwargs` dictionary and saves it to memory.
* `config()`: Loads the pickled dictionary from memory.
* `conf()`: Loads the pickled dictionary from memory and transforms it into `namedtuple`.

It would be reasonable to assume `conf()` performance is slower than `config()`. If I had to assume the largest performance drop is within the dumping and loading of pickled objects (even if from memory).

# Project

This is the entirety of the project, which is inside `__init__.py`. Uses [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple):

```python
import namedtupled

def make_config(**kwargs):
    globals()["aconf"] = kwargs

conf = lambda: namedtupled.map(globals()["aconf"])
config = lambda: globals()["aconf"]
```
