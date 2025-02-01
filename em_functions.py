import csv

def get_ml_log(filepath='ml_log.txt'):
    with open(filepath , 'r') as file:
        ml_logs = list(csv.reader(file))    # mnogu poprofi e vaka
    return ml_logs     # koj rezultat da go vrati taa funckija


def write_ml_log(ml_arg, filepath='ml_log.txt'):
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ml_arg)


def get_sleep_log(todos_arg, filepath='Todos.txt' ):
    with open(filepath , 'r') as file:
        ml_logs = file.readlines()    # mnogu poprofi e vaka
    return ml_logs


def write_sleep_log(todos_arg, filepath='Todos.txt' ):
    """ Saves the new Todo list. """  #Doc String
    with open(filepath, 'w') as file:  # zapishuvanje na nov file so skraten metod (WITH)
        file.writelines(todos_arg)