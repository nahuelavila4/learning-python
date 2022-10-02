"""
Operadores logicos

&& es and
|| es or
!= es not
"""

"""
Tipos de listas

List: coleccion ordenada y modificable. Permite miembros duplicados.

Tuple: coleccion ordenada pero NO se puede modificar. Permite miembros duplicados.

Set: coleccion desordenada, sin indice y NO se puede modificar, pero podemos
agregar objetos al Set. NO permite miembros duplicados.

Dictionary: coleccion desordenada, modificable y con indice. No permite miembros duplicados.
"""
lista = [12, 463, 5, 93, 52];
#print(lista)

#Se le puede asignar variables a cada posicion de una lista

pares = [4, 28, 492, 898, 48, 72, 180];
pos1, pos2, pos3, *demas = pares;

# Si la ultima variable tiene un * adelante esa var guarda todos los elementos
# que quedan sin variable

#print(pos1, demas)

unidad = [1, 2, 3, 4, 5, 6, 7];
prim, sec, *resto, seis, siete = unidad;
#print(seis)

# Operador in
# sirve para buscar un elemento en la lista. Devuelve true o false

frutas = ["manzana", "banana", "naranja", "mandarina", "uva"]
fruta_existe = "naranja" in frutas
#print(fruta_existe)

frutas.append("sandia") # Agrega item(elemento) al final de la lista
frutas.insert(2, "kiwi") #Agrega item con indice especifico
frutas.remove("naranja") #Elimina item de la lista

# El metodo copy copia los items de una lista en una variable que se elija
# extend hace join o concatena dos listas
# count retorna numero de veces que un item aparece en una lista

# sort ordena lista modificandola
# sorted ordena lista sin modificar la lista

# pop elimina un item y lo retorna. Si no se le dice cual elimina el ultimo

# Ejercicio

vacio = []
con_items = [12, 65, 345, 329, 19, 82, 49];
#print(len(con_items))

chose = con_items[0:9:3]
total = len(con_items)-1
forma_dos = [con_items[0], con_items[total // 2], con_items[total]]

#print(forma_dos)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)
print(len(it_companies))

it_companies.remove("Amazon")

#print("Twitter" in it_companies)

it_companies.insert(3, "Mercado Libre")

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
full_stack = front_end.copy()

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(full_stack)
