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
term = 'a,b,c,d'
if ('term' in data):
    terms = data['terms'].value.split(',')
defs = '1,2,3,4'
if ('defs' in data):
    def_list = data['defs'].value.split(',')

html= HTML_HEADER
#html+= '<br><a href="b.html">Try Again</a></br>'
html+='<p>', terms, '</p>' , '<p>' , def_list , '</p>'
html+= HTML_FOOTER
print(html)
