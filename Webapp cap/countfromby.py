class CountFromBy:
    #Estados, el valor que tendra inicialmente y el incremento
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    # Comportamiento, la accion de sumar
    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)