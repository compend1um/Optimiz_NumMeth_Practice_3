from source.task1.run_task1 import run_task1
from source.task_runs.run_task2 import run_task_2


def pause(): input("\nНажмите Enter, чтобы продолжить...")


def separator(symbol:str, long=86):
    """
    печатает строку-разделитель, путем дублирования указаной строки \n
    допустимо дублирование '= ' (двух знаков сразу)
    так как длина строки-разделителя останется прежней

    :param symbol: строка, которая будет продублирована на всю строку
    :param long: длинна строки в символах
    :return: примеры вывода: ------------------ / = = = = = = = = = = =
    """
    return symbol * int( long / len(symbol) )


def print_menu():

    print(
        "",
        separator("-"),
        #"\n"
        "\t:: TASK 1",
        "\t\t1. Найти локальные экстремумы методом градиентного спуска",
        "\n"
        "\t:: TASK 2",
        "\t\t2. Вычислить геометрическую медиану и сравните её со средним значением",
        "\t\t3. Построить 3D-график",
        separator("-"),
        "\t\t0. Выйти\n",

        sep="\n",
    )


def menu():

    pass_to_4 = False

    while True:

        print_menu()

        users_choice = int(input("Select option (0-3): "))
        print(separator("- "),
              "\n")


        if users_choice == 1:

            run_task1()
            pause()

        if users_choice == 2:

            run_task_2("print_results")
            pass_to_4 = True

            pause()

        if users_choice == 3:

            if not pass_to_4:

                print("Сначала запустите выполнение пункта 3")

            else:

                run_task_2("show_plot")

            pause()

        if users_choice == 0:

            break


menu()

