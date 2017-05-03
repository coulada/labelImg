import _init_path

from unittest import TestCase

from labelImg import get_main_app

from pascal_voc_io import PascalVocWriter
from pascal_voc_io import PascalVocReader


class TestMainWindow(TestCase):

    app = None
    win = None

    def setUp(self):
        self.app, self.win = get_main_app()

    def tearDown(self):
        self.win.close()
        self.app.quit()

    def test_noop(self):
        pass

# Test Write/Read
writer = PascalVocWriter('tests', 'test', (512, 512, 1), localImgPath='tests/test.bmp')
difficult = 1
writer.addBndBox(60, 40, 430, 504, 'person', difficult)
writer.addBndBox(113, 40, 450, 403, 'face', difficult)
writer.save('tests/test.xml')

reader = PascalVocReader('tests/test.xml')
shapes = reader.getShapes()
