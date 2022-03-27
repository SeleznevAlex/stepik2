import requests

url = f'http://numbersapi.com'
with open('dataset_24476_3.txt', 'r') as file:
    numbers = file.readlines()
    for number in numbers:
        url_num = url + '/' + number.strip() + '/math'
        params = {'json': True}
        res = requests.get(url_num, params)
        if res.status_code == 200:
            num_json = res.json()
            if num_json['found']:
                print('Interesting')
            else:
                print('Boring')
