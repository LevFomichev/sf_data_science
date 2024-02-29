import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Напишем функцию, которая принимает на вход загаданное число и возвращает число попыток угадывания.
       Нахождение загаданного числа будет происходить путём соединения двух предыдущих методов,
       которые предполагали последовательное сужение диапазона поиска и выбор следующего числа в зависимости от того,
       больше оно или меньше загаданного.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    predict_number = np.random.randint(1, 101)  # предполагаемое число
    
    while True:
        count += 1
        if predict_number > number:
            more_predict_number = predict_number
            predict_number = np.random.randint(1, more_predict_number)
        if predict_number < number:
            less_predict_number = predict_number
            predict_number = np.random.randint(less_predict_number, 101)
        else:
            break  # выход из цикла если угадали
    return count 


def score_game_v2(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score   