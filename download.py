from pytube import YouTube
from pprint import pprint as pp

#url = 'https://www.youtube.com/watch?v=MUo3sMXilho'
#url = 'https://www.youtube.com/watch?v=x_kiX0uUDNI'
url = 'https://www.youtube.com/watch?v=vrXkfDIODZI'

hi_vid = YouTube(url).streams.first()

print(hi_vid)
print('Downloading..')
hi_vid.download('./')
