from rembg import remove
from PIL import Image

class bg():

    def __init__(self, input_path, output_path):
        self.input = input_path
        self.output = output_path
        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)

bg1 = bg('apel.jpg', 'apel.png')
bg2 = bg('jeruk.jpg', 'jeruk.png')
bg3 = bg('semangka.jpg', 'semangka.png')

