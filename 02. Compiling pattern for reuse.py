#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (2) Compiling pattern for reuse
 
import re
date_pattern =re.compile(r'\d+/[a-zA-z]+/\d{4}')
#date_pattern =re.compile('\\d+/[a-zA-z]+/\\d{4}')

date_string = '12/Feb/2023 I have practiced python RegEx'

if date_pattern.match(date_string):
    print("Matched")
else:
    print("Mismatched")