import urllib2
import os


class subtitle:
    def __init__(self, file_path, md5):
        self.url = "http://api.thesubdb.com/?action=download&hash=" + md5 + "&language=en"
        # self.header = {'User-Agent': 'SubsDl (Subtitle Downloader; https://github.com/anmolvarshney05)'}
        self.header = {'User-Agent': 'SubDB/1.0 (Anmol/0.1; https://github.com/anmolvarshney05/SPOJ-Solutions)'}
        self.fname = os.path.splitext(file_path)[0]
        self.req = urllib2.Request(self.url, '', self.header)

    def get_subtitle(self):
        response = urllib2.urlopen(self.req).read()
        with open(self.fname + '.srt', "wb") as s:
            s.write(response)

