# for i in range(0,7):
#     for j in range(0,7-i):
#         print(' ',end='')
#     print('0')

# triangle_width = 9
# for i in range(0, triangle_width ):
#     for j in range(0,triangle_width-i):
#         print(' ',end='')
#     for k in range(0,2*i+1):
#         print('*', end='')
#     print('')
x = 2
y = 3
h = 9
l = 11
n = x*h
p = y*l
for i in range(0,n):
    for j in range(0,i+1):
        print(' ',end='')
    for k in range(2*i,p):
        print('*', end='')
    print()