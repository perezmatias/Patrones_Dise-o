from AutoDirector import AutoDirector
from FordBuilder import FordBuilder
from MitsubishiBuilder import MitsubishiBuilder

def main():
    director = AutoDirector()
    ford = FordBuilder()
    Mitsubishi = MitsubishiBuilder()
    director.set_auto_builder(ford)
    director.construct_auto()
    auto1 = director.get_auto()
    director.set_auto_builder(Mitsubishi)
    director.construct_auto()
    auto2 = director.get_auto()
    print(f"El auto A es un {auto1.get_modelo()} de la marca {auto1.get_marca()}")
    print(f"El auto B es un {auto2.get_modelo()} de la marca {auto2.get_marca()}")


if __name__ == "__main__":
    main()
