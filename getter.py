import requests

data = requests.get('https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv').content
data = data[data.index(b'\n') + 1:]

with open('dump.csv', 'w') as f:
    f.write(data.decode('windows-1251'))
