d = {'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0, 'total_credits': 0, 'grades': 0}
for i in range(1, int(input("Input number of classes:   "))+1):
    grade, num_credits = d[input("Input grade for class " + str(i) + ':   ').upper()], int(input("Input credits for class " + str(i) + ': '))
    d['total_credits'], d['grades'] = d['total_credits'] + num_credits, d['grades'] + grade*num_credits
print('your gpa is', str(d['grades']/d['total_credits']))