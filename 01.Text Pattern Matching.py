#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (1) Text pattern matching
import re
pattern = '\d+/[a-zA-z]+/\d{4}'
string = '12/Feb/2023 I have practiced python RegEx'

if re.match(pattern, string):
    print("Matched")
else:
    print("Mismatched")