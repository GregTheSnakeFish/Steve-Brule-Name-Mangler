import re
import time
import itertools as it

liebetest = False
jantest = False

while True:
    name = input("What's your name, dingus? ")
    test = re.findall(' ', name)
    if name in map(''.join, it.product(*((c.upper(), c.lower()) for c in 'Steve Brule'))):
        print("Dangit, that's my name not your name, ya dang hunk! Type your name!")
        continue
    elif name == "Jan Skylar":
        jantest = True
        break
    elif name == 'David Liebe Hart':
        newname = 'Dr. Daniel Drungle Harr'
        liebeintro = 'This is the prapett man,'
        liebetest = True
        break
    elif len(test) == 0:
        print('I need a first AND last name, ya turkey! What are ya, some kinda hunk?')
        continue
    elif len(test) > 1:
        print("Dangit I don't want your whole dangus family tree, just a first name and a last name, ya dumb hunk!")
        continue
    else:
        break
    
firstname = name[0].upper() + name[1:name.find(' ')].lower()
tentlastname = name[name.find(' '):].lstrip()
lastname = tentlastname[0].upper() + tentlastname[1:].lower()

intros = ["Mobin couldn't hack it so mom's new man is", "I bet I would be a cool guy too if my name was Dr.",
"It's time for Doctor to Doctor. My next guest is Dr.", "Nice to meet ya, person name of"]

mod1 = len(firstname) % 4
mod2 = len(lastname) % 4
if mod1 == 0:
    if mod2 == 0:
        intro = intros[0]
    if mod2 == 1:
        intro = intros[1]
    if mod2 == 2:
        intro = intros[2]
    else:
        intro = intros[3]
elif mod1 == 1:
    if mod2 == 0:
        intro = intros[3]
    if mod2 == 1:
        intro = intros[1]
    if mod2 == 2:
        intro = intros[0]
    else:
        intro = intros[2]
elif mod1 == 2:
    if mod2 == 0:
        intro = intros[0]
    if mod2 == 1:
        intro = intros[3]
    if mod2 == 2:
        intro = intros[1]
    else:
        intro = intros[2]
else:
    if mod2 == 0:
        intro = intros[3]
    if mod2 == 1:
        intro = intros[1]
    if mod2 == 2:
        intro = intros[0]
    else:
        intro = intros[2]

vowels = '[AEIOUaeiou]'
firstvowels = re.findall(vowels, firstname)
lastvowels = re.findall(vowels, lastname)

ronlist = ['Ronnie', 'Ron', 'Ronny', 'Rand', 'Ronald', 'Ronaldo']
genelist = ['Gene', 'Jean', 'Jeannie', 'John', 'Jon', 'Jenna', 'Jenn', 'Jen']
endlist1 = ['y', 'd', 'g', 's', 'i', 'l']
startlist1 = ['C', 'G', 'T', 'K', 'D']

if firstname == 'Denny':
    newfirst = firstname
    intro = 'Get off the dangus compruter and get back to work,'
elif firstname == 'Bill' and lastname == 'Gates':
    newfirst = firstname
    intro = 'Michaelsoft was invented by man name of'
elif firstname == 'Ronald':
    newfirst = 'Rungle'
elif firstname == 'Roy' and lastname == 'Bruce':
    newfirst = firstname
elif firstname == "George" and lastname == "Sallustio":
    newfirst = 'Gringus'
elif firstname == "Beverley":
    newfirst = firstname
elif firstname == "D'loran" and lastname == "Martin":
    newfirst = "Dilleren"
elif firstname == 'Diane' and lastname == 'Daniels':
    newfirst = firstname
elif firstname == 'Sunshine':
    newfirst = firstname
    intro = "You're just my cousin. Who cares,"
elif firstname == 'Mobin':
    newfirst = firstname
    intro = "You just couldn't hack it with Doris,"
elif firstname == 'Doris':
    newfirst = firstname
    intro = "My momma's name was Doris, but it wasn't"
elif firstname == 'Cindy':
    newfirst = 'Cynthia'
elif firstname == 'Sandy' and lastname == 'Sanders':
    newfirst = firstname
elif firstname == 'Daniel':
    newfirst = 'Dan'
elif firstname in genelist:
    newfirst = 'Jang'
elif len(firstvowels) == 2 and 'e' in firstvowels:
    if firstname[0] == 'J':
        newfirst = 'Jimmy'
    elif firstname[0] in ['K', 'G', 'N']:
        newfirst = 'Knee' + firstname[len(firstname)-1]
    else:
        newfirst = firstname[0] + 'eembu' + firstname[len(firstname)-2:]
elif firstname in ronlist:
    newfirst = 'Runnie'
elif firstname[len(firstname)-2] == 'l':
    if firstname[1] != 'u':
        extra = 'ungle'
    else:
        extra = 'ongle'
    newfirst = firstname[0] + extra
elif len(firstvowels) == 1 and len(firstname)>=5:
    newfirst = firstname[0] + 'immy'
elif firstname[0].lower() == firstname[len(firstname)-1]:
    newfirst = firstname[0] + 'ingi' + firstname[len(firstname)-1]
elif firstname[len(firstname)-1] in endlist1:
    newfirst = firstname[0] + 'umb' + firstname[len(firstname)-2].lower()
elif firstname[len(firstname)-1] in vowels and firstname[len(firstname)-2] not in vowels:
    if firstname[len(firstname)-1] == 'a' or 'i':
        newfirst = firstname[:len(firstname)-1] + 'ungus'
    elif firstname[len(firstname)-1] == 'o' or 'u':
        newfirst = firstname[:len(firstname)-1] + 'angle'
    elif firstname[len(firstname)-1] == 'e' and firstname[0] not in vowels:
        newfirst = firstname[0] + 'angus'
    else:
        newfirst = firstname[0] + 'mungle'
elif firstname[len(firstname)-1] == 'e' and firstname[0] not in vowels:
    newfirst = firstname[0] + 'rungus'
elif firstname[len(firstname)-1] in vowels:
    newfirst = firstname[:1] + 'rungled'
elif len(firstvowels) == 1:
    for vowel in firstvowels:
        if vowel == 'a' or vowel == 'e':
            newvowel = 'on'
        elif vowel == 'u' or vowel == 'o':
            newvowel = 'a'
        else:
            newvowel = 'i'
        newfirst = firstname[:firstname.find(vowel)] + newvowel + firstname[firstname.find(vowel)+1:]
elif firstname[0] in startlist1:
    newfirst = firstname[0] + 'rungles'
elif firstname[0] in ['M', 'R', 'L']:
    newfirst = firstname[0] + 'ongus'
elif firstname[len(firstname)-1] == 'n':
    if firstname[2] != 'r':
        newfirst = firstname[0] + 'r' + firstname[2:len(firstname)-1] + 'ingo'
    else:
        newfirst = firstname[0] + 'u' + firstname[2:4] + 'ango'
elif len(firstname) % 2 == 0:
    if firstname[0] in vowels:
        newfirst = 'Br' + firstname[0].lower() + firstname[1:]
    else:
        newfirst = firstname[0] + 'andleson'
elif firstname[0] in vowels and firstname [1] not in vowels:
    newfirst = firstname[0:2] + 'ungus'
elif firstname[len(firstname)-4:] == 'iyah':
    newfirst = firstname[:len(firstname)-4] + 'angrus'
elif firstname[len(firstname)-3:] == 'iah':
    newfirst = firstname[:len(firstname)-3] + 'angus'
elif firstname[len(firstname)-1] == 'r' and firstname[1] != 'r':
    newfirst = 'R' + firstname[1:len(firstname)-1] + firstname[0].lower() + 'dus'
elif firstname[0] == 'J':
    newfirst = 'Jangrus'
elif len(firstname) == 5:
    for vowel in firstvowels:
        newfirst = firstname[0] + vowel + 'rangus'
elif len(firstname) == 7:
    if firstname[1] not in vowels:
        newfirst = firstname[0:2] + 'angrid'
    else:
        newfirst = firstname[0:2] + 'ndlesung'
elif len(firstname) > 7:
    if firstname[1] in vowels:
        newfirst = firstname[0] + 'ungrid'
    else:
        firstname[:1] + 'andleson'
else:
    newfirst = firstname
    intro = ('Pretty wild name, even for a dang Dr.! Dangit, I never heard name of')

##LASTNAME BLOCK

doubler = lastname.find('rr')
brontmaker = lastname.find('re')

if len(lastname) <= 2:
    if lastname[1] not in vowels:
        newlast = 'W' + lastname[0].lower() + 'ngrus'
    else:
        newlast = lastname + 'mbrid'
elif firstname == 'Denny':
    newlast = " "
elif firstname == 'George' and lastname == 'Clooney':
    newfirst = firstname
    newlast = 'Crooney'
elif firstname == 'Bill' and lastname == 'Gates':
    newlast = 'Grates'
elif lastname == 'Falk':
    newlast = 'Forrester'
elif firstname == "George" and lastname == "Sallustio":
    newlast = " "
elif firstname == "D'loran" and lastname == "Martin":
    newlast = "Jorid"
elif lastname in ['Pringle-Brule', 'Pringle-Brule-Salahari']:
    newlast = lastname
    intro = 'Mommy? Is that you? No one else is named'
elif firstname == 'Diane' and lastname == 'Daniels':
    newlast = 'Drangle'
elif lastname == 'Salahari':
    newlast = lastname
    intro = "Get outta here Mobin, you stupid rangus! I know that's you, even though you typed"
elif lastname == 'Brule':
    newlast = 'Brule'
    intro = "We have the same dangus last name,"
elif lastname == 'Sanders':
    newlast = 'Grungerson'
elif lastname == 'Barker':
    newlast = 'Brenger'
elif firstname == "Beverley":
    newlast = 'Dangus'
elif lastname == 'Armstrong':
    newlast = 'Aurmstrang'
elif lastname == 'Rodriguez':
    newlast = 'Rungriguez'
elif lastname == 'Lindon':
    newlast = 'Drangle'
elif lastname == 'Davis' and firstname == 'Steve':
    newfirst = firstname
    newlast = "Drambus"
elif doubler != -1:
    newlast = lastname[:doubler + 2] + 'angers'
elif lastname[0] in ['B', 'C']:
    if firstname not in ['Roy', 'Ronald']:
        newlast = lastname[0] + 'rungus'
    else:
        if firstname == 'Roy':
            newlast = 'Bringus'
elif len(lastname) == 5 and lastname[0] not in vowels:
    newlast = lastname[0] + 'ungus'
elif lastname[0] == 'D' and len(lastvowels) == 2:
    newlast = lastname[0] + 'angus'
elif lastname[0] not in vowels and lastname[1] not in vowels:
    newlast = lastname[:2] + 'angersun'
elif lastname[0] in ['J', 'G', 'M', 'W']:
    newlast = lastname[0] + 'angles'
elif lastname[0] not in vowels and lastname[1] in vowels and lastname[2] not in vowels:
    if lastname[1] in ['a', 'u']:
        newvowel = 'o'
        end = 'mungus'
    if lastname[1] in ['o', 'e']:
        newvowel = 'u'
        end = 'andus'
    else:
        newvowel = 'e'
        end = 'angrus'
    newlast = lastname[0] + newvowel + lastname[2] + end
elif brontmaker != -1:
    newlast = lastname[:brontmaker] + 'orn' + lastname[brontmaker+1:]
elif lastname[len(lastname)-2:] == 'on':
    newlast = 'O' + lastname[1:len(lastname)-2] + 'ung'
elif lastname[0] in vowels:
    newlast = lastname[0] + 'mangus'
elif lastname[1:3] == 'ee':
    newlast = lastname[0] + 'eenus'
elif lastname[len(lastname)-1] == 'z':
    newlast = 'Zangus'
elif lastname[0] == 'S' and lastname[len(lastname)-1] == 'n':
    newlast = 'Sarangus'
elif lastname[1] in vowels and lastname[2] in vowels:
    newlast = lastname[0] + 'orn' + lastname[3:]
else:
    newlast = lastname
    intro = ('Pretty wild name, even for a dang Doctor! Dangit, I never heard name of')
    
if liebetest == True:
    print(liebeintro, newname + '!')
elif jantest == True:
    print("Janny Skrylur makes my dangus feel funny.")
elif newfirst == 'Jimmy' and newlast == 'Brungus':
    print(intro, newfirst, newlast + '!')
    time.sleep(2)
    print("...(it's actually Dr. Johnny Boden)...")
    time.sleep(1)
    print("Dr. Junky Brogan!")
else:
    print(intro, newfirst, newlast + '!')

time.sleep(2)
print("For your health!")
