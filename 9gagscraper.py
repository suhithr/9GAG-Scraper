import urllib
import urllib2
import bs4
url = 'http://www.9gag.com'
response = urllib2.urlopen(url)
html_doc = response.read()
soup = bs4.BeautifulSoup(html_doc)
list = soup.select('img.badge-item-img')
names = [i['alt'] for i in list]
links = [j['src'] for j in list]
n = 0
for l in links:
	urllib.urlretrieve(l,names[n])
	n = n + 1

