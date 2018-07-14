from bs4 import BeautifulSoup
def get_view(response):
    soup = BeautifulSoup(response.text, 'lxml')
    viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    return viewState