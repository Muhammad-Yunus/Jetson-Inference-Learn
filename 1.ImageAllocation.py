from jetson_utils import cudaImage, cudaDeviceSynchronize

img = cudaImage(width=1920, height=1080, format='rgb8')

cudaDeviceSynchronize()

del img