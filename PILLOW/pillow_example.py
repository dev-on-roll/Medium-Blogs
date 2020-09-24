from PIL import Image,ImageFilter

def read_image():
    # reading image ..
    img = Image.open("my_image.png")
    width, height = img.size
    # printing image dimensions ..
    print(width,height)
    img.show()

def crop_image():
    # reading image ..
    img = Image.open("my_image.png")
    width, height = img.size
    # Setting the points for cropped image
    left = 0
    top = 0
    right = width
    bottom = height / 2
    # calling the crop method
    img = img.crop((left,top,right,bottom))
    img.save('cropped_image.png')

def resize_image():
    #reading image
    img = Image.open("my_image.png")
    width, height = img.size
    # calling the resize method ...
    img = img.resize((int(width/2),int(height/2)))
    img.save('resized_image.png')

def add_filters():
   # filters = ['CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'SMOOTH', 'SHARPEN']
    img = Image.open('my_image.png')
    # Applying filters
    contour_image = img.filter(ImageFilter.CONTOUR)
    contour_image.save('Contour_image.png')
    # DETAIL FILTER
    detail_image = img.filter(ImageFilter.DETAIL)
    detail_image.save('detail_image.png')
    # EDGE ENHANCE FILTER
    edge_enhance_image = img.filter(ImageFilter.EDGE_ENHANCE)
    edge_enhance_image.save('edge_image.png')
    # SMOOTH FILTER
    smooth_image = img.filter(ImageFilter.SMOOTH)
    smooth_image.save('smooth_image.png')

def rotate_image():
    # reading image
    img = Image.open('my_image.png')
    #img = img.rotate(90)
    # Flipping image from left to right using transpose method
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # saving image
    img.save('rotated_image.png')


if __name__ == '__main__':
    # Uncomment the below lines one by one to see the magic ..
    #read_image()
    #crop_image()
    #resize_image()
    #add_filters()
    #rotate_image()