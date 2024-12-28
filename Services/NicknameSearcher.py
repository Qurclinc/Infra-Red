import requests
from Src.Websites import Websites
from bs4 import BeautifulSoup

class NicknameSearcher:

    def __init__(self):
        self.SearchList = Websites
        self.response_codes = ["vk", "github"]

    def do_search(self, nickname):
        for service, line in self.SearchList.items():
            url = line.format(nickname)
            response = requests.get(url)
            if self.check_profile(service, response, nickname):
                print(f"[+] {url}")

    def check_profile(self, service, response, nickname):
        if service in self.response_codes:
            if response.status_code == 200:
                return True
        elif service == "telegram":
            return True if response.text.count("tgme_page_extra") else False