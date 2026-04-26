import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashbord de Abandono de Clientes 🚀")

# 1. Cargar los datos (lee el csv que está en la carpeta de al lado)
df = pd.read_csv('../Datos/ventas.csv')

# 2. EL FRAGMENTO NUEVO: Segmentación de clientes
df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])

# 3. Mostrar la tabla
st.write("Vista previa de la base de datos con los nuevos segmentos:")
st.dataframe(df)

# 4. Mostrar un gráfico genial
st.subheader("Distribución de Clientes por Valor")
fig, ax = plt.subplots()
df['segmento_valor'].value_counts().plot(kind='bar', ax=ax, color=['#ff9999','#66b3ff','#99ff99'])
plt.xticks(rotation=0)
st.pyplot(fig)