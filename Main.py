from TrianguloFactory import TrianguloFactory
from TrianguloFactoryMethod import TrianguloFactoryMethod

def main():
    metodo = TrianguloFactory()
    triangulo = metodo.create_triangulo(10, 10, 10)

    print(triangulo.get_descripcion())

if __name__ == "__main__":
    main()