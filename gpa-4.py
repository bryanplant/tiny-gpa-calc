d = {'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0, 'credits': 0, 'grades': 0}
inputs = [(d[input("\nInput grade for class " + str(i) + ':   ').upper()], int(input("Input credits for class " + str(i) + ': '))) for i in range(1, int(input("Input number of classes:   "))+1)]
for i in inputs: d['credits'], d['grades'] = d['credits'] + i[1], d['grades'] + i[0]*i[1]
print("Your GPA is", d['grades']/d['credits'])