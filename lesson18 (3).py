'''Create new dictionary where you have 10 students and each of them have rating(1-10)'''

# students = {'Areg Grigoryan':8,'Arshak Tusinyan':4,'Vahagn Tusinyan':9,'Gexam Hakobyan':6,'Xachatur Martirosyan':8,'Jorik Mkrtchyan':10,'Harut Avetisyan':5,'Liparit Hambarcumyan':8,'Aleksandr Afrikyan':3,'Mikael Saribekyan':4}
# print(students)

'''Create python program which will calculate the arithmetic average of rating students.'''


# student ={1:'Arshak Tusinyan',3:'Areg Grigoryan',7:'Gexam Hakobyan',6:'Mikael Saribekyan', 2:'Xachatur Martirosyan'}
# count = 0
# for i in student:
# 	count += i
# print(count)	
# res = len(student)
# res1 = count / res
# print(res1)



'''Create a python program which will say you who they are good and bad students.'''

# students = {'Areg Grigoryan':8,'Arshak Tusinyan':4,'Vahagn Tusinyan':9,'Gexam Hakobyan':6,'Xachatur Martirosyan':8,'Jorik Mkrtchyan':10,'Harut Avetisyan':5,'Liparit Hambarcumyan':8,'Aleksandr Afrikyan':3,'Mikael Saribekyan':4}
# max_students = max(students.values())
# min_students = min(students.values())
# print(max_students,min_students)
# for i in students:
# 	if students[i] == max_students:
# 		print(i,max_students)
# 	if students[i] == min_students:
# 		print(i,min_students)

'''Create a python program which will say who have 5 or great rating in your Students.'''

# students = {'Areg Grigoryan':8,'Arshak Tusinyan':4,'Vahagn Tusinyan':9,'Gexam Hakobyan':6,'Xachatur Martirosyan':8,'Jorik Mkrtchyan':10,'Harut Avetisyan':5,'Liparit Hambarcumyan':8,'Aleksandr Afrikyan':3,'Mikael Saribekyan':4}
# for i in students:
# 	if students[i] > 5:
# 		print(i,'good')

'''Create a python program which will say who have 5 or little rating in your Students.'''
# students = {'Areg Grigoryan':8,'Arshak Tusinyan':4,'Vahagn Tusinyan':9,'Gexam Hakobyan':6,'Xachatur Martirosyan':8,'Jorik Mkrtchyan':10,'Harut Avetisyan':5,'Liparit Hambarcumyan':8,'Aleksandr Afrikyan':3,'Mikael Saribekyan':4}
# for i in students:
# 	if students[i] < 5:
# 		print(i,'lol')


'''Create a python program which will say if your dictionary have this name print name and rating.'''

# students = {'Areg Grigoryan':8,'Arshak Tusinyan':4,'Vahagn Tusinyan':9,'Gexam Hakobyan':6,'Xachatur Martirosyan':8,'Jorik Mkrtchyan':10,'Harut Avetisyan':5,'Liparit Hambarcumyan':8,'Aleksandr Afrikyan':3,'Mikael Saribekyan':4}
# for name, numbers in students.items():
#  	print(name,numbers)

'''Create a new dictionary: For example… s = 'a,2,b,5,c,8,a,4,e,11' {“a”:6,”b”:5,”c”:8,”e”:11}'''

# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# c = {}

# for i in range(0,len(s)-1,2):
# 	if s[i] in c:
# 		c[s[i]] = int(c[s[i]]) + int(s[i+1])
# 	else:
# 		c[s[i]] = s[i+1]
# print(c)	


'''Create a dictionary from a string. Track the count of the letters from the string.'''


# word = 'exercises'
# c = {}
# for i in  word:
# 	c[i] = word.count(i)
# print(c)	

'''Remove all duplicate items in list'''

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []
# for i in old_list:
# 	if i not in new_list:
# 		new_list.append(i)
# print(new_list)
