#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
<body>
"""

HTML_FOOTER = """
</body>
</html>
"""

data0 = cgi.FieldStorage()
terms = 'a,b,c,d'
defs = '1,2,3,4'
if 'terms' in data0:
    terms = data0['terms'].value
if 'defs' in data0:
    defs = data0['defs'].value
term_list = terms.split(',')
def_list = defs.split(',')
next_term = 'no'
show_def = 'no'

# Initialize index i
i = 0
if 'index' in data0:
    i = int(data0['index'].value)

html = HTML_HEADER
html += '<p>Term: ' + term_list[i] + '</p>'

if 'next_term' in data0 and data0['next_term'].value == 'yes':
    i += 1
    if i < len(term_list):
        html += '<p>Next Term: ' + term_list[i] + '</p>'
    else:
        html += '<p>No more terms.</p>'
        i = len(term_list) - 1
if 'show_def' in data0 and data0['show_def'].value == 'show_def':
    if i < len(def_list):
        html += '<p>Definition: ' + def_list[i] + '</p>'
html += HTML_FOOTER
print(html)
