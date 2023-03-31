#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (5) search and replace (must captured_group)
 
import re
date_pattern =re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')


date_string = '12/Feb/2023 I have practiced python RegEx'
#convert to 2023-Feb-12

print("before: ", date_string)

date_string01 = date_pattern.sub(r'\3-\2-\1', date_string)
print('After: ',date_string01)