from cryptodome import Cipher
from userData import User


def keySize():
    """
    Спрашиваем у пользователя желаемую длину ключа и логин и пароль
    """
    while True:
        print("Выберите длину ключа:")
        print(" 1. 16")
        print(" 2. 24")
        print(" 3. 32")
        
        #Проверка на корректность ввода
        try:
            key_size = int(input("Введите номер варианта: "))
            if 0 < key_size < 4: 
                break
            else:
                print("Нет такого варианта")
        except:
            print("Допускаются только цифры. Введите номер варианта")
            
    #Установление длины ключа в зависимости от выбора пользователем
    match key_size:
        case 1: key_size = 16
        case 2: key_size = 24
        case 3: key_size = 32

    #Ввод логина и пароля пользователем и их проверка на корректность
    login = User.inputLogin()
    passwd = User.inputPasswd()

    User.notifications(enterData=True)
    
    encryptData(key_size, login, passwd)

def encryptData(key_size, login, passwd):
    """
    Шифруем данные
    """
    derived_key, iv = Cipher.generate(key_size)

    try:
        encrypt_login, encrypt_passwd = Cipher.encrypt(login, passwd, derived_key, iv)
        User.notifications(encrypt=True)
        User.outEncrypt(encrypt_login, encrypt_passwd)
    except:
        User.notifications(encrypt=False)
        return 1
    
    data = [encrypt_login, encrypt_passwd, derived_key, iv]
    with open("file.cpd", "wb") as file:
        for line in data:
            file.write(line + b'\n')

    return

def decryptData():
    """
    Получаем шифрованные данные и декодируем их
    """
    try:
        with open("file.cpd", "rb") as file:
            lines = file.readlines()
            encrypt_login, encrypt_passwd, derived_key, iv = lines
    except FileNotFoundError:
        print("Файл не найден")
        
    try:
        decrypt_login, decrypt_passwd = Cipher.decrypt(encrypt_login[:-1], encrypt_passwd[:-1], derived_key[:-1], iv[:-1])
        User.notifications(decrypt=True)
        User.outDecrypt(decrypt_login, decrypt_passwd)
    except:
        User.notifications(decrypt=False)
        return 1

    User.check_decrypt(encrypt_login, encrypt_passwd, decrypt_login, decrypt_passwd)

    return

def main():
    while True:
        print("\nЧто вы хотите сделать?")
        print(" 1. Зашифровать данные\n 2. Расшифровать зашифрованные данные\n 3. Выйти")
        choice = input("Номер ответа: ")

        match choice:
            case '1': return keySize()
            case '2': return decryptData()
            case '3': exit()
            case _: print("Нет такого варианта")
    
if __name__ == "__main__":
    main()