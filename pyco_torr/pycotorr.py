import hashlib
import sys
import socket
import struct

from bencode import bencode, bdecode

import requests

from util import extract_meta_data, get_dict_hash

def run_pycotor():
    pass

class Client(object):
    def __init__(self):
        # Bind to tracker here?
        self.active_torrents = []

    def start_file(self, file):
        torr = Torrent(file)
        self.active_torrents.append(torr)

class Torrent(object):
    # A wrapper for both the torrenting session for a single file and the file metadata.
    def __init__(self, file):
        self.meta_data = extract_meta_data(file)
        info_hash = get_dict_hash(file)
        payload = {'info_hash': info_hash,
                   'peer_id':'-TR2610-dfhmjb0skee6',
                   'port':'6881',
                   'uploaded':'0',
                   'downloaded':'0',
                   'key':'2c4dec5f',
                   'left':'0',
                   'no_peer_id':'0',
                   'event':'started',
                   'numwant':'80'}

        response = requests.get(self.meta_data['announce'], params=payload)
        response = bdecode(response.content)

        peers = response['peers']
        print "RESPONSE: ", response
        peer_list = []
        try: # Try parsing in binary format first
            while peers:
                addr = socket.inet_ntoa(peers[:4])
                port = struct.unpack('!H', peers[4:6])[0]
                peer_list.append((addr, port))
                peers = peers[6:]
        except: # Now try parsing in dictionary format
            print "Bad list!"
            print "LIST: ", peers

        print "PEER LIST: ", peer_list
        self.peer_list = peer_list

if __name__ == '__main__':
    run_pycotor()
