import requests

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