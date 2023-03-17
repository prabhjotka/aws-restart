"""mylist=["apple","banana","orange"]
#print(mylist)
#mylist.append("grapes")
for x in mylist:
 print(x)
 
 
mylist[0]="hello"
print(mylist)
mylist=("apple","orage","milkshake")
a=len(mylist)
#print (a)
i=0
while i<a:
   print (mylist[i])
   i=i+1
    
student={
    "name":"prab","class":"computersc.","age":35,"inclass":True
    
}
for i ,z in student.items() :
     print(i,z)
 """
l = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for i in l:
    print ("{} is of data type {}".format(i,type(l)))
