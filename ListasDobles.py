class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None #Elemento que permite controlar el final de la lista 
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:#actual == true
            print (actual.valor, end=" ")
            actual = actual.siguiente
        print()

    def recorrer_atras(self):
        actual = self.cola
        while actual:
            print (actual.valor, end=" ")
            actual = actual.anterior
        print()

    def buscar(self,valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion =+ 1
        return -1 # En caso de que no este en la lista

    def cantidadElementos(self):
        return self.tamano

    def eliminarAlFinal(self):
        if self.esta_vacia():
            print("No se puede eliminar la lista está vacía.")
            return None
        if self.cabeza == self.cola:  # Si solo hay un nodo en la lista
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.tamano -= 1

    def insertar_final(self,valor):
        nuevo_nodo = Nodo(valor)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        self.tamano += 1

    def insertar_medio(self,valor,posicion):
        #Verificar que la posicion sea valida
        if posicion < 0 or posicion > self.tamano:
            print ("Posicion invalida")
            return

        #Si la posicion es 0, insertar al inicio
        if posicion == 0:
            self.agregar_inicio(valor)
            return

        

        #Si la posicion corresponde al final
        if posicion == self.tamano:
            self.insertar_final(valor)
            return

        nuevo_nodo = Nodo(valor)

        actual = self.cabeza

        #Llegar al nodo que actualmente ocupa la posicion
        for i in range(posicion):
            actual = actual.siguiente

        anterior = actual.anterior

        nuevo_nodo.anterior = anterior
        nuevo_nodo.siguiente = actual

        anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self.tamano += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("No se puede eliminar en una lista vacia")
            return None

        valor_eliminado = self.cabeza.valor

        #Caso que existe solo un nodo
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        self.tamano -= 1

        return valor_eliminado

    def eliminar_medio(self, posicion):
        if self.esta_vacia():
            print("No se puede eliminar en una lista vacia")
            return None
        
        if posicion < 0 or posicion >= self.tamano:
            print ("Posicion invalida")
            return None

        #Si es el primer elemento 
        if posicion == 0: 
            return self.eliminar_inicio()

        #Si es el ultimo elemento
        if posicion == self.tamano -1:
            return self.eliminarAlFinal()

        actual = self.cabeza

        for i in range(posicion):
            actual = actual.siguiente

        valor_eliminado = actual.valor

        anterior = actual.anterior
        siguiente = actual.siguiente

        anterior.siguiente = siguiente
        siguiente.anterior = anterior

        self.tamano -= 1

        return valor_eliminado

    def temperaturaMayor(self):
        if self.esta_vacia():
            print("No se puede recorrer una lista vacia")
            return None

        actual = self.cabeza
        mayor = actual.valor
        while actual:#actual == true
            if (actual.valor > mayor):
                mayor = actual.valor
            actual = actual.siguiente
        return mayor

    def temperaturaMenor(self):
        if self.esta_vacia():
            print("No se puede recorrer en una lista vacia")
            return None
        
        actual = self.cabeza
        menor = actual.valor
        while actual:#actual == true
            if (actual.valor < menor):
                menor = actual.valor
            actual = actual.siguiente
        
        return menor

    def promedioTemperatura(self):
        if self.esta_vacia():
            return 0
        
        suma = 0
        actual = self.cabeza

        while actual:
            suma += actual.valor
            actual = actual.siguiente

        return suma / self.tamano



if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = ListaDoblementeEnlazada()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.agregar_inicio(valor)
                    lista.recorrer_adelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")
            print(f"promedio  {lista.promedioTemperatura()}")
            lista.temperaturaMayor()
            lista.temperaturaMenor()
            with open("Reporte.txt", "w") as archivo:
                archivo.write("Elaborado por: German Nuñez Mora y Jose Valerio Rodriguez\n\n")
                archivo.write("====================================\n")
                archivo.write("    REPORTE DE TEMPERATURAS\n")
                archivo.write("====================================\n\n")
                archivo.write(
                "Cantidad de temperaturas: "
                + str(lista.cantidadElementos())
                + "\n"
                "Temperatura promedio :"
                + str(lista.promedioTemperatura())
                + "\n"
                "Temperatura mayor: "
                + str(lista.temperaturaMayor())
                + "\n"
                "Temperatura menor: "
                + str(lista.temperaturaMenor())
                + "\n"
                
        )




    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()