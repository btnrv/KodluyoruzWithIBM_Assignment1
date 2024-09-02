points = [(1, 2), (4, 6), (5, 3), (8, 9)]

def euclideanDistance(point1, point2):
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]
    distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
    return distance

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print("Minimum distance:", min_distance)