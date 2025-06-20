# 📊 Análise Estatística de Dados de E-commerce

## 📌 Descrição do Projeto
Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) de um dataset de produtos de e-commerce, utilizando ferramentas de visualização para compreender melhor a distribuição, correlações e comportamentos dos dados.

Foram aplicadas técnicas de estatística descritiva, categorização de variáveis e geração de gráficos para interpretar relações e padrões nos dados.

---

## 🗂️ Dataset Utilizado
- Arquivo: `ecommerce_estatistica.csv`
- Principais colunas:
  - `Nota` — Nota média dos produtos
  - `N_Avaliações` — Número de avaliações dos produtos
  - `Desconto` — Percentual de desconto aplicado
  - `Preço` — Preço do produto
  - `Gênero`, `Marca`, `Material`, `Temporada` — Categorias dos produtos
  - E versões escaladas de variáveis (`Nota_MinMax`, `N_Avaliações_MinMax`, etc.)

---

## 🛠️ Ferramentas e Bibliotecas Utilizadas
- `pandas` — Manipulação de dados
- `matplotlib` — Visualização de dados
- `seaborn` — Visualização de dados estatísticos

---

## 🔍 Análises e Visualizações Realizadas

### 📊 1. Histograma — Distribuição das Notas
- Visualiza como as notas dos produtos estão distribuídas.
- Mostra se há mais produtos com notas altas, médias ou baixas.

---

### 🔵 2. Gráfico de Dispersão — Nota vs Número de Avaliações
- Verifica se existe relação entre a nota média dos produtos e o número de avaliações.
- Permite avaliar se produtos bem avaliados tendem a ter mais avaliações.

---

### ♨️ 3. Heatmap — Correlação entre Variáveis Numéricas
- Variáveis analisadas:
  - `Nota`
  - `N_Avaliações`
  - `Desconto`
  - `Preço`
- Identifica quais variáveis possuem maior correlação entre si (positiva ou negativa).

---

### 📑 4. Gráfico de Barras — Distribuição por Gênero
- Mostra a quantidade de produtos em cada categoria de gênero.

---

### 🥧 5. Gráfico de Pizza — Faixas de Desconto
- Descontos categorizados em:
  - `0-20%`
  - `21-40%`
  - `41-60%`
  - `61-80%`
  - `81-100%`
- Exibe a proporção de produtos em cada faixa de desconto.

---

### 📈 6. Gráfico de Densidade — Distribuição de Preços
- Mostra a concentração dos preços dos produtos.
- Permite visualizar se há mais produtos baratos, médios ou caros.

---

### 🔺 7. Gráfico de Regressão — Nota vs Número de Avaliações
- Analisa a tendência e correlação entre a nota dos produtos e o número de avaliações.
- Inclui linha de regressão que indica a tendência dos dados.

---

## 🚀 Como Executar o Projeto
1. Clonar o repositório:
   ```bash
   git clone https://github.com/Arcanaido/nome-do-repositorio.git

2. Instalar as bibliotecas necessárias:
   ```bash
   pip install pandas matplotlib seaborn

3. Executar o script Python principal (ex.: analise_estatistica.py)

### ✨ Autor:
- Julius Maisonnette Ferreira Mota (https://github.com/Arcanaido)
