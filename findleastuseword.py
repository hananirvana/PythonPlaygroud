def myfind(sentence):
    words = sentence.split()
    freq = {}
    mylist = []
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        min_freq = min(freq.values())
    for word in words:
        #if(freq[word] == min_freq and len(mylist)<2):
        if freq[word] == min_freq:
            mylist.append(word)
    return mylist

sentence = "This repeated words words words This repeated word is"
print(myfind(sentence))
