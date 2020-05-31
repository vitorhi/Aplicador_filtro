from flask import Flask, Response, request
from main import url_to_filtered_image
app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_data():
	image_url=request.data.decode('ascii')
	print('Url recebida do cliente: {}'.format(image_url))
	
	url_to_filtered_image(image_url)

	return Response('Script executado')
if __name__ == '__main__':
	app.run(debug=False)