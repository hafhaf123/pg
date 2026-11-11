
import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Stáhne stránku a najde všechny odkazy.
    """

    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        text = response.text

        hrefs = re.findall(r'href="(.*?)"', text)

    else:
        print("Chyba při stahování stránky")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]

        odkazy = download_url_and_get_all_hrefs(url)

        for odkaz in odkazy:
            print(odkaz)

    except Exception as e:
        print("Program skončil chybou:", e)
