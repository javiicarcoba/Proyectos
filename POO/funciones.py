def suma(a,b,c):
    print(a+b+c)

class coche:
    def __init__(self, puertas):
        self.puertas = puertas
    
    def sumaPuertas(self):
        self.puertas += 1

def main():
    suma(5,2,6)
    miCoche = coche(2)
    miCoche.sumaPuertas()
    print("Mi coche tiene {} puertas".format(miCoche.puertas))

main()