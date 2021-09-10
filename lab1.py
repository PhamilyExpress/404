import requests
r = requests.get('https://raw.githubusercontent.com/PhamilyExpress/404/master/lab1.py')
print(r.text)