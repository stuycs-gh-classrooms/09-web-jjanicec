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
term_iter = iter(term_list)
def_list = defs.split(',')
def_iter = iter(def_list)

'''
# Initialize index i
i = 0
if 'index' in data0:
    i = int(data0['index'].value)
'''

html = HTML_HEADER
html += '''
<form action="test001.py" method="GET">
Show Def <input type="checkbox" name="show_def">
<br>
<input type="hidden" name="terms" value=" '''
html += terms
html += ''' "> <input type="hidden" name="definitions" value=" '''
html += defs
html += ''' ">
'''
<input type="submit" name="submit" value="Submit">
</form>
'''
'''
# Show the current term
html += '<p>Term: ' + next(term_iter) + '</p>'
#used to be term_list[i]

# Process form submission
# Maybe need to make a new python file for new form
if 'next_term' in data0 and data0['next_term'].value == 'on':
    #i += 1
    #if i < len(term_list):
    if next(term_iter) != term_list[len(term_list) - 1]:
        html += '<p>Next Term: ' + next(term_iter) + '</p>'
        #used to be term_list[i]
    else:
        html += '<p>No more terms.</p>'
        #i = len(term_list) - 1
if 'show_def' in data0 and data0['show_def'].value == 'on':
    #if i < len(def_list):
    if next(def_iter) != def_list[len(def_list) - 1]:
        html += '<p>Definition: ' + next(def_iter) + '</p>'
#used to be def_list[i]
# Update the hidden index value
#html += '<input type="hidden" name="index" value="' + str(i) + '">
'''
'''
for term in term_list:
    if 'next_term' in data0 and data0['next_term'].value == 'on':
        html += '<p>Next Term: ' + term + '</p>'
        print(html)
for defs in def_list:
    if 'show_def' in data0 and data['show_def'].value == 'on':
        html += '<p>Definition: ' + defs + '</p>'
        print(html)
'''

'''
i = 0
while i < len(term_list):
    html += '<p>Term: ' + term_list[i] + '</p>'
    html += '<br><p style="color:rgb(203 247 236);">Definition: ' + def_list[i] + '</p>'
    i += 1
if 'show_def' in data0 and data['show_def'].value == 'on':
    html.replace('rgb(203 247 236);', 'black')
    html += HTML_FOOTER
    print(html)
'''

html += HTML_FOOTER
print(html)
