import urllib.request

adres = "http://google.com"


header_kodlari = {
    'User_Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

}

html = urllib.request.urlopen(adres)
print(html.read())