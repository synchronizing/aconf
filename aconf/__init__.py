__version__ = "1.0.1"
import namedtupled

def make_config(**kwargs):
    globals()["aconf"] = kwargs

conf = lambda: namedtupled.map(globals()["aconf"])
config = lambda: globals()["aconf"]
