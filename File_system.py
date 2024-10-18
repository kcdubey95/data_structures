#load file in python
# f= open('file_demo.txt')
# for i in f:
#     print(i)

# file find number of count
# f= open('file_demo.txt')
# count= 0
# for i in f:
#     count= count+1
#     data_line = i.rstrip()
#     if not data_line.endswith('Using'):
#         # print(data_line)
#         continue
#     print(i)

# print('count of line: '+ str(count))

# file_data= f.read()
# print(len(file_data))
# if 'Python' in file_data:

#     print('YES! Python')

try:
    f= open('file.txt')
    count= 0
    for i in f:
        count= count+1
        line = i.rstrip()
        data_line = i.upper()
        print(data_line)
except:
     print('Not abele to open file')