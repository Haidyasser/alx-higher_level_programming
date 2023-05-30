
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                cnt += 1
        except (TypeError, ValueError):
            pass
    print()
    return cnt