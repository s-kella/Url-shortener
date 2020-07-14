import requests
import os
import argparse
from dotenv import load_dotenv





def short_link (long_link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {'long_url': long_link}
    header = {'Authorization': token}
    response = requests.post(url, headers=header, json=body)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(bitlink, token) :
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    header = {'Authorization': token}
    response = requests.get(url, headers=header)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    token = os.getenv("BITLY_TOKEN")
    parser = argparse.ArgumentParser(description='Short link/ number of clicks')
    parser.add_argument('link', help='Your link')
    args = parser.parse_args()
    if args.link.startswith('bit.ly'):
        try:
            print('Number of clicks:', count_clicks(args.link, token))
        except requests.exceptions.HTTPError:
            print('You entered a wrong link')
    else:
        try:
            print('Your short link:', short_link(args.link, token))
        except requests.exceptions.HTTPError:
            print('You entered a wrong link')


if __name__ == '__main__':
    load_dotenv()
    main()




