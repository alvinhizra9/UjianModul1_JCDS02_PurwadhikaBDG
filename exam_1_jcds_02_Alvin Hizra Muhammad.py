# Soal 1

# def Hashtag(text):
#     text_count = text.count('')
#     if text_count <=1 :
#         print(False)
#     else:
#         text_split = text.split(' ')
#         z=''
#         y=''
#         for item in text_split:
#             item = item.capitalize()
#             z += item
#         y += '#' + z
#         y_count = y.count('')
#         if y_count >141 :
#             print(False)
#         else:
#             print(y)
# Hashtag(" Hello there how are you doing")
# Hashtag(" Hello World " )
# Hashtag("")
# Hashtag("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


# Soal 2

# def create_phone_number(n):
#     print('({}{}{}) {}{}{}-{}{}{}{}'.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9]))
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Soal 3

# def Sort_odd_even(list):
#     listganjil = []
#     listgenap = []
#     listbaru = []
#     numganjil,numgenap=0,0
#     for item in list:
#         if item % 2 == 1:
#             listganjil.append(item)
#         else:
#             listgenap.append(item)
#     listganjil.sort()
#     listgenap.sort(reverse=True)
#     for item in list:
#         if item % 2 == 1:
#             listbaru.append(listganjil[numganjil])
#             numganjil+=1
#         else:
#             listbaru.append(listgenap[numgenap])
#             numgenap+=1
#     print(listbaru)
# Sort_odd_even([5, 3, 2, 8, 1, 4])

# Soal 4
# def hollowTriangle(line):
#     kali = 1
#     for bar in range(line):
#         for col in range(bar,bar+1):
#             if col == line-1:
#                 print('#'*(line+(line-1)))
#             elif col+1>=3:
#                 print('_'*(line-(col)-1) + '#_' + '__'*kali +'#'+'_'*(line-(col)-1))
#                 kali+=1
#             else:
#                 print('_'*(line-(col)-1) + '#_'*(col+1) + '_'*(line-(col)-2))
# hollowTriangle(1)
# hollowTriangle(2)
# hollowTriangle(3)
# hollowTriangle(4)
# hollowTriangle(5)
# hollowTriangle(6)