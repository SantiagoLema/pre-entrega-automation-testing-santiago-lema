import pytest

# Lista de archivos de las pruebas a ejecutar
test_files = [
    "pre-entrega-automation-testing-santiago-lema/tests/test_login.py",
    "pre-entrega-automation-testing-santiago-lema/tests/test_inventory.py",
    "pre-entrega-automation-testing-santiago-lema/tests/test_cart.py"
]

# Argumentos para ejecutar las pruebas: archivos y el reporte html
pytest_args = test_files + ["--html=report.html","--html=self-contained.html","-v"]

pytest.main(pytest_args)