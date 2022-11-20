from plotter import Plotter

def min_x(x1):
    res = x1[0]
    for x_mbr in x1[1:]:
        if x_mbr < res:
            res = x_mbr
    return res


def max_x(x1):
    res = x1[0]
    for x_mbr in x1[1:]:
        if x_mbr > res:
            res = x_mbr
    return res


def min_y(y1):
    res = y1[0]
    for y_mbr in y1[1:]:
        if y_mbr < res:
            res = y_mbr
    return res


def max_y(y1):
    res = y1[0]
    for y_mbr in y1[1:]:
        if y_mbr > res:
            res = y_mbr
    return res


def main():
    plotter = Plotter()

    print('read polygon.csv')
    with open('polygon.csv', 'r') as f1:
        results = []
        for line in f1:
            coordinates = line.split(',')
            coordinates[2] = coordinates[2].strip()
            results.append((coordinates[0], coordinates[1], coordinates[2]))

    polygon = list(results)
    length_polygon = len(polygon)

    x1 = list()
    y1 = list()
    _polygon = []

    for i in range(1, length_polygon):
        x_p = float(polygon[i][1])
        y_p = float(polygon[i][2])
        x1.append(x_p)
        y1.append(y_p)
        _polygon.append([x_p, y_p])

    print('Insert point information')
    x = float(input('x coordinate: '))
    y = float(input('y coordinate: '))
    point = (x, y)

    print('categorize point')
    n1 = int(len(polygon))
    mbr = []
    for i in range(1, n1):
        x_mbr = float(polygon[i][1])
        y_mbr = float(polygon[i][2])
    mbr.append(x_mbr)
    mbr.append(y_mbr)

    def point_polygon(point, rangelist):
        if (point[0] > max_x(x1) or point[0] < min_x(x1) or
                point[1] > max_y(y1) or point[1] < min_y(y1)):
            return 'outside'
        count = 0
        point1 = rangelist[0]
        for i in range(1, len(rangelist)):
            point2 = rangelist[i]
        if (point[1] == point2[1] == point1[1] and (point1[0] <= point[0] <= point2[0]
                                                    or point2[0] <= point[0] <= point1[0])):
            return 'boundary'
        if ((point[0] == point1[0] and point[1] == point1[1])
            or (point[0] == point2[0] and point[1] == point2[1])):
            return 'boundary'
        if (point1[1] < point[1] <= point2[1]) or (point2[1] < point[1] <= point1[1]):
            point12lng = (point2[0] - (point2[1] - point[1]) *
            (point2[0] - point1[0]) / (point2[1] - point1[1]))
            if point12lng == point[0]:
                return 'boundary'
            if point12lng < point[0]:
                count += 1
        point1 = point2
        if count % 2 == 0:
            return 'outside'
        else:
            return 'inside'


    print('plot polygon and point')
    plotter.add_polygon(x1, y1)
    point_status = point_polygon(point, _polygon)
    if point_status == 'outside':
        plotter.add_point((x, y, 'outside'))
        print('outside point')
    elif point_status == 'boundary':
        plotter.add_point((x, y, 'boundary'))
        print('boundary point')
    elif point_status == 'inside':
        plotter.add_point((x, y, 'inside'))
        print('inside point')
    plotter.show()

if __name__ == '__main__':
    main()
