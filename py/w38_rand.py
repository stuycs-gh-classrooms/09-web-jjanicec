#!/usr/bin/python3
print('Content-type: text/html\n')

from random import random
r = random()
print('Have a random number! :D', r)

print('''
<head><title>random w38</title></head>
<body style = "background-color:lime;">
<p>
Hello! This is a random number:''', r,
      '''</p> </body>''')