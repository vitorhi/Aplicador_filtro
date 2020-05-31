# Autor: Vítor Hideki Ishikura
# Data: 30/05/2020

# Importando pacotes necessários
import numpy as np
from urllib.request import Request, urlopen
import cv2
from filters import Filters


def url_to_image(url):
	# Faz o Download da imagem, converte para um array numpy, e 
	# o transforma em formato OpenCV
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	resp = urlopen(req).read()
	image = np.asarray(bytearray(resp), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# Retorna imagem
	return image

def url_to_filtered_image(image_url):

	filename = image_url.split("/")[-1]

	image = url_to_image(image_url)

	# Inicia classe de Filtros e lista os filtros disponíveis
	fil = Filters()
	print("Lista de filtros disponíveis:\n")
	for i,item in enumerate(fil.filter_names):
		print(str(i) + "- " + item 	+ "\n")

	# Recebe os inputs do usuário para selecionar o filtro
	# e sua intensidade
	num_filter=-1
	num_param=-1
	while num_filter<0 or num_filter>=len(fil.filter_names):
		num_filter = int(input("Indique o número do filtro: "))

	while num_param<=0 or num_param>999:
		num_param = int(input("Indique a intensidade do filtro (valores acima de 0): "))

	# Executa a funcao do filtro sobre a imagem 
	image = fil.filter_funcs[num_filter](image, num_param)

	# Salva imagem
	cv2.imwrite(filename, image) 

	# Mostra a imagem filtrada
	cv2.imshow('imagem', image)

	# Espera o fechamento da janela da imagem
	while cv2.getWindowProperty('imagem', cv2.WND_PROP_VISIBLE) > 0:
		keyCode = cv2.waitKey(50)

	cv2.destroyAllWindows()

	

# Exemplos de URLs
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
# image_url = "https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png"
# image_url ='https://docs.opencv.org/3.4/nlm_result1.jpg'
if __name__ == "__main__":

	# Seleciona a URL da foto
	image_url = input("Digite uma Url de uma imagem: ")
	url_to_filtered_image(image_url)
