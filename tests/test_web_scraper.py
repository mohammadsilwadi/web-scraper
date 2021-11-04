from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count , get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_count():
    domain ='https://en.wikipedia.org'
    History_of_Mexico_url = f'{domain}/wiki/History_of_Mexico'
    excepted = 5
    actual = get_citations_needed_count(History_of_Mexico_url)
    assert excepted == actual
    
    
def test_report():
    domain ='https://en.wikipedia.org'
    History_of_Mexico_url = f'{domain}/wiki/History_of_Mexico'
    excepted = get_citations_needed_report(History_of_Mexico_url)
    assert 'The Spanish had no intention to turn over Tenochtitlan to the Tlaxcalteca.' in excepted
