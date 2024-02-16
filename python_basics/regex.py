import re
string = 'Mr Hello World'

#print('s\atring')

pattern = re.compile(r'lo')

matches = pattern.finditer(string)

for match in matches:
    print(match)

print('Fun Section')    
print(dir(string))
print(string.removeprefix('Mr'))
if string.startswith('J'):
    print('your surname')
else:
    print('Not you sir')
