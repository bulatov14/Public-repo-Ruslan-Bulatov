import requests

class Test_new_joke():
    """Create new joke"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):      # create method
        """Create random joke"""

        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print('Status code: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success')
        else:
            print('Fail')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get('categories')
        # print(check_info)
        # assert check_info == []
        # print("Category is right")
        check_info_value = check.get('value')
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('value has word Chuck')
        else:
            print('valeu has no word Chuck')


random_joke = Test_new_joke()       # переменная, является экземпляром класса Test_new_joke()
random_joke.test_create_new_random_joke()       # вызов метода test_create_new_random_joke()