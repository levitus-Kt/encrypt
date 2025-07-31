from getpass import getpass

class User():
    def inputPasswd():
        passwd = getpass("Введите пароль: ")    #Символы не выводятся
        passwd_check = getpass("Повторите пароль: ")
        if passwd == passwd_check: 
            return passwd
        else:
            print("Пароли не совпадают")
            return 1
    
    def notifications(encrypt=None, decrypt=None):
        if encrypt: 
            print("Данные зашифрованы")
        elif encrypt == None:
            pass
        else:
            print("Не удалось зашифровать данные. Попробуйте еще раз")

        if decrypt: 
            print("Данные успешно расшифрованы")
        elif decrypt == None:
            pass
        else:
            print("Не удалось расшифровать данные. Попробуйте еще раз")

    def outEncrypt(encrypt_login, encrypt_passwd):
        print(f"Зашифрованный логин: {encrypt_login}")
        print(f"Зашифрованный пароль: {encrypt_passwd}")

    def outDecrypt(decrypt_login, decrypt_passwd):
        print(f"Расшифрованный логин: {decrypt_login}")
        print(f"Расшифрованный пароль: {decrypt_passwd}")

    def check_decrypt(login, passwd, decrypt_login, decrypt_passwd):
        if login == decrypt_login and passwd == decrypt_passwd:
            print("Расшифровка данных прошла успешна. Данные не изменены")
        else:
            print("При расшифровке даные могли быть изменены. Проверьте их")
            