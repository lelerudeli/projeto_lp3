from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True)) #com mascara
print(cpf.generate(False)) #sem mascara

print(cpf.validate('660.661.537-22')) #True
print(cpf.validate('50000')) #False

cpfs = {
    "39973705831",
    "28800502865",
    "30294"
}

print(cpf.validate_list(cpfs)) # True, True e False

