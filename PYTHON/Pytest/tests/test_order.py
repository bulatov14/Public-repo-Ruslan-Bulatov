import pytest


@pytest.mark.run(order=3)

def test_method_1():
    print('Method_1')
@pytest.mark.run(order=2)
def test_method_2():
    print('Method_2')
@pytest.mark.run(order=1)
def test_method_3():
    print('Method_3')