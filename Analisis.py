#librerias a usar
import os
import pkg_resources
import matplotlib.pyplot as plt
import numpy as np
import imageio
##%matplotlib inline  

import whitebox


#definir dataset
def dataset(data_dir):

    wbt.set_working_dir(data_dir)    #indicamos que esta va a ser el dataset
    wbt.verbose = False              #desactivamos notificaciones

    print(os.listdir(data_dir))      #imprimimos los archivos

def print_raster(file):
    # print the raster
    raster = imageio.imread(os.path.join(data_dir, file))
    raster1=np.where(raster==-99999.,np.nan,raster) #99999
    plt.imshow(raster1)
    plt.colorbar()
    plt.savefig('Sabaleta.jpg')
    plt.show()


if __name__ == '__main__':
    wbt = whitebox.WhiteboxTools()

    #archivo a procesar
    file = 'Sabaleta.tif'       #nombre archivo
    data_dir = './data'         #definimos la carpeta donde se encuentra

    #definimos dataset
    dataset(data_dir)

    #imprimimos el raster
    print_raster(file)



