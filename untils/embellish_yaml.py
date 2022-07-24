import jinja2
import os, random, yaml, string
from string import Template

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                         'manufacturing_data.yaml')


def ue_code():
    print()
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))


def number():
    print()
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))

def render(func):
    def wrapper(path=data_path, **kwargs):
        path, filename = os.path.split(path)
        data_yaml = jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(
            "manufacturing_data.yaml").render(**kwargs)
        print()
        return data_yaml


if __name__ == '__main__':
    r = render(**{"ue_code": ue_code, "number": number})
    print(r)
