import re
import string

word = "This is a cat. This is a dog. dog and cat are very different animals. This lazy cat and lazy dog are animals. I love to have both cat and dog"
s1 = re.sub("[.!-@*]", "", word)
print(s1)
print("-----------------------")
word1 = s1.split(" ")
print(word1)
print("-----------------------")

dic = {}
for w in word1:
    count1 = 0
    for i in range(len(word1)):
        if w == word1[i]:
            count1 = count1 + 1
    key = w
    val = count1
    dic = {**dic, key: val}     # To add to dictionary
print(dic)

print("-----------------------")

dic1 = []
for x in dic:
    if (dic[x] < 3):
        dic1.append(x)
print(dic1[:5])

for letter in "Maibam Pritam":
    print(letter)
print("-----------------------")
frn = ["Shin", "Lei", "Hana", "Ryan"]
print(len(frn))
for f in frn:
    print(f)
print("-----------------------")
for i in range(len(frn)):
    print(frn[i])
print("-----------------------")

for i in range(10):
    if i == 0:
        print("First")
    else:
        print(i)
print("-----------------------")


# list=[10, 20, 50, 30, 40, 80, 60]
# for i in range(1, len(list)):
#     print(list[i])

# key = '1'
# val = 'New'
# dic = {**dic,key:val}
# print(dic)

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(4, 5))
