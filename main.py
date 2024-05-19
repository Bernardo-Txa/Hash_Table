from hashlib import sha256

espaces = '-'*100

class TabelaHash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor


    def __init__(self):
        self.__capacidade_atual = 5 # capacidade/tamanho interno
        self.__tabela_interna = [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0 # quantidade de elementos salvos na tabela hash


    def __len__(self):
        return self.__tamanho


    @staticmethod
    def __verificar_chave(chave):
        hash(chave)


    @staticmethod
    def __hash_deterministico(chave):
        codificado = str(chave).encode()
        return int(sha256(codificado).hexdigest(), 16)


    def __descobrir_indice(self, chave):
        return self.__hash_deterministico(chave) % self.__capacidade_atual


    def __setitem__(self, chave, valor):
        self.__verificar_chave(chave)
        indice = self.__descobrir_indice(chave)

        # Verifica se a chave ja existe na tabela
        for elemeto in self.__tabela_interna[indice]:
            if elemeto.chave == chave:
                elemeto.valor = valor # se encontrar atualiza o valor
                return
            
        # se nao encontrar, adiciona um novo elemento
        novo_elemento = self.__Elemento(chave, valor)
        self.__tabela_interna[indice].append(novo_elemento)
        self.__tamanho += 1

    def __iter__(self):
        for lista in self.__tabela_interna:
            for elemento in lista:
                yield elemento.chave, elemento.valor

    def __getitem__(self, chave):
        self.__verificar_chave(chave)
        indice = self.__descobrir_indice(chave)

        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                return elemento.valor   
            
        raise KeyError(f'Chave {chave} nao encontrada')
    
    def __delitem__(self, chave):
        self.__verificar_chave(chave)

        indice = self.__descobrir_indice(chave)


        for i, elemento in enumerate(self.__tabela_interna[indice]):
            if elemento.chave == chave:
                del self.__tabela_interna[indice][i]
                self.__tamanho -= 1
                return

        raise KeyError(f'Chave {chave} nao encontrada')






pessoa = TabelaHash()
pessoa['nome'] = 'Bernardo'
pessoa['idade'] = 21
pessoa['sexo'] = 'Masculino'
pessoa['profissao'] = 'progamador'
pessoa['nacionalidade'] = 'Brasileira'
pessoa['cpf'] = 128123123442


print(f'\n{espaces}\n')

print(f'Nome: {pessoa["nome"]}')
print(f'idade: {pessoa["idade"]}')
print(f'sexo: {pessoa["sexo"]}')
print(f'profissao: {pessoa["profissao"]}')
print(f'nacionalidade: {pessoa["nacionalidade"]}')
print(f'cpf: {pessoa["cpf"]}')

print(f'\n{espaces}')

print(f'quantidade de elementos: {len(pessoa)}')


print(f'{espaces}/n')
del pessoa['cpf']
for k, v in pessoa:
    print(f'{k}: {v}')

print(f'\n{espaces}')
