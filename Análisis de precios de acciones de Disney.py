"""Los datos bursátiles diarios de Disney ofrecen un registro detallado del rendimiento de las acciones de The Walt Disney Company día a día. 
Este conjunto de datos incluye varias métricas clave, como:

Fecha : la fecha de cada día de negociación, lo que le permite realizar un seguimiento del rendimiento a lo largo del tiempo.
Precio de apertura : el precio al que las acciones de Disney comenzaron a cotizar ese día.
Precio alto : el precio más alto que alcanzó la acción durante el día.
Precio bajo : el precio más bajo registrado para la acción ese día.
Precio de cierre : El precio final de la acción al final del día de negociación.
Volumen : Número total de acciones negociadas, que indica la actividad del mercado.
"""

import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import seaborn as sns
import plotly.graph_objects as go


data = pd.read_csv('DIS.csv', index_col = 'Date')
print(data)

fig = go.Figure()

#Agregar rastros de precios de apertura, máximos, mínimos y cierre
fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data.index, y=data['High'], mode='lines', name='High', line=dict(color='green')))
fig.add_trace(go.Scatter(x=data.index, y=data['Low'], mode='lines', name='Low', line=dict(color='red')))
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close', line=dict(color='purple')))

#Agregar gráfico de velas
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'],
                             name='Candlestick',
                             increasing_line_color='green',
                             decreasing_line_color='red'))

#Personalizar el diseño
fig.update_layout(title='Análisis del precio de las acciones de Disney\n',
                  xaxis_title='Fecha\n',
                  yaxis_title='Precio\n',
                  template='plotly_dark')

#Mostrar la trama interactiva
fig.show()

fig = go.Figure()

#Agregar traza de volumen
fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume', marker_color='blue', opacity=0.3))

#Calcular media móvil
data['Moving_Avg'] = data['Close'].rolling(window=30).mean()
fig.add_trace(go.Scatter(x=data.index, y=data['Moving_Avg'], mode='lines', name='30-Day Moving Average', line=dict(color='orange')))

#Personalizar el diseño
fig.update_layout(title='Volumen de las acciones de Disney y promedio móvil\n',
                  xaxis_title='Fecha\n',
                  yaxis_title='Volumen\n',
                  template='plotly_dark')

#Mostrar la trama interactiva
fig.show()

plt.figure(figsize=(14, 7))

#Trazando el precio de cierre
sns.lineplot(data=data, x=data.index, y='Close', label='Precio de cierre', color='purple')

#Añadir media móvil
data['Moving_Avg'] = data['Close'].rolling(window=30).mean()
sns.lineplot(data=data, x=data.index, y='Moving_Avg', label='Promedio móvil de 30 días', color='orange', linestyle='--')

#Añadir títulos y etiquetas
plt.title('Precio de las acciones de Disney y media móvil\n', fontsize = 16, fontweight = 'bold')
plt.xlabel('Fecha\n')
plt.ylabel('Precio\n')
plt.legend()
plt.show()
