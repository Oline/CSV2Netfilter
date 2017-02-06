'''This module is used to get hashes sums from different hash functions'''

import hashlib
from functools import partial

###########################################################################
def sha1sum(filename):
    '''Calculate the sha1 value of a file's content.'''
    with open(filename, mode='rb') as file_desc:
        hsha1 = hashlib.sha1()
        for buf in iter(partial(file_desc.read, 128), b''):
            hsha1.update(buf)
    file_desc.close()
    return hsha1.hexdigest()

###########################################################################
def sha256sum(filename):
    '''Calculate the sha256 value of a file's content.'''
    with open(filename, mode='rb') as file_desc:
        hsha256 = hashlib.sha256()
        for buf in iter(partial(file_desc.read, 128), b''):
            hsha256.update(buf)
    file_desc.close()
    return hsha256.hexdigest()

###########################################################################

if __name__ == "__main__":
    sha1sum("rules.csv")
