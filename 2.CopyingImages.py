from jetson_utils import cudaMemcpy, cudaImage, loadImage

img_a = loadImage("my_image.jpg")

img_b = cudaImage(width=img_a.width, height=img_a.height, format=img_a.format)

cudaMemcpy(img_b, img_a)

img_c = cudaMemcpy(img_a)