"""
felipedelosh

utilizando la busqueda de simpleai se desea generar una cadena desde un conjunto de caracteres.
el problema lo resolvera A* por medio de un arbol
Nota: el problema se tiene que ligar a un visualizador //en este caso por consola

"""

# 1 - se importa simpleai.search
from simpleai.search import SearchProblem
# 1.1 - se importa astar(A*)
from simpleai.search import astar
# 1.2 - se importa un visualizador
from simpleai.search.viewers import ConsoleViewer


# 2 - se define el objetivo 
objetivo = "YO SOY EL LOCO MAS LOCO DE TODOS"

# 3 - se define el conjunto de caracteres
caracteres = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 4 - se crear una clase que resuelva esta wea apoyada en simpleai
# 4.1 - se crea el metodo actios
# 4.2 - se crea el metodo de heuristica
# 4.2.1 - el metodo de la euristica necesita de result
# 4.3 - esto tiene que tener un ojetivo
class resolvedor(SearchProblem):
    def actions(self, estado):
        if len(estado) < len(objetivo):
            return list(caracteres)
        else:
            return []

    def heuristic(self, estado):
        erradas = sum([1 if estado[i] != objetivo[i] else 0 for i in range(len(estado))])
        perdidas = len(objetivo) - len(estado)
        return erradas + perdidas

    def result(self, estado, accion):
        return estado + accion
    
    def is_goal(self, estado):
        return estado == objetivo


# 5 - se instancia
#     se parte desde vacio
#     se crea un visualizador de solucion
#     se le dice que lo resuelva
problema = resolvedor(initial_state="")
visualizadorSolucion = ConsoleViewer()
solucion = astar(problema, viewer=visualizadorSolucion)
# Se procede a mostar la solucion:
print(solucion.path())
