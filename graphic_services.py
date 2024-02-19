#3508 х 2480, 1754 x 1280
# frames 74 (37x2), 80 (40x2)
# 1680 x 1200
# 840 x 600
# 842x598
# 72 points in 1 inch  11.7 x 8.3 " дюймов  koef=2.1
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
        with open('files/flag_masks/no_data.png', 'rb') as default_image_file:
            default_image = default_image_file.read()
        images_list = None
        #images_list = get_images_list(self.manufacturer, self.model)
        if images_list:
            pass
        self.image = default_image

    def get_emblem(self, emblem_file_name):
        pass

    def get_box(self, box_file_name):
        pass


def get_images_list(manufacturer, model):
    gis = GoogleImagesSearch(DEV_API_KEY, PROJECT_CX)
    gis.search(search_params={'q': f'{manufacturer} {model}', 
                              'num': 1})
    results = gis.results()


def create_new_pdf():
    pdf = fitz.open()
    page = pdf._newPage()
    database = Base.read_excel_file()
    cards = [Card('civil', database), 
             Card('commercial', database), 
             Card('military', database),
             Card('aero', database)]
    rects = [fitz.Rect(14, 14, 301, 416),
             fitz.Rect(301, 14, 586, 416),
             fitz.Rect(14, 416, 301, 817),
             fitz.Rect(301, 416, 586, 817)]
    for i in range(4):
        page.insert_image(rects[i], stream=cards[i].image, rotate=90, keep_proportion=False)
        pdf.save(f'temp_pdf_{i}.pdf')
    return pdf
    

def make_preview_image_binary():
    pdf = create_new_pdf()
    zoom = 0.5
    mat = fitz.Matrix(zoom, zoom)
    page = pdf.load_page(0)
    pix = page.get_pixmap(matrix=mat)
    pdf.close()
    return pix.tobytes()