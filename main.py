from datetime import datetime

from feed import RssFeed


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

all_updates.sort(key=lambda item: item.dt, reverse=True)  # изучить

fresh_items = all_updates[:10]

while True:
    for num, item in enumerate(fresh_items):
        print(num, item.title)

    choice = int(input("\nКакую из этих новостей посмотреть ? - "))

    item = fresh_items[choice]

    print(item.description, item.link, sep="\n --- \n")

    input("Чтобы вернуться к списку новостей - нажмите Enter")