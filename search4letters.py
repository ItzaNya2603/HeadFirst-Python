def search4letters

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}  # Empezamos con el diccionario vacío

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)  # La magia: si no existe, crea la cuenta en 0
        found[letter] += 1           # Luego suma 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')