"""
Iegūt ziņas, izmantojot rss no google.lv.






"""
import feedparser

#janorada RSS  plusmas URL
rss_url='https://news.google.com/rss?hl=en-LV&gl=LV&ceid=LV:lv'

#lejupladet uz izanalizet RSS plusmu
feed=feedparser.parse(rss_url)

# paradit zinu virsrakstus un saites

for entry in feed.entries:
    print('virsraksts:', entry.title)
    print('Saite:', entry.link)
    print('\n')
