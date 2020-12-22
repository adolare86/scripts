#!/usr/bin/awk -f
###############################################################
#                                                             #
#       This scipt is written by Ashok Dolare.                #
#                                                             #
###############################################################
# e.g. echo -e "1\n2\n3\n4\n5" | awk -f patterns.awk

END {

print "pattern. 1\n"
for(i=1; i<=NR; i++) {
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""


print "pattern. 2\n"
for(i=NR; i>=1; i--) {
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 3\n"
for(i=1; i<=NR; i++) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 4\n"
for(i=NR; i>=1; i--) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 5\n"
for(i=1; i<=NR; i++) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        for(k=2; k<=i; k++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 6\n"
for(i=NR; i>=1; i--) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        for(k=2; k<=i; k++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 7\n"
for(i=1; i<=NR; i++) {
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
for(i=NR; i>=1; i--) {
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 8\n"
for(i=1; i<=NR; i++) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
for(i=NR; i>=1; i--) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        print ""
}
print ""

print "pattern. 9\n"
for(i=1; i<=NR; i++) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        for(k=2; k<=i; k++) {
                printf "#"
        }
        print ""
}
for(i=NR; i>=1; i--) {
        for(j=NR; j>=i; j--) {
                printf " "
        }
        for(j=1; j<=i; j++) {
                printf "#"
        }
        for(k=2; k<=i; k++) {
                printf "#"
        }
        print ""
}

}
