


#1-usul


votes = ["Samarkand", "Bukhara", "Samarkand", "Khiva", "Samarkand", "Bukhara"]
counts={}
for vote in votes:
     counts[votes]=counts.get(vote,0)+1
print(counts)
print(counts.get("Khiva"))
print(counts.get("Tashkent", 0))



#2-usul
'''votes = ["Samarkand", "Bukhara", "Samarkand", "Khiva", "Samarkand", "Bukhara"]
counts={}
for vote in votes:
    if vote in counts:
       counts[vote]+=1
    else:
        counts[vote]=1
    
print(counts)
print(counts.get("Khiva"))
print(counts.get("Tashkent",0))
















































'''words = ["olma", "anor", "olma", "banan"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0)

print(frequency)'''
