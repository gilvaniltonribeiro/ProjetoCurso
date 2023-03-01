champ = input('Qual lane você joga no League?')
if champ == 'Jungle':
    print('Você deve ter boa percepção e visão de jogo para essa rota!')
elif champ in 'Adc':
    print('Você precisa demonstrar paciência para seu momento de brilhar na partida!')
elif champ == 'Mid':
    print('Nesta lane se recebe muitos ganks então ward bem.')
elif champ in 'Top Sup':
    print('Parabéns você joga em seu próprio mini-game.')
else:
    print('As opções são Jungle, Adc, Mid, Top e Sup. Verifique se digitou corretamente.')
