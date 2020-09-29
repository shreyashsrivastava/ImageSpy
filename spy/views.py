from django.http import HttpResponse, JsonResponse
from PIL import Image 
import requests
from io import BytesIO

def get_dom(request):
    url = request.GET['src']
    image = requests.get(url)

    im = Image.open(BytesIO(image.content))
    im.convert("RGB")
    print(im.mode)
    border = imborder(im)

    bottom_border = border[0]
    bottom_dom = dom_color(bottom_border)

    left_border = border[1]
    left_dom = dom_color(left_border)

    top_border = border[2]
    top_dom = dom_color(top_border)

    right_border = border[3]
    right_dom = dom_color(right_border)

    r = (bottom_dom[0] + left_dom[0] + top_dom[0] + right_dom[0])//4
    g = (bottom_dom[1] + left_dom[1] + top_dom[1] + right_dom[1])//4
    b = (bottom_dom[2] + left_dom[2] + top_dom[2] + right_dom[2])//4

    logo_border = '#%02x%02x%02x' % (r,g,b)
    # dominant_color = '#%02x%02x%02x' % dom_color(im)
    dominant_color = '#{:02x}{:02x}{:02x}'.format(*dom_color(im))
    # dominant_color = dom_color(im)

    return JsonResponse({'logo_border':logo_border, 
                        'dominant_color':dominant_color,
                       })

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
