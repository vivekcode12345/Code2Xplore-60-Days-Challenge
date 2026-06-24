# num=[1,2,3,4,5]
# num2=[i*i for i in num]
# print(num2)
#
# num=[i for i in range(1,11)]
# print(num)

# :List of fruites
# fruits=['Apple','mango','banana','grape']
# print(fruits)
# new_fruits=[]
# for i in fruits:
#     if "a" in i:
#         new_fruits.append(i)
#         print(new_fruits)

fruits=['apple','mango','banana','grape']
new_fruits=[i for i in fruits if 'a' in i]
new_fruits1=[i.upper() for i in fruits if 'a' not  in i]
new_fruits2=[fruits[i] for i in range(3)]
new_fruits3=[i.upper() for i in fruits if len(i)<6 ]

print(new_fruits3)
