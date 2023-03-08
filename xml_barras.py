import csv
from dataclasses import replace
import os
from cleantext import clean

new_file = 1
letra = 1

nome_arquivo = os.path.join(os.getcwd(),r'files\barras.csv')

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

		nome_arquivo_xml = os.path.join(os.getcwd(),r'files\LinxCadastraProdutosCodebar'+str(letra)+'.xml')
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
					<linx2:Comando>LinxCadastraProdutosCodebar</linx2:Comando>
					<linx2:Registros>'''
		xml_produto.write(head)

	cod_barras, codigo_produto = clean(row[0]),clean(row[1])
        
	middle = '''	
						<linx:Registros>
							<linx:Colunas>
								<linx1:CommandParameter>
									<linx1:Name>cod_barras</linx1:Name>
									<linx1:Value>'''+cod_barras+'''</linx1:Value>
								</linx1:CommandParameter>
								<linx1:CommandParameter>
									<linx1:Name>codigo_produto</linx1:Name>
									<linx1:Value>'''+codigo_produto+'''</linx1:Value>
								</linx1:CommandParameter>
							</linx:Colunas>
						</linx:Registros>'''
	xml_produto.write(middle)

	new_file = new_file + 1
	if new_file == 400:
		new_file = 1
