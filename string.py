word = 'Raven Dexter'
sentence = 'rdr2,god of war,bloodborne'
print(word.upper())
print(word.isupper())
print(word.islower())
print(word.lower())
print(word.capitalize())
print(word.find('n'))
game = sentence.split(',')
print(game)
result = ', '.join(game)
print(result)

f = 'football'
print(f[0:4])
print(f[4:])
print(f[4:-1])