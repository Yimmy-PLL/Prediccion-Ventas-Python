"""Proyecto IDAT: predicción de unidades vendidas según precios y tienda."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Leer y limpiar los datos
carpeta = Path(__file__).resolve().parent
datos = pd.read_csv(carpeta / 'dataset.csv')
datos['Total Price'] = datos['Total Price'].fillna(datos['Total Price'].median())
datos['Descuento'] = datos['Base Price'] - datos['Total Price']
print('Registros:', len(datos))
print('Tiendas:', datos['Store ID'].nunique())

# 2. Graficar precio frente a ventas
plt.scatter(datos['Total Price'], datos['Units Sold'], alpha=0.15, s=5)
plt.xlabel('Precio final')
plt.ylabel('Unidades vendidas')
plt.title('Precio frente a unidades vendidas')
plt.tight_layout()
plt.savefig(carpeta / 'precio_vs_ventas.png', dpi=150)
plt.close()

# 3. Preparar variables: la tienda es una categoría
X = pd.get_dummies(datos[['Base Price', 'Total Price', 'Store ID']], columns=['Store ID'])
y = datos['Units Sold']
X_entreno, X_prueba, y_entreno, y_prueba = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 4. Entrenar y comparar dos modelos
modelos = {
    'Regresión lineal': LinearRegression(),
    'Random Forest': RandomForestRegressor(
        n_estimators=60, max_depth=16, min_samples_leaf=5,
        random_state=42, n_jobs=-1
    )
}
for nombre, modelo in modelos.items():
    modelo.fit(X_entreno, y_entreno)
    prediccion = modelo.predict(X_prueba).clip(min=0)
    print('\n', nombre)
    print('MAE:', round(mean_absolute_error(y_prueba, prediccion), 2))
    print('RMSE:', round(mean_squared_error(y_prueba, prediccion) ** 0.5, 2))
    print('R²:', round(r2_score(y_prueba, prediccion), 4))

# 5. Simular un escenario con el modelo Random Forest
nuevo = pd.DataFrame(0.0, index=[0], columns=X.columns)
nuevo.loc[0, 'Base Price'] = 100
nuevo.loc[0, 'Total Price'] = 85
nuevo.loc[0, 'Store ID_8091'] = 1
unidades = max(0, modelos['Random Forest'].predict(nuevo)[0])
print('\nUnidades estimadas para tienda 8091:', round(unidades, 1))
