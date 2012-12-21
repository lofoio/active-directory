#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.template import Template, Context
raw_template = """<p>Dear {{ person_name }},</p>

<p>Thanks for placing an order from {{ company }}. It's scheduled to
ship on {{ ship_date|date:"F j, Y" }}.</p>

{% if ordered_warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% else %}
<p>You didn't order a warranty, so you're on your own when
the products inevitably stop working.</p>
{% endif %}

<p>Sincerely,<br />{{ company }}</p>"""
t = Template(raw_template)
import datetime
c = Context({'person_name': 'John Smith',
    'company': 'Outdoor Equipment',
    'ship_date': datetime.date(2009, 4, 2),
    'ordered_warranty': False})
t.render(c)
