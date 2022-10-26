import pytest

def pytest_addoption(parser):
    parser.addoption('--city_name', action='store', default=None,
                     help="Choose city name to group records")

@pytest.fixture(scope="class")
def group_city_name(request):
    city_name=request.config.getoption("city_name")
    yield city_name