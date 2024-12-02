str_input = input()
inputs = []
while str_input != '':
    inputs.append(str_input)
    str_input = input()

print('[' + ', '.join(inputs)+ ']')

print(type(1.2))