from addyRip import *



chan = chanRIP()
links = chan.ripArchiveLinks()

# print(links)

allMatches = []

for link in links:
    print(f"Working on thread # {link.split('/')[-2]} - {link.split('/')[-1]}")
    posts = chan.ripThreads(link)
    addy = addyRip()
    for post in posts:
        message = post.find(True, {"class": "postMessage"})
        if message == None:
            continue
        else:
            matches = addy.extractFromText(message.text)
            allMatches = allMatches + matches


for x in allMatches:
    print(x)
