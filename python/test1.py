
WORD1 = input("Enter the first world: ")
WORD2 = input("Enter the second word: ")

list1 = WORD1.split()
list2 = WORD2.split()

list1.sort()
list2.sort()
print(list1)
if " ".join(list1) == " ".join(list2):
    print("Given Two words are Anagram!!")
else:
    print("Given two worlds are not Anagram!")