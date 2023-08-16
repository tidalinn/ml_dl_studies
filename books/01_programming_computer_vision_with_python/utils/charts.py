'''module with charts plotting functions
'''

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
    
    
'''
Построение графиков гистограмм и изображений до и после трансформации
'''
def plot_image_before_after_transformation(image_before: np.array, 
                                           image_after: np.array,
                                           cdf: np.array,
                                           n_bins: int = 128) -> None:
    
    fig = plt.figure(figsize=(8, 5))

    grid = (2, 3)

    ax1 = plt.subplot2grid(grid, (0, 0))
    ax2 = plt.subplot2grid(grid, (0, 1), colspan=1)
    ax3 = plt.subplot2grid(grid, (0, 2), colspan=1)
    ax4 = plt.subplot2grid(grid, (1, 0), colspan=1)
    ax5 = plt.subplot2grid(grid, (1, 2), colspan=1)

    ax1.hist(image_before.flatten(), bins=n_bins)
    ax4.imshow(image_before)
    ax4.set_xlabel('before')

    ax2.plot(cdf)
    ax2.set_xlabel('transformation')

    ax3.hist(image_after.flatten(), bins=n_bins)
    ax5.imshow(image_after)
    ax5.set_xlabel('after')

    plt.tight_layout()
    plt.show()
    
    
'''
Построение графиков нескольких изображений
'''
def plot_images_row(images: List[str], 
                    n_images: int, 
                    image_type = None, 
                    titles: List[str] = None) -> None:
    
    fig, ax = plt.subplots(1, n_images, figsize=(10, 3))
    
    if image_type == np.ndarray:
        for i in range(len(images[:n_images])):
            ax[i].imshow(images[i])
            ax[i].set_axis_off()
            
            if titles != None:
                ax[i].set_title(titles[i])
            
    elif image_type == np.uint8:
        for i in range(len(images[:n_images])):
            ax[i].imshow(np.uint8(images[i]))
            ax[i].set_axis_off()
            
            if titles != None:
                ax[i].set_title(titles[i])
        
    else:
        for i, image in enumerate(images[:n_images]):
            ax[i].imshow(Image.open(image))
            ax[i].set_axis_off()
            ax[i].set_title(image)

    plt.tight_layout()
    plt.show()
    
    
'''
Построение графиков вычисления главных компонент
'''
def plot_images_pca(images: List[np.array], 
                    n_images: int, 
                    m_n_shape: Tuple[int],
                    pca: Tuple[np.array]) -> None:
    
    plt.figure()
    plt.gray()
    
    n_cols = 4
    n_rows = n_images // n_cols
    
    if n_cols * n_rows != n_images:
        n_images = n_cols * n_rows
        print(f'Reduced images quantity to {n_images}')
        
    plt.subplot(n_rows, n_cols, 1)
    
    m, n = m_n_shape
    im_v, im_s, im_x_mean = pca

    plt.imshow(im_x_mean.reshape(m, n))

    for i in range(1, n_images + 1):
        plt.subplot(n_rows, n_cols, i)
        plt.imshow(im_v[i].reshape(m, n))
        plt.axis('off')

    plt.tight_layout()
    plt.show()