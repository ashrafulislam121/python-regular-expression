#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (6) Capital letter of month name (must captured_group)
 
import re
date_pattern =re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')


date_string = '12/Feb/2023 I have practiced python RegEx'
#convert to 2023-Feb-12

print("before: ", date_string)

def to_upper(groups):
    return '{} {} {}'.format(groups.group(3),groups.group(2).upper(), groups.group(1))

date_string02 = date_pattern.sub(to_upper, date_string)
print('After: ',date_string02)