import random
from colorama import Fore, Style

niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]
situacao = ["Muito baixo (Crítico)", "Baixo", "Médio", "Alto", "Muito alto (alerta)"]

sorteado = random.choice(niveis)
print(f'Nível sorteado: {sorteado}')

if sorteado == "Nível 1":
    print(Fore.RED + "Muito baixo (Crítico)")
elif sorteado == "Nível 2":
    print(Fore.YELLOW +  "Baixo")
elif sorteado == "Nível 3":
    print(Fore.GREEN + "Médio")
elif sorteado == "Nível 4":
    print(Fore.CYAN + "Alto")
elif sorteado == "Nível 5":
    print(Fore.BLUE + "Muito alto (alerta)")
print(Style.RESET_ALL)