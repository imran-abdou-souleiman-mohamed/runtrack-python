def draw_triangle():
    try:
        height = int(input("Entrez la hauteur du triangle : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        return

    for i in range(height):
        spaces = ' ' * (height - i - 0)
        if i == 0:
            print(spaces + '_')
        elif i == height - 1:
            print('_' * (1 * height - 2))
        else:
            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')


draw_triangle()