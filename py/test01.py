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
<title>Bad Quizlet</title>
<link href="final.css" rel="stylesheet">
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

# Initialize index i
i = 0
if 'index' in data0:
    i = int(data0['index'].value)

html = HTML_HEADER
html += '''
<form action="/py/test01.py" method="GET">
Next Term <input type="checkbox" name="next_term" value="yes">
<br>
Show Def <input type="checkbox" name="show_def" value="show_def">
<br>
<input type="hidden" name="terms" value="'''
html += terms
html += '''"><input type="hidden" name="defs" value="'''
html += defs
html += '''">
<input type="hidden" name="index" value="'''
html += str(i)
html += '''">
<input type="submit" name="submit" value="Submit">
</form>
'''

# Show the current term
html += '<p>Term: ' + term_list[i] + '</p>'

# Process form submission
# Maybe need to make a new python file for new form
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

# Update the hidden index value
html += '<input type="hidden" name="index" value="' + str(i) + '">'

html += HTML_FOOTER
print(html)
