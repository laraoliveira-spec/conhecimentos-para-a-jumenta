nome_negativado = input("Você possui o nome negativado (sim ou não)? ")
if nome_negativado == "sim":
    print("Não pode realizar empréstimo.")
else:
    carteira_assinada = input("Você trabalha de carteira assinada (sim ou não)? ")
    if carteira_assinada == "não":
        print("Não pode realizar empréstimo.")
    else:
        casa_propria = input("Possui casa própria (sim ou não)? ")
        if casa_propria == "não":
            print("Não pode realizar empréstimo.")
        else:
            print("Conceder empréstimo.")