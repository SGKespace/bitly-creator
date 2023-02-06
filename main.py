import requests
import os
from dotenv import load_dotenv
import argparse
from urllib.parse import urlparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='?')
    return parser


def main():
    url = create_parser().parse_args().url
    if not url:
        url = input('Введите ссылку: ')
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]

    try:
        if is_bitlink(token, url):
            number_clicks = count_clicks(token, url)
            print(f"По вашей ссылке было {number_clicks} перехода(ов)")
        else:
            short_link = shorten_link(token, url)
            print(short_link)
    except requests.exceptions.HTTPError:
        print('Вы ввели неправильную ссылку или неверный токен.')
    except requests.exceptions.ConnectionError:
        print('ConnectionError: Не могу подключиться к серверу.')


def is_bitlink(token, url):
    headers = {'Authorization': token}
    url_parse = urlparse(url)
    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url_parse.netloc}{url_parse.path}"
    response = requests.get(request_url, headers=headers)
    return response.ok


def count_clicks(token, url):
    headers = {'Authorization': token}
    params = (('unit', 'day'), ('units', '-1'),)
    url_parse = urlparse(url)
    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url_parse.netloc}{url_parse.path}/clicks/summary"
    response = requests.get(request_url, headers=headers, params=params)
    return response.json()['total_clicks']
    

def shorten_link(token, url):
    headers = {'Authorization': token}
    request_body = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=request_body)
    response.raise_for_status()
    return response.json()['link']
       

if __name__ == '__main__':
    main()