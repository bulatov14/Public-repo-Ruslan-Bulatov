import requests

class Test_new_joke():
    """Create new joke"""

    def __init__(self):
        pass

    def test_create_new_random_categories_joke(self):
        """Create random joke in sport"""

        category = 'sport'
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
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
        check_info = check.get('categories')
        print(check_info)
        assert check_info == ['sport']
        print("Category is right")
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck'
        # if name in check_info_value:
        #     print('value has word Chuck')
        # else:
        #     print('valeu has no word Chuck')



sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()