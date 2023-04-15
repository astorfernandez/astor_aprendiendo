
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(self.nombre + ' dice guau')


class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def maullar(self):
        print(self.nombre + ' dice miau')


if __name__ == '__main__':
    coca = Perro('Coca')
    chanchi = Gato('chanchi')
    nico = Gato('Nico')

    nico.maullar()
    coca.ladrar()
