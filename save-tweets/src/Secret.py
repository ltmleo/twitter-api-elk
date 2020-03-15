
import os, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class Crypt:
    def __init__(self):
        self.password = os.environ["PASSWORD"].encode()
        salt =  b'L]\x94\xd6\x99\xd2\xe7z\x94\x16\xbf\x9e;\xa8\x83\xce'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(self.password))

    def encrypt(self, message):
        message = message.encode()
        f = Fernet(self.key)
        return f.encrypt(message)

    def decrypt(self, encrypted):
        encrypted = encrypted.encode()
        f = Fernet(self.key)
        decrypted = f.decrypt(encrypted)
        return decrypted.decode("utf-8")

#TO GENERATE A NEW SECRET
# 1 - Export de variable PASSWORD;
# 2 - Execute this:
#x = Crypt()
#a = x.encrypt("INSERT THE TOKEN HERE")
