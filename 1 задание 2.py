word = input()

s = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
t = ['a', 'e', 'i', 'o', 'u','y']

print("Кол-во гласных букв:", len([1 for x in list(word) if x in t]))
print("Кол-во согласных букв:", len([1 for x in list(word) if x in s]))