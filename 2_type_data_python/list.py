#Create a list
mylist = ["jhon", "doe", "foo", "foo","bar"]
print("This is mylist default : ", mylist)
#or by function
mylist_2 = list(("jhon", "doe", "foo","foo", "bar")) 
print("This is mylist create with function : ", mylist_2)

#Add Item into the list
mylist.append("zack")
print("This is mylist default append : ", mylist)

#Remove Item in the list by value 
mylist.remove("zack")
print("This is mylist default remove : ", mylist)

#Remove Item in the list by index
mylist.append("zack")
mylist.pop(4)
print("This is mylist default then pop : ", mylist)

#Change Item inside list
mylist[0] = "Jhon Change"
print("This is mylist change: ", mylist)
#Return Error : out of index range
#mylist[5] 

#Count the item inside list
count = mylist.count("foo")
print("This is total \"foo\" in the list : ", count)

#Can bee loop
num = 0
for item in mylist :
    num = num + 1
    print(f"--- this is item number {num} contain {item}")


# This is Nested List
nested = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print Number 1
number_1  = nested[0][0]
print("This is nested : " , number_1 )

# Print through number 1 - 9
for lists in nested :
    print()
    for item in lists :
        print(f"{item} |", end=' ')