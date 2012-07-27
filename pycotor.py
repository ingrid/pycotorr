import hashlib
import sys

from bencode import bencode, bdecode

import requests

from util import extract_meta_data

def run_pycotor():
    pass

torrent = decode(TEST_FILE)
info_hash = sha.new(bencode(torrent['info']))
payload = {'info_hash':torrent['info'],
           'peer_id':'-TR2610-dfhmjb0skee6',
           'port':'6881',
           'uploaded':'0',
           'downloaded':'0',
           'key':'2c4dec5f',
           'left':'0',
           'compact':'0',
           'no_peer_id':'0',
           'event':'started'}

if __name__ == '__main__':
    run_pycotor()
