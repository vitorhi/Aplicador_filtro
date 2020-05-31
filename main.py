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


# Exemplos de URLs
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
# image_url = "https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png"
# image_url ='https://docs.opencv.org/3.4/nlm_result1.jpg'

# Seleciona a URL da foto
image_url = input("Digite uma Url de uma imagem: ")
image = url_to_image(image_url)

# Inicia classe de Filtros e lista os filtros disponíveis
fil = Filters()
print("Lista de filtros disponíveis:\n")
for i,item in enumerate(fil.filter_names):
	print(str(i) + "- " + item 	+ "\n")

# Recebe os inputs do usuário para selecionar o filtro
# e seus parâmetros
num_filter = int(input("Indique o número do filtro: "))
num_param = int(input("Indique o parâmetro do filtro: "))

# Executa a funcao do filtro sobre a imagem 
image = fil.filter_funcs[num_filter](image, num_param)

# Mostra a imagem filtrada
cv2.imshow('imagem', image)

# Espera o fechamento da janela da imagem
while cv2.getWindowProperty('imagem', cv2.WND_PROP_VISIBLE) > 0:
	keyCode = cv2.waitKey(50)

cv2.destroyAllWindows()
