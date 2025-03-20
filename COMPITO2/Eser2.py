def count_isolated(lista:list) -> int:
    for numbers in lista:
        ordinata= sorted(lista)
        return len(list(set(ordinata)))