import csv
import os
from cleantext import clean

new_file = 1
letra = 1

nome_arquivo = os.path.join(os.getcwd(),r'files\produtos.csv')

csv_file =  open(nome_arquivo, encoding="mbcs")

csv_reader = csv.reader(csv_file,delimiter=';')

for row in csv_reader:

    if new_file == 1:
        if letra > 1:
            foot = '''
                    </linx2:Registros>
                </linx:Tabela>
                <linx:UserAuth>
                    <linx2:Pass>linx_import</linx2:Pass>
                    <linx2:User>linx_import</linx2:User>
                </linx:UserAuth>
            </tem:request>
        </tem:Importar>
</soapenv:Body>
</soapenv:Envelope>'''
            xml_produto.write(foot)

        nome_arquivo_xml = os.path.join(os.getcwd(),r'files\LinxCadastraProduto'+str(letra)+'.xml')
        letra = letra + 1
        xml_produto = open(nome_arquivo_xml,'w', encoding="mbcs")
        head = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:linx="http://schemas.datacontract.org/2004/07/Linx.Microvix.WebApi.Importacao.Requests" xmlns:linx1="http://schemas.datacontract.org/2004/07/Linx.Microvix.WebApi.Business.Api" xmlns:linx2="http://schemas.datacontract.org/2004/07/Linx.Microvix.WebApi.Importacao">
<soapenv:Header/>
<soapenv:Body>
    <tem:Importar>
            <tem:request>
                <linx:ParamsSeletorDestino>
                    <linx1:CommandParameter>
                        <linx1:Name>chave</linx1:Name>
                        <linx1:Value>62CB8F1D-1737-481A-ABC8-E44D55AB9859</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cnpjEmp</linx1:Name>
                        <linx1:Value>87848180000144</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>IdPortal</linx1:Name>
                        <linx1:Value>12082</linx1:Value>
                    </linx1:CommandParameter>
                </linx:ParamsSeletorDestino>
                <linx:Tabela>
                    <linx2:Comando>LinxCadastraProdutos</linx2:Comando>
                    <linx2:Registros>'''
        xml_produto.write(head)

        
    codigo_ws = clean(row[0])
    nome_produto = row[1]
    nome_produto = nome_produto.replace('&','&amp;')
    referencia = row[2]
    setor = row[3]
    linha = row[4]
    marca = row[5]
    colecao = row[6]
    unidade = row[7]
    preco = row[8]
    preco = preco.replace(',','.')
    classificacao = row[9]
    espessura = row[10]
    origem = row[11]
    cest = row[12]
    cest = cest.replace('.','')
    #if cest:
        #cest = str(int(cest))
    ncm = row[13].zfill(8)
    desativado = row[14]
    
    middle = '''
            <linx:Registros>
                <linx:Colunas>
                    <linx1:CommandParameter>
                        <linx1:Name>codigo</linx1:Name>
                        <linx1:Value>'''+codigo_ws+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>nome_produto</linx1:Name>
                        <linx1:Value>'''+nome_produto+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_fornecedor</linx1:Name>
                        <linx1:Value>3118</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>referencia</linx1:Name>
                        <linx1:Value>'''+referencia+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_auxiliar</linx1:Name>
                        <linx1:Value>'''+referencia+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_setor</linx1:Name>
                        <linx1:Value>'''+setor+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_linha</linx1:Name>
                        <linx1:Value>'''+linha+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_marca</linx1:Name>
                        <linx1:Value>'''+marca+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_colecao</linx1:Name>
                        <linx1:Value>'''+colecao+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_grade1</linx1:Name>
                        <linx1:Value>1</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_grade2</linx1:Name>
                        <linx1:Value>1</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>unidade</linx1:Name>
                        <linx1:Value>'''+unidade+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>preco_custo</linx1:Name>
                        <linx1:Value>'''+preco+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>preco_venda</linx1:Name>
                        <linx1:Value>'''+preco+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_classificacao</linx1:Name>
                        <linx1:Value>'''+classificacao+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>cod_espessura</linx1:Name>
                        <linx1:Value>'''+espessura+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>origem_mercadoria</linx1:Name>
                        <linx1:Value>'''+origem+'''</linx1:Value>
                    </linx1:CommandParameter>'''
    """if cest:
        middle = middle+'''                        
                    <linx1:CommandParameter>
                        <linx1:Name>cest</linx1:Name>
                        <linx1:Value>'''+cest+'''</linx1:Value>
                    </linx1:CommandParameter>
                    '''
    """
    middle = middle+ '''<linx1:CommandParameter>
                        <linx1:Name>ncm</linx1:Name>
                        <linx1:Value>'''+ncm+'''</linx1:Value>
                    </linx1:CommandParameter>
                    <linx1:CommandParameter>
                        <linx1:Name>desativado</linx1:Name>
                        <linx1:Value>'''+desativado+'''</linx1:Value>
                    </linx1:CommandParameter>
                </linx:Colunas>
            </linx:Registros>'''
    xml_produto.write(middle)

    new_file = new_file + 1
    if new_file == 100:
        new_file = 1
