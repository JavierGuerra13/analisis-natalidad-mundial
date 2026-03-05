"""
Generador de Avatar Profesional para Redes Sociales
Crea un avatar con iniciales JG y elementos de datos
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_avatar(output_path='avatar_jg.png', size=1000):
    """
    Crea un avatar profesional con iniciales JG
    
    Args:
        output_path: Ruta donde guardar la imagen
        size: Tamaño del avatar en píxeles (cuadrado)
    """
    
    # Crear imagen base
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # Colores (matching con banner - cyan/verde tech)
    color_fondo_1 = (10, 25, 47)       # Azul muy oscuro (como banner)
    color_fondo_2 = (0, 172, 193)      # Cyan brillante (como banner)
    color_acento = (0, 230, 118)       # Verde neón (matching perfecto)
    color_texto = (255, 255, 255)      # Blanco puro
    
    # Crear gradiente circular
    center = size // 2
    for y in range(size):
        for x in range(size):
            # Calcular distancia del centro
            dx = x - center
            dy = y - center
            distance = math.sqrt(dx*dx + dy*dy)
            
            # Crear gradiente radial
            if distance <= center:
                ratio = distance / center
                r = int(color_fondo_1[0] + (color_fondo_2[0] - color_fondo_1[0]) * ratio)
                g = int(color_fondo_1[1] + (color_fondo_2[1] - color_fondo_1[1]) * ratio)
                b = int(color_fondo_1[2] + (color_fondo_2[2] - color_fondo_1[2]) * ratio)
                img.putpixel((x, y), (r, g, b))
    
    # Dibujar círculo exterior (borde)
    draw.ellipse([10, 10, size-10, size-10], outline=color_acento, width=8)
    
    # Agregar elemento de datos (mini gráfico)
    # Línea de tendencia ascendente estilizada
    puntos_grafico = [
        (size*0.15, size*0.75),
        (size*0.25, size*0.70),
        (size*0.35, size*0.68),
        (size*0.45, size*0.50),
        (size*0.55, size*0.45),
        (size*0.65, size*0.35),
        (size*0.75, size*0.28),
        (size*0.85, size*0.25),
    ]
    
    # Dibujar línea del gráfico (sutil, en el fondo)
    for i in range(len(puntos_grafico) - 1):
        draw.line(
            [puntos_grafico[i], puntos_grafico[i+1]], 
            fill=color_acento, 
            width=4
        )
    
    # Dibujar puntos del gráfico
    for punto in puntos_grafico:
        radio = 8
        draw.ellipse(
            [punto[0]-radio, punto[1]-radio, punto[0]+radio, punto[1]+radio],
            fill=color_acento
        )
    
    # Agregar iniciales "JG" en el centro
    # Intentar usar fuente Arial Bold, si no existe usar default
    try:
        # Windows
        font = ImageFont.truetype("arialbd.ttf", size//2.5)
    except:
        try:
            # Linux/Mac
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size//2.5)
        except:
            # Fallback
            font = ImageFont.load_default()
    
    texto = "JG"
    
    # Calcular posición centrada del texto
    bbox = draw.textbbox((0, 0), texto, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - size//20  # Ligeramente arriba del centro
    
    # Dibujar texto con sombra
    sombra_offset = 4
    draw.text((text_x + sombra_offset, text_y + sombra_offset), texto, font=font, fill=(0, 0, 0, 128))
    draw.text((text_x, text_y), texto, font=font, fill=color_texto)
    
    # Guardar imagen
    img.save(output_path, quality=95)
    print(f"✅ Avatar creado exitosamente: {output_path}")
    print(f"📐 Dimensiones: {size}x{size} px")
    print(f"💾 Tamaño: {img.size}")
    
    return output_path


def create_avatar_variations():
    """Crea múltiples variaciones del avatar"""
    
    print("🎨 Generando avatars...\n")
    
    # Avatar estándar (para X, LinkedIn, etc.)
    create_avatar('avatar_jg_standard.png', size=1000)
    
    # Avatar pequeño optimizado
    create_avatar('avatar_jg_small.png', size=400)
    
    # Avatar alta resolución
    create_avatar('avatar_jg_hd.png', size=2000)
    
    print("\n🎉 ¡Todos los avatars generados!")
    print("\nArchivos creados:")
    print("  - avatar_jg_standard.png  (1000x1000) - Para redes sociales")
    print("  - avatar_jg_small.png     (400x400)   - Versión optimizada")
    print("  - avatar_jg_hd.png        (2000x2000) - Alta resolución")


if __name__ == "__main__":
    # Ejecutar generación de avatars
    create_avatar_variations()
