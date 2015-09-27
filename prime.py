#!/usr/bin/env python

import time
import sys

def isDiv3(str_num):
    orig_num = str_num
    while len(str_num) > 1:
        str_num = str(sum(map(int, list(str_num))))
    if str_num in ["3", "6", "9"]:
        print "%s%s is divisible by 3" % (" " * 44, orig_num)
        return True
    else:
        return False

def isDiv2_5(str_num):
    last_char = str_num[-1]
    if last_char in ["0", "2", "4", "6", "8"]:
        print "%s%s is divisible by 2" % (" " * 44, str_num)
        return True
    elif last_char == "5":
        print "%s%s is divisible by 5" % (" " * 44, str_num)
        return True
    return False




def isDivUpToHalf(num, prime_list):
#    print prime_list[4:]
    for i in prime_list[4:]:
        if i <= num/2:
            if num % i == 0:
                print "%s%s is divisible by 3" % (" " * 44, num, i)
                return True
        else:
            return False

try:
    target = int(sys.argv[1])
except:
    print "Usage: %s <target_number>" % sys.argv[0]
    sys.exit()

i = 6
prime_list = [1,2,3,5]
for i in prime_list:
    print "%s is prime. Hardcoded" % (i)

orig_time = time.time()
for i in range(6,target):
    i += 1
    start_time = time.time()
    str_i = str(i)
    if isDiv2_5(str_i):
        continue
    if isDiv3(str_i):
        continue
    if isDivUpToHalf(i, prime_list):
        continue
    prime_list.append(i)
    print "%s is prime. Calculated in %f seconds" % (i, time.time()-start_time)

print("\n\nDone. Found %s prime numbers below %s in a total of %f seconds" % (len(prime_list), target, time.time()-orig_time))