#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/4

import sys
import hashlib

def hash_calc(filename):
  #input is used to make the md5, output is the result
  input = open(filename, 'rU').read()
  #first hash the file input to prove it works
  output = hashlib.md5(input)
  return output.hexdigest()

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  coin_hash = hash_calc(sys.argv[1])
  print "The hash Santa is looking for is " + coin_hash + "."

if __name__ == '__main__':
  main()