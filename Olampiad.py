n = int(input())
count = 0
dtl_list = []
while count < n :
    dtl = input()
    dtl_list.append(dtl.split('.'))
    count +=1

for i in dtl_list:
   i[1]=i[1].capitalize()
f_list=[]
m_list=[]
for i in dtl_list:
    if i[0] == 'f':
        f_list.append(i)
    else:
        m_list.append(i)

for i in sorted(f_list):
    print('%s %s %s'%(i[0],i[1],i[2]))

for i in sorted(m_list):
    print('%s %s %s'%(i[0],i[1],i[2]))



