# 🔬 Tiroides Toolkit

App web clínica para el manejo de patología tiroidea. Tres herramientas integradas:

## Herramientas

### 1. 🔍 Clasificador ACR TI-RADS
Clasificación dinámica de nódulos tiroideos por ecografía:
- Selecciona 5 características (composición, ecogenicidad, forma, bordes, focos ecogénicos)
- Calcula puntos TI-RADS automáticamente
- Recomendación FNA según tamaño (TR1-TR5)
- Riesgo de malignidad estimado

### 2. 📊 Seguimiento de Vigilancia Activa
Para pacientes con microPTC en vigilancia activa:
- Registro de pacientes con tamaño inicial
- Agregar controles seriados (fecha + tamaño)
- Detección automática de progresión (>3 mm)
- Visualización de curva de crecimiento

### 3. 📈 Clasificador de Respuesta Dinámica (DRS)
Post-tiroidectomía total ± RAI:
- Clasifica en: Excelente, Indeterminada, Bioquímica Incompleta, Estructural Incompleta
- Conducta recomendada por categoría
- Próximo control sugerido
- Historial de clasificaciones

## Deploy en Vercel

```bash
npm i -g vercel
vercel --prod
```

O simplemente arrastra la carpeta a vercel.com.

## Uso en consulta
- Abrir en iPad/tablet desde el navegador
- Todos los datos se guardan localmente (localStorage)
- Funciona offline una vez cargado

## Fuentes
ACR TI-RADS, AACE 2024, ATA 2025, Hegedüs et al. NEJM 2026