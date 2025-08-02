import pytest
from main import keySize, encryptData, decryptData, main


@pytest.mark.parametrize("choice, expected_result", [
    (1, None),
    (2, None),
    (3, None),
    (4, None),
    ("a", None),
    ("adgadg", None),
    ("1", None),
    ("2", None),
    ("3", None),
    ("4", None),
])
def test_main(capsys, monkeypatch, choice, expected_result):
    monkeypatch.setattr('builtins.input', lambda _: expected_result)
    i = input("Номер ответа")
    assert i == expected_result


@pytest.mark.parametrize("key_size, expected_result", [
    (1, None),
    (2, None),
    (3, None),
    (4, None),
    ("a", None),
    ("adgadg", None),
    ("1", None),
    ("2", None),
    ("3", None),
    ("4", None),
])
def test_keySize(monkeypatch, key_size, expected_result):
    monkeypatch.setattr('builtins.input', lambda _: expected_result)
    i = input("Введите номер варианта")
    assert i == expected_result


@pytest.mark.parametrize("key_size, login, passwd, expected_result", [
    (16, 'jfjfjfjfjffjfj', '123456789', None),
    (24, 'homiho', "123", None),
    (1, 'hom', "1", 1),
])
def test_encryptData(key_size, login, passwd, expected_result):
    assert encryptData(key_size, login, passwd) == expected_result


def test_decryptData():
    assert decryptData() == None
