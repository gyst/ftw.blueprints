from ftw.blueprints.sections import mapper
from ftw.blueprints.tests.base import BlueprintTestCase


INPUT = {
    '_path': '/foo/bar',
    '_type': 'Folder',
    '_id': 'bar',
    'title': 'test',
    }


class TestPathMapper(BlueprintTestCase):

    def setUp(self):
        self.klass = mapper.PathMapper
        self.input_data = INPUT

    def _get_options(self, additional_options=None):
        options = {'blueprint': 'ftw.blueprints.pathmapper'}
        if additional_options:
            options.update(additional_options)
        return options

    def test_map_value(self):
        expected = self._get_expected({'_path': '/qux/bar'})

        options = self._get_options(
            {'mapping': "python:( ('^/foo', '/qux'), )"}
        )
        self.assert_result(options, expected)

    def test_map_order(self):
        expected = self._get_expected({'_path': '/qux/bar'})

        options = self._get_options(
            {'mapping': "python:("
                "('^/foo', '/qux'),"
                "('^/foo/bar', '/nix/nax'),"
             ")"}
        )
        self.assert_result(options, expected)

    def test_map_condition(self):
        expected = self._get_expected()

        options = self._get_options({
            'mapping': "python:( ('^/foo', '/qux'), )",
            'condition': 'python: False',
        })
        self.assert_result(options, expected)