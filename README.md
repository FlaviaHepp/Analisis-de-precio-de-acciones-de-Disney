# 📊Análisis del Precio de las Acciones de Disney (DIS)

Este proyecto realiza un análisis exploratorio del precio de las acciones de The Walt Disney Company (DIS) utilizando datos bursátiles diarios.
El objetivo principal es visualizar el comportamiento histórico del precio, el volumen de negociación y la tendencia mediante medias móviles.

## 🎯Objetivo del proyecto

- Analizar la evolución diaria del precio de las acciones de Disney.
- Visualizar precios de apertura, cierre, máximo y mínimo.
- Representar el precio mediante gráficos de velas (candlestick).
- Analizar el volumen de operaciones junto con una media móvil de 30 días.
- Combinar visualizaciones interactivas (Plotly) y estáticas (Matplotlib / Seaborn).

## 📁Descripción de los datos

El dataset contiene información bursátil diaria de Disney, incluyendo:
- Date: fecha de negociación
- Open: precio de apertura
- High: precio máximo del día
- Low: precio mínimo del día
- Close: precio de cierre
- Volume: volumen de acciones negociadas

## 📈Análisis realizado

1. Visualización de precios
- Series temporales de:
  - Precio de apertura
  - Precio máximo
  - Precio mínimo
  - Precio de cierre
- Gráfico de velas para observar:
  - Tendencia
  - Volatilidad
  - Rangos diarios de precio

2. Análisis de volumen
- Gráfico de barras del volumen diario
- Cálculo y visualización de:
- Media móvil de 30 días del precio de cierre

3. Análisis exploratorio clásico
- Gráfico estático del precio de cierre
- Superposición de media móvil
- Estilo oscuro orientado a análisis financiero

## 🛠️Tecnologías utilizadas

- Python
- pandas / numpy
- Plotly
- Matplotlib
- Seaborn

## 📂Estructura del proyecto

├── Análisis de precios de acciones de Disney.py
├── DIS.csv
└── README.md

## 📌Resultados principales

- Identificación visual de tendencias en el precio de DIS.
- Relación entre volumen y movimientos de precio.
- Suavización del comportamiento del precio mediante medias móviles.
- Comparación entre gráficos interactivos y estáticos.

## ⚠️Disclaimer

Este proyecto es educativo y demostrativo.
No constituye asesoramiento financiero ni recomendaciones de inversión.
## 👤Autor

**Flavia Hepp**
Data Science en formación · Análisis Financiero · Visualización de Datos
