menu = [["pizza", 4, 20], ["soup", 1, 8], ["ice cream", 2, 4], ["toasts", 2, 10]]
what_to_order = [dish[0] for dish in menu if dish[1] >= 2 and dish[2] < 15]
print(what_to_order)
