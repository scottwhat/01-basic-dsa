list_nums = list(range(1, 12))

odds = []
# standard for loop
for x in list_nums:

    if x % 2 != 0:
        odds.append(x)

print(odds)

# list comprehensions
print([x for x in list_nums if x % 2 != 0])
