# try:
#     var  = 'hello world'
#     print(varsi)
# except NameError:
#     print('Check variable name')

# try:
#     num  = int(input('Enter a number: '))
#     print(num*num)
# except ValueError:
#     print('Enter an integer eg 1,2,3...')

f = open('text.txt', 'r')
# file_content = f.write('hello world')
file_contents = f.read()
print(f.name)
print(file_contents)

f.close()
