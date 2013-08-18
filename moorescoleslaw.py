#python
#Moore's Coleslaw

import sys        # to be able to exit the script

def calculate_speed(year):
    return 2 ** ((year - 2010) / 2.0) * 5.2
  
year = raw_input("Pick a year: ") 

try:
    speed = calculate_speed(float(year))
except ValueError:
    print "Sorry, only numbers after 2009."
    sys.exit(1)
  
print "Moore's Law suggests consumer computing power in %s will be %.2f GHz." % (year, speed)
