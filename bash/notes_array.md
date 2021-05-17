## Array

An array is a variable containing multiple values may be of same type or of different type. There is no maximum limit to the size of an array, nor any requirement that member variables be indexed or assigned contiguously. Array index starts with zero.

#### Creating arrays

Indirect declaration is done using the following syntax to declare a variable:
```
name[index]=value
```
- name is any name for an array
- index could be any number or expression that must evaluate to a number greater than or equal to zero.You can declare an explicit array using declare -a arrayname.

Explicit declaration of an array is done using the declare built-in
```
declare -a ARRAYNAME 
ARRAYNAME=(value1 value2 ... valueN) 
```
#### Print the Whole Bash Array

There are different ways to print the whole elements of the array. If the index number is @ or *, all members of an array are referenced. You can traverse through the array elements and print it, using looping statements in bash.

```
ARRAY=(one two three)
echo ${ARRAY[*]} #All of the items in the array
echo $ARRAY[*] #output will be "one[*]"
echo ${ARRAY[2]} #output will be "three"
```
#### Length of the Bash Array
```
ARRAY=(one two three)
echo ${#ARRAY[@]} #Number of elements in the array
echo ${!ARRAY[@]} All of the indexes in the array
echo ${#ARRAY} #Number of characters in the first element of the array
```

#### Extraction by offset and length for an array
```
ARRAY=(one two three four five six)
echo ${ARRAY[@]:3:2} #output will be "five six"
echo ${ARRAY[2]:1:3} #output will be "hre"
```

#### Search and Replace in an array elements
```
ARRAY=(one two three four five six)
echo ${ARRAY[@]/thr/fr} #output will be "one two free four five six"
```

#### Add and remove an element to an existing Bash Array
```
ARRAY=(one two three)
ARRAY=(${ARRAY[@]} four five) #output will be "one two three four five"
unset ARRAY[2] #output will be "one two four five"
```

#### Remove Bash Array Elements using Patterns
```
ARRAY=(one two three four five six)
A1=(${ARRAY[@]/thr*/}) #output will be "one two four five six"
```

#### Copying an Array
```
ARRAY=(one two three)
A1=(${ARRAY[@]})
```

#### Concatenation of two Bash Arrays
```
ARRAY1=(one two three)
ARRAY2=(four five six)
ARRAY=(${ARRAY1[@]} ${ARRAY2[@]})
```

#### Deleting an Entire Array
```
ARRAY=(one two three)
unset ARRAY
```

#### Load Content of a File into an Array
```
file=($(cat filename))
```
