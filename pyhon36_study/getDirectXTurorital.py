import requests
from bs4 import BeautifulSoup as bs


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def main():
    url = 'http://www.rastertek.com/tutdx11.html'
    urlHeader = 'http://www.rastertek.com/'
    html = getHtmlText(url)
    soup = bs(html, 'html.parser')
    # 找到所有的url链接
    urls = []
    tags = soup.find_all('a')
    for tag in tags:
        urls.append(urlHeader + tag.attrs['href'])
    urls.remove('http://www.rastertek.com/tutindex.html')
    for url in urls:
        print(url)


def main1():
    baseUrl = 'http://www.rastertek.com/tutdx11.html'
    urlHeader = 'http://www.rastertek.com/'
    html = getHtmlText(baseUrl)
    soup = bs(html, 'html.parser')
    # 找到所有的url链接
    urls = []
    tables = soup.find_all('table')
    for table in tables:
        title = table.text.replace("\n", "")
        tds = table.find_all('td')
        url = tds[0].find('a').attrs['href']
        title = url.split('.')[0]
        url = urlHeader + tds[0].find('a').attrs['href']

        urls.append([title, url])

    for url in urls:
        html = getHtmlText(url[1])
        soup = bs(html, 'html.parser')
        body = soup.find('body')
        title = url[0] + ".txt"
        print(title)
        with open("D:/" + title, 'w') as f:
            f.write(body.text)

        f.close()


main1()
