class No:

    def __init__ (self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.valor, self.valor, self.esquerda and self.direita.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else: 
            self.inserir_em_nivel_recursivo(valor, self.raiz)
        
    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else: 
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else: 
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)
    
    
    def MostrarRaiz(self):
        return self.raiz.valor


    def altura(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.alturaRecursivo(self.raiz))
    
    def alturaRecursivo(self, no):
        if no is None:
            return 0
        
        altE = self.alturaRecursivo(no.esquerda)
        altD = self.alturaRecursivo(no.direita)
        
        if altE > altD:
            return altE + 1
        else:
            return altD + 1


    def MostrarFolhas(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            self.MostrarFolhasRecursivo(self.raiz)
    
    def MostrarFolhasRecursivo(self, no):
        if no is None:
            return False
        if no.esquerda is None and no.direita is None:
            print(no.valor, end = " ")
        self.MostrarFolhasRecursivo(no.esquerda)
        self.MostrarFolhasRecursivo(no.direita)


    def NosInternos(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.NosInternosRecursivo(self.raiz)
            
    def NosInternosRecursivo(self, no):
        if no is None:
            return False
        if no.esquerda is not None or no.direita is not None:
            print(no.valor, end = " ")
        self.NosInternosRecursivo(no.esquerda)
        self.NosInternosRecursivo(no.direita)
        
        
    def BuscarValor(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            return self.BuscarValorRecursivo(self.raiz, valor)
            

    def BuscarValorRecursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor > no.valor:
            return self.BuscarValorRecursivo(no.direita, valor)
        else:
            return self.BuscarValorRecursivo(no.esquerda, valor)

Arvore = ArvoreBinaria()

Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)

print("Raiz:", Arvore.MostrarRaiz())

print("Altura:", end= " ")
Arvore.altura()

print("Nós Internos:", end=" ")
Arvore.NosInternos()

print("\nFolhas:", end=" ")
Arvore.MostrarFolhas()
print()


n = int(input("Informe o Número que deseja Buscar: "))

if Arvore.BuscarValor(n):
    print(f"O valor {n} está presente na árvore!!!")
else:
    print(f"O valor {n} NÃO está presente na árvore!!!")




