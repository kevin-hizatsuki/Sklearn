from sklearn import  tree

irregular = 0
lisa = 1
pelos= 2
espinhos = 3
comprido = 4

laranja = 0
maca = 1
pera = 2
abacaxi = 3
banana = 4
abacate = 5
kiwi = 6
pessego = 7

assido = 0
neutro = 1

pomar = [[150,lisa,1],[130,lisa,1],[180,irregular,0],[160,irregular,0],[300,espinhos,0],
         [320,espinhos,0],[100,lisa,1],[80,lisa,1],[50,comprido,1],[60,comprido,1],[50,pelos,0],[40,pelos,0],
         [50,pelos,1],[80,pelos,1]]

resultado = [maca,maca,laranja,laranja,abacaxi,abacaxi,pera,pera,banana,banana,kiwi,kiwi,pessego,pessego]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar,resultado)

peso = input("Entre com o peso: ")
superficie = input("Entre com a superficie: ")
acidez = input("Entre com a acidez: ")

resultadoUsuario = clf.predict([[peso,superficie,acidez]])


print (resultadoUsuario)
 
