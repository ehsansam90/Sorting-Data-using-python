from collections import OrderedDict


count = 0
n = int(input())
people_janr_lis=list()
Horror_count=0
Romance_count=0
Comedy_count=0
History_count=0
Adventure_count=0
Action_count = 0

while count <n:
    count +=1
    people_janr = input()
    people_janr_lis.append(people_janr.split( ))


for i in people_janr_lis:
    for j in i:
        if j == 'Horror':
            Horror_count+=1
        elif j == 'Romance':
            Romance_count+=1
        elif j == 'Comedy':
            Comedy_count+=1
        elif j == 'History':
            History_count+=1
        elif j == 'Adventure':
            Adventure_count+=1
        elif j == 'Action':
            Action_count+=1

dict_janr = {'Romance':Romance_count , 'Horror': Horror_count, 'Comedy':Comedy_count , 'History':History_count,'Adventure':Adventure_count,'Action':Action_count}
dict_list=list(dict_janr.items())
value_list = list(dict_janr.values())
dict_list.sort(key= lambda x:x[1],reverse=True)

repeat_list = list()
for x in dict_list:
    if value_list.count(x[1])>1:
        repeat_list.append(x)

repeat_list.sort()

for x in dict_list:
    if value_list.count(x[1])==1:
        repeat_list.append(x)
repeat_list.sort(key = lambda x:x[1],reverse =True)
for i in repeat_list:
    print(i[0]+' : '+str(i[1]))




















