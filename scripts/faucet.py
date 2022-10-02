#!/usr/bin/env python
import argparse
import requests
import sys
# import time


def send_request(proxy):
    proxies = {
        "http": "http://"+proxy,
        "https": "http://"+proxy,
    }

    # username = "202210021334586276"
    # password = "73597761"
    # proxies = {
    #     "http": "http://%(user)s:%(pwd)s@%(proxy)s" % {"user": username, "pwd": password, "proxy": proxy},
    #     "https": "http://%(user)s:%(pwd)s@%(proxy)s" % {"user": username, "pwd": password, "proxy": proxy}
    # }

    requests.packages.urllib3.disable_warnings()
    num = 9
    success = 0
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
            success += 1
            # time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(proxy, e)
            break
    return success


def parse_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main(args=None):
    proxy_content = open("proxy_list.txt", "r")
    proxy_list = [line.rstrip() for line in proxy_content.readlines()]
    total_success = 0
    for proxy in proxy_list:
        total_success += send_request(proxy)
    print("Total success:", total_success)


if __name__ == '__main__':
    sys.exit(main(parse_args()))
