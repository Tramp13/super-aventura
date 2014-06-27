import os

#default bindings
default_bindings = """KEY_UP:UP
KEY_RIGHT:RIGHT
KEY_DOWN:DOWN
KEY_LEFT:LEFT
x:SELECT
q:QUIT
k:UP
l:RIGHT
j:DOWN
h:LEFT"""

bindings = {}

def load_bindings():
    if (os.path.isdir(os.path.expanduser('~/.adventure')) == False):
        os.makedirs(os.path.expanduser('~/.adventure'))
    if (os.path.exists(os.path.expanduser('~/.adventure/keys.txt')) == False):
        binding_file = open(os.path.expanduser('~/.adventure/keys.txt'), 'w')
        binding_file.write(default_bindings)
        binding_file.close()

    binding_file = open(os.path.expanduser('~/.adventure/keys.txt'), 'r')

    binding_data = binding_file.read()
    binding_data.replace(' ', '')
    binding_data = binding_data.split('\n')
    for i in binding_data:
        binding = i.split(':')
        if len(binding) < 2:
            continue
        bindings[binding[0]] = binding[1]
    binding_file.close()
