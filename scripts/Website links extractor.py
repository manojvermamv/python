#!/usr/bin/python3
# Extract all links from a website by python file

from bs4 import BeautifulSoup
import urllib.request

print("<------------------ Website links extractor ------------------>")
parser = 'html.parser'
resp = urllib.request.urlopen(input("Enter a Web URL : "))
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    links = link['href']

    print("[+]", links)

    f = open("links.txt", "a")
    f.write(f"[+] {links}\n")
    f.close()
print("\n[+] All links extracted & saved to links.txt")