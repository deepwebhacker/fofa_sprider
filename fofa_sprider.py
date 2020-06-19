import requests
import re
import base64
import urllib.parse
import warnings
from config import headers
import time


def waf():
    print("          _____                    _____                    _____           ")
    print("         /\    \                  /\    \                  /\    \          ")
    print("        /::\____\                /::\    \                /::\    \         ")
    print("       /:::/    /               /::::\    \              /::::\    \        ")
    print("      /:::/   _/___            /::::::\    \            /::::::\    \       ")
    print("     /:::/   /\    \          /:::/\:::\    \          /:::/\:::\    \      ")
    print("    /:::/   /::\____\        /:::/__\:::\    \        /:::/__\:::\    \     ")
    print("   /:::/   /:::/    /       /::::\   \:::\    \      /::::\   \:::\    \    ")
    print("  /:::/   /:::/   _/___    /::::::\   \:::\    \    /::::::\   \:::\    \   ")
    print(" /:::/___/:::/   /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  ")
    print("|:::|   /:::/   /::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\ ")
    print("|:::|__/:::/   /:::/    /\::/    \:::\  /:::/    /\::/    \:::\   \::/    / ")
    print(" \:::\/:::/   /:::/    /  \/____/ \:::\/:::/    /  \/____/ \:::\   \/____/  ")
    print("  \::::::/   /:::/    /            \::::::/    /            \:::\    \      ")
    print("   \::::/___/:::/    /              \::::/    /              \:::\____\     ")
    print("    \:::\__/:::/    /               /:::/    /                \::/    /        ")
    print("     \::::::::/    /               /:::/    /                  \/____/         ")
    print("      \::::::/    /               /:::/    /                                   ")
    print("       \::::/    /               /:::/    /                                    ")
    print("        \::/____/                \::/    /                                     ")
    print("         --                       \/____/                                      ")
    print("                                                                               ")
    print("                                                             --WAF 2.1         ")


headers = headers
warnings.filterwarnings("ignore")


def fofa1_request(url, headers):
    with open("fofa.txt", 'a+') as f:
        res = requests.get(url=url, headers=headers).text.encode('utf-8').decode('unicode_escape')
        time.sleep(4)
        res1 = re.compile('<a target="_blank" href="(https://|http://)(.*?)"', re.S)
        res2 = res1.findall(res)
        for i in res2:
            if "gov" not in i:
                f.write((i[0] + i[1]) + "\n")
                f.flush()
            else:
                pass
        f.close()


def page_numbers(pagenumbers1, pagenumbers2, arg):
    for i in range(int(pagenumbers1), int(pagenumbers2) + 1):
        url = "https://fofa.so/result?q=" + str(s) + "&page=" + str(i) + "&qbase64=" + str(arg)
        fofa1_request(url, headers)
        print("第{0}页以成功爬取完".format(i))


if __name__ == "__main__":
    waf()
    pagenumbers1 = input("请输入抓取起始页：")
    pagenumbers2 = input("请输入抓取结尾页：")
    f = input("请输入关键词：").encode('utf-8')
    print("等待吧，心急吃不了热豆腐....")
    arg = str(base64.b64encode(f), "utf-8").replace('+', '%2B')
    s = urllib.parse.quote(f)
    page_numbers(pagenumbers1, pagenumbers2, arg)
    print("抓取成功")
