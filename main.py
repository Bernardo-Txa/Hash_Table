from hashlib import sha256
from math import ceil

espaces = '-'*100

class TabelaHash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

        def __str__(self):
            return f'{self.chave}: {self.valor}'
        
        def __repr__(self):
            return self.__str__()



    def __init__(self):
        self.__capacidade_atual = 5 # capacidade/tamanho interno
        self.__tabela_interna = [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0 # quantidade de elementos salvos na tabela hash

        self.__limiar_expandir = 0.75
        self.__fator_expansao = 2
        self.__limiar_reduzir = 0.20
        self.__fator_reducao = 0.5
    
    

    def __str__(self):
        retorno = '{'
        total = len(self)
        i = 0
        for k, v in self:
            retorno += f'{k}:'

            if isinstance(v, str):
                retorno += f"'{v}'"
            else:
                retorno += f'{v}'

            if i < total - 1:
                retorno += ', '
            i += 1
        retorno += '}'

        return retorno
    
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__tamanho

    @property
    def __fator_carga(self):
        return self.__tamanho / self.__capacidade_atual

    def __verificar_chave(self, chave):
        self.__hash_deterministico(chave)


    @staticmethod
    def __hash_deterministico(chave):
        codificado = str(chave).encode()
        return int(sha256(codificado).hexdigest(), 16)


    def __descobrir_indice(self, chave):
        return self.__hash_deterministico(chave) % self.__capacidade_atual


    def __setitem__(self, chave, valor):
        self.__verificar_chave(chave)

        if self.__fator_carga >= self.__limiar_expandir:
            self.__atualizar_tabela(self.__capacidade_atual * self.__fator_expansao)

        indice = self.__descobrir_indice(chave)

        ## Verifica se a chave ja existe na tabela
        #for elemeto in self.__tabela_interna[indice]:
        #    if elemeto.chave == chave:
        #        elemeto.valor = valor # se encontrar atualiza o valor
        #        return
        #    
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

        if self.__fator_carga <= self.__limiar_reduzir:
            self.__atualizar_tabela(ceil(self.__capacidade_atual * self.__fator_reducao))

        indice = self.__descobrir_indice(chave)


        for i, elemento in enumerate(self.__tabela_interna[indice]):
            if elemento.chave == chave:
                del self.__tabela_interna[indice][i]
                self.__tamanho -= 1
                return

        raise KeyError(f'Chave {chave} nao encontrada')

    def __atualizar_tabela(self, nova_capacidade):
        tabela_antiga = self.__tabela_interna


        self.__tabela_interna = [[] for _ in range(nova_capacidade)]
        self.__capacidade_atual = nova_capacidade
        self.__tamanho = 0

        for lista in tabela_antiga:
            for elemento in lista:
                self[elemento.chave] = elemento.valor





pessoa = TabelaHash()
pessoa['nome'] = 'Bernardo'
pessoa['nome'] = 'Giovanna'
pessoa['idade'] = 21
pessoa['sexo'] = 'Masculino'
pessoa['profissao'] = 'progamador'
pessoa['nacionalidade'] = 'Brasileira'
pessoa['cpf'] = 128123123442
pessoa['salario'] = 30000
pessoa['estado_civil'] = 'solteiro'
pessoa['telefone'] = '(27) 99267-1511'
pessoa['cep'] = 29129721

print(f'\n{espaces}')

print(f'quantidade de elementos: {len(pessoa)}')


print(f'{espaces}/n')

del pessoa['nome']

for k, v in pessoa:
    print(f'{k}: {v}')
#
print(f'\n{espaces}')

print(pessoa)
