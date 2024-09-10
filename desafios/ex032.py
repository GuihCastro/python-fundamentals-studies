# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

year = str(input('Informe um ano (no formato "0000"), ou digite "0" para analisar o ano atual: '))

if int(year) == 0:
    year = str(date.today().year)

if ((year[2:] != '00') and (int(year) % 4 == 0)) or ((year[2:] == '00') and (int(year) % 400 == 0)):
    print('O ano informado É BISSEXTO!')
else:
    print('O ano informado NÃO é BISSETO!')
