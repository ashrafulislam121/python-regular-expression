#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (7) Case-insensitive search
 
import re
pattern =re.compile('good')


text = 'You are GOOD, but I am not very good.'

list = re.findall("GoOd", text, flags=re.IGNORECASE )
print(list)

list = re.sub("GoOd", "BAD",text, flags=re.IGNORECASE )
print(list)