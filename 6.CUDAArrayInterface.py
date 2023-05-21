import cupy
from jetson_utils import cudaImage

cuda_img = cudaImage(640, 480, 'rgb8')
cupy_array = cupy.ones((480, 640, 3))

print(cupy.add(cuda_img, cupy_array))