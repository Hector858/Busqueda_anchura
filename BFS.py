#Se importa la librería queue de python
from queue import Queue

class Grafo:
    """
    Una clase que representa los algoritmos de búsqueda 
    para recorrer los nodos de un grafo

    ...

    Atributos
    ----------
    numero_de_nodos : int
            indica el número de nodos que va a llevar el grafo
    dirigido : boolean
            Si el grafo se encuentra en dirigido (True) o no dirigido (False)

    Métodos
    -------
    __init__(self, numero_de_nodos, dirigido=Treu):
        Constructor de la clase Grafo
        
        Crea el diccionario de la lista de adyacencia seteando cada nodo.
   añadir_arista(self, nodo1, nodo2, peso):
        Método que agrega una arista al grafo.
        
        Si el primer grafo no se encuentra dirigido se pasa al siguiente
   imprimir_lista_adyacencia(self):
        Método que imprime la lista de adyacencia.
        
        Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
    """
    # Constructor
    def __init__(self, numero_de_nodos, dirigido=True):#self es uno mismo
        '''
        Constructor de la clase Grafo
        
        Crea el diccionario de la lista de adyacencia seteando cada nodo.
        
        
            Parámetros: 
            ----------
            numero_nodos: int   
                    Número de nodos que posee el grafo
            dirigido: boolean 
                    Si el grafo es dirigido (true) o no dirigido (false)
        '''
        self.m_numero_de_nodos = numero_de_nodos#El número de nodos
        self.m_nodos = range(self.m_numero_de_nodos)#genera un rango del número de nodos
		
        #Indica dentro del contructor si es dirigido o no dirigido
        self.m_dirigido = dirigido
		
        # Representación grafo - Lista de adyacencia
        # En python esto es un diccionario e implementar una lista de adyacencia
        self.m_lista_adyacencia = {
            node: set() for node in self.m_nodos#Hace un ciclo de repetición en los nodos para setearlos cada uno
            }
        
    # Agrega una arista al grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        '''
        Método que agrega una arista al grafo.
        
        Si el primer grafo no se encuentra dirigido se pasa al siguiente
        
        Se definen los nodos y el peso va a hacer un valor opcional (puede ser cualquiera)
        
            Parámetros:
            ----------
            nodo1 : int 
                    Nodo 1 o de inicio
            nodo2 : int
                    Nodo 2 o de fin
            peso : int 
                    Peso de la arista
                    
                    Este atributo puede tener un valor opcional (proporcionado por uno mismo)
        '''
        #Agregar una arista del nodo 1 a la lista de adyacencia
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        
        #Si el grafo no esta dirigido se agrega la arista al otro nodo
        if not self.m_dirigido:
            #Agregar una arista del nodo 2 de la lista de adyacencia
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))  
        
    # Imprimir la representación del grafo
    def imprimir_lista_adyacencia(self):
        ''' 
        Método que imprime la lista de adyacencia por medio de una matriz.
        
        Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
        '''
        #Realiza un recorrido en la lista de adyacencia a través de sus llaves
        for llave in self.m_lista_adyacencia.keys():
            #Imprime cada uno de los nodos que se encuentren en la lista de adyacencia
            #colocan donde se dirigen los nodos y su peso
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
            
#Main de la clase
if __name__ == "__main__":
        
    # Crea una instancia de la clase `Grafo`
    # Este grafo es no dirigido y tiene 5 nodos
    g = Grafo(5, dirigido=False)
    
    # Agrega las aristas del grafo
    g.agregar_arista(0,1)# Agrega las aristas (0,1) con peso=1
    g.agregar_arista(0,2)# Agrega las aristas (0,2) con peso=1
    g.agregar_arista(1,2)# Agrega las aristas (1,2) con peso=1
    g.agregar_arista(1,4)# Agrega las aristas (1,4) con peso=1
    g.agregar_arista(2,3)# Agrega las aristas (2,3) con peso=1
    
    # Imprime la lista de adyacencia en el formulario del nodo
    g.imprimir_lista_adyacencia()