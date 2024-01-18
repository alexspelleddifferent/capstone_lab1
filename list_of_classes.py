#intro
print('Welcome to the class list')
print('Please enter the classes you are taking, separated by enter. click enter again when done')

#empty list
class_list=[]

#input loop
while True:
    month=input()
    if month=='':
        break
    else:
        class_list.append(month)

#output loop
print('The classes you are currently taking are:')
for cls in class_list:
    print(cls)