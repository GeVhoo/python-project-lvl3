import pytest
import tempfile
import os
from page_loader.save import save

HELLO = 'Hello World!'


def test_save():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = tmpdirname
        file_name = os.path.join(str(tmpdir), 'new.jpg')
        with open('./tests/fixtures/bs.jpg', 'rb') as ef:
            expected_file = ef.read()
            save(file_name, expected_file, write_mod='wb')
            with open(file_name, 'rb') as nf:
                new_file = nf.read()
                assert new_file == expected_file


def test_save_exceptions():
    with pytest.raises(PermissionError) as error:
        save('/new.html', HELLO)
    assert 'Permission denied' in str(error)
