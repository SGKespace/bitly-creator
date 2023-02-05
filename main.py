import requests
import os
from dotenv import load_dotenv
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='?', default="https://google.com", type=str)
    return parser.parse_args()

def main():

    # url = input('Введите ссылку: ')
    url = createParser().url
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]

    if is_bitlink (token, url):
        try:
            number_clicks = count_clicks(token, url)
            print(f"По вашей ссылке было {number_clicks} перехода(ов)")
        except requests.exceptions.HTTPError:
            print('Что то пошло не так' )
    else:
        try:
            short_link = shorten_link(token, url)
            print(short_link)
        except requests.exceptions.HTTPError:
            print('Что то пошло не так')
        

def is_bitlink (token, url):
    headers = {'Authorization': token}
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url.replace('http://', '').replace('https://', '')}", headers=headers)
    return response.ok


def count_clicks(token, url):
    headers = {'Authorization': token}
    params = (('unit', 'day'), ('units', '-1'),)
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url.replace('http://', '').replace('https://', '')}/clicks/summary",headers=headers, params=params)
    return response.json()['total_clicks']
    

def shorten_link(token, url):
    headers = {'Authorization': token}
    request_body = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=request_body)
    response.raise_for_status()
    return response.json()['link']
       

if __name__ == '__main__':
    main()