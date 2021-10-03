import requests

from bs4 import BeautifulSoup


def crawler(url, find_key, all_url):
    true_urls = []

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    all_a_tag = soup.findAll('a')

    for sub_url in all_a_tag:
        page = requests.get(url + sub_url['href'])
        soup = BeautifulSoup(page.content, "html.parser")

        true_urls.append(url + sub_url['href'])

    return true_urls
