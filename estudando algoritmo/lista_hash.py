class HashTable:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        bucket = self.tabela[indice]

        # Atualiza caso a chave já exista
        for item in bucket:
            if item[0] == chave:
                item[1] = valor
                return

        # Insere nova chave
        bucket.append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        bucket = self.tabela[indice]

        for item in bucket:
            if item[0] == chave:
                return item[1]

        return None

    def remover(self, chave):
        indice = self._hash(chave)
        bucket = self.tabela[indice]

        for i, item in enumerate(bucket):
            if item[0] == chave:
                del bucket[i]
                return True

        return False

    def mostrar(self):
        for i, bucket in enumerate(self.tabela):
            print(f"{i}: {bucket}")