#!/usr/bin/env python
import argparse
import requests
import sys

def send_request(proxy):
    proxies = {
        "http": "http://"+proxy,
        "https": "http://"+proxy,
    }

    requests.packages.urllib3.disable_warnings()
    num = 9
    for _ in range(num):
        try:
            response = requests.post(
                url="https://faucet.testnet.aptoslabs.com/mint?address=0x4b5ec05f912473401eda3b15a3412191a646584da2ce1707388330add593d57d&amount=10000000000000000",
                proxies=proxies,
                verify=False
            )
            if response.status_code != 200:
                break
            print(response.status_code, response.content)
        except requests.exceptions.RequestException as e:
            print(proxy, e)
            break


def parse_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args

def main(args=None):
    proxy_content = open("proxy_list.txt", "r")
    proxy_list = [line.rstrip() for line in proxy_content.readlines()]
    for proxy in proxy_list:
        send_request(proxy)

if __name__ == '__main__':
    sys.exit(main(parse_args()))
