from flask import Flask, Response, request, send_file
from main import url_to_filtered_image
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def get_data():
	
	received=request.get_json(silent=True)

	# Separando os dados recebidos
	image_url=received["url"]
	fil_str=received["filter"]
	intensity=int(received["intensity"])

	# Filtrando a imagem
	image=url_to_filtered_image(image_url,fil_str,intensity)
	
	# Envia a imagem filtrada como resposta
	resp = Response(image, status=200, mimetype='image/jpeg')
	return resp
	
if __name__ == '__main__':
	app.run(debug=False)