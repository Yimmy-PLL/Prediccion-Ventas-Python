# Proyecto final IDAT: predicción de unidades vendidas

Este proyecto estima unidades vendidas en función del precio base, el precio final y la tienda, para apoyar la planificación del abastecimiento.

## Cómo ejecutarlo

1. Instalar Python 3.10 o superior.
2. Abrir una terminal en esta carpeta.
3. Ejecutar `pip install -r requirements.txt`.
4. Ejecutar `python proyecto_final.py`.

El script imprime las métricas MAE, RMSE y R², genera `precio_vs_ventas.png` y simula un escenario para la tienda 8091.

## Importante

El dataset no incluye producto, fecha ni inventario. Por tanto, no permite determinar qué producto comprar, cuándo ni en qué cantidad. Los resultados describen estimaciones de unidades vendidas, no efectos causales de cambiar precios.
