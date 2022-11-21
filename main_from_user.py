from plotter import Plotter


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
    with open('polygon.csv', 'r') as f1:
        results = []
        for line in f1:
            co = line.split(',')
            co[2] = co[2].strip()
            results.append((co[0], co[1], co[2]))
    # Aldo,L(2020)
    # Error handling functionality
    try:
        open('polygon.csv')
    except:
        print('cannot get to this file')
    else:
        print('polygon file has been opened successfully')
    finally:
        print('next step?')

    polygon = list(results)
    len_polygon = len(polygon)

    x1 = list()
    y1 = list()
    _polygon = []

    # Output lists about points of polygon
    for i in range(1, len_polygon):
        x_p = float(polygon[i][1])
        y_p = float(polygon[i][2])
        x1.append(x_p)
        y1.append(y_p)
        _polygon.append([x_p, y_p])

    print('Insert point information')
    # Input the coordinates of the point for test
    x = float(input('x coordinate: '))
    y = float(input('y coordinate: '))
    point = (x, y)

    print('categorize point')
    # Calculate MBR of polygon
    n1 = int(len(polygon))
    mbr = []
    for i in range(1, n1):
        x_mbr = float(polygon[i][1])
        y_mbr = float(polygon[i][2])
    mbr.append(x_mbr)
    mbr.append(y_mbr)

    # Classify the status of point (outside,boundary,inside)
    def point_polygon(point, rangelist):
        # Points outside the minimum bounding rectangle must be outside the polygon
        if (point[0] > max_x(x1) or point[0] < min_x(x1) or
                point[1] > max_y(y1) or point[1] < min_y(y1)):
            return 'outside'
        count = 0
        point1 = rangelist[0]
        for i in range(1, len(rangelist)):
            point2 = rangelist[i]
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

    print('plot polygon and point')
    plotter.add_polygon(x1, y1)
    point_status = point_polygon(point, _polygon)
    # Plot point status of 'outside' points
    if point_status == 'outside':
        plotter.add_point(x, y, 'outside')
        print('outside point')
    # Plot point status of 'boundary' points
    elif point_status == 'boundary':
        plotter.add_point(x, y, 'boundary')
        print('boundary point')
    # Plot point status of 'inside' points
    elif point_status == 'inside':
        plotter.add_point(x, y, 'inside')
        print('inside point')
    plotter.show()


if __name__ == '__main__':
    main()

#Reference
#Read CSV:
#Aldo, L. (2020). Week 3 - Python Data Structures, IDE and Debugger, Lecture Material, 21.
#MBR:
#Aldo, L. (2020). Week 4 - Object-Oriented Programming, Lecture Material, 4 - 6.
#RCA/Output:
#Mian, Q. (2021). Python3 ray method to determine whether a point is within a polygon. Retrieved from https://www.mianshigee.com/note/detail/51088gsb/
