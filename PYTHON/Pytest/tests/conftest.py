import pytest

@pytest.fixture()
def set_up():
    print('Setup is successful')

@pytest.fixture(scope='module')
def some():
    print('Start')