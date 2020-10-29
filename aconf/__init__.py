import fs, pickle, namedtupled

mem = fs.open_fs("mem://")

def make_config(**kwargs):
    mem.writebytes("config.pkl", pickle.dumps(kwargs))

conf = lambda: namedtupled.map(pickle.loads(mem.readbytes("config.pkl")))
config = lambda: pickle.loads(mem.readbytes("config.pkl"))
