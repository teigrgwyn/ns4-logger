# Notes:
#   · Script requires knowledge of the code to ascertain relevant results.
#   · Resultant saves lines always come directly after the initated attack; in the case of multiple targets, multiple lines will be displayed; scan all of them
#   · Save line regex: ' : (Fortitude|Reflex) Save : \*(success|failure)\* : \([0-2]?[0-9] \+ '
#
# Fortitude
#   Construct Shape - Iron Golem - Dragon Breath: Slow
#       r' breathes gas.'
#       -> match save line regex
# Reflex
#   Construct Shape - Stone Golem - Knockdown Bolt
#       r' attempts Ranged Touch Attack on '
#       -> match save line regex

import re 

gSavingThrowDict = {}
gSavingThrow = None

gActiveSearch = None
gSearchString = None

gSpellDescriptorDict = {
    
}
    vs. Spells
    -
    vs. Death
    vs. Fear
    vs. Mind-affecting
    -
    vs. Acid
    vs. Cold
    vs. Electricity
    vs. Fire
    vs. Sonic
    -
    vs. Disease
    vs. Poison
    -
    vs. Divine
    vs. Positive
    vs. Negative
    -
    vs. Good
    vs. Evil
    vs. Lawful
    vs. Chaotic

for line in open('cr/input.txt'):
    # remove non-essentials from line
    line = re.sub(r'^\[CHAT WINDOW TEXT\] \[(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-2][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]\] ', '', line)
    line = re.sub('\n', '', line)

    if (gActiveSearch == 1): gSearchString = r' attempts Ranged Touch Attack on (.+) : '
    elif (gActiveSearch == 1): gSearchString = r' attempts Ranged Touch Attack on (.+) : '

    if (re.search(r' attempts Ranged Touch Attack on .+ : \*((critical )?hit|miss)\* : \([1-2]?[0-9] +|- [0-9]?[0-9] = (-)?[0-9]?[0-9]\)', line)):
        gActiveSearch = 1
    elif (re.search(r' attacks .+ : ', line)):
        gActiveSearch = 2

for key, value in sorted(gSavingThrowDict.items()):
    print('{} : {}'.format(key, value))