## Parameter Expansion and String Manipulation

### Default Values

#### syntax

${parameter:-word} #to use a default value
${parameter:=word} #to assign a default value
${parameter:?word} #to display an error if unset or null
${parameter:+word} #to use an alternate value

#### e.g.

##### Get the value of a variable 
```
root@wiki:/home/adolare # test="Hello"
root@wiki:/home/adolare # echo $test
Hello
root@wiki:/home/adolare # echo ${test}
Hello
```

##### Assign variable if null 
```
root@wiki:/home/adolare # echo $test

root@wiki:/home/adolare # echo ${test:=test1}
test1
root@wiki:/home/adolare # echo ${test:=test2}
test1
root@wiki:/home/adolare # echo $test
test1
```

##### Substitute variable if null 
```
root@wiki:/home/adolare # test=""
root@wiki:/home/adolare # echo ${test:-test1}
test1
root@wiki:/home/adolare # echo $test

root@wiki:/home/adolare # test=test2
root@wiki:/home/adolare # echo ${test:-test1}
test2
```

##### to display an error if unset or null
```
root@wiki:/home/adolare # test=""
root@wiki:/home/adolare # echo ${test:?nothing}
bash: test: nothing
root@wiki:/home/adolare # echo $?
1
root@wiki:/home/adolare # test=test1
root@wiki:/home/adolare # echo ${test:?nothing}
test1
root@wiki:/home/adolare # echo $?
0
```

##### to use an alternate value ( Substitute variable if not null )
```
root@wiki:/home/adolare # test=""
root@wiki:/home/adolare # echo $test

root@wiki:/home/adolare # echo ${test:+test1}

root@wiki:/home/adolare # test=test2
root@wiki:/home/adolare # echo ${test:+test1}
test1
```

### Substrings

#### syntax
```
${parameter:offset}
or
${parameter:offset:length}
```
This will expand to up to length character of parameter starting from character positioned at offset. If length is omitted, if will expand till the end of parameter. If offset is negative, the value is used as an offset starting from the end of parameter

#### e.g.

#####  Substrings from index 
```
$str="this is a string with spaces and words"
$echo ${str:10}
string with spaces and words

$echo ${str:10:6}
string

$echo ${str: -5}
words

$echo ${str:(-5)}
words

#####Length of a string 
root@wiki:/home/adolare # echo ${#str}
38
```
Mind that when using a negative offset, you should either leave a whitespace after the colon : or add parenthesis around the number. If you do not do so, bash will believe you are using the form ${parameter:-word} !

### String substitution

#### syntax
```
${parameter/pattern/string}
```
If pattern begins with /, all matches of pattern will be replaced. if pattern begins with % it must match at the end. if pattern begins with # if must match at the beginning. If string is null, matches of pattern are deleted.
```
$ str="this is a string with spaces and words"

##### replace first match
$ echo ${str/i/o}
thos is a string with spaces and words

##### replace all
$ echo ${str//i/o}
thos os a strong woth spaces and words

##### from left
$ echo ${str/#t/i}
ihis is a string with spaces and words

##### from right
$ echo ${str/%s/i}
this is a string with spaces and wordi

##### delete first match
$ echo ${str/i}
ths is a string with spaces and words

##### delete all matches
$ echo ${str//i}
ths s a strng wth spaces and words
```

#### Case Modification
```
${parameter^pattern}
or
${parameter^^pattern}
or
${parameter,pattern}
or
${parameter,,pattern}
```
The versions using ^ will be used to change the letter to uppercase and version using , change the letter to lowercase. When we use the form ^^ or ,, all letter of the string will be modified.

##### e.g.
```
str="this is a string with spaces and words"

##### upper case first
$ echo ${str^}
This is a string with spaces and words

$ echo ${str^^[aeiou]}
thIs Is A strIng wIth spAcEs And wOrds

##### upper case all
$ echo ${str^^}
THIS IS A STRING WITH SPACES AND WORDS

$ echo ${str^^t}
This is a sTring wiTh spaces and words

##### lower case first
$ str2="THIS IS A STRING WITH SPACES AND WORDS"
$ echo ${str2,}
tHIS IS A STRING WITH SPACES AND WORDS

##### lower case all
$ echo ${str2,,}
this is a string with spaces and words

##### lower case for first match
$ echo ${str2,T}
tHIS IS A STRING WITH SPACES AND WORDS

##### lower case for all matches
$ echo ${str2,,T}
tHIS IS A StRING WItH SPACES AND WORDS

$ echo ${str2,,[AEIOU]}
THiS iS a STRiNG WiTH SPaCeS aND WoRDS
```

### Removing Prefix and Suffix

##### To remove prefixes
```
${parameter#word}
or
${parameter##word}
```

##### To remove suffixes
```
${parameter%word}
or
${parameter%%word}
```

##### e.g.
```
$  time="/a/b/c/d/e/mytime.txt"

#####  Delete from left 
$echo ${time#*.}
txt

$echo ${time#*/}
a/b/c/d/e/mytime.txt

$ echo ${time##*/}
mytime.txt

#####  Delete from right 
$ echo ${time%/*}
/a/b/c/d/e

$ echo ${time%%.*}
/a/b/c/d/e/mytime
```

In both cases, when we use only single # or % we will remove the shortest matching pattern from the beginning or the end, respectively.

When using ## or %%, we will remove the longest matching pattern.

### Together
```
#####  Used together with parameter expansions 

root@wiki:~ # A=abc
root@wiki:~ # B=a
root@wiki:~ # echo ${A/#${B}}
bc


#####  Used together with tilde expansion 

root@wiki:~ #  A="./d"
root@wiki:~ # echo $A
./d
root@wiki:~ # echo ${A/#./~}
/root/d



#####  Used together with command substitution 

root@wiki:~ # A="./d"
root@wiki:~ # cd /root/
root@wiki:~ # echo ${A/#./$(pwd)}
/root/d



#####   Used together with arithmetic expansion 

root@wiki:~ #  echo ${A/#./$((10 + 11))}
21/d
```
