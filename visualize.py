import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pdb

def show_champion_data(champion_information):
    '''Will show information, not ready yet'''
    champion_information = np.array(champion_information)
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    a = io.imread()
    
    plt.imshow(a)
    plt.axis('off')
    plt.show()