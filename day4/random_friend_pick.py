import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanual"]

# Method 1: 
random_friend = random.randint(0, len(friends) - 1)

print(friends[random_friend])

# Method 2:
print(random.choice(friends))
