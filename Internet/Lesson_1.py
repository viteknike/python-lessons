import requests, bs4

url = 'https://market.yandex.ru/catalog--mobilnye-telefony/34512430/list?hid=91491&rs=eJwz4v7EyMHBIMGg8PgUq9MaRi5pLjYORglGBUYBNinOlNS0xNKcknhDBQYNBiMGLkOwpKwChwC7lFBuYkpZfHFGak5avHF8QWJ6qpHCxguNjBpn159iNGLnAFECTFzaYC1cClxALTxIWowUDn9pYdT4ClH8FVkxrwILmmJjha6tTYwab78tAikGUQJMAkxeHEYpiWmWBkkGQUaG5sYmFpZGJgbmZhZG-qYWaeZGZoYmqeZGSYmpqRbmpmmmiamGKakGRpYGZgYG-ob6hgCokkE_'
r = requests.get(url)
r.encoding = 'utf-8'

b = bs4.BeautifulSoup(r.text, 'html.parser')

spantitles = b.select('div.m4M-1 span')
spanprices = b.select('span._3tooO span.ds-text_headline-5_bold')
titles = []
prices = []
titlePrices = {}

for span in spantitles:
    titles.append(span.text)
for span in spanprices:
    prices.append(span.text.replace('\u2009', ''))

for name, price in zip(titles, prices):
        titlePrices[name] = price.replace('\u2009', '')

print(titlePrices)