#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (3) Matching all occurances 
 
import re

date_pattern =re.compile(r'\d+/[a-zA-z]+/\d{4}')
date_string = '12/March/2023 hmm 13/JunE/2022 okay 14/FEB/2021 I have practiced python RegEx'

result = date_pattern.findall(date_string)
print(result)