from os import mkdir    
from qrcode import make


print('Cadastro de Alunos via QRcode. V1')
name = input('Nome completo do Aluno: ')
mkdir(f'{name}')
qrcode_image = make(name)
qrcode_image.save(f'{name}\\{name}.png')
