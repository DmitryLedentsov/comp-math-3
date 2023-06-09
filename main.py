from calculations import *
from functions import *
from io_functions import *

def app():
    mode = ask_mode();
    if (mode == 1):
        num = ask_function()
        a, b = ask_a_b()
        epsilon = ask_error()

        #случай, если а оказывается больше b: интеграл будет равен интегралу с противоположным знаком
        mul = 1
        if a > b:
            mul = -1
            a, b = b, a

        method = ask_method()

        if method == 1:
            ans, partition, err = calc_integral(get_function(num), squad_method_left, a, b, epsilon, 2)
        elif method == 2:
            ans, partition, err = calc_integral(get_function(num), squad_method_right, a, b, epsilon, 2)
        elif method == 3:
            ans, partition, err = calc_integral(get_function(num), squad_method_mid, a, b, epsilon, 2)
        elif method == 4:
            ans, partition, err = calc_integral(get_function(num), trapezoid_method, a, b, epsilon, 2)
        else:
            ans, partition, err = calc_integral(get_function(num), simpson_method, a, b, epsilon, 4)

        print(f"Получен ответ {ans * mul}, {partition} разбиений")

    elif mode==2:
        num = ask_break_function()

        a, b = ask_a_b()
        epsilon = ask_error()
        mul = 1
        if a > b:
            mul = -1
            a, b = b, a

        func, brk = get_break_function(num)

        method = ask_method_with_simpson()

        if method == 1:
            if (num == 1):
                ans = calc_with_2nd_break(func, squad_method_left, a, b, brk, epsilon, 2)
            else:
                ans = calc_with_1st_break(func, squad_method_left, a, b, brk, epsilon, 2)
        elif method == 2:
            if (num == 1):
                ans = calc_with_2nd_break(func, squad_method_right, a, b, brk, epsilon, 2)
            else:
                ans = calc_with_1st_break(func, squad_method_right, a, b, brk, epsilon, 2)
        elif method == 3:
            if (num == 1):
                ans = calc_with_2nd_break(func, squad_method_mid, a, b, brk, epsilon, 2)
            else:
                ans = calc_with_1st_break(func, squad_method_mid, a, b, brk, epsilon, 2)
        elif method == 4:
            if (num == 1):
                ans = calc_with_2nd_break(func, trapezoid_method, a, b, brk, epsilon, 2)
            else:
                ans = calc_with_1st_break(func, trapezoid_method, a, b, brk, epsilon, 2)
        else:
            if (num == 1):
                ans = calc_with_2nd_break(func, simpson_method, a, b, brk, epsilon, 4)
            else:
                ans = calc_with_1st_break(func, simpson_method, a, b, brk, epsilon, 4)

        print(f"Ответ: {ans * mul}")
    else:
        return False
    
    return True


def exit():
    print("\nВыходим...")
while(True):
    try:
        if not app():
            exit()
            break
    except KeyboardInterrupt:
        exit()
        break
