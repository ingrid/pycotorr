# Utility methods!
from bencode import bencode, bdecode
import hashlib

def extract_meta_data(file):
    meta_data = bdecode(open(file, 'rb').read())
    return meta_data

def get_dict_hash(file):
    contents = open(file, 'rb').read()
    start = contents.index('4:info') + 6
    end = -1
    dictliteral = contents[start:end]
    dictsha = hashlib.sha1(dictliteral)
    return dictsha.digest()

        

