import sys
import requests
from bs4 import BeautifulSoup


def main(songId):
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    html = requests.get(
        'https://www.melon.com/song/detail.htm?songId='+songId, headers={'User-Agent': USER_AGENT}).text
    soup = BeautifulSoup(html, 'html.parser')

    song_name_tag = soup.find(class_='song_name')

    title = song_name_tag.text.replace("곡명", "").strip()

    print(title)


if __name__ == "__main__":
    main(sys.argv[1])
