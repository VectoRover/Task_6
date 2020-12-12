import math
eps = 0.00000001


def enter():
    try:
        count_1 = int(input("Введите количество вершин 1- го многоугольника: "))
    except ValueError:
        print("Вы ввели некорректные данные")
        exit(-2)
    if count_1 == 0 or count_1 < 3:
        print("Вы ввели некорректное значение")
        exit(-1)
    dots_1 = []
    for i in range(count_1):
        print("Ввод координат", i + 1, "-й вершины")
        try:
            a = float(input("Введите абсциссу: "))
            b = float(input("Введите ординату: "))
        except ValueError:
            print("Вы ввели некорректные данные")
            exit(-3)
        dots_1.append([a, b])
    try:
        count_2 = int(input("Введите количество вершин 2- го многоугольника: "))
    except ValueError:
        print("Вы ввели некорректные данные")
        exit(-2)
    if count_2 == 0 or count_2 < 3:
        print("Вы ввели некорректное значение")
        exit(-1)
    dots_2 = []
    for i in range(count_2):
        print("Ввод координат", i + 1, "-й вершины")
        try:
            a = float(input("Введите абсциссу: "))
            b = float(input("Введите ординату: "))
        except ValueError:
            print("Вы ввели некорректные данные")
            exit(-3)
        dots_2.append([a, b])
    return [dots_1, dots_2, count_1, count_2]


def dist(dot1, dot2): #расстояние между точками
    a = dot1[0] - dot2[0]
    b = dot1[1] - dot2[1]
    return math.sqrt(a * a + b * b)


def normal(dot, dot1, dot2): #возвращает расстояние от точки dot до прямой, проходящей, через dot1 и dot2
    a = dist(dot, dot1)
    b = dist(dot, dot2)
    c = dist(dot1, dot2)
    p = 0.5*(a+b+c)
    try:
        n = (2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/(c)
    except ZeroDivisionError:
        n = 0
    if abs(n - round(n)) < eps:
        return float(round(n))
    else:
        return n


def obt_ang(dot, dot1, dot2): #возвр 1, если треугольник из dot, dot1, dot2 остроуг или прямоуг, либо тупой угол находится при вершине dot
    a = dist(dot, dot1)
    b = dist(dot, dot2)
    c = dist(dot1, dot2)
    lst = []
    try:
        lst.append((b**2 + c**2 - a**2)/(2*c*b))
        lst.append((a**2 + c**2 - b**2)/(2*a*c))
        lst.append((a**2 + b**2 - c**2)/(2*a*b))
    except ZeroDivisionError:
        return 1
    for i in range(3):
        if abs(lst[i]) < eps:
            lst[i] = 0
    #print(lst)
    if lst[0] < 0:
        return -1
    if lst[1] < 0:
        return -1
    if lst[2] < 0:
        return 1
    lst.clear()
    return 1


def intersection(dot1, dot2, dot3, dot4): #вернет 1, если отрезки пересекаются или совпадают и -1 в противном случае
    x1=dot1[0]
    y1=dot1[1]
    x2=dot2[0]
    y2=dot2[1]
    x3=dot3[0]
    y3=dot3[1]
    x4=dot4[0]
    y4=dot4[1]
    A1 = y1 - y2
    B1 = x2 - x1
    C1 = x1*y2 - y1*x2
    A2 = y3 - y4
    B2 = x4 - x3
    C2 = x3*y4 - y3*x4
    if A1*B2 - A2*B1 == 0 and B1*C2-B2*C1 == 0:
        if (abs(x2 - x1) + abs(x3 - x4) < abs(max(x1, x2) - max(x3, x4))) and (abs(y2 - y1) + abs(y3 - y4) < abs(max(y1, y2) - max(y3, y4))):
            return 1
        else:
            return -1
    if A1*B2 - A2*B1 == 0 and B1*C2-B2*C1 != 0:
        return -1
    x = -(-B2*C1 + B1*C2)/(A2*B1 - A1*B2)
    y = -(A2*C1 - A1*C2)/(A2*B1 - A1*B2)
    if (abs(abs(x1 - x) + abs(x2 - x) - abs(x1 - x2)) < eps) and (abs(abs(x3 - x) + abs(x4 - x) - abs(x3 - x4)) < eps) and (abs(abs(y1 - y) + abs(y2 - y) - abs(y1 - y2)) < eps) and (abs(abs(y3 - y) + abs(y4 - y) - abs(y3 - y4)) < eps):
        return 1
    else:
        return -1


def inclusion(dots_1, dots_2, count_1, count_2): #вернет 1, если вершина одного многоугольника лежит внутри другого, иначе -1
    in_polygon = False
    for i in range(count_1):
        x = dots_1[i][0]
        y = dots_1[i][1]
        for j in range(count_2):
            xp = dots_2[j][0]
            yp = dots_2[j][1]
            xp_prev = dots_2[j - 1][0]
            yp_prev = dots_2[j - 1][1]
            if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (
                    x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
                in_polygon = not in_polygon
        if in_polygon == True:
            return in_polygon
    for i in range(count_2):
        x = dots_2[i][0]
        y = dots_2[i][1]
        for j in range(count_1):
            xp = dots_1[j][0]
            yp = dots_1[j][1]
            xp_prev = dots_1[j - 1][0]
            yp_prev = dots_1[j - 1][1]
            if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (
                    x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
                in_polygon = not in_polygon
        if in_polygon == True:
            return in_polygon
    return in_polygon   


def min_dist_vert_vert(dots_1, dots_2, count_1, count_2):
    min_dist = dist(dots_1[0], dots_2[0])
    for i in range(count_1):
        for k in range(count_2):
            tmp_dist = dist(dots_1[i], dots_2[k])
            if tmp_dist < min_dist:
                min_dist = tmp_dist
    return min_dist


def min_dist_vert_edge(dots_1, dots_2, count_1, count_2):
    min_dist = dist(dots_1[0], dots_2[0])
    for i in range(count_1):
        for k in range(count_2):
            if k < count_2-1:
               # print(obt_ang(dots_1[i], dots_2[k], dots_2[k+1]))
                if obt_ang(dots_1[i], dots_2[k], dots_2[k+1]) == 1:
                    tmp_dist = normal(dots_1[i], dots_2[k], dots_2[k+1])
                    if tmp_dist < min_dist:
                        min_dist = tmp_dist
            else:
                if obt_ang(dots_1[i], dots_2[k], dots_2[0]) == 1:
                    tmp_dist = normal(dots_1[i], dots_2[k], dots_2[0])
                    if tmp_dist < min_dist:
                        min_dist = tmp_dist
    return min_dist


def dist_polygons(dots_1, dots_2, count_1, count_2):
    if inclusion(dots_1, dots_2, count_1, count_2) == True:
        return 0
    for i in range(count_1):
        for j in range(count_2):
            if intersection(dots_1[i-1], dots_1[i], dots_2[j-1], dots_2[j]) == 1:
                return 0
    return min(min_dist_vert_vert(dots_1, dots_2, count_1, count_2), min_dist_vert_edge(dots_1, dots_2, count_1, count_2))


def autotest():
     a = dist_polygons([[-3, 3], [3, 3], [3, -3], [-3, -3]], [[-1, 0], [1, 0], [0, 1]], 4, 3)
     b = dist_polygons([[0, 0], [0, 1], [1, 1], [1, 0]], [[2, 0], [2, 1], [3, 1], [3, 0]], 4, 4)
     c = dist_polygons([[-1, 0], [1, 0], [0, 1]], [[-2, 3], [2, 3], [0, 7]], 3, 3)
     d = dist_polygons([[-1, 0], [1, 0], [0, 1]], [[0, 2], [-1, 10], [1, 7]], 3, 3)
     if a != 0 or b != 1 or c != 2 or d != 1:
         print("Автотест провален")
     else:
         print("Автотест сдан")

autotest()
lst = enter()
dots_1 = lst[0]
dots_2 = lst[1]
count_1 = lst[2]
count_2 = lst[3]
lst.clear()

print("Расстояние между многоугольниками: ")
print(f'{dist_polygons(dots_1, dots_2, count_1, count_2):.3f}')

