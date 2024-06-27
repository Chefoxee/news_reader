
from item import Item
import requests
import xml.etree.ElementTree as ET


content = requests.get('https://habr.com/ru/rss/hubs/sql/articles/?fl=ru').text

tree = ET.fromstring(content)

channel = tree.find("channel")
nodes = channel.findall("item")
updates: list[Item] = []
for node in nodes:
    title = node.find("title")
    print(title.text)
