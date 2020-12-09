# Objectives:
#   · Identify AB line
#   · Determine whether it should continue an attack round of a previous NPC or create new
#   · Connect new input to an NPC AB array
#   · Print NPC followed by all the AB arrays associated with it alphabetically by NPC name
# Notes:
#   · placeholder

import re

gCombatRoll = r' : \([1-2]?[0-9] (+|-) [0-9]?[0-9] = (-)?[0-9]?[0-9]\)'

gABdict = {[]} # implementing a set of list objects
gAttackBonus = 0
gAttackPenalty = 0

for line in open('input.txt'):
    # remove non-essentials from line
    line = re.sub(r'^\[CHAT WINDOW TEXT\] \[(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-2][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]\] ', '', line)
    line = re.sub('\n', '', line)

    attacker = None
    # if we keep regex very clear during the searches, we can be loose within the block
    if re.search(r'attempts (Improved )?Disarm on .+ : \*(success|failure)\*' + gCombatRoll', line):
        attacker = re.split('attempts', line)[0]
        gAttackBonus = re.split(r' : \*(success|failure)\* : \([1-2]?[0-9] ', line)[1] # how to we get posi/nega value of ab?
        gAttackPenalty = 6
    elif re.search(r'attempts (Improved )?Knockdown on .+ : \*(success|failure)\*' + gCombatRoll, line):
        attacker = re.split('attempts', line)[0]
        gAttackPenalty = 4
    elif re.search(r'attempts Called Shot: (Arm|Leg) on .+ : \*(success|failure)\*' + gCombatRoll, line):
        attacker = re.split('attempts', line)[0]
        gAttackPenalty = 2
    elif re.search(r'attacks .+ : \*((critical )?hit|miss)\*' + gCombatRoll, line)
        attacker = re.split('attacks', line)[0]
        gAttackPenalty = 0