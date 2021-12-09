def main():
    lista = [1, 2, 3]
    chamada(lista)
    print(lista[0])

def chamada(lista):
    lista[0] = 3

if __name__ == "__main__":
    main()