import random
import string
numbers=['0','1','2','3','4','5','6','7','8','9']
specialcharacters=['!','@','#','$','%','^','&','*','(',')''_']
smallalphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
largealphabets=['A','B','C','D','E','F','G','H','L','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Mylist=[numbers,specialcharacters,smallalphabets,largealphabets]
password=""
pwd_size=int(input("enter size"))
for i in range(pwd_size):
     rand_array = random.choice(Mylist)
     password+=random.choice(rand_array)
print(password)
