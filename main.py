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

def url_to_filtered_image(image_url,fil_str,intensity):
	""" Recebe url da imagem, nome do filtro e intensidade e retorna imagem filtrada"""

	# filename = image_url.split("/")[-1]

	filename="image.jpg"
	image = url_to_image(image_url)

	# Inicia classe de Filtros e lista os filtros disponíveis
	fil = Filters()
	for i,item in enumerate(fil.filter_names):
		if item == fil_str:
			break

	# Recebe os inputs do usuário para selecionar o filtro
	# e sua intensidade
	num_filter=i
	num_param=intensity

	# Executa a funcao do filtro sobre a imagem 
	image = fil.filter_funcs[num_filter](image, num_param)

	# Salva imagem
	cv2.imwrite(filename, image) 

	# Armazena em um buffer
	retval, buff = cv2.imencode('.jpg', image)
	
	# Envia imagem filtrada
	# return buff

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
