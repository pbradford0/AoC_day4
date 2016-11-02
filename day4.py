#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/4

import sys
import hashlib
import re

def hash_calc(filename):
  #input and num are used to make the md5, output is the result
  #brute force the correct hash by adding a number to the end and looping till it's the right one
  input = open(filename, 'rU').read()
  num = 0
  #the correct output starts with 5 zeroes
  first_five = re.compile('000000*')
  #loop variables
  not_done = 1
  while (not_done == 1):
    #combine input and num, then md5 hash it and check for 0s
    output = hashlib.md5()
    output.update(input)
    output.update(str(num))
    #check if it starts with 5 zeroes
    match = re.match(first_five, output.hexdigest())
    if match:
      break
    #elif num >= 1000000:
    #  not_done = 0
    #  print "No matches found in "+str(num)+" attempts"
    #no good? add 1 to num and try again
    num = num+1
  return output.hexdigest()

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  coin_hash = hash_calc(sys.argv[1])
  print "The hash Santa is looking for is " + coin_hash + "."

if __name__ == '__main__':
  main()