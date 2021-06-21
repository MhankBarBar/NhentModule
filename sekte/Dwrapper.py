#!/usr/bin/python3
import re
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests
from io import BytesIO
from PIL import Image
class ChapterNotFound(Exception):
    pass
class mangaObject:
    def __init__(self, json) -> None:
        self.json     = json
        self.chapters = json["chapter"][::-1]
        self.sinopsis = json["sinopsis"]
        self.author   = json["author"]
        self.status   = json["status"]
        self.genre    = json["genre"]
        self.released = json["released"]
        self.title    = json["title"]
        self.url      = json["url"]
        self.bytes    = BytesIO()

    def getLink(self, url):
        self.parse = BeautifulSoup(requests.get(url).text, 'html.parser')
        return [_.get('src').replace('https://cdn.statically.io/img/sekte/','https://') for _ in self.parse.find('div', id='readerarea').findAll('img')[1:]]

    # chapter: Integer
    def download(self, chapter, workers=5):
        assert isinstance(chapter, int)
        assert isinstance(workers, int)
        if self.bytes.getbuffer().tobytes():
            return self.bytes
        else:
            with ThreadPoolExecutor(max_workers=workers) as thread:
                result = []
                for i in self.getLink(self.chapters[chapter - 1]):
                    result.append(Image.open(BytesIO(thread.submit(requests.get, i).result().content)).convert("RGB"))
            result[0].save(fp=self.bytes,format='pdf', save_all=True, append_images=result[1:])
            return self.bytes

    def save_to_file(self, fn):
        assert isinstance(fn, str)
        if not self.bytes.getbuffer().tobytes():
            raise ChapterNotFound("Call download function first!")
        open(f"{fn}{'' if fn[-4:].lower() == '.pdf' else '.pdf'}", 'wb').write(self.bytes.getbuffer().tobytes())

    def __repr__(self):
        return f"<[{self.title}]>"

    def __str__(self) -> str:
        return self.__repr__()

class Search:
    def __init__(self, query) -> None:
        self.query = query
        self.req = requests.get("https://sektekomik.com/", params={"s": self.query}).text
        self.all_fetch = []

    @property
    def fetch(self):
        if self.all_fetch:
            return self.all_fetch
        title = re.findall("title=\"(.*?)\"", self.req)[3:][:-2]
        link = re.findall("<div class=\"bsx\"> <a href=\"(.*?)\"", self.req)
        thumb = [_.img['src'] for _ in BeautifulSoup(self.req, 'html.parser').findAll('div', class_='bs')]
        chapters = [_.replace('Chapter ','') for _ in re.findall("<div class=\"epxs\">(.*?)</div>", self.req)]
        for i in enumerate(thumb):
            self.all_fetch.append(Sekte(link[i[0]], i[1], title[i[0]], int(chapters[i[0]])))
        return self.all_fetch

    def __str__(self) -> str:
        return f"<[count {self.fetch.__len__()}]>"

    def __repr__(self) -> str:
        return self.__str__()


class Sekte:
    def __init__(self, link, thumb=None, title=None, chapters=None) -> None:
        self.link = link
        self.thumb  = thumb
        self.title  = title
        self.chapters = chapters

    def __str__(self) -> str:
        return self.title.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    # chapt: Integer
    @property
    def manga(self):
        try:
            self.html = requests.get(self.link)
            parsing = BeautifulSoup(self.html.text, 'html.parser')
            komik = [_.a.get('href') for _ in parsing.find('div', id='chapterlist').findAll('div', class_='eph-num')]
            return mangaObject(
                {
                    'title': re.findall("title=\"(.*?)\"", self.html.text)[3:][:-2][0],
                    'chapter': komik,
                    'url': self.html.url,
                    'sinopsis': parsing.find('div', attrs={'itemprop': 'description'}).text,
                    'genre': [_.text for _ in parsing.find('div', class_='bigcontent').findAll('a', rel='tags')],
                    'status': re.search('Status <i>(.*?)</i>', self.html.text).group(1),
                    'released': parsing.find('div', class_='fmed').span.text.strip(),
                    'author': parsing.find('div', class_='fmed').nextSibling.span.text.strip()
                }
            )
        except IndexError:
            raise ChapterNotFound("Error")
