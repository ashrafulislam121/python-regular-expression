#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (4) Capture groups using parenthesis ()
 
import re

date_pattern =re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')
date_string = '12/March/2023 hmm 13/JunE/2022 okay 14/FEB/2021 I have practiced python RegEx'

result = date_pattern.match(date_string)


print(result.group(0))
print(result.groups()) #-->touple
day, month, year = result.groups()

for x in range(1,4):
    print(result.group(x))