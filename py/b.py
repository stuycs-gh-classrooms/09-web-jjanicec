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
"""

HTML_FOOTER = """
</body>
</html>
"""

data = cgi.FieldStorage()
terms = 'a,b,c,d'
if ('terms' in data):
    terms = data['terms'].value
defs = '1,2,3,4'
if ('defs' in data):
    defs = data['defs'].value
term_list = terms.split(',')
def_list = defs.split(',')

html= HTML_HEADER
#html+= '<br><a href="b.html">Try Again</a></br>'
html+='<p>' + terms + '</p>' + '<p>' + defs + '</p>'
html+='<p>', term_list, '</p>' , '<p>' , def_list , '</p>'
html+= HTML_FOOTER
print(html)
