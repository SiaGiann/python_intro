letters = {i: 1 for i in 'AEIOULNSTR'}
letters.update({i: 2 for i in 'DG'})
letters.update({i: 3 for i in 'BCMP'})
letters.update({i: 4 for i in 'FHVWY'})
letters.update({i: 5 for i in 'K'})
letters.update({i: 8 for i in 'JX'})
letters.update({i: 10 for i in 'QZ'})

words_points = {}

while 1:
    inp = input('Enter word (or `q` to terminate): ')
    if inp == 'q':
        break
    else:
        points = 0
        for letter in inp:
            points += letters[letter]
        words_points[inp] = points
        print('Word Scrabble points: ', points)

for word in sorted(words_points):
    print(word, ' ', words_points[word])
