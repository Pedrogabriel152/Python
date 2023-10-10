def cpf_valido(cpf) -> bool:
    return len(cpf) == 11

def nome_valido(nome) -> bool:
    return nome.isalpha()

def rg_valido(rg) -> bool:
    return len(rg) != 9

def celular_valido(celular):
    return len(celular) < 11