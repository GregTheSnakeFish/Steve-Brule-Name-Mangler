import re

fname = 'topnames.txt'
fh = open(fname)

ronlist = ['Ronnie', 'Ron', 'Ronny', 'Rand', 'Ronald', 'Ronaldo']
genelist = ['Gene', 'Jean', 'Jeannie', 'John', 'Jon', 'Jenna', 'Jenn', 'Jen']
endlist1 = ['y', 'd', 'g', 's', 'i', 'l']
startlist1 = ['C', 'G', 'T', 'K', 'D']

count = 0
for line in fh:
    firstname = line.strip()
    vowels = '[AEIOUaeiou]'
    firstvowels = re.findall(vowels, firstname)
    if firstname == 'Cindy':
        continue
    elif firstname in genelist:
        continue
    elif len(firstvowels) == 2 and 'e' in firstvowels:
        continue
    elif firstname in ronlist:
        continue
    elif firstname[len(firstname)-2] == 'l':
        continue
    elif len(firstvowels) == 1 and len(firstname)>=5:
        continue
    elif firstname[0].lower() == firstname[len(firstname)-1]:
        continue
    elif firstname[len(firstname)-1] in endlist1:
        continue
    elif firstname[len(firstname)-1] in vowels:
        continue
    elif firstname[0] in startlist1:
        continue
    elif len(firstvowels) == 1:
        continue
    elif firstname[0] in ['M', 'R', 'L']:
        continue
    elif firstname[len(firstname)-1] == 'n':
        continue
    elif len(firstname) % 2 == 0:
        continue
    elif firstname[0] in vowels and firstname [1] not in vowels:
        continue
    elif firstname[len(firstname)-4:] == 'iyah':
        continue
    else:
        print(firstname)
        count += 1

print(count)
