import os.path
import unittest
from files.FileUtils import FileUtils
from Constants import ROOT_PATH


class TestFileUtils(unittest.TestCase):
    def test_file_001(self):
        file_utils = FileUtils()
        content_write = 'mi contenido'
        file_path = 'MiNombre.txt'
        target_dir = os.path.join(ROOT_PATH, 'tests')
        file_utils.write_file(content_write, target_dir, file_path)

        content_read = file_utils.read_file(target_dir, file_path)

        self.assertEqual(content_read, content_write)

        file_utils.delete_file(target_dir, file_path)

        try:
            file_utils.read_file(target_dir, file_path)
            self.assertTrue(False)
        except FileNotFoundError as e:
            self.assertTrue('No such file or directory' in str(e))
