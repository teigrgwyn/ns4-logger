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