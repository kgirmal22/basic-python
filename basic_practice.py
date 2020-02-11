# s=input('Enter a string: ')
# print('you enter: ' + s)
# # string operations
# print('string in upper case: ' + s.upper())
# print('string in lower case: ' + s.lower())
# print('is string in uppercase :'+ str(s.isupper()))
# print('is string in lowercase: '+ str(s.islower()))
# print('length of string is '+ str(len(s)))
#
# p=input('enter the index you want to know:')
# print('on index ' + str(p) +' letter is ' + s[int(p)])
#
# # functions on number
# x,y=input('enter two values').split()
# print('maximum number in both is '+ max(x,y))
# print('minimum number in both is ' + min(x,y))
# print('absolute value of -6 is '+ str(abs(-6)))
# print(pow(2,3))
# print(round(9.5))
# # floor function is same as round function but it just takes base value

# functions used in list (append,pop,insert,remove,sort,extend,count,clear,copy,reverse)
list=['Akash','Amey','Amruta',2,3,True,'om']
list.append('shivay')
print(list)

list.insert(4,'om')
print(list)

list.remove(True)
print(list)

num=[8,9,7]
list.extend(num)
print(list)

num.sort()
print(num)
# if we apply sort function on list it won't sort the list bcoz it contains different data type values(num and str)

list.reverse()
print(list)
s=list.count('om')
print(s)
