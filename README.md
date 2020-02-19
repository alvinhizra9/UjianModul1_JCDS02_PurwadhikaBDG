# Soal dan Jawaban Ujian Modul 1 Data Science Purwadhika
Soal dan jawaban ujian modul 1 (basic python) Program Job Connector Data Science Batch 2 Purwadhika Kampus Bandung.

### Soal 1
Create a function called Hashtag that generate hashtag which accepting string separated by space as presented in the below with following rules.
- It must start with a hashtag (#). 
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return False
- If the input or the result is an empty string it must return False. 

##### Solution
```
def Hashtag(text):
    text_count = text.count('')
    if text_count <=1 :
        print(False)
    else:
        text_split = text.split(' ')
        z=''
        y=''
        for item in text_split:
            item = item.capitalize()
            z += item
        y += '#' + z
        y_count = y.count('')
        if y_count >141 :
            print(False)
        else:
            print(y)
```
###### Let's try:
```
Hashtag(" Hello there how are you doing")
Hashtag(" Hello World " )
Hashtag("")
Hashtag("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
```
###### Outputs will be :
```
#HelloThereHowAreYouDoing
#HelloWorld
False
False
```

### Soal 2
Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

###### Solution
```
def create_phone_number(n):
    print('({}{}{}) {}{}{}-{}{}{}{}'.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9]))
```

###### Let's try:
```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
```
###### Outputs will be :
```
(123) 456-7890
```

### Soal 3
You are given a list of integers. Your task is to sort odd numbers within the list in ascending order, and even numbers in descending order but keep all the odds or the evens number in the same index group.
###### Solution
```
def Sort_odd_even(list):
    listganjil = []
    listgenap = []
    listbaru = []
    numganjil,numgenap=0,0
    for item in list:
        if item % 2 == 1:
            listganjil.append(item)
        else:
            listgenap.append(item)
    listganjil.sort()
    listgenap.sort(reverse=True)
    for item in list:
        if item % 2 == 1:
            listbaru.append(listganjil[numganjil])
            numganjil+=1
        else:
            listbaru.append(listgenap[numgenap])
            numgenap+=1
    print(listbaru)
```

###### Let's try:
```
Sort_odd_even([5, 3, 2, 8, 1, 4])
```
###### Outputs will be :
```
[1, 3, 8, 4, 5, 2]
```

### Soal 4
Create a function hollowTriangle(height) that returns a hollow triangle of the correct height or level.

###### Solution
```
def hollowTriangle(line):
    kali = 1
    for bar in range(line):
        for col in range(bar,bar+1):
            if col == line-1:
                print('#'*(line+(line-1)))
            elif col+1>=3:
                print('_'*(line-(col)-1) + '#_' + '__'*kali +'#'+'_'*(line-(col)-1))
                kali+=1
            else:
                print('_'*(line-(col)-1) + '#_'*(col+1) + '_'*(line-(col)-2))
```
###### Let's try:
```
hollowTriangle(1)
```
###### Outputs will be :
```
#
```
###### Let's try:
```
hollowTriangle(2)
```
###### Outputs will be :
```
_#_
###
```
###### Let's try:
```
hollowTriangle(3)
```
###### Outputs will be :
```
__#__
_#_#_
#####
```
###### Let's try:
```
hollowTriangle(4)
```
###### Outputs will be :
```
___#___
__#_#__
_#___#_
#######
```
###### Let's try:
```
hollowTriangle(5)
```
###### Outputs will be :
```
____#____
___#_#___
__#___#__
_#_____#_
#########
```
###### Let's try:
```
hollowTriangle(6)
```
###### Outputs will be :
```
_____#_____
____#_#____
___#___#___
__#_____#__
_#_______#_
###########
```

> Thank you for Reading 😊
> Pull it. Run it. Evaluate it. 🔥🔥🔥
