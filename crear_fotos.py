import os
from PIL import Image, ImageDraw

if not os.path.exists('assets'):
    os.makedirs('assets')

# Configuración de Colores
COLOR_FONDO = (5, 12, 24) # Azul Marino Profundo
COLOR_BORDE = (212, 175, 55) # Dorado Elegante

def crear_imagen(ruta, tamaño):
    img = Image.new('RGB', tamaño, color=COLOR_FONDO)
    draw = ImageDraw.Draw(img)
    # Dibujamos un borde sutil para darle ese toque técnico
    draw.rectangle([0, 0, tamaño[0]-1, tamaño[1]-1], outline=COLOR_BORDE, width=10)
    img.save(ruta)

# Generar Icono y Splash
crear_imagen('assets/icon.png', (1024, 1024))
crear_imagen('assets/presplash.png', (2732, 2732))
print("✅ Identidad visual generada en /assets")
