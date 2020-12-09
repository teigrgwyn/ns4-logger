# Objectives:
#   · Identify CR print
#   · Save CR temporarily
#   · Identify NPC death print
#   · If we're expecting death print, save NPC into death array so we only print once at the very end
#   · Print array to output alphabetically
# Notes:
#   · I've tried making it more readable; oddly enough, with my font, it's more readable this way.

import re

gCRdict = {}
gCombatRating = None

for line in open('input.txt'):
    # remove non-essentials from line
    line = re.sub(r'^\[CHAT WINDOW TEXT\] \[(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-2][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]] ', '', line)
    line = re.sub('\n', '', line)

    # we're expecting a 'killed' message, it exists, and the attacker is known
    if ((gCombatRating != None) and (re.search("killed", line)) and (re.split(" killed ", line)[0] != 'Someone')):
        gCRdict.update({(re.split(" killed ", line)[1]): gCombatRating})
        gCombatRating = None
    # we're ready for the next NPC death, and we got a CR message
    elif ((gCombatRating == None) and (re.search("Creature CR: ", line))):
        gCombatRating = int(re.split(r'\.', re.split("Creature CR: ", line)[1])[0]) # converts CR to int for ease of access in dict later

for key, value in sorted(gCRdict.items()):
    print('{} : {}'.format(key, value))
