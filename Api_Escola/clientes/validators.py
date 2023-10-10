import re
from validate_docbr import CPF

def cpf_valido(cpf) -> bool:
    cpfVrify = CPF()
    return cpfVrify.validate(cpf)

def nome_valido(nome) -> bool:
    return nome.isalpha()

def rg_valido(rg) -> bool:
    return len(rg) == 9

def celular_valido(celular):
    """Vrificar se o celular é valido (62) 99691-5851"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    respota = re.findall(modelo, celular)
    return respota