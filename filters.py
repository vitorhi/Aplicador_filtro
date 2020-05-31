import cv2
import numpy as np

class Filters(object):
    """Classe que abriga metodos de filtros"""

    def __init__(self):
        
        self.filter_funcs = [self.gaussian_blur, self.median_blur,
                             self.denoiser_enhance, self.unsharp_enhance,
                             self.erode, self.dilate]
        self.filter_names = ['Gaussian Blur','Median Blur',
                             'Denoiser Enhance','Unsharp Enhance',
                             'Erode', 'Dilate']
       
    # Metodos dos filtros:
    
    def gaussian_blur(self, image, size):
        # Filtro de Blur Gaussiano

        if size < 0:
            raise Exception("Só são aceitos valores maiores do que 0") 
        # Convertendo size para ímpar
        if size % 2 == 0:
            size += 1
        
        return cv2.GaussianBlur(image, (size, size), 0)

    def median_blur(self, image, size):
        # Filtro de Blur Mediano

        if size < 0:
            raise Exception("Só são aceitos valores maiores do que 0") 
        # Convertendo size para ímpar
        if size % 2 == 0:
            size += 1
        return cv2.medianBlur(image, size)

    def denoiser_enhance(self,image, size):
        # Filtro de exclusão de ruído

        if size < 0:
            raise Exception("Só são aceitos valores maiores do que 0") 
        # Convertendo size para ímpar
        if size % 2 == 0:
            size += 1

        return cv2.fastNlMeansDenoisingColored(image,None,10,10,7,size)

    def unsharp_enhance(self, image, size):
        # Filtro de Sharpness

        if size < 0:
            raise Exception("Só são aceitos valores maiores do que 0") 
        # Convertendo size para ímpar
        if size % 2 == 0:
            size += 1

        gaussian = cv2.GaussianBlur(image, (size,size), 10.0)
        return cv2.addWeighted(image, 1.5, gaussian, -(size/18), 0, image)
    
    def erode(self, image, size):
        # Filtro de erosao da imagem
        if size < 0:
            raise Exception("Só são aceitos valores maiores do que 0") 
        
        kernel = np.ones((size,size),np.uint8)
        return cv2.erode(image,kernel,iterations = 1)

    def dilate(self, image, size):
       # Filtro de dilatacao da imagem
       if size < 0:
           raise Exception("Só são aceitos valores maiores do que 0") 
       
       kernel = np.ones((size,size),np.uint8)
       return cv2.dilate(image,kernel,iterations = 1)