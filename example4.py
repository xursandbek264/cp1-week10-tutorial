'''votes = ["Samarkand", "Bukhara", "Samarkand", "Khiva", "Samarkand", "Bukhara"]
counts={}
for i in votes:
     counts[i]=counts.get(i,0)+1
print(counts)
print(counts.get("Khiva"))
print(counts.get("Tashkent", 0))'''

words = ["olma", "anor", "olma", "banan"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0)

print(frequency)
