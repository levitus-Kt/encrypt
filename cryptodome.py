from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
import random, string


class Cipher():
    def generate(key_size):
        """
        Генерация ключей, соли и вектора инициализации (iv)
        """
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(key_size))
        iterations = 10000
        salt = Random.new().read(key_size)
        iv = Random.new().read(AES.block_size)
        derived_key = PBKDF2(key, salt, key_size, iterations)
        return derived_key, iv
    
    def encrypt(login, passwd, derived_key, iv):
        """
        Шифрование логина пароля алгоритмом AES
        """
        encrypt_AES = AES.new(derived_key, AES.MODE_CBC, iv)
        encrypt_login = encrypt_AES.encrypt(pad(login.encode("utf8"), AES.block_size))
        encrypt_passwd = encrypt_AES.encrypt(pad(passwd.encode("utf8"), AES.block_size))

        return encrypt_login, encrypt_passwd
        

    def decrypt(encrypt_login, encrypt_passwd, derived_key, iv):
        """
        Расшифрока логина пароля алгоритмом AES
        """
        decrypt_AES = AES.new(derived_key, AES.MODE_CBC, iv)
        decrypt_login = unpad(decrypt_AES.decrypt(encrypt_login), AES.block_size).strip().decode()
        decrypt_passwd = unpad(decrypt_AES.decrypt(encrypt_passwd), AES.block_size).strip().decode()

        return decrypt_login, decrypt_passwd