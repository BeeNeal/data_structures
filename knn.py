import math
def kClosest(points, K):
    output = []
    origin = [0,0]

    for i in range(len(points)):
        # Use Euclidean distance formula
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(points[i], origin)]))
        output.append((distance, points[i]))
    
    values = sorted(output)
    closest_points = []
    for i in range(K):
        closest_points.append(values[i][1])
    return closest_points

