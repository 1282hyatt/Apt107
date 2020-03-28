# 출력 : 2020년 03월 03일 ***,***,***원 

import csv 

def comma (num):
#num=100410
    cal= num[:3] + ',' + num[3:]
    return cal

file = open('Approve20200321.csv')
data=csv.reader(file)

i = list(data)

sum=0

for (j,i1) in enumerate(i): 
    
    date=i[j][0]
    price=i[j][5]
    price2=price.replace(",","")
    print(date[:4])
    if(date[:4]=='2020'):  
        # print(j,i1)
        # print(price2)
            
        sum += int(price2)

sum=str(sum)
# print(num[3:])   
print(sum)
# print("2020년 03월 03일" +comma(sum)+"원")