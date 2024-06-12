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

'''
# Initialize index i
i = 0
if 'index' in data0:
    i = int(data0['index'].value)
'''

html = HTML_HEADER
i = 0
while i < len(term_list):
    html += '<p>Term: ' + term_list[i] + '</p>'
    html += '<br><p style="color:rgb(203 247 236);">Definition: ' + def_list[i] + '</p>'
    i += 1
if 'show_def' in data0 and data['show_def'].value == 'yes':
    html = html.replace('rgb(203 247 236);', 'black')

html += HTML_FOOTER
print(html)
