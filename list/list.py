friends = ['Jane', 'lilian', 'Ken', 'Rodgers']

friends.append('Tony')
friends.insert(2, 'Montana')
del friends[1]

for friend in friends:
    print("Hi my friend " + friend.title())

latest_friend = friends.pop()
print("My recently acquired friend is " + latest_friend)