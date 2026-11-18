


stock = {"paracetamol": 20, "vitamin C": 5, "bandage": 12}

#Part A

def sell(stock, item, amount):
    if item not in stock:
        return "not sold here"
    elif stock[item]<amount:
        return "not enough"
    else:
        stock[item]=stock[item]-amount
        return "sold"

test = {"bandage": 4}
assert sell(test, "bandage", 3) == "sold"
assert test == {"bandage": 1}
assert sell(test, "bandage", 2) == "not enough"
assert test == {"bandage": 1}
assert sell(test, "aspirin", 1) == "not sold here"


#Part B
stock = {"paracetamol": 20, "vitamin C": 5, "bandage": 12}

def restock(stock, item, amount):
    if item not in stock:
        stock[item]=stock.get(item, 0)+amount
    else:
        stock[item]+=amount


test = {"bandage": 4}
restock(test, "bandage", 5)
assert test == {"bandage": 9}
restock(test, "aspirin", 2)
assert test == {"bandage": 9, "aspirin": 2}
        