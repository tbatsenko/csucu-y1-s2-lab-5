from urllib.request import urlopen
import time


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None
        self._last_update = None

    @property
    def content(self):
        update_interval = 2  # update interval in seconds
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self._last_update = time.time()
        if time.time()-self._last_update > update_interval:
            print("Reloading the Page...")
            self._content = urlopen(self.url).read()
            self._last_update = time.time()
        return self._content
