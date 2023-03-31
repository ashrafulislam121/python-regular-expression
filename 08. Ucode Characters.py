#Ashraful Islam
#----------------------------
# Python Regular Expression
#----------------------------


### (8) Ucode Characters
 
import re

num_pattern =re.compile('\d') #-->['১', '২', '৩', '৪']
#num_pattern =re.compile('\d+') #-->['১২৩৪']


list = num_pattern.findall('১২৩৪ আমার সোনার বাংলা ')
print(list)