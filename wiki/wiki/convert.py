import markdown 

s = '''\
# Hello World!

This is a little demonstration of how to convert markdown into HTML in a pretty lazy way.

** an enumeration **

1. Anton
2. Berta
3. Carla
4. Detlef
5. Emil

See more information on [devdungeon](https://www.devdungeon.com/content/convert-markdown-html-python).
\
'''

print(markdown.markdown(s))  
