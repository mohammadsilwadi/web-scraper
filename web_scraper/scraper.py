import requests
from bs4 import BeautifulSoup
import json
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
def get_citations_needed_count(url):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    return len(result)
def get_citations_needed_report(url):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('sup', class_= 'noprint Inline-Template Template-Fact')
    string = ""
    for citation in result:
        string+= f'Citation needed for "{citation.parent.text}"'
    return string

if __name__ =='__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))