import random

def generate_array(size, min_value=0, max_value=100):
    """
    Генерирует массив случайных чисел.

    Эта функция создает массив заданного размера, заполняя его случайными
    целыми числами в диапазоне от min_value до max_value.
    """
    return [random.randint(min_value, max_value) for _ in range(size)]

def input_array():
    """
    Запрашивает у пользователя ввод массива чисел.

    Пользователь должен вводить числа, разделенные пробелами.
    """
    user_input = input("Введите числа через пробел: ")
    return list(map(int, user_input.split()))

def main_menu():
    """
    Отображает меню выбора задания.

    Пользователь может выбрать одно из доступных заданий.
    """
    print("Выберите задание:")
    print("1. Сумма двух массивов")
    print("2. Проверка трех массивов")
    print("3. Поворот матрицы")
    print("4. Завершение работы программы")

def sort_arrays(arr1, arr2):
    """
    Сортирует два массива.

    Первый массив сортируется по убыванию, второй - по возрастанию.
    """
    arr1_sorted = sorted(arr1, reverse=True)
    arr2_sorted = sorted(arr2)
    return arr1_sorted, arr2_sorted

def task_1(arr1, arr2):
    """
    Выполняет первую задачу.

    Принимает два массива, сортирует их и возвращает новый массив,
    где каждый элемент является суммой соответствующих элементов из двух массивов.
    
    Если элементы равны, добавляется 0.
    """
    
   # Сортируем оба массива
   arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
    
   result = []
    
   # Проходим по элементам обоих массивов
   for a, b in zip(arr1_sorted, arr2_sorted):
       if a == b:
           result.append(0)  # Если элементы равны, добавляем 0
       else:
           result.append(a + b)  # Иначе добавляем сумму

   return sorted(result)  # Возвращаем отсортированный результат

def task_2(arr1, arr2, arr3):
   """
   Выполняет вторую задачу.

   Принимает три массива и возвращает список результатов,
   где каждый элемент является результатом вычисления условия задачи:
   если сумма двух элементов равна третьему элементу,
   то результатом будет (a + b + c) возведенное в степень min(a, b, c).
   """
   
   results = []
    
   # Проходим по элементам трех массивов
   for a, b, c in zip(arr1, arr2, arr3):
       if a + b == c:
           results.append((a + b + c) ** min(a, b, c))  # Вычисляем результат

   return results

def rotate_matrix(matrix):
   """
   Поворачивает матрицу на 90 градусов по часовой стрелке.

   Принимает матрицу (список списков) и возвращает новую матрицу,
   повернутую на 90 градусов по часовой стрелке.
   """
   
   return [list(reversed(col)) for col in zip(*matrix)]

def main():
   """
   Основная функция программы с меню выбора заданий.

   Пользователь может выбрать задание и программа выполнит его.
   """
   
   while True:
       main_menu()
       choice = int(input("Выберите пункт меню: "))
       
       if choice == 1:
           array1 = input_array()  # Ввод первого массива
           array2 = input_array()  # Ввод второго массива
           result = task_1(array1, array2)  # Выполнение первой задачи
           print("Результат задачи 1:", result)
       elif choice == 2:
           array1 = input_array()  # Ввод первого массива
           array2 = input_array()  # Ввод второго массива
           array3 = input_array()  # Ввод третьего массива
           result = task_2(array1, array2, array3)  # Выполнение второй задачи
           print("Результат задачи 2:", result)
       elif choice == 3:
           # Пример матрицы для поворота
           matrix = [[1, 2], [3, 4]]
           rotated_matrix = rotate_matrix(matrix)  # Поворот матрицы
           print("Повернутая матрица:", rotated_matrix)
       elif choice == 4:
           print("Завершение работы программы.")
           break  # Выход из цикла и завершение программы
       else:
           print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
   main()  # Запуск основной функции программы