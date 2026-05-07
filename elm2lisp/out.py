from collections import namedtuple
from jinja2 import Template

with open('templates/object.jinja') as f:
    tmpl = Template(f.read())

object_type = namedtuple("Object",["name","parent"])
objects = [object_type("shape",None), object_type("rectangle","shape"), object_type("circle","shape"), object_type("square","rectangle")]
print(tmpl.render(objects=objects))
