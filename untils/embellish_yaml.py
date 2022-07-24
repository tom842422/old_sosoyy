import jinja2
import os, random, yaml,string
from string import Template

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                         'manufacturing_data.yaml')


class EmbellishYaml:
    def __init__(self):
        pass

    @staticmethod
    def render(**kwargs):
        data_yaml = jinja2.Environment(loader=jinja2.FileSystemLoader(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                         'manufacturing_data.yaml'))).get_template('manufacturing_data.yaml').render(
            **kwargs)
        return data_yaml

    def uncode(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))

    def number(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))
