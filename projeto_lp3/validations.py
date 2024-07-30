from validate_docbr import CPF, CNPJ

def validaCpf():
    cpf = CPF()
    cpf = cpf.generate(True) #com mascara
    # cpf.validate(cpf) #True

    return cpf

def validaCnpj():
    cnpj = CNPJ()
    cnpj = cnpj.generate(True) #com mascara
    # cpf.validate(cpf) #True

    return cnpj