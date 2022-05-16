def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            //return name of txt file
            module = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, module, ids=[repr(id) for id in module])