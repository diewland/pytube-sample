import sys
import pathlib
from datetime import datetime as dt
from pytube import YouTube

# create date folder
folder_name = dt.now().strftime("%Y%m%d")
pathlib.Path(folder_name).mkdir(exist_ok=True) 

# gather urls
if len(sys.argv) > 1:
    print("read url(s) from commandline")
    lines = sys.argv[1:]
else:
    print("read url(s) from list.txt")
    f = open("list.txt")
    lines = f.readlines()

for line in lines:
    url = line.strip()
    print("downloading.. %s" % url)
    hi_vid = YouTube(url).streams.first()
    hi_vid.download(folder_name)

print('done, videos in folder %s/' % folder_name)
