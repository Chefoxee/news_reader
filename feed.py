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
