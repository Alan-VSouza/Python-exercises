# Faça um programa que leia o salário fixo de um vendedor e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 18% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês.

salario = float(input())
comis = float(input())

salariof = salario + (comis/100 * 18)

print(f'{salariof:.2f}')