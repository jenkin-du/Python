import requests
from bs4 import BeautifulSoup as bs
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'urf-8'
        return r.text
    except:
        return ""


def fillUnivList(uList, html):
    soup = bs(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            uList.append([tds[0].string, tds[1].string, tds[2].string])
    pass


def printUnivList(uList, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t"
    print(tplt.format("排名", "学校名称", "省份", chr(12288)))
    for i in range(num):
        u = uList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
