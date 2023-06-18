import pytest

@pytest.fixture()
def set_up():
    print('Setup is successful')   # fixture - действие ДО - действия будут выполнены ДО того как мы запустим каждый наш модуль
def test_sending_mail_1():
    print('Letter is sent')     # input 'pytest -s -v' in the terminal

def test_sending_mail_2():
    print('Letter is sent')
