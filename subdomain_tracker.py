import requests
import urllib3
import time
import sys


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", type=str, required=True, help='Target domain')
    return parser.parse_args()


def banner():
    print(
        ''' 
                                                   | |            
           ___ _ __  _   _ _ __ ___   ___ _ __ __ _| |_ ___  _ __ 
          / _ \ '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __/ _ \| '__|
         |  __/ | | | |_| | | | | | |  __/ | | (_| | || (_) | |   
          \___|_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__\___/|_|   
                                                          
    ''')
    print('Name: subdomainTracker')
    print('Author: @paktiko1986')
    time.sleep(3)


def parsing_url(url):
    try:
        alamat = urllib3.util.url.parse_url(url)
    except Exception as e:
        print('[-] Alamat website salah, silakan coba lagi...!!!')
        sys.exit(1)
    return alamat


def main():
    banner()
    subdomains = []

    args = parse_args()
    target = parsing_url(args.domain)

    req = requests.get(f"https://crt.sh/?q={target}&output=json")

    if req.status_code != 200:
        print('[!] Informasi tidak tersedia!')
        sys.exit(1)

    for (key, value) in enumerate(req.json()):
        subdomains.append(value['name_value'])

    print(f"[*] Subdomain: {target} ditemukan!!!!")
    subs = sorted(set(subdomains))

    for s in subs:
        print(f"{s}")

    print("\nPencarian sudah selesai, semua subdomain sudah ditemukan berdasarkan informasi dari crt.sh!")


if __name__ == '__main__':
    main()
