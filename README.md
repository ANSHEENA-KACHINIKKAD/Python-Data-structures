# Python-Data-structures
This repository contains Python code demonstrating the use of lists, dictionaries, sets, and tuples.

## Data structure creation and simple element addition task

1.LIST
===============================================================
Q1.Create a list of 5 random numbers and print the list.

code:
      
    import random as r
    from random import randint
    l1=[]
    for i in range(5):
    l1.append(randint(11,99))
    print(l1)

Q2. Insert 3 new values to the list and print the updated list

Code:

    for i in range(3):
    num=int(input("enter 3 random number:"))
    l1.append(num)
    print(l1) 
    
Q3.Try to use a for loop to print each element in the list.

code:

    for i in range (len(l1)):
    print(l1[i])


Result:

![Screenshot (229)](https://github.com/user-attachments/assets/5be2a780-3f05-49aa-aa26-4a2d8c690e84)

 

2.DICTIONARY
===============================================================
Q1.Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively. 

code:
      
    dict1={'name':'John','age':25,'address':'New york'}

Q2.Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'. 

Code:

    dict1['phone']='1234567890' 
    
Q3.Print Dictionary.

code:

    print(dict1)


Result:

![Screenshot (230)](https://github.com/user-attachments/assets/8a977471-cb58-4bd8-af68-c17c94bf6ead)



3.SET
===============================================================
Q1.Create a set with values 1, 2, 3, 4, and 5.

code:
      
    set1={1,2,3,4,5}

Q2.Add the value 6 to the set created in Q1. 

Code:

    set1.add(6) 
    
Q3. Remove the value 3 from the set created in Q1. And print set.

code:

    set1.remove(3) 
    print(set1)


Result:

![Screenshot (231)](https://github.com/user-attachments/assets/cda82e3b-9593-4dd3-b178-417073d4675a)




4.TUPLE
===============================================================
Q1.Create a tuple with values 1, 2, 3, and 4.

code:
      
    tuple1=(1,2,3,4)

Q2.Print the length of the tuple created in Q1.

Code:

    print(len(tuple1)) 
    
Result:

![Screenshot (232)](https://github.com/user-attachments/assets/7dcb8357-620a-478b-bdde-55e9a5b47d07)


## Note:

This project explores fundamental Python data structures: lists, dictionaries, sets, and tuples.

* Lists: Ordered collections of elements, allowing for duplicates.
    Demonstrated by creating a list of random numbers, adding new elements, and iterating through the list.

* Dictionaries: Collections of key-value pairs.
    Demonstrated by creating a dictionary representing a person and adding a new key-value pair.

* Sets: Unordered collections of unique elements.
    Demonstrated by creating a set of numbers, adding a new element, and removing an existing element.

* Tuples: Ordered, immutable collections.
    Demonstrated by creating a tuple and determining its length.

This work provides a basic understanding of these data structures and their common operations.










