#!/bin/bash

# Обновление списка пакетов
sudo dnf update -y

# Установка Python и pip
sudo dnf install python3 -y
sudo dnf install python3-pip -y

# Установка зависимостей из файла requirements.txt
pip3 install -r requirements.txt

echo "Установка завершена"
