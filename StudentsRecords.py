students = {}

while 1:
    inp = input('Enter ID, Name (or character `q` to terminate): ')
    if inp == 'q':
        break
    else:
        am, name = inp.split(', ')
        students[am] = name

for am in sorted(students):
    print(am, ' ', students[am])
