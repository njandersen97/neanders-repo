while True:
    print('Who are you?')
    name = input()
    if name != 'Nelson':
        continue
    print('Hello, Nelson. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')