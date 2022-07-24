import os
import random
from string import Template
import jinja2

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                         'manufacturing_data.yaml')


def render(**kwargs):
    data_yaml = jinja2.Environment(loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                     'manufacturing_data.yaml'))).get_template('manufacturing_data.yaml').render(
        **kwargs)
    return data_yaml


def rand_str(num1, num2):
    return str(random.randint(num1, num2))
