"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(hidden_number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_r = 1
    max_r = 101
    
    min_n = 1 # Минимальное значение рассматриваемого интервала
    max_n = 100 # Максимальное значение рассматриваемого интервала
    
    predict_number = np.random.randint(min_r, max_r) # загадываем рандомное число, используя генератор рандомных чисел
    while True:
        count += 1
        if predict_number > hidden_number:
            max_n = predict_number - 1
            predict_number = min_n + (max_n - min_n) // 2
        elif predict_number < hidden_number:
            min_n = predict_number + 1
            predict_number = min_n + (max_n - min_n) // 2
        else:
            break # конец игры и выход из цикла
    return(count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
