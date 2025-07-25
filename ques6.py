from collections import Counter

x = int(input())  
shoe_sizes = list(map(int, input().split()))  
n = int(input())  
inventory = Counter(shoe_sizes)

earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1  

print(earnings)
