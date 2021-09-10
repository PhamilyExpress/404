import requests

print(requests.__version__)
print(requests.get('https://www.google.com/'))

r = requests.get('https://raw.githubusercontent.com/PhamilyExpress/404/master/lab1.py')
print(r.text)