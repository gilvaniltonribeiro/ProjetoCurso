from urllib.error import URLError
import urllib.request

try:
    site = urllib.request.urlopen('https://www.twitch.tv/directory')
except urllib.error.URLError:
    print('Não foi possivel acessar o site :(')
else:
    print('O site esta acessivel :)')
    print(site.read())
