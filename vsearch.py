def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Devuelve el conjunto de letras de 'letters' encontradas en 'phrase'."""
    found = set(letters).intersection(set(phrase))
    return sorted(list(found))  # Esto convierte el conjunto en una lista alfabética, pa que ya no salga desordewnado
