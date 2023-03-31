#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (9) Unwanted space remove
 
import re

text = 'Life      is       beautiful'
pattern = re.compile(r'\s+')

result = pattern.sub(' ', text)
print(result)
#Life is beautiful