#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_lista = []
        for i in my_list:
            if i % 2 == 0:
                new_lista.append(True)
            else:
                new_lista.append(False)
        return new_lista
