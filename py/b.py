#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

data = cgi.FieldStorage()
terms = 'a,b,c,d'
if ('terms' in data):
    terms = data['terms'].value.split(',')
defs = '1,2,3,4'
if ('defs' in data):
    defs = data['defs'].value.split(',')
    
form = cgi.FieldStorage()