#!/usr/bin/python

# Required header to tell the browser the type of content to expect
print('Content-type: text/html\n')

# Enable debugging and error reporting
import cgitb
cgitb.enable()

import cgi

# HTML templates for the header and footer
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

# Retrieve the form data
data = cgi.FieldStorage()

# Extract the form fields with default values
terms = data.getvalue('terms', 'No Terms Provided')
defs = data.getvalue('defs', 'No Defs Provided')

# Create the HTML response
html = HTML_HEADER
html += f'<h1>Submitted Data</h1>'
html += '<ul>'
html += f'<li>Terms: {terms}</li>'
html += f'<li>Defs: {defs}</li>'
html += '</ul>'
html += '<br><a href="hello.html">Try Again</a>'
html += HTML_FOOTER
print(html)
