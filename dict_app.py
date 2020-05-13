n=int(input('enter number of students:'))

d={}
for i in range(n):
    name=input('enter student name:')
    marks=int(input('enter marks:'))
    d[name]=marks

print(d)

while True:
    name=input('enter name of the studnet to get marks:')
    marks=d.get(name,-1)

    if marks==-1:
        print('studnet not found')

    else:
        print('student name',name,'and his marks are',marks)

    option=input('do you want to find other names and marks[Yes|No]')

    if option =='No':
        break

print('thanks for using application')
