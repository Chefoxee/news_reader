from item import Item
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


class Feed:

    def get_updates(self) -> list[Item]:
        pass


class RssFeed(Feed):
    date_format = '%a, %d %b %Y %H:%M:%S %Z'

    def __init__(self, feed_url: str, last_read_dt: datetime):
        self.last_read_dt = last_read_dt
        self.feed_url = feed_url

    def get_updates(self) -> list[Item]:
        content = self.get_feed_content()
        root = ET.fromstring(content) 
        channel = root.find("channel")
        nodes = channel.findall("item")

        updates: list[Item] = []
        for node in nodes:
            title = node.find("title").text
            dt = node.find("pubDate").text
            link = node.find("link").text
            description = node.find("description").text
            item = Item(
                title=title,
                dt=datetime.strptime(dt, self.date_format),
                link=link,
                description=description,
            )
            updates.append(item)

        updates = [item for item in updates if item.dt > self.last_read_dt]

        return updates


    def get_feed_content(self) -> str:
        return requests.get(self.feed_url).text

if __name__ == '__main__':


    feeds = [
        RssFeed(
            'https://habr.com/ru/rss/hubs/sql/articles/?fl=ru&limit=100',
            last_read_dt=datetime(1901, 1, 1, 0, 0, 0)
        ),
        RssFeed(
            'https://habr.com/ru/rss/hubs/python/articles/?fl=ru&limit=100',
            last_read_dt=datetime(1901, 1, 1, 0, 0, 0)
        ),

    ]

    all_updates = []

    for feed in feeds:
        updates = feed.get_updates()
        all_updates.extend(updates)

    all_updates.sort(key= lambda item: item.dt)#изучить
    from pprint import pprint
    pprint(all_updates)


