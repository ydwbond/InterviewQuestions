data_file = open('Data.txt', 'r')
content = data_file.read()

data_file.close()
print(content)

file_writing = open('data.txt','w')
file_writing.write("2333")
file_writing.close()

test = open('Data.txt','r')
test.readline()

with  open('Data.txt','r') as t:
    f = t.read()
print(f)