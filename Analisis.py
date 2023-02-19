#librerias a usar
import shutil
import os
import pkg_resources
import matplotlib.pyplot as plt
import numpy as np
import imageio

import whitebox


#definir dataset
def dataset(data_dir):

    wbt.set_working_dir(data_dir)    #indicamos que esta va a ser el dataset
    wbt.verbose = False              #desactivamos notificaciones

    print(os.listdir(data_dir))      #imprimimos los archivos

def print_raster(file,n):
    filename = str(name(file,n))
    filename = (filename + '.png')
    print(filename)
    # print the raster
    raster = imageio.imread(os.path.join(data_dir, file))
    raster1=np.where(raster==-99999.,np.nan,raster) #99999
    plt.imshow(raster1)
    plt.colorbar()
    plt.savefig(filename)
    plt.show()

    move(filename)

def move(inicio):
    inicio = './{}'.format(inicio)
    #print(inicio)
    shutil.move(inicio, './Outputs')

def name(namefile, n):
    name = namefile
    n = n

    name = name[:-n]
    return(name)

def hillshade(file,n):
    filename = str(name(file,n))
    filename = (filename + '_hillshade.tif')

    wbt.hillshade(
        file, 
        filename, 
        azimuth=315.0, 
        altitude=30.0, 
        zfactor=None
    )

    move(filename)

def slope(file,n):
    filename = str(name(file,n))
    filename = (filename + '_slope.tif')

    wbt.slope(
    file, 
    filename, 
    zfactor=None, 
    units="degrees", # 'degrees', 'radians', 'percent'
    )

    move(filename)

def aspect(file,n):
    filename = str(name(file,n))
    filename = (filename + '_aspect.tif')

    wbt.aspect(
    file, 
    filename, 
    zfactor=None, 
    )

    move(filename)

def plan_curvature(file,n):
    filename = str(name(file,n))
    filename = (filename + '_plan_curvature.tif')

    # plan curvature
    wbt.plan_curvature(
    file, 
    filename, 
    log=False, #Display output values using a log-scale
    zfactor=None, 
    )

    move(filename)

def profile_curvature(file,n):
    filename = str(name(file,n))
    filename = (filename + '_profile_curvature.tif')

    #profile curvature
    wbt.profile_curvature(
    file, 
    filename, 
    log=False, 
    zfactor=None, 
    )

    move(filename)

def total_curvature(file,n):
    filename = str(name(file,n))
    filename = (filename + '_total_curvature.tif')

    #total curvature Total curvature measures the curvature of the topographic surface rather than the curvature of a line across the surface in some direction
    wbt.total_curvature(
    file, 
    filename, 
    log=False, 
    zfactor=None, 
    )

    move(filename)


def average_normal_vector_angular_deviation(file,n):
    filename = str(name(file,n))
    filename = (filename + '_Roughness.tif')

    # Roughness
    wbt.average_normal_vector_angular_deviation(
    file, 
    filename, 
    filter=11, #Size of the filter kernel
    )

    move(filename)


def roughness_index(file,n):
    filename = str(name(file,n))
    filename = (filename + '_roughness_index.tif')

    # roughness index calculates the root-mean-square-deviation (RMSD) for each grid cell in a digital elevation model (DEM), calculating the residuals (i.e. elevation differences) between a grid cell and its eight neighbours.
    wbt.ruggedness_index(
    file, 
    filename, 
    )
    
    move(filename)


def circular_variance_of_aspect(file,n):
    filename = str(name(file,n))
    filename = (filename + '_aspect_variance.tif')

    # circular variance of aspect
    wbt.circular_variance_of_aspect(
    file, 
    filename, 
    filter=11,  #Size of the filter kernel
    )
    
    move(filename)


def dev_from_mean_elev(file,n):
    filename = str(name(file,n))
    filename = (filename + '_dev_elev.tif')

    #difference between the elevation of each grid cell and the mean elevation of the centering local neighbourhood, normalized by standard deviation
    wbt.dev_from_mean_elev(
    file, 
    filename, 
    filterx=11, 
    filtery=11, 
    )
    
    move(filename)


def diff_from_mean_elev(file,n):
    filename = str(name(file,n))
    filename = (filename + '_diff_elev.tif')

    # the difference between the elevation of each grid cell and the mean elevation of the centering local neighbourhood
    wbt.diff_from_mean_elev(
    file, 
    filename, 
    filterx=11, 
    filtery=11, 
    )
    
    move(filename)

def edge_density(file,n):
    filename = str(name(file,n))
    filename = (filename + '_edge_density.tif')

    # Edge density
    wbt.edge_density(
    file, 
    filename, 
    filter=11, 
    norm_diff=5.0, 
    zfactor=None, 
    )
    
    move(filename)



def find_ridges(file,n):
    filename = str(name(file,n))
    filename = (filename + '_ridges.tif')

    # find ridges
    wbt.find_ridges(
    file, 
    filename, 
    line_thin=True, 
    )
    
    move(filename)


def geomorphons(file,n):
    filename = str(name(file,n))
    filename = (filename + '_geomorphons.tif')

    #geomorphons landform classification. Jasiewicz et al. (2013) identified 10 common landform types by reclassifying related geomorphons codes.
    #1	Flat, 2	Peak (summit), 3	Ridge, 4	Shoulder, 5	Spur (convex), 6	Slope, 7	Hollow (concave), 8	Footslope, 9	Valley, 10	Pit (depression)
    wbt.geomorphons(
    file, 
    filename, 
    search=200, 
    threshold=0.0, 
    fdist=0, 
    skip=0, 
    forms=True, 
    residuals=False
    )
    
    move(filename)


def clip_raster_to_polygon(file,n):
    filename = str(name(file,n))
    filename = (filename + 'tinted_hillshade.tif')

    catchments=['.tif']
    for catchment in catchments:
        wbt.clip_raster_to_polygon(file,
                                    f"{catchment}_12m.shp", 
                                    f"{catchment}_12m.tif", 
                                    maintain_dimensions=False,)
    
    #Hypsometric analysis of one or more input digital elevation models (DEMs)
    catchments=[file]
    for catchment in catchments:
        wbt.hypsometric_analysis(f"{catchment}_12m.tif", f"{catchment}_12m_hypso.html", watershed=None,)
    
    #hypsometrically tinted shaded relief 
    wbt.hypsometrically_tinted_hillshade(
        file, 
        filename, 
        altitude=45.0, 
        hs_weight=0.5, 
        brightness=0.5, 
        atmospheric=0.0, 
        palette="atlas", 
        reverse=False, 
        zfactor=None, 
        full_mode=False, 
    )


if __name__ == '__main__':
    wbt = whitebox.WhiteboxTools()

    #archivo a procesar
    file = 'Sabaletas.tif'    #nombre archivo
    n = 4                     #numero de caracteres de la execion del archivo contando el punto
    data_dir = './data'        #definimos la carpeta donde se encuentra

    #definimos dataset
    dataset(data_dir)

    #imprimimos el raster
    print_raster(file,n)

    #herramientas
    hillshade(file,n)


