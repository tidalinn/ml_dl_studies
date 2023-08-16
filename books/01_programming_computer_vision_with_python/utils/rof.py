'''module with ROF method
'''

import numpy as np
from typing import Tuple


'''
Очистка от шумов Рудина-Ошура-Фатеми (ROF) с использованием численного алгоритма, приведённого в формуле Шамболя:
'''
def denoise(image: np.array, 
            U_init: np.array, 
            tolerance: float = 0.1, 
            tau: float = 0.125,
            tv_weight: int = 100) -> Tuple[np.array]:
    
    m, n = im.shape
    
    # init
    U = U_init
    Px = image # x component of dual task
    Py = image # y component of dual task
    error = 1
    
    while (error > tolerance):
        U_old = U
        
        # gradient of straight task variable
        grad_Ux = np.roll(U, -1, axis=1) - U # x component of U gradient
        grad_Uy = np.roll(U, -1, axis=0) - U # y component of U gradient
        
        # change variable of dual task
        Px_new = Px + (tau / tv_weight) * grad_Ux
        Py_new = Py + (tau / tv_weight) * grad_Uy
        
        norm_new = np.maximum(1, np.sqrt(Px_new ** 2 + Py_new ** 2))
        
        Px = Px_new / norm_new # change x component of dual task
        Py = Py_new / norm_new # change y component of dual task
        
        # change variable of stright task
        Rx_Px = np.roll(Px, 1, axis=1) # circular bias of x component along x axis
        Ry_Py = np.roll(Py, 1, axis=0) # circular bias of y component along y axis
        
        div_P = (Px - Rx_Px) + (Py - Ry_Py) # divergence of dual field
        U = image + tv_weight * div_P # change variable of straight task
        
        # update error
        error = np.linalg.norm(U - U_old) / np.sqrt(n * m)
        
    return U, im - U # cleared image, residual texture