# -*- coding: utf-8 -*-
name = input("Введите название реактива:")
quantity = input("Введите колличество поступившего реактива")
clean_name = name.strip()
clean_quantity = quantity.strip()
print(f"Реактив '{clean_name}' поступил на склад в колличестве {clean_quantity} шт")
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(f"Реактив '{clean_name}' поступил на склад в колличестве {clean_quantity} шт")
  
