#Generate symmetric key for AES
import os

def gen_key(size: int) -> str:
    return os.urandom(32).hex()

def __main__():
    print ("this is main func")