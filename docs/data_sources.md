# Fuentes de Datos

## 🎯 Criterios de Selección de Fuentes

- **Credibilidad**: Organizaciones reconocidas internacionalmente
- **Cobertura**: Datos de múltiples países y años
- **Accesibilidad**: APIs públicas o datos descargables
- **Actualización**: Datos recientes (hasta 2023 o cercano)
- **Formato**: Preferiblemente CSV, JSON o API REST

---

## 📊 Fuentes Principales

### 1. Banco Mundial - World Development Indicators
**URL**: https://data.worldbank.org/

**Datos disponibles:**
- ✅ Tasa de fertilidad total (SP.DYN.TFRT.IN)
- ✅ PIB per cápita (NY.GDP.PCAP.CD)
- ✅ Tasa de desempleo (SL.UEM.TOTL.ZS)
- ✅ Matrícula educativa femenina (SE.SEC.ENRR.FE)
- ✅ Participación laboral femenina (SL.TLF.CACT.FE.ZS)
- ✅ Población urbana (% del total) (SP.URB.TOTL.IN.ZS)

**Acceso:**
- API disponible: `pip install wbdata` o `wbgapi`
- Descarga directa: CSV/Excel
- Cobertura temporal: 1960-2023 (según indicador)
- Cobertura geográfica: ~200+ países

**Ventajas:**
- Muy completa y bien documentada
- API fácil de usar
- Datos estandarizados

---

### 2. Naciones Unidas - Population Division
**URL**: https://population.un.org/wpp/

**Datos disponibles:**
- ✅ Tasa de fertilidad total
- ✅ Proyecciones demográficas
- ✅ Esperanza de vida
- ✅ Edad mediana de la población

**Acceso:**
- Descarga de archivos CSV
- Datos por quinquenio (cada 5 años)

**Ventajas:**
- Autoridad en demografía
- Proyecciones confiables

---

### 3. OECD Data
**URL**: https://data.oecd.org/

**Datos disponibles:**
- ✅ Políticas de licencias parentales
- ✅ Gasto en políticas familiares
- ✅ Edad promedio de la madre al primer hijo
- ✅ Precio de vivienda

**Acceso:**
- API REST
- Descarga CSV/Excel

**Limitación:**
- Solo países OECD (~38 países)

**Ventajas:**
- Datos de políticas públicas detallados
- Alta calidad

---

### 4. Our World in Data
**URL**: https://ourworldindata.org/

**Datos disponibles:**
- ✅ Recopilación de múltiples fuentes
- ✅ Fertilidad histórica
- ✅ Educación
- ✅ Desarrollo humano

**Acceso:**
- GitHub: https://github.com/owid/owid-datasets
- Descarga directa

**Ventajas:**
- Datos limpios y listos para usar
- Documentación excelente

---

### 5. Gapminder
**URL**: https://www.gapminder.org/data/

**Datos disponibles:**
- ✅ Indicadores socioeconómicos históricos
- ✅ Datos limpios y verificados

**Acceso:**
- Descarga CSV
- Google Sheets

---

## 🗂️ Plan de Recolección de Datos

### Fase 1: Datos Core (Esenciales)
**Fuente**: Banco Mundial API

1. Tasa de fertilidad total (2000-2023)
2. PIB per cápita (2000-2023)
3. Educación femenina (2000-2023)
4. Participación laboral femenina (2000-2023)
5. Urbanización (2000-2023)

**Países**: Todos los disponibles (~200+)

---

### Fase 2: Datos Complementarios
**Fuente**: OECD + ONU

1. Políticas de licencias parentales (OECD)
2. Proyecciones demográficas (ONU)
3. Gasto en políticas familiares (OECD)

**Países**: Subconjunto (países OECD + casos de interés)

---

### Fase 3: Datos Opcionales (Si hay tiempo/necesidad)
**Fuente**: Diversas

1. Costo de vivienda
2. Desigualdad (Gini)
3. Acceso a anticonceptivos
4. Religiosidad

---

## 🔧 Herramientas de Acceso

```python
# Bibliotecas para acceder a los datos
pip install wbgapi              # Banco Mundial
pip install pandas              # Manipulación de datos
pip install requests            # APIs REST
pip install openpyxl            # Leer archivos Excel
```

---

## 📝 Formato de Almacenamiento

### Datos Raw (sin procesar)
```
data/raw/
├── worldbank_fertility.csv
├── worldbank_gdp.csv
├── worldbank_education.csv
├── un_population.csv
└── oecd_policies.csv
```

### Datos Procesados (limpios)
```
data/processed/
├── master_dataset.csv          # Dataset principal integrado
├── fertility_timeseries.csv    # Serie temporal de fertilidad
└── countries_metadata.csv      # Información de países
```

---

## ✅ Checklist de Validación de Datos

Para cada fuente, verificar:
- [ ] Cobertura temporal completa (2000-2023)
- [ ] Valores faltantes < 30%
- [ ] Consistencia de formatos
- [ ] Documentación de metodología
- [ ] Licencia de uso (debe ser abierta)

---

## 📚 Referencias y Documentación

- Banco Mundial API Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- ONU Population: https://population.un.org/wpp/Publications/
- OECD Data: https://data.oecd.org/api/
- Our World in Data GitHub: https://github.com/owid

---

**Última actualización**: Febrero 2026  
**Estado**: Planificación - No se han descargado datos aún
