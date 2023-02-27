import scrapetube, time, requests
    
class YouTube:
    videos = []
    aktualnaIlosc = 0
    def checkForVideos():
        if(len(YouTube.videos) > YouTube.aktualnaIlosc):
            YouTube.aktualnaIlosc = len(YouTube.videos)
            return YouTube.videos[0]['title']['runs'][0]['text']
        return False
    
class Twitch:
    isLive = False
    def ifLive():
        contents = requests.get('https://www.twitch.tv/' + 'YoungMulti').content.decode('utf-8')
        if 'isLiveBroadcast' in contents:
            if(Twitch.isLive == True):
                return
            else:
                Twitch.isLive = True
                return True
        else:
            if(Twitch.isLive == False):
                return
            else:
                Twitch.isLive = False
                return False

scrapedVideos = scrapetube.get_channel("UC2bNJW1mb0VaN0-o-llWwAw")
for vid in scrapedVideos:
    YouTube.videos.append(vid)

while True:
    #YouTube check
    print('Checking for any new videos...')
    isNew = YouTube.checkForVideos()
    if(isNew != False):
        print('New video found! Title:', isNew)
    
    #Twitch check
    if(Twitch.ifLive() == True):
        print('YoungMulti went live!')
    time.sleep(10)