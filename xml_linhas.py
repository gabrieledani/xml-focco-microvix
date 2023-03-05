import csv
from dataclasses import replace
import os
from cleantext import clean

nome_arquivo_xml = os.path.join(os.getcwd(),r'arquivos\LinxCadastraLinhas.xml')
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
					<linx2:Comando>LinxCadastraLinhas</linx2:Comando>
					<linx2:Registros>'''
xml_produto.write(head)

nome_arquivo = os.path.join(os.getcwd(),r'arquivos\linhas.csv')
#print(nome_arquivo)

with  open(nome_arquivo, encoding="mbcs") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')

    for row in csv_reader:
        codigo, nome_linha = row[0],row[1]
        
        codigo = clean(codigo)

        nome_linha = clean(nome_linha)

        middle = '''
						<linx:Registros>
							<linx:Colunas>
								<linx1:CommandParameter>
									<linx1:Name>codigo</linx1:Name>
									<linx1:Value>'''+codigo+'''</linx1:Value>
								</linx1:CommandParameter>
								<linx1:CommandParameter>
									<linx1:Name>nome_linha</linx1:Name>
									<linx1:Value>'''+nome_linha.upper()+'''</linx1:Value>
								</linx1:CommandParameter>
							</linx:Colunas>
						</linx:Registros>'''
        xml_produto.write(middle)

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