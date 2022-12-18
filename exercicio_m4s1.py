def get_modelos_veiculos(id_marca):
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas/22/modelos"
    headers = {'user-agent':'MyStudyApp'}
    resposta = requests.get(url,headers=headers)

    if resposta.status_code != 200:
        print('Houve um erro na requisição!!')

    resposta_json = resposta.json()
    return resposta_json['modelos']

class ListaFipe():
    def __init__(self,id_marca):
        self.id_marca = id_marca
        self.indice = 0
        self.modelos = []

    def __iter__(self):
        self.modelos = get_modelos_veiculos(self.id_marca)
        return self

    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration

        modelo = self.modelos[self.indice]
        self.indice += 1
        return modelo

lista_fipe = ListaFipe(22)

for veiculo in lista_fipe:
    print(f'nome:{veiculo["nome"]}')
    print(f'ID: {veiculo["codigo"]}')
    print("-"*50)



