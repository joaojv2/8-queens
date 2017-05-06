class Arquivo(object):

	def lerArquivo(self,path):
		conteudoArquivo = open(path , "r")
		return conteudoArquivo

	def getMatrizArquivo(self , pathArquivo):
		conteudoArquivo = self.lerArquivo(pathArquivo)
		matriz = []
		for linhaArquivo in conteudoArquivo:
			valores = linhaArquivo.replace("\n" , "").split(' ')
			linha = []
			for valor in valores:
				linha.append(valor)
			matriz.append(linha)
		return matriz