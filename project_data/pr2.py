import xlsxwriter
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

m=[]
n=[]
d1={}
d={}
d3={}
d5={}
d4={}
d2={}
##x="online shopping"
urls=["https://www.jabong.com/","https://www.snapdeal.com/","https://www.koovs.com/","https://www.tatacliq.com/","https://www.homeshop18.com/","https://www.voonik.com/"]
files=['koovs.txt','jabong.txt','tata.txt','homeshop.txt','voonik.txt','snapdeal.txt']
l=[]

x=input("Enter keyword:")
y=input("Enter keyword:")
z=input("Enter keyword:")
workbook=xlsxwriter.Workbook('d:\\project_data\\finalreport.xlsx')
worksheet=workbook.add_worksheet()
for i in files:
      f=open(i,"r")
      s=f.read()
      count=s.count(x)
      count1=s.count(y)
      count2=s.count(z)
      print("the count for ",x,y,z ,"in file ",i,"is ",count,count1,count2 )
      d1 = {i:count}
      d2={i:count1}
      d3={i:count2}
      d.update(d1)
      d5.update(d2)
      d4.update(d3)
worksheet.write('A1', 'url')
worksheet.write('B1', 'Count of keyword 1')
worksheet.write('C1','Count of keyword 2')
worksheet.write('D1','Count of keyword 3')
row = 1
col = 0
for url,count in d.items():
     worksheet.write(row, col,url )
     worksheet.write(row, col + 1, count)
     row += 1
row = 1
col = 2
for url,count1 in d5.items():
     worksheet.write(row, col, count1)
     row += 1

row = 1
col = 3
for url,count2 in d4.items():
     worksheet.write(row, col, count2)
     row += 1     
workbook.close()
df=pd.read_excel('finalreport.xlsx')
width = 0.25 
pos = list(range(len(df['Count of keyword 1'])))
fig, ax = plt.subplots(figsize=(15,5))
plt.bar(pos, 
        #using df['pre_score'] data,
        df['Count of keyword 1'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['url'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['Count of keyword 2'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['url'][1]) 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['Count of keyword 3'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        label=df['url'][2]) 

# Set the y axis label
ax.set_ylabel('Count')
ax.set_ylabel('Count of keyword in url')
# Set the chart's title
ax.set_xlabel('online shopping sites')
ax.set_title('Count of keywords in online shopping sites')
# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(df['url'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Count of keyword 1'] + df['Count of keyword 2'] + df['Count of keyword 3'])] )
plt.legend([x,y,z], loc='upper left')
plt.grid()
plt.show()

 
   
