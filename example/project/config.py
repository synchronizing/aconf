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
