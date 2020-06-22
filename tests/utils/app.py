import os
from jinja2 import FileSystemLoader, PrefixLoader
from flask import Flask, render_template_string, request

app = Flask(__name__)

loader = PrefixLoader({
    'govuk_frontend_jinja': FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__),
                                             '../../govuk_frontend_jinja/templates'))
})
app.jinja_loader = loader

@app.route('/template', methods=['POST'])
def template():
    data = request.json
    template = '''
        {% extends "govuk_frontend_jinja/template.html" %}
        {% block pageTitle %}{% if pageTitle %}{{ pageTitle }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block headIcons %}{% if headIcons %}{{ headIcons }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block head %}{% if head %}{{ head }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block bodyStart %}{% if bodyStart %}{{ bodyStart }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block skipLink %}{% if skipLink %}{{ skipLink }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block header %}{% if header %}{{ header }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block main %}{% if main %}{{ main }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block beforeContent %}{% if beforeContent %}{{ beforeContent }}{% else %}{{ super() }}{% endif %}{% endblock %} # noqa: E501
        {% block content %}{% if content %}{{ content }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block footer %}{% if footer %}{{ footer }}{% else %}{{ super() }}{% endif %}{% endblock %}
        {% block bodyEnd %}{% if bodyEnd %}{{ bodyEnd }}{% else %}{{ super() }}{% endif %}{% endblock %}
    '''

    return render_template_string(template, **data)

@app.route('/component/<component>', methods=['POST'])
def component(component):
    data = request.json

    return render_template_string('''
        {{% from "govuk_frontend_jinja/components/" + component + "/macro.html" import govuk{macro_name} %}}
        {{{{ govuk{macro_name}(params) }}}}
    '''.format(macro_name=data['macro_name']),
        component=component,
        params=data['params']
    )




