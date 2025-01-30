# Automatización de Consulta de Títulos y Certificaciones en Senescyt

## Introducción  
Este flujo automatiza la consulta de información académica y certificaciones de un ciudadano en el portal de **Senescyt** (Ecuador) utilizando **Power Automate Desktop**. A continuación, se detalla su funcionamiento:

## Requisitos Previos  
Antes de ejecutar el flujo, asegúrate de contar con los siguientes elementos:  
- **Cuenta en Senescyt** con acceso a la consulta de títulos.  
- **Power Automate Desktop** instalado y configurado en tu equipo.  
- **Datos del ciudadano**, como número de cédula o nombres completos.  
- Conexión estable a **Internet**.  

## Pasos para la Automatización  

1. **Abrir Power Automate Desktop**  
   - Iniciar sesión en Power Automate Desktop.  
   - Crear un nuevo flujo de escritorio.  

2. **Acceder al Portal de Senescyt**  
   - Configurar la acción "Lanzar navegador" e ingresar la URL del portal de Senescyt.  
   - Asegurar que el navegador utilizado sea compatible con la automatización.  

3. **Ingresar los Datos del Ciudadano**  
   - Configurar la acción para identificar el campo de búsqueda en el portal.  
   - Introducir el número de cédula o nombres completos del ciudadano.  
   - Ejecutar la acción de búsqueda.  

4. **Extraer la Información**  
   - Capturar los datos obtenidos en la consulta, como título, universidad y fecha de registro.  
   - Almacenar los datos en un archivo Excel o base de datos.  

5. **Generar Reporte Automático**  
   - Configurar Power Automate para exportar la información a un archivo JSON. 
     

## Solución de Problemas  
Si el flujo no funciona correctamente, revisa lo siguiente:  
- Verifica la conexión a Internet.  
- Asegúrate de que los campos de búsqueda en el portal de Senescyt no hayan cambiado.  
- Revisa que Power Automate Desktop tenga permisos adecuados para interactuar con el navegador.  

## Conclusión  
Este flujo permite agilizar la consulta de títulos y certificaciones en Senescyt, eliminando procesos manuales y reduciendo errores. Su implementación mejora la eficiencia en la verificación académica de ciudadanos.  

