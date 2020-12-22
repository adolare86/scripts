#!/usr/bin/awk -f
###############################################################
#                                                             #
#       This scipt is written by Ashok Dolare.                #
#                                                             #
###############################################################
# e.g.  echo 1990 | awk -f leap_year.awk

{

if (($0 % 4 == 0 && $0 % 100 != 0)  || ($0 % 400 == 0))
        print $0" is a leap year"
else
        print $0 " is not a leap year"

}
