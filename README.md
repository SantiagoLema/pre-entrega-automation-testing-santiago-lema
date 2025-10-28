Proyecto de Automatización QA

Propósito del proyecto El objetivo de este proyecto es automatizar casos de prueba funcionales para garantizar la calidad de la página SauceDemo. Mediante la implementación de scripts automatizados, se busca optimizar el tiempo de ejecución de pruebas repetitivas, detectar errores de forma temprana y generar reportes detallados de resultados que faciliten la toma de decisiones durante el proceso de desarrollo.

Tecnologías utilizadas Lenguaje: Python Framework de testing: Pytest Generación de reportes: pytest-html Control de versiones: Git/GitHub Entorno de desarrollo: Visual Studio Code

pre-entrega-automation-testing-santiago-lema/ ├── conftest.py #Configuraciones adicionales para pytest ├── utils.py #Funciones auxiliares reutilizables ├── run_tests.py #Ejecución de las pruebas ├── report.html #Reporte de las pruebas └── tests/ # Casos de prueba automatizados

Instalar las dependencias necesarias: Tener Python 3.7 o superior instalado. pip install selenium pytest pytest-html Descarga el WebDriver correspondiente a tu navegador: ChromeDriver

Comando para ejecutar las pruebas py -m pytest pre-entrega-automation-testing-santiago-lema/run_tests.py -v
Este comando ejecutará los casos de prueba con salida detallada y generará un archivo reporte.html con el resultado de la ejecución.
