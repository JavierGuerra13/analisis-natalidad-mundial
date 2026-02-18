# 📊 Análisis de la Caída de Natalidad Mundial

## 🌍 Descripción del Proyecto

Este proyecto analiza la tendencia global de disminución de las tasas de natalidad, explorando qué países están experimentando este fenómeno y qué factores económicos, sociales y políticos podrían explicarlo.

**Motivación**: La caída de natalidad es uno de los fenómenos demográficos más importantes del siglo XXI, con implicaciones profundas para la economía, sistemas de pensiones, y la estructura social de las naciones.

---

## 🎯 Objetivos

1. **Mapear la tendencia global**: Identificar países con caída vs estabilidad en natalidad
2. **Análisis causal**: Explorar correlaciones con factores económicos, sociales y políticos
3. **Casos de estudio**: Analizar países outliers (contra la tendencia)
4. **Generar insights**: Crear visualizaciones y conclusiones compartibles

---

## 📁 Estructura del Proyecto

```
natalidad-mundial/
│
├── docs/                          # Documentación del proyecto
│   ├── project_brief.md          # Descripción completa del proyecto
│   ├── research_questions.md     # Preguntas de investigación
│   └── data_sources.md           # Fuentes de datos
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_collection.ipynb  # Recolección de datos
│   ├── 02_data_cleaning.ipynb    # Limpieza y procesamiento
│   ├── 03_exploratory_analysis.ipynb  # Análisis exploratorio
│   └── 04_final_report.ipynb     # Reporte final
│
├── src/                           # Código fuente (pipeline)
│   ├── __init__.py
│   ├── data_collection.py        # Scripts de recolección
│   ├── data_cleaning.py          # Scripts de limpieza
│   └── visualization.py          # Scripts de visualización
│
├── data/
│   ├── raw/                       # Datos originales (no modificar)
│   └── processed/                 # Datos procesados
│
├── outputs/
│   ├── figures/                   # Gráficos generados
│   └── reports/                   # Reportes en PDF/HTML
│
├── requirements.txt               # Dependencias del proyecto
├── .gitignore                     # Archivos a ignorar en Git
└── README.md                      # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **Matplotlib / Seaborn** - Visualización estática
- **Plotly** - Visualización interactiva
- **GeoPandas / Folium** - Mapas
- **Jupyter** - Notebooks interactivos
- **wbgapi** - API del Banco Mundial

---

## 🚀 Cómo Empezar

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/natalidad-mundial.git
cd natalidad-mundial
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar los Notebooks
```bash
jupyter notebook
```

---

## 📊 Fuentes de Datos Principales

- **Banco Mundial** - World Development Indicators
- **Naciones Unidas** - Population Division
- **OECD** - Políticas familiares y económicas
- **Our World in Data** - Datos compilados

Ver [data_sources.md](docs/data_sources.md) para detalles completos.

---

## 🔍 Preguntas de Investigación

### Principales:
1. ¿La caída de natalidad es un fenómeno universal?
2. ¿Qué factores económicos están más correlacionados?
3. ¿Qué países van contra la tendencia y por qué?
4. ¿Las políticas públicas son efectivas?

Ver [research_questions.md](docs/research_questions.md) para la lista completa.

---

## 📈 Estado del Proyecto

- [x] ✅ Planificación y documentación
- [ ] 🔄 Recolección de datos
- [ ] ⏳ Limpieza de datos
- [ ] ⏳ Análisis exploratorio
- [ ] ⏳ Análisis profundo
- [ ] ⏳ Visualizaciones finales
- [ ] ⏳ Reporte y publicación

---

## 📝 Roadmap

### Fase 1: Datos (En progreso)
- [ ] Descargar datos del Banco Mundial
- [ ] Descargar datos de ONU
- [ ] Integrar datasets

### Fase 2: Análisis
- [ ] EDA (Análisis Exploratorio)
- [ ] Correlaciones y estadísticas
- [ ] Identificar outliers

### Fase 3: Visualización
- [ ] Mapas interactivos
- [ ] Gráficos de tendencias
- [ ] Dashboard (opcional)

### Fase 4: Comunicación
- [ ] Reporte final
- [ ] Publicaciones para X/Twitter
- [ ] Actualizar GitHub

---

## 🤝 Contribuciones

Este es un proyecto personal de aprendizaje y portafolio. Sin embargo, sugerencias y feedback son bienvenidos.

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Los datos utilizados provienen de fuentes públicas y mantienen sus licencias originales.

---

## 👤 Autor

**[Tu Nombre]**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [Tu perfil](https://linkedin.com/in/tu-perfil)
- X/Twitter: [@tu-usuario](https://twitter.com/tu-usuario)

---

## 📚 Referencias

- World Bank Data: https://data.worldbank.org/
- UN Population Division: https://population.un.org/
- Our World in Data: https://ourworldindata.org/

---

**Última actualización**: Febrero 2026
