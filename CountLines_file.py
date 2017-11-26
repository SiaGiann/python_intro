try:
    with open('cities.txt') as f:
        lines = f.readlines()
except:
    print("There was an error opening file \"cities.txt\"")
else:
    try:
        with open('out.txt', 'w') as w:
            for index, line in enumerate(lines):
                w.write(str(index+1) + ': ' + lines[index])
    except:
        print("There was an error while writing file \"out.txt\"")