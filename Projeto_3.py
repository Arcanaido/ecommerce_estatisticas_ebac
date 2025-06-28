import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.figure_factory as ff


# Histograma da Distribuição de Notas
def criar_histograma(df):
    fig1 = px.histogram(df,
                        x='Nota_MinMax',
                        nbins=5,
                        color='Gênero',
                        title='Distribuição das Notas por Gênero',
                        color_discrete_sequence=px.colors.qualitative.Set2,
                        hover_data=['Marca', 'Preço', 'Qtd_Vendidos'])
    fig1.update_layout(
        xaxis_title='Notas',
        yaxis_title='Quantidade',
        legend_title='Gênero',
        bargap=0.1,
        plot_bgcolor='#F9F9F9'
    )
    fig1.update_traces(
        marker=dict(line=dict(width=1, color='black'))
    )
    return fig1


# Gráfico de Dispersão notas vs N_avaliações
def criar_graph_dispersao(df):
    fig2 = px.scatter(df,
                      x='Nota_MinMax',
                      y='N_Avaliações_MinMax',
                      title='Notas vs Número de Avaliações',
                      color='Material',
                      color_discrete_sequence=px.colors.qualitative.Set2,
                      opacity=0.7,
                      hover_data=['Marca', 'Material', 'Preço'])

    fig2.update_traces(marker=dict(size=30)) #Define o tamanho dos marcadores

    fig2.update_layout(
        xaxis_title='Número de Avaliações',
        yaxis_title='Nota Média',
        legend_title='Marca',
    )
    return fig2

# Heatmap Correlação entre Notal, N_Aval, Descontos, Qtd_Vendidos e preço
def criar_heatmap(df):
    df_corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].corr().round(2)
    fig3 = px.imshow(df_corr,
                     text_auto=True, # Mostra valores nas células
                     aspect='auto',
                     color_continuous_scale='RdBu_r', # Invertido para tons tradicionais de correlação
                     title='Mapa de Calor - Correlação entre Variáveis Numéricas',
                     labels=dict(color='Correlação')
    )
    fig3.update_layout(
        xaxis_title='Variáveis',
        yaxis_title='Variáveis',
        margin=dict(l=60, r=30, t=60, b=40),
        plot_bgcolor='#F9F9F9'
    )
    fig3.update_xaxes(tickangle=0, side='top')
    fig3.update_yaxes(autorange='reversed')
    fig3.update_traces(textfont_size=14)
    return fig3

# Gráfico de Barra
def criar_bar_grafico(df):
    contagem_genero = df['Gênero'].value_counts().reset_index()
    contagem_genero.columns = ['Gênero', 'Quantidade']
    contagem_genero['Percentual'] = 100 * contagem_genero['Quantidade'] / contagem_genero['Quantidade'].sum() #Calculando o percentual de cada categoria de gênero em relação ao total

    fig4 = px.bar(contagem_genero,
                x='Gênero',
                y='Quantidade',
                color='Gênero', # Cada gênero com cor diferente
                title='Distribuição por Gênero',
                text='Quantidade', # Rótulo de valor direto na barra
                color_discrete_sequence=px.colors.qualitative.Plotly,
                hover_data={'Quantidade': True, 'Percentual': ':.1f'},
                height=500
    )
    fig4.update_traces(marker_line_color='#A9A9A9',
                       marker_line_width=1.5, # borda da barra
                       textposition='auto'
    )  #mosta valores acima das barras
    fig4.update_layout(xaxis_tickangle=45,  # rotação do texto do eixo X
                      xaxis_title='Gênero',
                      yaxis_title='Quantidade',
                      bargap=0.1,
                      plot_bgcolor='white',
                      showlegend=False,
                      margin=dict(t=100, l=60, r=30, b=40))

    return fig4

# Gráfico de Pizza
def criar_grafico_pizza(df):
    df = df.copy()
    df['Faixa_Desconto'] = df['Desconto'].map(lambda x:
                                              '0-20%' if x <= 20 else
                                              '21-40%' if x <= 40 else
                                              '41-60%' if x <= 60 else
                                              '61-80%' if x <= 80 else
                                              '81-100%')

    contagem = df['Faixa_Desconto'].value_counts().sort_index().reset_index()
    contagem.columns = ['Faixa_Desconto', 'Quantidade']
    contagem['Percentual'] = 100 * contagem['Quantidade']/contagem['Quantidade'].sum()

    destaque = [0.08 if qtd == contagem['Quantidade'].max() else 0 for qtd in contagem['Quantidade']]

    fig5 = px.pie(
        contagem,
        names='Faixa_Desconto',
        values='Quantidade',
        title='Distribuição por Faixas de Desconto (%)',
        color_discrete_sequence=px.colors.sequential.Plasma_r, #paleta diferenciada
        hole=0.25)

    fig5.update_traces(
        textinfo='percent+label+value', #mostra % + nome + valor absoluto na fatia
        pull=destaque, #destaca a faixa com maior quantidade
        marker=dict(line=dict(color='white', width=2)) #borda branca separandoa as fatias
    )
    fig5.update_layout(
        legend_title_text='Faixa de Desconto',
        legend=dict(font=dict(size=14)),
        plot_bgcolor='#F9F9F9',
        title_x=0.5 #centraliza o título
    )

    return fig5

# Gráfico de Densidade
def criar_grafico_densidade(df):
    grupos = df['Gênero'].unique()
    data = []
    group_labels = []
    for g in grupos:
        valores = df[df['Gênero'] == g]['Preço'].dropna()
        if len(valores) >= 2:
            data.append(valores)
            group_labels.append(str(g))
    if not data:
        import plotly.graph_objects as go
        fig6 = go.Figure()
        fig6.update_layout(title='Sem dados suficientes para exibir a densidade')
        return fig6

    fig6 = ff.create_distplot(
        data,
        group_labels,
        show_hist=True,
        show_rug=False,
        colors=px.colors.qualitative.Set2,
    )
    fig6.update_traces(line={'width': 3}, opacity=0.7, selector=dict(type='scatter'))
    fig6.update_layout(
        title='Distribuição de Densidade de Preço por Gênero',
        xaxis_title='Preço',
        yaxis_title='Densidade',
        plot_bgcolor='#F9F9F9',
        legend_title_text='Gênero',
        title_x=0.5
    )

    return fig6

# Gráfico Regressão
import numpy as np
import plotly.graph_objects as go

def criar_grafico_regressao(df):
    x = df['Nota']
    y = df['N_Avaliações']

    # Calcula regressão linear (reta) - y = m * x + b
    m, b = np.polyfit(x, y, 1)
    y_pred = m * x + b

    # R² (Coeficiente de determinação)
    r2 = np.corrcoef(x, y)[0, 1] ** 2

    fig7 = go.Figure()

    #Pontos de dispersão
    fig7.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(color='#6495ED', size=10, line=dict(width=1, color='#000000')),
        name='Dados',
        text=[f"Nota: {a}<br>Nº Avaliações: {b}" for a, b in zip(x, y)],
        hoverinfo='text'
    ))

    #Linha de regressão
    fig7.add_trace(go.Scatter(
        x=np.sort(x),
        y=np.sort(y_pred), #mantém pareado com x ordenado
        mode='lines',
        line=dict(color='#FF0000', width=3, dash="dash"),
        name=f'Regressão Linear<br>y = {m:.2f}x + {b:.2f}<br>R² = {r2:.2f}'
    ))

    fig7.update_layout(
        title=dict(
            text='Relação entre Nota e Número de Avaliações<br><span style="font-size: 14px"> Com regressão linear e R²</span>',
            x=0.5  # centraliza o título
        ),
        xaxis_title='Nota',
        yaxis_title='Número de Avaliações',
        plot_bgcolor='#F9F9F9',
        legend=dict(font=dict(size=13)),
        width=900,
        height=550
    )

    return fig7

df = pd.read_csv('ecommerce_estatistica.csv')

def criar_app(df):
    app = Dash(__name__)

    figures = {
        "Histograma": criar_histograma(df),
        "Dispersão": criar_graph_dispersao(df),
        "Heatmap": criar_heatmap(df),
        "Barras": criar_bar_grafico(df),
        "Pizza": criar_grafico_pizza(df),
        "Densidade": criar_grafico_densidade(df),
        "Regressão": criar_grafico_regressao(df)
    }

    app.layout = html.Div([
        dcc.Checklist(
            id="check_graficos",
            options=[{"label": k, "value": k} for k in figures.keys()],
            value=["Histograma"],
            inline=True
        ),
        html.Div(id="varios_graficos")
    ])

    @app.callback(
        Output("varios_graficos", "children"),
        Input("check_graficos", "value")
    )
    def mostrar_graficos_nomes(nome_graficos):
        return [dcc.Graph(figure=figures[nome]) for nome in nome_graficos]

    return app


if __name__ == '__main__':
    app = criar_app(df)
    app.run(debug=True, port=8051, use_reloader=False)





