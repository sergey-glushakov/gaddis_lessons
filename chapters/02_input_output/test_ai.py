def calculate_data(x, y):
    print("Начало расчета")
    try:
        result = x / y
    except ZeroDivisionError:
        result = "Ошибка: Деление на ноль"
    return result


# Пример использования
result = calculate_data(10, 5)
print(result)  # Выведет: Ошибка: Деление на ноль
