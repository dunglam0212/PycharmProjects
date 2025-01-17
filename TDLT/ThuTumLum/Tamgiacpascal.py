def create_pascal_triangle(h):
    triangle=[]
    for i in range(h):
        row=[1]
        for j in range(i):
            row.append(triangle[i-1][j] + triangle[i-1][j])
        if i>0:
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    h=len(triangle)
    for row in triangle:
        print(*row)

rs=create_pascal_triangle(5)
print_pascal_triangle(rs)