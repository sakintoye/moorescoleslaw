#python
#Moore's Coleslaw

import sys        # to be able to exit the script

# directory of years in relation to computing power
year = {
  "2010" : (5.31 * 2.0 ** 1.0) - 5.31,
  "2011" : (5.31 * 2.0 ** 1.0) - 5.31 / 2.0,
  "2012" : (5.31 * 2.0 ** 2.0) - 5.31 * 2.0,
  "2013" : (5.31 * 2.0 ** 2.0) - 5.31 * (2.0 / 2.0),
  "2014" : (5.31 * 2.0 ** 3.0) - 5.31 * 2.0 ** 2.0,
  "2015" : (5.31 * 2.0 ** 3.0) - 5.31 * (2.0 ** 2.0 / 2.0),
  "2016" : (5.31 * 2.0 ** 4.0) - 5.31 * 2.0 ** 3.0,
  "2017" : (5.31 * 2.0 ** 4.0) - 5.31 * (2.0 ** 3.0 / 2.0),
  }
  
speed = year[years]

years = raw_input("Pick a year starting at 2010: ") 

if years not in year:            			                                      
    #check if we have year
  i=0
  while i <= 5:							                                          
      #let's give user 5 tries
    i+=1
    print "We haven't gone that far back, try an earlier year or come back later."	      #print info
    years = raw_input("Pick a different year: ") 			                        
    #ask for new input
    if years in year:
      break
    if i == 5:  						
      print "Try again later!"  			                        #say bye
      sys.exit()						                                         
      #end of program
else:					          # if star is in stars
  pass					        # just continue
  
print "Moore's Law suggests consumer computing power in %r will be %r GHz." % (years, speed)
