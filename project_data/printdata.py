from pyexcel_xls import read_data
import pandas as pd
import matplotlib as plt

import xlsxwriter
from datetime import datetime
workbook=xlsxwriter.Workbook('d:\\vrp\\finalreport.xlsx')

worksheet=workbook.add_worksheet()

m=[]
n=[]
d1={}
d={}
x="online shopping"
urls=["https://www.jabong.com/","https://www.snapdeal.com/","https://www.koovs.com/","https://www.tatacliq.com/","https://www.homeshop18.com/","https://www.voonik.com/"]
files=['koovs.txt','jabong.txt','tata.txt','homeshop.txt','voonik.txt','snapdeal.txt']
for i in files:
    f=open(i,"r")
    s=f.read()
    count=s.count(x)
    print("the count for ",x,"in file ",i,"is ",count)
    d1 = {i:count}
    d.update(d1)

print(d)

##    m.append(i)
##    n.append(count)


worksheet.write('A1', 'url')
worksheet.write('B1', 'Count')

row = 1
col = 0

for url,count in d.items():
     worksheet.write(row, col,url )
     worksheet.write(row, col + 1, count)
     row += 1

 # Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B2:B5)')
workbook.close()
data=read_data("finalreport.xlsx")
print(data)


chartsheet = workbook.add_chartsheet()
chart      = workbook.add_chart({'type': 'bar'})

# Configure the chart.

chartsheet.set_chart(chart)
chart.add_series({'values': '=Sheet1!$A$2:$A$7'})
chart.add_series({'values': '=Sheet1!$B$2:$B$7'})


# Insert the chart into the worksheet.
worksheet.insert_chart('A13', chart)
workbook.close()

