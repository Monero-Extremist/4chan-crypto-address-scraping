from addyRip import *

url = "https://boards.4channel.org/biz/thread/42574674"



thread = chanRIP()

posts = thread.ripThreads(url)

addy = addyRip()

allMatches = []

for post in posts:
    message = post.find(True, {"class": "postMessage"})
    if message == None:
        continue
    else:
        matches = addy.extractFromText(message.text)
        allMatches = allMatches + matches





# matches = addy.extractFromText(text)

# print(allMatches)

for x in allMatches:
    print(x)
