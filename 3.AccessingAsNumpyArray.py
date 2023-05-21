import numpy as np
from jetson_utils import cudaImage

cuda_img = cudaImage(320, 240, 'rgb32f')
array = np.ones(cuda_img.shape, np.float32)

print(np.add(cuda_img, array))