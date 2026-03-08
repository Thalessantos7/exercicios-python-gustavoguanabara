""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense. """
times = ("Palmeiras", "São Paulo", "Corinthians", "Bahia", "Fluminense", "Athletico-PR", "Red Bull Bragatino", 'Grêmio', "Chapecoense",
        "Mirassol", "Flamengo", "Coritiba", "Santos", "Botafogo", "Vitória", "Remo", "Atlético-MG", "Internacional", "Cruzeiro", "Vasco")

print(f"""5 primeiros times:
1. {times[0]}
2. {times[1]}
3. {times[2]}
4. {times[3]}
5. {times[4]}

Últimos 4 colocados:
17. {times[-4]}
18. {times[-3]}
19. {times[-2]}
20. {times[-1]}

Times em ordem alfabética:
{sorted(times)}"

Posição da Chapecoense:
{times.index("Chapecoense") + 1}. Chapecoense""")