import requests

class Test_new_location():
    """Work with new location"""

    def test_create_new_location(self):
        """Create new location"""

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'                         # parameter for all requests
        post_resource = '/maps/api/place/add/json'      # resource post method

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print('Status code is ' + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print('New location is created')
        else:
            print('Status code is Wrong')

new_place = Test_new_location()
new_place.test_create_new_location()