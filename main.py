import feedparser,time,re

URL="http://un-lazy-midnight.tistory.com/rss"
README_PATH="/busymidnight/README.md"
RSS_FEED = feedparser.parse(URL)
MAX_NUM = 5
latest_posts = ""

markdown_text="""
## ✅ Latest Blog Posts

"""  # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
  if idx > MAX_NUM:
     break
  feed_date = feed['published_parsed']
  markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
with open(README_PATH, 'r+') as f:
    content = f.read()
    new_content = re.sub(r'## ✅ Latest Blog Posts*\n', markdown_text, content, flags=re.DOTALL)
    f.seek(0)
    f.write(new_content)
    f.truncate()
