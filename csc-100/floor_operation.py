from math import floor

# whether you use the in built python floor function i.e
# print(floor(p / o)), or you use;
# print(p // o) all are thesame.

p = int(input('Enter a big number: '))
o = int(input('Enter a small number: '))
l = int(input('Enter a small number differently: '))

print(o, 'can enter into "' + str(p) + '"', p // o, 'times, with a remainder of', p % o)

print(l, 'can enter into "' + str(p) + '"', p // l, 'times, with a remainder of', p % l)

print(floor(p / o))

print(floor(p / l))