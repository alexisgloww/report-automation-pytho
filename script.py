import pandas as pd
from datetime import datetime

# Leer archivo
df = pd.read_csv("datos.csv")

# Limpiar datos
df = df.dropna()

# Agrupar datos
resumen = df.groupby("categoria")["ventas"].sum()

# Ordenar
resumen = resumen.sort_values(ascending=False)

# Nombre con fecha
fecha = datetime.now().strftime("%Y-%m-%d")
nombre_archivo = f"reporte_{fecha}.xlsx"

# Guardar
resumen.to_excel(nombre_archivo)

print("✅ Reporte generado:", nombre_archivo)
