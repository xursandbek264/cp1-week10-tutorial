steps={
    "Mon":6500,
    "Tue":8200,
    "Wed":4300,
    "Thu":10100,
    "Fri":7600
}
sum=0
for i,j in steps.items():
    sum=sum+j
    print(f"{i}: {j}")
print(f"Total: {sum}")
print("Goal reached:")
for i,j in steps.items():
    if j>=8000:
        print(i)