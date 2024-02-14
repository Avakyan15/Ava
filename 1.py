import csv
with open('game2.csv', encoding='windows-1251') as csvfile:
    reader=csv.reader(csvfile, delimiter=';', quotechar='"')
    answer=list(reader)[1:]
    a=[]

for i in range(len(answer)):
    for j in range(0,4):
        if '55' in answer[i][j]:
            a+=[('У персонажа',answer[i][1], 'в игре', answer[i][0], 'нашлась ошибка c кодом:', answer[i][2],  'Дата фиксации:', answer[i][3])]
with open('game_new.csv', 'w', newline='', encoding='windows-1251') as file:
    w=csv.writer(file)
    w.writerow(['characters', 'GameName', 'nameError', 'date'])
    w.writerows(a)
