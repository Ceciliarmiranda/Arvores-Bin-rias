class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        def _inserir(raiz, valor):
            if raiz is None:
                return No(valor)
            if valor < raiz.valor:
                raiz.esquerda = _inserir(raiz.esquerda, valor)
            else:
                raiz.direita = _inserir(raiz.direita, valor)
            return raiz
        self.raiz = _inserir(self.raiz, valor)

    def remover(self, valor):
        def menor_no(no):
            atual = no
            while atual.esquerda:
                atual = atual.esquerda
            return atual

        def _remover(raiz, valor):
            if raiz is None:
                return None
            if valor < raiz.valor:
                raiz.esquerda = _remover(raiz.esquerda, valor)
            elif valor > raiz.valor:
                raiz.direita = _remover(raiz.direita, valor)
            else:
                if not raiz.esquerda:
                    return raiz.direita
                elif not raiz.direita:
                    return raiz.esquerda
                substituto = menor_no(raiz.direita)
                raiz.valor = substituto.valor
                raiz.direita = _remover(raiz.direita, substituto.valor)
            return raiz

        self.raiz = _remover(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(no, valor):
            if no is None:
                return False
            if no.valor == valor:
                return True
            elif valor < no.valor:
                return _buscar(no.esquerda, valor)
            else:
                return _buscar(no.direita, valor)
        return _buscar(self.raiz, valor)

    def altura(self):
        def _altura(no):
            if no is None:
                return -1
            return 1 + max(_altura(no.esquerda), _altura(no.direita))
        return _altura(self.raiz)

    def grau_no(self, valor):
        def _procurar(no, valor):
            if no is None:
                return None
            if no.valor == valor:
                return no
            elif valor < no.valor:
                return _procurar(no.esquerda, valor)
            else:
                return _procurar(no.direita, valor)

        alvo = _procurar(self.raiz, valor)
        if alvo is None:
            return None

        grau = 0
        if alvo.esquerda:
            grau += 1
        if alvo.direita:
            grau += 1
        return grau

    def em_ordem(self):
        def _em_ordem(no):
            if no:
                return _em_ordem(no.esquerda) + [no.valor] + _em_ordem(no.direita)
            return []
        return _em_ordem(self.raiz)

    def pre_ordem(self):
        def _pre_ordem(no):
            if no:
                return [no.valor] + _pre_ordem(no.esquerda) + _pre_ordem(no.direita)
            return []
        return _pre_ordem(self.raiz)

    def pos_ordem(self):
        def _pos_ordem(no):
            if no:
                return _pos_ordem(no.esquerda) + _pos_ordem(no.direita) + [no.valor]
            return []
        return _pos_ordem(self.raiz)

    def estritamente_binaria(self):
        def _verificar(no):
            if no is None:
                return True
            if (no.esquerda is None and no.direita is None):
                return True
            if no.esquerda and no.direita:
                return _verificar(no.esquerda) and _verificar(no.direita)
            return False
        return _verificar(self.raiz)

    def cheia(self):
        def _verificar(no):
            if no is None:
                return True
            if (no.esquerda is None) != (no.direita is None):
                return False
            return _verificar(no.esquerda) and _verificar(no.direita)
        return _verificar(self.raiz)

    def completa(self):
        if self.raiz is None:
            return True
        fila = [(self.raiz, 0)]
        i = 0
        while i < len(fila):
            no, idx = fila[i]
            i += 1
            if no.esquerda:
                fila.append((no.esquerda, 2 * idx + 1))
            if no.direita:
                fila.append((no.direita, 2 * idx + 2))
        return fila[-1][1] == len(fila) - 1

def menu():
    arvore = ArvoreBinaria()
    while True:
        print("\n==== MENU ÁRVORE BINÁRIA ====")
        print("1 - Inserir valor")
        print("2 - Remover valor")
        print("3 - Buscar valor")
        print("4 - Em ordem (in-order)")
        print("5 - Pré-ordem")
        print("6 - Pós-ordem")
        print("7 - Verificar se é estritamente binária")
        print("8 - Verificar se é cheia")
        print("9 - Verificar se é completa")
        print("10 - Altura da árvore")
        print("11 - Grau de um nó")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            val = int(input("Valor a inserir: "))
            arvore.inserir(val)
        elif opcao == "2":
            val = int(input("Valor a remover: "))
            arvore.remover(val)
        elif opcao == "3":
            val = int(input("Valor a buscar: "))
            print("Encontrado!" if arvore.buscar(val) else "Não encontrado.")
        elif opcao == "4":
            print("Em ordem:", arvore.em_ordem())
        elif opcao == "5":
            print("Pré-ordem:", arvore.pre_ordem())
        elif opcao == "6":
            print("Pós-ordem:", arvore.pos_ordem())
        elif opcao == "7":
            print("Estritamente binária?" , "Sim" if arvore.estritamente_binaria() else "Não")
        elif opcao == "8":
            print("Árvore cheia?" , "Sim" if arvore.cheia() else "Não")
        elif opcao == "9":
            print("Árvore completa?" , "Sim" if arvore.completa() else "Não")
        elif opcao == "10":
            print("Altura:", arvore.altura())
        elif opcao == "11":
            val = int(input("Valor do nó: "))
            grau = arvore.grau_no(val)
            if grau is not None:
                print(f"Grau do nó {val}: {grau}")
            else:
                print("Nó não encontrado.")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
