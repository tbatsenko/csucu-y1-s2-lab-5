import time
from cashe_webpage import WebPage


page = WebPage("https://www.gutenberg.org/wiki/Animals-Domestic_(Bookshelf)")
now = time.time()
content1 = page.content
print(time.time() - now)

now = time.time()
time.sleep(5)
content2 = page.content

print(time.time() - now)
print(content2 == content1)
