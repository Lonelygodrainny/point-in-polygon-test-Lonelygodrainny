from plotter import Plotter

x_out, y_out, x_on, y_on, x_in, y_in = [], [], [], [], [], []
xy_out, xy_on, xy_in = [], [], []


# Calculate the points of MBR
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
# Aldo,L(2020)


def main():
    plotter = Plotter()
    print('read polygon.csv')
    # Read the points of polygon from csv file
    with open('polygon.csv', 'r') as f1:
        results = []
        for line in f1:
            co = line.split(',')
            co[2] = co[2].strip()
            results.append((co[0], co[1], co[2]))
    # Aldo,L(2020)

    polygon = list(results)
    len_polygon = len(polygon)

    x1 = list()
    y1 = list()
    _polygon = []

    # Output lists about points of polygon
    for i in range(1, len_polygon):
        x1.append(float(polygon[i][1]))
        y1.append(float(polygon[i][2]))
        _polygon.append([float(polygon[i][1]), float(polygon[i][2])])

    print('read input.csv')
    # Read the points of polygon from csv file
    with open('input.csv', 'r') as f2:
        results2 = []
        for line in f2:
            if line.strip() != 'id,x,y':
                co2 = line.split(',')
                co2[2] = co2[2].strip()
                results2.append((int(co[0]), float(co2[1]), float(co2[2])))

    points = list(results2)
    len_points = len(points)

    x2 = list()
    y2 = list()
    # Output lists about coordinates of test points
    for i in range(1, len_points):
        x2.append(float(points[i][1]))
        y2.append(float(points[i][2]))

    print('categorize points')

    # Calculate MBR of polygon
    n1 = int(len(polygon))
    mbr = []
    for i in range(1, n1):
        x_mbr = float(polygon[i][1])
        y_mbr = float(polygon[i][2])
    mbr.append(x_mbr)
    mbr.append(y_mbr)

    # Classify the points (outside,boundary,inside)
    def point_polygon(point, rangelist):
        # Points outside the minimum bounding rectangle must be outside the polygon
        if (point[0] > max_x(x1) or point[0] < min_x(x1) or
                point[1] > max_y(y1) or point[1] < min_x(y1)):
            return 'outside'

        count = 0
        point1 = rangelist[0]

        for i in range(1, len(rangelist)):
            point2 = rangelist[i]
            x2.append(float(points[i][1]))
            y2.append(float(points[i][2]))
            # Points are between the two endpoints of the horizontal side of the polygon
            if (point[1] == point2[1] == point1[1] and (point1[0] <= point[0] <= point2[0]
                                                        or point2[0] <= point[0] <= point1[0])):
                return 'boundary'
            # Points coincident with polygon vertices
            if ((point[0] == point1[0] and point[1] == point1[1])
                    or (point[0] == point2[0] and point[1] == point2[1])):
                return 'boundary'
            # Determine whether the two ends of the line segment are on both sides of the ray.
            # If they are not, they must not intersect. Ray (-∞, y) (x, y)
            if (point1[1] < point[1] <= point2[1]) or (point2[1] < point[1] <= point1[1]):
                # Find the intersection point of the line segment and the ray and compare it with x
                point12x = (point2[0] - (point2[1] - point[1]) *
                            (point2[0] - point1[0]) / (point2[1] - point1[1]))
                # points on the boundary of polygon
                if point12x == point[0]:
                    return 'boundary'

                if point12x < point[0]:
                    count += 1
            point1 = point2
        # points outside the polygon
        if count % 2 == 0:
            return 'outside'
        # points inside the polygon
        else:
            return 'inside'
        # Mian, Q.(2021).

    print('write output.csv')
    arr = []
    # Output lists of point coordinates and their category
    for point in points:
        point = list(point)[1:]
        category = point_polygon(point, _polygon)
        arr.append(category)
        # Output lists of outside points' coordinates
        if category == 'outside':
            x_out.append(float(point[0]))
            y_out.append(float(point[1]))
            xy_out.append((x_out[0], y_out[0]))
        # Output lists of boundary points' coordinates
        elif category == 'boundary':
            x_on.append(float(point[0]))
            y_on.append(float(point[1]))
            xy_on.append((x_on[0], y_on[0]))
        # Output lists of inside points' coordinates
        elif category == 'inside':
            x_in.append(float(point[0]))
            y_in.append(float(point[1]))
            xy_in.append((x_in[0], y_in[0]))

    # Write output csv file
    with open('output.csv', 'w') as f:
        f.writelines("id,category\n")
        i = 0
        for line in arr:
            f.writelines(str(i + 1) + ',' + line + '\n')
            i = i + 1
    # Write id and point status of 'outside' points
    print('outside point')
    for i in range(len(x_out)):
        print(xy_out[i], end=' ')
    print('\n')
    # Write id and point status of 'boundary' points
    print('boundary point')
    for i in range(len(x_on)):
        print(xy_on[i], end=' ')
    print('\n')
    # Write id and point status of 'inside' points
    print('inside point')
    for i in range(len(x_in)):
        print(xy_in[i], end=' ')
    print('\n')

    for i in range(len(arr)):
        print(arr[i], end=' ')
    print('\n')

    print('plot polygon and points')

    # plot the polygon
    plotter.add_polygon(x1, y1)
    # plot the points with their category
    for i in range(len(x_out)):
        plotter.add_point((x_out[i]), (y_out[i]), 'outside')
    for i in range(len(x_on)):
        plotter.add_point((x_on[i]), (y_on[i]), 'boundary')
    for i in range(len(x_in)):
        plotter.add_point((x_in[i]), (y_in[i]), 'inside')

    plotter.show()


if __name__ == '__main__':
    main()


