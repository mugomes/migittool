#!/bin/bash

# Copyright (C) 2025 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Site: https://www.mugomes.com.br

while true; do
	echo ""
	echo "-------------------------------- CreateExecutable --------------------------------"
    echo "Selecione uma opção:"
    echo "1. Preparar o Ambiente"
    echo "2. Compilar o migittool"
    echo "3. Sair"
    echo "-------------------------------- /CreateExecutable --------------------------------"
	echo ""
	
    read -p "Opção: " option

    case $option in
    	1)
            echo "Preparando o ambiente para Linux..."
            rm -rf linux/
            mkdir -p linux/
            cd linux/

    	    echo "Criando diretório mivenv..."
			python3 -m venv mivenv/

			echo "Instalando o pyinstaller..."
			mivenv/bin/pip install pyinstaller
            
            cd ../

			echo "Concluido!"
			;;
        2)
			echo "Compilando 'migittool.py' para Linux..."
			
            rm -f migit.spec
            rm -rf dist/

            mivenv/bin/pyinstaller -F --collect-all ttkbootstrap --hidden-import PIL._tkinter_finder migittool.py
			
			echo "Concluido!"
			;;
        3)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Por favor, escolha uma opção válida."
            ;;
    esac
done
