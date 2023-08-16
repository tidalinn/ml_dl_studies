'''module with PCA method
'''

import numpy as np
from typing import Tuple
    

'''
Понижение размерности изображения методом главных компонент
'''
def pca(X: np.array) -> Tuple[np.array]:
    n_data, dim = X.shape
    
    X_mean = X.mean(axis=0)
    X = X - X_mean # center data
    
    # get eigenvectors
    if dim > n_data:
        # compact PCA
        M = np.dot(X, X.T) # covariation matrix -> eigen values
        e, EV = np.linalg.eigh(M) # eigenvalues and eigenvectors
        
        tmp = np.dot(X.T, EV).T 
        
        V = tmp[::-1]
        S = np.sqrt(e)[::-1]
        
        for i in range(V.shape[1]):
            V[:, i] /= S
    
    else:
        # SVD PCA
        U, S, V = np.linalg.svd(X)
        V = V[:n_data]
    
    return V, S, X_mean