import argparse
import requests
import sys
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url", required=True)
parser.add_argument("-p", "--payloads", help="payload list", required=True)
args = parser.parse_args()


def fuzz(url, payloads):
    for payload in open(payloads, "r").readlines():
        new_url = url.replace(f'{fuzz}', payloads)
        request = requests.get(new_url)
        if request.elapsed.total_seconds() > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout detected with ", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not work with this payload: ", payload)


def verif(url):
    url_test = url.replace(f"{fuzz}", "")
    req = requests.get(url_test)
    if req.elapsed.total_seconds() > 6:
        sys.exit(Style.BRIGHT + Fore.RED + "Please make sure you have a good connection")
    else:
        fuzz(args.url, args.payloads)


if not f'{fuzz}' in args.url:
    sys.exit(Style.BRIGHT + Fore.RED + f"Missing {fuzz} parameter!")
else:
    verif(args.url)
