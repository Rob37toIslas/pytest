class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, numero: int, numero2: int):
        result = None
        if numero > numero2:
            result = numero
        elif numero2 > numero:
            result = numero2
        return result
