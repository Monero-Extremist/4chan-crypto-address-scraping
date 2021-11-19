import re
import json
import requests
from bs4 import BeautifulSoup



class addyRip:
    def __init__(self):
        self.crypto_regex_match = {
                "btc": "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
                "xmr": "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
                "eth": "^0x[a-fA-F0-9]{40}$",
                "dash": "^X[1-9A-HJ-NP-Za-km-z]{33}$",
                "xrp": "^r[0-9a-zA-Z]{24,34}$",
                "doge": "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
                "ada": "^D[A-NP-Za-km-z1-9]{35,}$",
                "lite": "^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$",
                "tron": "^T[a-zA-Z0-9]{33}$",
                "nano": "^(xrb|nano)_([' + 13456789abcdefghijkmnopqrstuwxyz + ']{60})$",
                # "dot": "^[1-9A-HJ-NP-Za-km-z]*$"
            }

    def matchAddress(self,_string):
        for k, v in self.crypto_regex_match.items():
            # print(type(v))
            if bool(re.search(v, _string)):
                return str(k)
    def extractFromText(self,_text):
        if _text == None:
            return None
        text = _text.split()
        matches = []
        for x in text:
            # print(self.matchAddress(x))
            if self.matchAddress(x) == None:
                continue
            else:
                type = self.matchAddress(x)
                addy = x
                match = {
                "type": type,
                "address": addy,
                "blockchainData": self.getBalance(addy,type)
                }
                # match = f'{x} {self.matchAddress(x)}'
                matches.append(match)
        return matches
    def getBalance(self,_addy,_type):
        # return "test"
        if _type == "btc":
            balance = self.getBtcBalance(_addy)
        elif _type   == "eth":
            balance = "n/a"
        else:
            balance = "n/a"
        return balance
    def getBtcBalance(self,_addy):
        # All bitcoin values are in Satoshi i.e. divide by 100000000 to get the amount in BTC
        # url = f"https://blockchain.info/q/addressbalance/{_addy}"
        url = f"https://blockchain.info/balance?active={_addy}"
        # print(url)
        answer = json.loads(requests.get(url).text)
        if 'error' in answer:
            balance = "Error"
        else:
            balance = answer[_addy]
        return balance







class chanRIP:
    def __init__(self):
        self.url = ""
        self.soup = ""
    def getSoup(self):
        r = requests.get(self.url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup
    def ripThreads(self,_url):
        self.url = _url
        self.soup = self.getSoup()
        posts = self.soup.findAll(True, {'class':['post', 'reply']})
        return posts
    def ripArchiveLinks(self):
        hostname = "https://boards.4channel.org"
        url = f"{hostname}/biz/archive"
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        table = soup.find(True,{"id":"arc-list"})
        a = table.findAll(True,{"class":"quotelink"})
        links = []
        for x in a:
            link = x['href']
            link = f"{hostname}{link}"
            links.append(link)
        return links

class redditRip:
    def __init__(self):
        self.url = ""
        self.soup = ""
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    def getSoup(self):
        r = requests.get(self.url,headers=self.headers)
        if r.status_code != 200:
            print(f"error code {r.status_code}")
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup
    def ripThreads(self,_url):
        self.url = _url
        self.soup = self.getSoup()
        replies = self.soup.findAll(True,{"class":["usertext-body", "may-blank-within","md-container"]})
        return replies
    def ripArchiveLinks(self):
        hostname = "https://boards.4channel.org"
        url = f"{hostname}/biz/archive"
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        table = soup.find(True,{"id":"arc-list"})
        a = table.findAll(True,{"class":"quotelink"})
        links = []
        for x in a:
            link = x['href']
            link = f"{hostname}{link}"
            links.append(link)
        return links
