from rest_framework.generics import ListAPIView
from .models import UploadImageTest, nameFile
from .serializers import ImageSerializer
from django.http import HttpResponse
import json
from PIL import Image


class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = UploadImageTest.objects.create(image=file)
        img  = UploadImageTest.objects.get(id=image.id)
        im = Image.open(img.image)
        im.convert("RGB")

        dominant_color = dom_color(im)

        border = imborder(im)

        bottom_border = border[0]
        bottom_dom = dom_color(bottom_border)

        left_border = border[1]
        left_dom = dom_color(left_border)

        top_border = border[2]
        top_dom = dom_color(top_border)

        right_border = border[3]
        right_dom = dom_color(right_border)


        return HttpResponse(json.dumps({'message': "Uploaded", 
                                        'dominant_color':dominant_color, 
                                        'bottom_border_color':bottom_dom, 
                                        'left_border_color':left_dom, 
                                        'top_border_color':top_dom, 
                                        'right_border_color':right_dom, 
                                        }), status=200)

def imborder(im):
    image_resized = im.resize((500,500))

    top_border = (0, 0, 500, 25)
    top_img = image_resized.crop(top_border)

    left_border = (0,0,25,500)
    left_img = image_resized.crop(left_border)  

    bottom_border = (25,475,500,500)
    bottom_img = image_resized.crop(bottom_border)
    
    right_border = (475,25,500,500)
    right_img = image_resized.crop(right_border)

    return [bottom_img, left_img, top_img, right_img]

def dom_color(im):
    im.resize((1, 1), resample=0)
    return im.getpixel((0, 0))
