""" Use of the global configuration through the `conf` function. """

from aconf import conf

class Example:
    def __init__(self):
        func = conf().func
        arg = conf().arg

        self.arg = func(arg)
