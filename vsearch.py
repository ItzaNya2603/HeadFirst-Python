def search4letters(phrase: str, letters: str= 'aeiou') -> set:
 """Devuelve el set de letras que se encuentren en una frase"""
 return set(letters).intersection(set(phrase))
