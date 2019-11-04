import os
import urllib3
import requests
url_file = "images.txt"
with open(url_file, "r") as f:
    url_pages = f.read()
print(url_pages)
list_pathlist = []
f = open("check.txt", "a+")

for url in url_pages.split('\n'):
    pathlist = "images" + "/" + url.rsplit('/', 1)[1]
    list_pathlist.append(pathlist)
    f.write("\n%s" % pathlist)
print(list_pathlist)
