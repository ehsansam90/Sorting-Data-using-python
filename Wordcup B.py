from collections import OrderedDict

spain = {'name':'Spain','wins':0,'loses':0,'draws':0, 'goal diffrence':0,'points':0}
iran = {'name':'Iran','wins':0,'loses':0,'draws':0 ,'goal diffrence':0,'points':0}
morocco={'name':'Morocco','wins':0,'loses':0,'draws':0 ,'goal diffrence':0,'points':0}
portugal = {'name':'Portugal','wins':0,'loses':0,'draws':0 ,'goal diffrence':0,'points':0}

goals = list()
count = 0
res_game_list = list()
while count<6:
    count+=1
    res_game = input()
    res_game_list.append(res_game)

each_game = list()
for i in res_game_list:
    each_game.append(i.split('-'))

for i in each_game:
   for j in i:
       goals.append(int(j))

iran['goal diffrence'] = goals[0]+goals[2]+goals[4]-goals[1]-goals[3]-goals[5]
spain['goal diffrence'] = goals[1]+goals[6]+goals[8]-goals[0]-goals[7]-goals[9]
morocco['goal diffrence'] = goals[5]+goals[9]+goals[11]-goals[4]-goals[8]-goals[10]
portugal['goal diffrence'] = goals[3]+goals[7]+goals[10]-goals[2]-goals[6]-goals[11]

for i in range(0,11,2):
    if goals[i]>goals[i+1]:
        if i == 0:
            iran['wins']+=1
            spain['loses']+=1
            iran['points']+=3
        elif i ==2:
            iran['wins'] += 1
            portugal['loses'] += 1
            iran['points'] += 3
        elif i ==4:
            iran['wins'] += 1
            morocco['loses'] += 1
            iran['points'] += 3
        elif i==6:
            spain['wins'] += 1
            portugal['loses'] += 1
            spain['points'] += 3
        elif i ==8:
            spain['wins'] += 1
            morocco['loses'] += 1
            spain['points'] += 3
        elif i==10:
            portugal['wins'] += 1
            morocco['loses'] += 1
            portugal['points'] += 3
    elif goals[i]==goals[i+1]:

        if i == 0:
            iran['draws']+=1
            spain['draws']+=1
            iran['points']+=1
            spain['points']+=1
        elif i ==2:
            iran['draws'] += 1
            portugal['draws'] += 1
            iran['points'] += 1
            portugal['points']+=1
        elif i ==4:
            iran['draws'] += 1
            morocco['draws'] += 1
            iran['points'] += 1
            morocco['points']+=1
        elif i==6:
            spain['draws'] += 1
            portugal['draws'] += 1
            spain['points'] += 1
            portugal['points']+=1
        elif i ==8:
            spain['draws'] += 1
            morocco['draws'] += 1
            spain['points'] += 1
            morocco['points']+=1
        elif i==10:
            portugal['draws'] += 1
            morocco['draws'] += 1
            portugal['points'] += 1
            morocco['points']+=1
    else:
        if i == 0:
            iran['loses']+=1
            spain['wins']+=1
            spain['points']+=3
        elif i ==2:
            iran['loses'] += 1
            portugal['wins'] += 1
            portugal['points'] += 3
        elif i ==4:
            iran['loses'] += 1
            morocco['wins'] += 1
            morocco['points'] += 3
        elif i==6:
            spain['loses'] += 1
            portugal['wins'] += 1
            portugal['points'] += 3
        elif i ==8:
            spain['loses'] += 1
            morocco['wins'] += 1
            morocco['points'] += 3
        elif i==10:
            portugal['loses'] += 1
            morocco['wins'] += 1
            morocco['points'] += 3
team_list=[spain,iran,morocco,portugal]

point_list=list()
team_dic = {'Spain':spain,'Iran':iran,'Morocco':morocco,'Portugal':portugal}

lis = sorted(team_list, key = lambda i:i['points'],reverse = True)
for i in lis:
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'%(i['name'],i['wins'],i['loses'],i['draws'],i['goal diffrence'],i['points']))



























