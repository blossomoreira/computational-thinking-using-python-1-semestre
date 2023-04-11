salario_fixo = float (input(""))
valor_comissao = float (input(""))
nrm_carros = int (input(""))
valor_total_vendas = float (input(""))

salario_fixo = salario_fixo + (nrm_carros * valor_comissao) + (valor_total_vendas * 3.05)
print(salario_fixo)