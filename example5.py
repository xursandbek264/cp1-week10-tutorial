#Part a

reviews = ["Good coffee","very GOOD tea", "good food and good coffee", "Tea is very hot"]
def count_words(text):
    counts={}

    words=text.lower().split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    return counts


print(count_words(reviews[2]))






#Part b

reviews = ["Good coffee","very GOOD tea", "good food and good coffee", "Tea is very hot"]
text=" ".join(reviews)
print(text)

counts=count_words(text)


for word, count in counts.items():
    if count>=2:
        print(f"")


























