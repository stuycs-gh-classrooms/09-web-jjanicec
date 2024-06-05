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

data0 = cgi.FieldStorage()
terms = 'a,b,c,d'
if ('terms' in data0):
    terms = data0['terms'].value
defs = '1,2,3,4'
if ('defs' in data0):
    defs = data0['defs'].value
term_list = terms.split(',')
def_list = defs.split(',')

html= HTML_HEADER
#html+= '<br><a href="b.html">Try Again</a></br>'
#html+='<body>' + '<p>' + terms + '</p>' + '<p>' + defs + '</p>'
#html+='<p>' + str(term_list) + '</p>' + '<p>' + str(def_list) + '</p>'

html+='''
<body>
<form action="py/b.py" method="GET">
Next Term <input type="checkbox" name="next_term" value="yes">
<br>
<input type="submit" name="submit">
<br>
Show Def <input type="checkbox" name="show_def" value="show_def">
<br>
<input type="submit" name="submit">
</form>
'''

#another form
i = 0
html+= '<p>' + str(term_list[i]) + '</p>'

data1 = cgi.FieldStorage()
next_term = 'yes'
if ('next_term' in data1):
    next_term = data1['next_term'].value
    if next_term == 'yes':
        i += 1
        html += '<p>' + str(term_list[i]) + '</p>'
        html += HTML_FOOTER
        print(html)
show_def = 'no_show'
if ('show_def' in data1):
    show_def = data1['show_def'].value
    if show_def == 'show_def':
        html += '<p>' + str(def_list[i]) + '</p>'
        html += HTML_FOOTER
        print(html)

html+= HTML_FOOTER
print(html)
