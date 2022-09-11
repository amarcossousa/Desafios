students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
['Akriti', 41], ['Harsh', 39]]

#Cria a lista vazia de scores
scores  = []

# percorre students lista e pega os valores de scores
for x in students:
    scores.append(x[1])

# define o valor de segundo score
second_score = sorted(set(scores)) [1]

# Define os dois estudantes com scores iguais e os colocam em ordem alfabetica
for student in sorted(students):
    if student[1] == second_score:
        print(student[0])
