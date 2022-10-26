import pytest

from Tests.data_util.data_resolver import inject_json_from_file
from jsonschema import validate

class TestCityName:
    schema = inject_json_from_file(file="schema.json")
    test_data = inject_json_from_file(file="elastic_data.json")['hits']['hits']

    @pytest.mark.parametrize("input", test_data)
    @pytest.mark.from_console
    def test_city_name_from_console(self, input, group_city_name):
        print(group_city_name)
        if input.get("_source").get("geoip").get("city_name")==group_city_name:
            validate(instance=input, schema=self.schema)
        else: pytest.skip("record out of group")

    @pytest.mark.parametrize("input", test_data)
    def test_city_name_is_none(self, input):
        if input.get("_source").get("geoip").get("city_name") is None:
            validate(instance=input, schema=self.schema)
        else: pytest.skip("record out of group")

    @pytest.mark.parametrize("input", test_data)
    def test_city_name_except_none(self, input):
        if input.get("_source").get("geoip").get("city_name") is not None:
            validate(instance=input, schema=self.schema)
        else: pytest.skip("record out of group")