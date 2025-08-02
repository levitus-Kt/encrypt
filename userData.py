from getpass import getpass

class User():
    def inputPasswd():
        """
        Ввод пароля
        """
        while True:
            passwd = getpass("Введите пароль: ")    #Символы не выводятся
            passwd_check = getpass("Повторите пароль: ")
            if passwd == passwd_check: 
                return passwd
            else:
                print("Пароли не совпадают\n")
        
    def inputLogin():
        """
        Ввод логина
        """
        login = input("Введите логин: ")
        while True:
            check = input(f"\nВаш логин {login}? (y/n) ")
            match check:
                case "n" | "N":
                    login = input("Введите логин: ")
                    continue
                case "y" | "Y":
                    break
                case _:
                    print("Ответьте y или n")
        return login
    
    def notifications(encrypt=None, decrypt=None, enterData=None):
        """
        Уведомление пользователя
        """
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
        
        if enterData: print("Вы подтвердили корректность данных. Данные приняты")

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
            