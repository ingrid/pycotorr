import ConfigParser
import os

env_keys = []
this_mod = sys.modules[__name__]

for key in envkeys:
    setattr(this_module, key, os.environ.get(key, None))


def parse_config(file):
    parser = ConfigParser.ConfigParser()
    parser.read(file)
