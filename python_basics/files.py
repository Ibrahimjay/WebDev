
# f = open('texts.txt', 'r')
# f_content = f.read()
# print(f_content)
# print(f.name)

# f.close()

# with open('texts.txt', 'r') as f:
#     for tetx in f:
#         f_content = f.read()
#         print(f_content, end='')

# print(f.closed)
# print(f.mode)

# with open('texts.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end='')

    # f_contents = f.readline()
    # print(f_contents, end='')

# with open('texts.txt', 'r') as f:
#     for line in f:
#         print(line, end='')


# with open('texts.txt', 'r') as f:
#     word_count = 10
#     f_content = f.read(word_count)
#     print(f_content, end='*')
#     #     f_content = f.read(word_count)

#     # f.seek(30) #set position back to any point base on parameter pass ex seek(0) start at begining
#     f_content = f.read(word_count)
#     print(f_content, end='*') 
    #     f_content = f.read(word_count)

    # while len(f_content) > 0:
    #     print(f_content, end='*')
    #     f_content = f.read(word_count)

    #print(f.tell()) #tell you your current position

with open('texts.txt', 'r') as rf:
    with open('texts2.txt', 'a') as wf:
        for line in rf:
            # word_count = 10
            # f_content = wf.read(word_count)
            #print(f_content, end='')
            wf.write(line) #write from one file to another

