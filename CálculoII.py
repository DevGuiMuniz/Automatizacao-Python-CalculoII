# -*- coding: utf-8 -*-
"""CálculoII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/180NGI0G05bp3jtqOfCEAolC_hivt3wz0

![Sem título-1 1.png]( data:image/png;base64,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)

# **Cálculo II**

# *   **PARA UMA VISUALIZAÇÃO MELHOR UTILIZE O GOOGLE COLAB**
*   Utilizar a Materia de Cálculo II no Projeto de Desenvolvimento Web
*   Pontos **Máximos** e **Mínimos** e indentificando qual é a dor mais recorrente das pessoas em situação Vulnerável

# Utilizar pontos **Máximos** e pontos **Mínimos** de pessoas em situação Vulneráveis e traçar um grafico representando elas

## **Dados Capturados**

1. Taxa de Desemprego Geral
A taxa de desemprego no Brasil foi de 7,9% no segundo trimestre de 2023, o equivalente a cerca de 8,5 milhões de pessoas desempregadas (IBGE, PNAD Contínua).
2. Jovens e Desemprego
Jovens entre 18 e 24 anos são os mais afetados pelo desemprego no Brasil. Em 2022, a taxa de desemprego entre essa faixa etária foi de aproximadamente 22,8%, ou seja, quase 1 em cada 4 jovens estava sem emprego (IBGE).
O acesso limitado a oportunidades de qualificação profissional e formação técnica é um dos principais fatores que contribuem para o desemprego entre os jovens.
3. Impacto da Baixa Escolaridade no Desemprego
Pessoas sem o ensino médio completo têm maior dificuldade de inserção no mercado de trabalho. Em 2023, a taxa de desemprego entre pessoas com baixo nível de escolaridade (ensino fundamental incompleto) foi de cerca de 18% (PNAD Contínua).
Já entre aqueles com ensino superior completo, a taxa de desemprego é consideravelmente menor, em torno de 5%.
4. Desemprego por Falta de Qualificação
Estima-se que 40% dos desempregados no Brasil estão sem emprego devido à falta de qualificação ou habilidades técnicas exigidas pelo mercado (Instituto de Pesquisa Econômica Aplicada - IPEA, 2021).
Muitas empresas relatam dificuldades em encontrar trabalhadores com qualificações adequadas às suas necessidades, mesmo com vagas disponíveis.
5. Desenvolvimento Pessoal e Profissional
O Programa Nacional de Acesso ao Ensino Técnico e Emprego (Pronatec), criado para aumentar as oportunidades de educação técnica, alcançou cerca de 10,5 milhões de matrículas desde sua criação. No entanto, muitos jovens em situação de vulnerabilidade ainda têm dificuldade de acesso a esses programas, especialmente em áreas rurais e periféricas.
O Índice de Oportunidades de Desenvolvimento Pessoal e Profissional no Brasil é desigual. Populações de baixa renda, que representam uma grande parcela dos desempregados, têm menos acesso a programas de qualificação e educação continuada.
6. Desigualdade Regional
O desemprego é mais acentuado nas regiões Norte e Nordeste, que também enfrentam maiores dificuldades no acesso a educação de qualidade e cursos de qualificação profissional. Em algumas áreas, a taxa de desemprego pode chegar a 20% entre pessoas sem qualificação (Caged - Cadastro Geral de Empregados e Desempregados, 2022).
7. Impacto da Pandemia no Desenvolvimento Profissional
A pandemia de COVID-19 ampliou as barreiras de desenvolvimento pessoal e profissional, especialmente entre trabalhadores informais e de baixa qualificação. Durante a pandemia, mais de 5 milhões de pessoas deixaram de procurar emprego por falta de perspectiva, em parte devido à falta de habilidades compatíveis com as novas exigências do mercado de trabalho pós-pandemia (IBGE, 2021).
8. Projeções Futuras
O Banco Mundial estima que até 2030, cerca de 30% das ocupações no Brasil vão exigir níveis mais altos de qualificação profissional, o que pode aumentar ainda mais a disparidade de emprego entre os que têm acesso à educação e qualificação e os que não têm.
Sem investimentos massivos em desenvolvimento de habilidades, cerca de 40 milhões de trabalhadores brasileiros podem ficar excluídos das oportunidades de emprego que surgirão nos próximos anos.
"""

# Importar a bibliotecas do python
import pandas as pd
import matplotlib.pyplot as plt

#Dados
data = {
    "Categorias": [
        "Taxa de Desemprego Geral",
        "Desemprego Jovens (18-24 anos)",
        "Baixa Escolaridade (Sem Ensino Médio)",
        "Alta Escolaridade (Ensino Superior)",
        "Desemprego por Falta de Qualificação",
        "Desemprego Regional (Norte/Nordeste)"
    ],
    "Taxa de Desemprego (%)": [
        7.9, 22.8, 18.0, 5.0, 40.0, 20.0
    ]
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Identificar pontos máximos e mínimos
min_value = df["Taxa de Desemprego (%)"].min()
max_value = df["Taxa de Desemprego (%)"].max()

# Usar Pandas para plotar o gráfico
ax = df.plot(
    x="Categorias",
    y="Taxa de Desemprego (%)",
    kind="line",
    marker='o',
    color='b',
    figsize=(10, 6),
    title="Taxa de Desemprego por Falta de Oportunidade de Desenvolvimento Pessoal e Profissional"
)

# Destacar os pontos máximos e mínimos
ax.scatter(df.index[df["Taxa de Desemprego (%)"] == min_value], [min_value], color='green', label='Mínimo')
ax.scatter(df.index[df["Taxa de Desemprego (%)"] == max_value], [max_value], color='red', label='Máximo')

# Adicionar anotações
ax.text(df.index[df["Taxa de Desemprego (%)"] == min_value].values[0], min_value + 0.5, f'{min_value}%', ha='center', color='green')
ax.text(df.index[df["Taxa de Desemprego (%)"] == max_value].values[0], max_value + 0.5, f'{max_value}%', ha='center', color='red')

# Ajustar ticks para o número exato de categorias
ax.set_xticks(df.index)
ax.set_xticklabels(df["Categorias"], rotation=45, ha='right')

# Personalizar e exibir o gráfico
ax.set_ylabel("Taxa de Desemprego (%)")
ax.set_xlabel("Categorias")
plt.legend()
plt.tight_layout()

# Exibir gráfico
plt.show()