from getpass import getpass

class User():
    def inputPasswd():
        passwd = getpass("Введите пароль: ")    #Символы не выводятся
        return passwd
    
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

    def check_decrypt(login, passwd, decrypt_login, decrypt_passwd):
        if login == decrypt_login and passwd == decrypt_passwd:
            print("Расшифровка данных прошла успешна. Данные не изменены")
        else:
            print("При расшифровке даные могли быть изменены. Проверьте их")
            