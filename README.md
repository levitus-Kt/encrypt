### Консольное Python-приложение для шифрования и дешифрования логина и пароля с использованием алгоритма AES и ключа, заданного пользователем.

## Возможности

Шифрование логина и пароля алгоритмом AES (режим CBC)

Ключ длиной 16, 24 или 32 байта (на выбор)

Генерация соли, IV и ключа из строки

Безопасный ввод пароля (не отображается в терминале)

Проверка корректности расшифровки

Если данные после расшифровки не совпадают — пользователь об этом узнаёт

## Использование

Необходим python 3.10 (или выше) и библиотека pycryptodome

`pip3 install pycryptodome`

или

`pip3 install -r requirements.txt`

После установки запустите файл main.py

`python3 main.py`

Следуйте инструкциям в терминале:

1. Выберите длину ключа

2. Введите логин

3. Введите пароль (ввод скрыт)

# Примеры

<img width="671" height="295" alt="image" src="https://github.com/user-attachments/assets/65dc9216-e11c-4ae9-ae52-5f6672a06df0" />

<img width="502" height="179" alt="image" src="https://github.com/user-attachments/assets/c5350fe6-f54c-4bd7-be0b-9783a5662424" />

<img width="582" height="180" alt="image" src="https://github.com/user-attachments/assets/b79f9671-4977-47d0-a499-19e23ed4a33f" />
