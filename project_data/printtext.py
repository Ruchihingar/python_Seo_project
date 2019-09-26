import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://www.koovs.com/").read()
soup = bs.BeautifulSoup(source,'html.parser')
for script in soup(["script","style"]):
    script.extract()
s=soup.get_text()
print(s)
f=open("koovs.txt","w")
f.write(s)
##l=s.split(" ")
##s1=set(l)
##c=0
##for i in s1:
##    for j in l:
##        if i==j:
##            c+=1
##    print(i,c)        
##    c=0


