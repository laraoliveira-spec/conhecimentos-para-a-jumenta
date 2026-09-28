idade = int(input("Informe sua idade: "))
condicionamento_bom = input("Você tem um bom condicionamento? (True ou False)")
permissao_medica = input("Você tem permissão médica? (True ou False)")
if 18 <= idade <=35 and (condicionamento_bom == "True" or permissao_medica == "True"):
    print("Você pode entrar!")
else:
    print("Você não pode entrar.")