print("I am learning Python")

import re

# Long String and Parameterization
des = "Lei"
org = "Shin"

email = f"""
Hello {des},
How are you doing? It's been a while. I am looking forward to see you this Spring.
Take Care.
{org}
"""
print(email)

# # String Playground - Removing all special character and joining the text
s = "Thi$s i$s &@always a &$problem*, which I w@ant to chec%k!. "
s1 = "".join(c for c in s if c.isalnum())
print(s1)

# String Playground - Removing a set of special character from a string
spChar = "!@#$%^&,*()."
s2 = re.sub(f"[{spChar}]", "", s)
print("S2 ---> "+s2)

# Get the first 20 character
s3 = s2[:25]
print(s3)

# Reverse the String
s4 = s3[::-1]
print(s4)

# Remove all whitespace from a string and join the characters using give special character
s5 = re.sub(r'\s', '', s4)
print(s5)

# Replace all whitespace from a string and join the characters using give special character
spChar2 = ","
s6 = s4.replace(' ', spChar2)
print("---", s6)

ss1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# Check if all string from a list is present in a given string
#ls = ["want", "problem", "is"]
ls = ["adipiscing","aliqua","exercitation"]
p = ss1.split(" ")
count = 0
for i in p:
    for j in ls:
        if i == j:
            count = count + 1
            #print(count)
if count == len(ls):
    print(f"Every string in {ls} were present")
else:
    print(f"Every string in {ls} were not present")

# Split every word from word1 and print the first 5 strings as a list.
num1 = 5
print(s2.split()[:num1])

# To identify how many times a word is appeared in a given sentence
word = "This is a cat. This is a dog. dog and cat are very different animals. cat is lazy while dog is active. I love to have both cat and dog"
word1 = word.split(" ")
print("word1 ", word1)
count1 = 0
dic = {}
for w in word1:
    count1 = 0
    for i in range(len(word1)):
        if w == word1[i]:
            count1 = count1+1
    key = w
    val = count1
    dic = {**dic,key:val}
print(dic)

#identify the first Nth word the appear less than 3 times
dic1 = []
num2 = 5
for x in dic:
    #print(x)
    if(dic[x] < 3):
        dic1.append(x)
print(dic1[:num2])

# last index
print(word1[-1])


# key = '1'
# val = 'New'
# dic = {**dic,key:val}
# print(dic)
#dict = {'key1':'geeks', 'key2':'for'}
# adding dict1 (key3, key4 and key5) to dict
#dict1 = {'key3':'geeks', 'key4':'is', 'key5':'fabulous'}
#dict1.update(key3='Shin')
#dict.update(dict1)
#print(dict1)

# existing_dict = {'key1': 'value1', 'key2': 'value2'}
# new_key = 'key3'
# new_value = 'value3'
#
# updated_dict = {**existing_dict, new_key: new_value}
# print(updated_dict)

