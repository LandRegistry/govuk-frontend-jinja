#!/usr/bin/env python3

import argparse
import json
import os
from jinja2 import Environment, FileSystemLoader, PrefixLoader

loader = PrefixLoader({
    'govuk_frontend_jinja': FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), '../../govuk_frontend_jinja/templates'))
})
env = Environment(loader=loader, autoescape=True)

parser = argparse.ArgumentParser(description='Render a govuk_frontend_jinja template.')
parser.add_argument('--component', metavar='Component name', nargs=1, help='The name of the component')
parser.add_argument('--params', metavar='Params', nargs=1,
                    help='JSON representation of the params to pass to the component macro')

args = parser.parse_args()


def hyphenated_to_camel(string):
    return ''.join(x.capitalize() for x in string.split('-'))


template = env.from_string('''
    {{% from "govuk_frontend_jinja/components/" + component + "/macro.html" import govuk{macro_name} %}}
    {{{{ govuk{macro_name}(params) }}}}
'''.format(macro_name=hyphenated_to_camel(args.component[0])))

print(template.render(
    component=args.component[0],
    params=json.loads(args.params[0])
))
