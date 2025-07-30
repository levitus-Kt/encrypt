from cryptodome import Cipher
from userData import User


def main():
    """
    Спрашиваем у пользователя желаемую длину ключа и логин и пароль
    """
    print("Выберите длину ключа:")
    print(" 1. 16")
    print(" 2. 24")
    print(" 3. 32")
    
    #Проверка на корректность ввода
    try:
        key_size = int(input("Введите номер варианта: "))
    except:
        print("Допускаются только цифры. Введите номер варианта")
        exit()

    if not 0 < key_size < 4: print("Нет такого варианта"); exit()

    #Установление длины ключа в зависимости от выбора пользователем
    match key_size:
        case 1: key_size = 16
        case 2: key_size = 24
        case 3: key_size = 32

    login = input("Введите логин: ")
    passwd = User.inputPasswd()

    derived_key, iv = Cipher.generate(key_size)

    try:
        encrypt_login, encrypt_passwd = Cipher.encrypt(login, passwd, derived_key, iv)
        User.notifications(encrypt=True)
    except:
        User.notifications(encrypt=False)
        exit()

    try:
        decrypt_login, decrypt_passwd = Cipher.decrypt(login, passwd, encrypt_login, encrypt_passwd, derived_key, iv)
        User.notifications(decrypt=True)
    except:
        User.notifications(decrypt=False)
        exit()

    User.check_decrypt(login, passwd, decrypt_login, decrypt_passwd)

    return decrypt_login, decrypt_passwd

    
if __name__ == "__main__":
    main()