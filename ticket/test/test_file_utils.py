import os.path

import pytest

from ticket.files.FileUtils import FileUtils
from ticket.Constants import ROOT_PATH


@pytest.mark.unit
def test_file_001():
    file_utils = FileUtils()
    content_write = 'my content'
    file_path = 'MyName.txt'
    target_dir = os.path.join(ROOT_PATH, 'tests')
    file_utils.write_file(content_write, target_dir, file_path)

    content_read = file_utils.read_file(target_dir, file_path)

    assert (content_read == content_write)
    file_utils.delete_file(target_dir, file_path)

    try:
        file_utils.read_file(target_dir, file_path)

        assert False
    except FileNotFoundError as e:

        assert ('No such file or directory' in str(e))
