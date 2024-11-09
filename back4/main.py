from functions import divide_by_zero, invalid_input, handle_exception, handle_exception_with_finally, handle_multiple_exceptions, generate_exception, handle_custom_exception, calculate_average, calculate_sum, process_string, NegativeValueException, InvalidInputError

def run_all_functions():
    """
    Шаг 9: Функция, вызывающая все остальные функции
    """
    try:
        divide_by_zero(10, 0) # Вызов функции с делением на ноль
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")

    try: # Добавляем try...except для обработки ValueError
        invalid_input(-5) # Вызов функции с некорректным входным значением
    except ValueError as e:
        print(f"Ошибка: {e}")

    handle_exception(10, 0) # Вызов функции с обработкой исключений Exception

    handle_exception_with_finally(10, 0) # Вызов функции с блоком finally

    handle_multiple_exceptions(100, 0) # Вызов функции с обработкой нескольких типов исключений

    generate_exception(10) # Вызов функции, генерирующей исключения

    try:
        handle_custom_exception(-5) # Вызов функции с обработкой пользовательского исключения
    except InvalidInputError as e:
        print(f"Ошибка: {e}")

    numbers = [1, 2, 3, 4]
    try:
        average = calculate_average(numbers)
        print(f"Среднее значение: {average}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        sum = calculate_sum(5, -3)
        print(f"Сумма: {sum}")
    except NegativeValueException as e:
        print(f"Ошибка: {e}")

    text = "Hello, world!"
    try:
        processed_text = process_string(text)
        print(f"Обработанный текст: {processed_text}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    run_all_functions()
