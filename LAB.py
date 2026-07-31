#Laboratorio 1 31/7
import os
import time


class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregarAlInicio(self, valor):
        new_nodo = Nodo(valor)
        new_nodo.next=self.head
        self.head=new_nodo

    def agregarAlFinal(self, valor):
        new_nodo = Nodo(valor)
        if (self.head is None):
            self.head = new_nodo 
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_nodo
        
    def agregarEnPosicion(self, valor, posicion):
        new_nodo = Nodo(valor)
        if (self.head is None):
            self.head = new_nodo
            return
        current = self.head
        cantidad = 0
        while (current is not None and cantidad != posicion -1):
            current = current.next
            cantidad += 1
        if cantidad == posicion -1 :
            new_nodo.next = current.next
            current.next = new_nodo



    def AgregarEnMedio(self,valor):
        new_nodo = Nodo(valor)
        if (self.head is None):
           self.head = new_nodo
           return

        slow = self.head
        fast = self.head

        while (slow is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        new_nodo.next = slow.next
        slow.next = new_nodo


    def mostrar(self):
            current = self.head
            while(current):
                print(current.valor, end=" -> ")
                current = current.next
            print("None")

    def eliminarAlInicio(self):
        if( self.head is None):
            print("La lista está vacía.")
            return
        self.head = self.head.next


    def eliminarAlFinal(self):
        if( self.head is None):
            print("La lista está vacía.")
            return

        if self.head.next is None :
           self.head = None
           return

        current = self.head

        while current.next.next is not None :
            current = current.next

        current.next = None

    def eliminarEnPosicion(self, posicion):
        if( self.head is None):
            print("La lista está vacía.")
            return

        if posicion == 0:
            self.head = self.head.next
            return
        current = self.head
        contador = 0

        while current.next is not None and contador > posicion -1:
            current = current.next
            contador += 1

        if current is None :
            print("La posicion esta fuera del rango")

        current.next = current.next.next

    def estaVacia(self):
        if( self.head is None):
            print("La lista está vacía.")
        else:
            print("La lista no está vacía.")

    def display(self):
        current = self.head
        if( self.head is None):
            print("La lista está vacía.")
            return

        while(current):
             print(current.valor, end=" -> ")
             current = current.next
        print("None")

    def busacarElemento(self,buscado):
        if( self.head is None):
            print("La lista está vacía.")
            return
        current = self.head
        posicion = 0

        while current is not None and current.valor != buscado :
            current = current.next
            posicion += 1

        if current is not None and current.valor == buscado :
            print (f"Elemento {buscado} encontrado en la lista : ")
            print (f"Se encuentra en al posicion : {posicion + 1}")
        else:
            print("No se encontro el elemento en la lista")

        

                
            

lista = ListaEnlazada()

repetir = True

while repetir :
    os.system('cls')  #es posible que no funcione si es u
    print("\n===== MENÚ =====")
    print("1. Agregar al inicio")
    print("2. Agregar al final")
    print("3. Agregar en una posición")
    print("4. Agregar en medio")
    print("5. Eliminar al inicio")
    print("6. Eliminar al final")
    print("7. Eliminar en una posición")
    print("8. Mostrar lista")
    print("9. Verificar si está vacía")
    print("10. Buscar elemento")
    print("0. Salir")

    opcion = int(input("Digite una opcion: "))

    match opcion:
        case 1:
            valor = int(input("Ingrese el valor: "))
            lista.agregarAlInicio(valor)

        case 2:
            valor = int(input("Ingrese el valor: "))
            lista.agregarAlFinal(valor)
            

        case 3:
            valor = int(input("Ingrese el valor: "))
            posicion = int(input("Ingrese la posicion: "))
            lista.agregarEnPosicion(valor, posicion -1)

        case 4:
            valor = int(input("Ingrese el valor: "))
            lista.AgregarEnMedio(valor)

        case 5:
            lista.eliminarAlInicio()
            

        
        case 6:
            lista.eliminarAlFinal()
            

        
        case 7:
            posicion = int(input("Ingrese la posicion a eliminar: "))
            lista.eliminarEnPosicion(posicion)
            time.sleep(3)

        
        case 8:
            lista.display()
            time.sleep(4)

        case 9:
            lista.estaVacia()
            time.sleep(3)

        case 10:
            bucar = int(input("Digite el valor a buscar en la lista: "))
            lista.busacarElemento(bucar)
            time.sleep(3)
        
        case 0:
            print("Adios")
            repetir = False

        case _:
            valor = int(input("Opcion invalida"))
        


        
        
        

    