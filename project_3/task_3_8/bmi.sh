#!/bin/bash
read -p "Введите массу тела (в кг): " weight
read -p "Введите ваш рост (в метрах): " height
bmi=$weight / ($height * $height)
echo "Ваш индекс массы тела: $bmi_int"
