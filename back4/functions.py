def divide_by_zero(x, y):
    """
    Шаг 1: Функция выбрасывает исключение ZeroDivisionError при делении на ноль
    """
    return x / y

def invalid_input(data):
    """
    Шаг 1: Функция выбрасывает исключение ValueError при некорректном входном значении
    """
    if data < 0:
        raise ValueError("Входное значение должно быть неотрицательным")

def handle_exception(x, y):
    """
    Шаг 2: Функция с обработчиком общего типа исключений Exception
    """
    try:
        result = x / y
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def handle_exception_with_finally(x, y):
    """
    Шаг 3: Функция с обработчиком исключений Exception и блоком finally
    """
    try:
        result = x / y
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение операции")

def handle_multiple_exceptions(x, y):
    """
    Шаг 4: Функция с обработкой нескольких типов исключений
    """
    try:
        result = x / y
        if y < 0:
            raise ValueError("Знаменатель должен быть положительным")
        if x > 100:
            raise OverflowError("Числитель слишком большой")
    except ZeroDivisionError as e:
        print(f"Произошла ошибка: {e}")
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except OverflowError as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение операции")

def generate_exception(data):
    """
    Шаг 5: Функция генерирует исключения
    """
    try:
        if data == 0:
            raise ZeroDivisionError("Деление на ноль")
        if data < 0:
            raise ValueError("Значение меньше нуля")
        if data > 100:
            raise OverflowError("Значение слишком большое")
    except ZeroDivisionError as e:
        print(f"Произошла ошибка: {e}")
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except OverflowError as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение операции")

class InvalidInputError(Exception):
    """
    Шаг 6: Пользовательское исключение InvalidInputError
    """
    def __init__(self, message):
        super().__init__(message)

class NegativeValueException(Exception):
    """
    Шаг 6: Пользовательское исключение NegativeValueException
    """
    def __init__(self, message):
        super().__init__(message)

class ZeroDivisionException(Exception):
    """
    Шаг 6: Пользовательское исключение ZeroDivisionException
    """
    def __init__(self, message):
        super().__init__(message)

def handle_custom_exception(data):
    """
    Шаг 7: Функция с обработкой пользовательского исключения
    """
    try:
        if data < 0:
            raise InvalidInputError("Входное значение должно быть неотрицательным")
    except InvalidInputError as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение операции")

def calculate_average(numbers):
    """
    Шаг 8: Функция для расчета среднего значения
    """
    if not numbers:
        raise ValueError("Список чисел пуст")
    try:
        sum = 0
        for number in numbers:
            sum += number
        return sum / len(numbers)
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
    except TypeError:
        print("Ошибка: Некорректный тип данных")

def calculate_sum(a, b):
    """
    Шаг 8: Функция для расчета суммы
    """
    try:
        if a < 0 or b < 0:
            raise NegativeValueException("Оба числа должны быть неотрицательными")
        return a + b
    except NegativeValueException as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение операции")

def process_string(text):
    """
    Шаг 8: Функция для обработки строки
    """
    try:
        if text.isdigit():
            raise ValueError("Текст должен содержать буквы")
        return text.upper()
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except AttributeError:
        print("Ошибка: Некорректный тип данных")