@echo off
cd /d "%~dp0"

start "API Cliente 5001" cmd /k python api_cliente.py
start "API Compras 5002" cmd /k python api_compras.py
start "API Financeiro 5003" cmd /k python api_financeiro.py

echo Aguardando as APIs de origem iniciarem...
timeout /t 5 /nobreak >nul

start "API Consolidar 5004" cmd /k python api_consolidar.py
start "API Consolidados 5005" cmd /k python api_consolidados.py
start "API Exportar 5006" cmd /k python api_exportar.py
