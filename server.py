from flask import Flask, Response, request, send_file
from main import url_to_filtered_image
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def get_data():
	# image_url=request.data.decode('ascii')
	received=request.get_json(silent=True)
	print('Recebida do cliente: {}'.format(received))

	image_url=received["url"]
	fil_str=received["filter"]
	intensity=int(received["intensity"])
	image=url_to_filtered_image(image_url,fil_str,intensity)
	
	
	return send_file('image.jpg', mimetype='image/jpg')
	return response

	
	# return app.send_static_file('image.jpg')
	# return send_file("image.jpg", mimetype='image/jpg')
if __name__ == '__main__':
	app.run(debug=False)