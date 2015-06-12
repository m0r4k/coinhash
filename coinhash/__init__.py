import hashlib
import neoscrypt
import skeinhash
import qubit_hash
import groestlcoin_hash
import darkcoin_hash
import ltc_scrypt

def SHA256Hash(x):
    return hashlib.sha256(x).digest()

def SHA256dHash(x):
    return hashlib.sha256(hashlib.sha256(x).digest()).digest()

def NeoscryptHash(x):
    return neoscrypt.getPoWHash(x)

def SkeinHash(x):
    return skeinhash.getPoWHash(x)

def QubitHash(x):
    return qubit_hash.getPoWHash(x)

def GroestlHash(x):
    return groestlcoin_hash.getHash(x, len(x))

def X11Hash(x):
    return darkcoin_hash.getPoWHash(x)

def ScryptHash(x):
    return ltc_scrypt.getPoWHash(x)
