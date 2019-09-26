import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all('meta')
##print(metas)
a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ]
list1=" ".join(a)

l2=[]
for i in list1.split(","):
    l2.append(i)

print(l2)

url = 'https://www.voonik.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all('meta')
#print(metas)
a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ]
list1=" ".join(a)

l2=[]
for i in list1.split(","):
    l2.append(i)

print(l2)

url = 'https://www.snapdeal.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all('meta')
#print(metas)
a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ]
list1=" ".join(a)

l2=[]
for i in list1.split(","):
    l2.append(i)

print(l2)

url = 'https://www.jabong.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all('meta')
#print(metas)
a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ]
list1=" ".join(a)

l2=[]
for i in list1.split(","):
    l2.append(i)

print(l2)


##url = 'https://www.limeroad.com/'
##
##response = requests.get(url)
##soup = BeautifulSoup(response.text, "html.parser")
##
##metas = soup.find_all('meta')
###print(metas)
##a=[ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords' ]
##list1=" ".join(a)
##
##l2=[]
##for i in list1.split(","):
##    l2.append(i)
##
##print(l2)
