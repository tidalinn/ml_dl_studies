'''module with useful functions
'''

import numpy as np
from typing import Tuple


'''
Преобразование списка изображений в переданных формат
'''
def convert_files_to_type(files: List[str], file_type: str) -> None:
    for in_file in files:
        out_file = os.path.splitext(in_file)[0] + file_type

        if in_file != out_file:            
            try:
                Image.open(in_file).save(out_file)
            except IOError:
                print('Cannot convert', in_file)
                
                
'''
Формирование списка имён всех файлов в папке
'''
def get_files_list(path: str, file_type: str) -> List[str]:
    return [os.path.join(path, file) 
            for file in os.listdir(path) 
            if file.endswith(file_type)]


'''
Изменение размера массива изображения
'''
def resize_image(image: np.array, size: Tuple[int]) -> np.array:
    image_converted = Image.fromarray(np.uint8(image))
    return np.array(image_converted.resize(size))


'''
Выравнивание гистограммы изображения
'''
def hist_equalize(image: np.array, n_bins: int = 256) -> Tuple[np.array]:
    image_hist, bins = np.histogram(image.flatten(), bins=n_bins, density=True)
    cdf = image_hist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalizing
    
    image_equalized = np.interp(image.flatten(), bins[:-1], cdf)
    return image_equalized.reshape(image.shape), cdf


'''
Вычисление среднего списка изображений
'''
def compute_average_image(images: List[str]) -> np.array:
    image_average = np.array(Image.open(images[0]), 'f')
    
    for image in images[1:]:
        try:
            image_average += np.array(Image.open(image))
        except:
            print(image, 'passed')
            image_average /= len(images)
            
    return np.array(image_average, 'uint8')