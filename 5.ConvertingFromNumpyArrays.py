import numpy as np
from jetson_utils import cudaFromNumpy

array = np.zeros((240, 320, 3), dtype=np.float32)
cuda_img = cudaFromNumpy(array)