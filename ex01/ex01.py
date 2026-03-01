texto = "Sítio do pica-pau amarelo \n 2023"

caracteres = [c for c in texto if not c.isspace()]

print("String original :", repr(texto))
print("Caracteres filtrados:", caracteres)
print("Resultado como string:", "".join(caracteres))
