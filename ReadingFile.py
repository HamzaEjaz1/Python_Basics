text_file =open('text','r')
# print(text_file.readlines()[3])
for lines in text_file.readlines():
    print(lines)

text_file.close()
