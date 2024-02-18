#3508 х 2480, 1754 x 1280
# frames 74 (37x2), 80 (40x2)
# 1680 x 1200
# 840 x 600
import fitz
from google_images_search import GoogleImagesSearch
import base_services as Base

DEV_API_KEY = "AIzaSyCKjwxRY4QXtpEj50JjYHZ8L0OBdpfZCV4"
PROJECT_CX = "3551db191960f40c9"

class Card:
    def __init__(self, _type, database):
        self._type = _type
        self.manufacturer = None
        self.model = None
        self.image = None
        self.emblem = None
        self.box = None
        self.get_tech(database)
        self.get_image()

    def get_tech(self, database):
        new_tech = Base.get_new_tech(self._type, database)
        self.manufacturer = new_tech[0]
        self.model = new_tech[1]
        self.emblem = self.get_emblem(new_tech[2])
        self.box = self.get_box(new_tech[3])

    def get_image(self):
        with open('files/no_data.png', 'rb') as default_image_file:
            default_image = default_image_file.read()
        images_list = get_images_list(manufacturer, model)
        if images_list:
            pass
        return default_image

    def get_emblem(self, emblem_file_name):
        pass

    def get_box(self, box_file_name):
        pass


def get_images_list(manufacturer, model):
    gis = GoogleImagesSearch(DEV_API_KEY, PROJECT_CX)
    gis.search(search_params={'q': f'{manufacturer} {model}', 
                              'num': 10})
    results = gis.results()
    print(type(results))


def create_new_pdf():
    pdf = fitz.open()
    page = pdf._newPage()
    page.set_rotation(90)
    database = Base.read_excel_file()
    cards = [Card('civil', database), 
             Card('commercial', database), 
             Card('military', database),
             Card('aero', database)]
    rects = [page.Rect(40, 37, 640, 877),
             page.Rect(640, 37, 1240, 877),
             page.Rect(40, 877, 640, 1717),
             page.Rect(640, 877, 1240, 1717)]
    for i in range(3):
        page.insert_image(rects[i], stream=cards[i].image)
    return pdf
    

def make_preview_image_binary():
    pdf = create_new_pdf()
    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    page = pdf.load_page(0)
    pix = page.get_pixmap(matrix=mat)
    pdf.close()
    return pix