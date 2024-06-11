#!usr/bin/python
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
term_list = terms.split(',')
def_list = defs.split(',')

html = HTML_HEADER

#Show the current term
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

# Update the hidden index value
html += '<input type="hidden" name="index" value="' + str(i) + '">'

html += HTML_FOOTER
print(html)
