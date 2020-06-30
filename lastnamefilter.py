import re

vowels = '[AEIOUaeiou]'


fname = 'toplastnames.txt'
fh = open(fname)
count = 0
for line in fh:
    pos1 = line.find('|')
    linelater = line[pos1 + 1:]
    pos2 = linelater.find('|')
    lastname = line[pos1 + 2 :pos1 + pos2]
    lastvowels = re.findall(vowels, lastname)
    doubler = lastname.find('rr')
    if lastname == 'Falk':
        newlast = 'Forrester'
    elif lastname == 'Sanders':
        newlast = 'Grungerson'
    elif lastname == 'Barker':
        newlast = 'Brenger'
    elif lastname == 'Armstrong':
        newlast = 'Aurmstrang'
    elif lastname == 'Rodriguez':
        newlast = 'Rungreguez'
    elif doubler != -1:
        newlast = lastname[:doubler + 2] + 'angers'
    elif lastname[0] in ['B', 'C']:
        newlast = lastname[0] + 'rungus'
    elif len(lastname) == 5 and lastname[0] not in vowels:
        newlast = lastname[0] + 'ungus'
    elif lastname[0] == 'D' and len(lastvowels) == 2:
        newlast = lastname[0] + 'angus'
    else:
        print(lastname)
        count += 1

print (count)
