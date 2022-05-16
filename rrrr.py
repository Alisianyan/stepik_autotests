def test_example():
    file_name = os.path.basename("./example.txt")
    print(file_name)
    #assert 3 == 3, "3 == 3"
    assert "example.txt" == str(file_name), "expected {},  got {}".format(file_name, param)