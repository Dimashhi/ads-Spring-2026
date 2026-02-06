#1
i=0
while i<5:
    i+=1
    if i==3:continue
    print(i)
#2
i=0
while i<6:
    i+=1
    if i%2==0:continue
    print(i)
#3
i=0
word="hello"
while i<len(word):
    char=word[i]
    i+=1
    if char=='l':continue
    print(char)
#4
nums=[1,-2,3]
i=-1
while i<2:
    i+=1
    if nums[i]<0:continue
    print(nums[i])
#5
i=0
while i<15:
    i+=1
    if i%5==0:continue
    print(i)