import numpy as np
from jetson_utils import cudaImage, cudaToNumpy

cuda_img = cudaImage(320, 240, 'rgb32f')
array = cudaToNumpy(cuda_img)

print(array.mean())