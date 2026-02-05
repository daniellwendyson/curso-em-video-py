msg = input('Digite algo: ')
print(type(msg))
print(f'O valor é alfanumérico? {msg.isalnum()}')
print(f'O valor é alfabético? {msg.isalpha()}')
print(f'Está em letras minúsculas? {msg.islower()}')
print(f'Está em letras maiúsculas? {msg.isupper()}')
print(f'O valor é numérico? {msg.isnumeric()}')
print(f'Está capitalizado? {msg.istitle()}')

