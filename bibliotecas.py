
import json
"""
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
z =  '[{ "name":"John", "age":30, "city":"New York"}]'
# parse x:
y = json.loads(x)
w = json.loads(z)

# the result is a Python dictionary:
print(y["age"])
print(w)

print([1,2,3])


# Separators argument
print(json.dumps(y, indent=4, separators=(". ", " = ")))

# Sort keys
print(json.dumps(y, indent=4, sort_keys=True))

"""

import emoji

print(emoji.emojize('Python is :thumbs_up:'))


from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Treinamento'))

