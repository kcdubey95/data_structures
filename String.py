s = 'Hello'
print(s[::])
print(s[2:])
print(s[::-1])
print(s[2:5:2])

print value using for loop
for e1 in s:
    print(e1)

get the value from index
print(s[0])

lower the  string
print(s.lower())

upper the sting
print(s.upper())

check the value is upper or lower reture true or false

print(s.islower())
print(s.isupper())


remove white space or extraspace from all side

str1 = '   Krishna     '
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())



# parsing and extracting
str2 = ' A common format that peter.parker@zylker.com uses both first and last name'
find_str = str2.find('@')

next_str_stop = str2.find(' ',find_str)
print(str2[find_str:next_str_stop])
# print(next_str_stop)

str_data = 'Perfect-Plan-B:0.7541'
f_no = str_data.find(':')
data = str_data[f_no+1:f_no+7]
print(float(data))

