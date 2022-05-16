import os
import pytest

print(os.path.splitext("/path/to/some/file.txt")[0])

@pytest.mark.parametrize('param', ['hello.txt', 'pupkin.txt', 'example.txt'])
def test_example(param, alice):
    file_name = os.path.basename("./example.txt")
    print(file_name)

    assert str(file_name) == str(param), "expected {},  got {}".format(file_name, param)
