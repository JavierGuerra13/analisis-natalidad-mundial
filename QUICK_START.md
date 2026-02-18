# 🚀 Guía de Inicio Rápido

## Para empezar a trabajar en este proyecto

### 1️⃣ Abrir el proyecto en VS Code

```bash
# Navega a la carpeta del proyecto
cd ruta/donde/guardaste/natalidad-mundial

# Abre VS Code en esta carpeta
code .
```

### 2️⃣ Verificar que tienes Python instalado

```bash
# En la terminal de VS Code (Terminal > New Terminal)
python --version
# o
python3 --version

# Deberías ver algo como: Python 3.10.x o superior
```

**Si no tienes Python:**
- Windows: Descarga desde https://www.python.org/downloads/
- Mac: `brew install python3` (si tienes Homebrew)
- Linux: `sudo apt install python3 python3-pip`

### 3️⃣ Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Verás (venv) al inicio de tu terminal cuando esté activado
```

### 4️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt

# Esto instalará todas las bibliotecas necesarias
# Puede tomar unos minutos
```

### 5️⃣ Iniciar Jupyter Notebook

```bash
jupyter notebook

# Se abrirá en tu navegador
# Navega a notebooks/ y abre el primer notebook
```

---

## 📝 Próximos Pasos (orden sugerido)

1. **Lee la documentación** en `docs/`:
   - `project_brief.md` - Visión general
   - `research_questions.md` - Qué vamos a responder
   - `data_sources.md` - De dónde sacaremos los datos

2. **Empieza con los notebooks** en orden:
   - `01_data_collection.ipynb` - Descargar datos
   - `02_data_cleaning.ipynb` - Limpiar datos
   - `03_exploratory_analysis.ipynb` - Explorar patrones
   - `04_final_report.ipynb` - Reporte final

3. **A medida que avances**, el código repetible irá a `src/`

---

## 💡 Consejos

- **Guarda frecuentemente**: Ctrl+S (Windows/Linux) o Cmd+S (Mac)
- **Ejecuta celda por celda** en los notebooks (Shift+Enter)
- **Si algo no funciona**: Lee el error, generalmente indica qué falta
- **Consulta documentación**: Cada biblioteca tiene docs excelentes

---

## 🆘 Problemas Comunes

### "pip no se reconoce"
Reinstala Python y asegúrate de marcar "Add Python to PATH"

### "No module named 'pandas'"
Asegúrate de tener activado el entorno virtual y haber corrido `pip install -r requirements.txt`

### "Jupyter no abre"
Verifica: `pip install jupyter notebook`

---

## 📚 Recursos Útiles

- Python para Data Science: https://www.learnpython.org/
- Pandas tutorial: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/index.html

---

**¿Listo?** ¡Vamos a analizar datos! 🎯
