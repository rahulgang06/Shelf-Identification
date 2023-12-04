from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ShelfLayoutSerializer



def max_area_of_island(grid):
    max_area = 0
    r, c = len(grid), len(grid[0])
    res = [0, 0, 0]

    def dfs(i, j):
        nonlocal max_area
        if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        return area

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                area = dfs(i, j)
                if area > max_area:
                    max_area = area
                    res[0] = max_area
                    res[1] = i
                    res[2] = j

    return res

def check_perfect_square(number):
    sqrt = int(number ** 0.5)
    return sqrt * sqrt == number

def check_horizontal_rect(matrix, x, y, r, c, max_area):
    return c - y >= max_area and matrix[x][y] == matrix[x][y + max_area - 1]

def check_vertical_rect(matrix, x, y, r, c, max_area):
    return r - x >= max_area and matrix[x][y] == matrix[x + max_area - 1][y]

def find_location(x, y, r, c):
    s = ""
    if x + 1 < r // 2:
        s += "top"
    elif x + 1 == r // 2:
        s += "middle"
    else:
        s += "bottom"

    if y < c // 2:
        s = s + " " + "left"
    else:
        s = s + " " + "right"
    return s

@api_view(['POST'])
def identify_shelf_shapes(request):
    print('enter')
    serializer = ShelfLayoutSerializer(data=request.data)

    if serializer.is_valid():
        layout_data = serializer.validated_data['layout_data']
        print(layout_data)

        def run_with_variable(variable,layout_data):
            arr = layout_data

            r = len(arr)
            c = len(arr[0])

            matrix = [[0 for _ in range(c)] for _ in range(r)]
            matrix1 = [[0 for _ in range(c)] for _ in range(r)]
            max_area = 0

            # Assign the variable to arr[i][j]
            for i in range(r):
                for j in range(c):
                    if arr[i][j] == variable:
                        matrix[i][j] = 1
                        matrix1[i][j] = 1
                    else:
                        matrix[i][j] = 0
                        matrix1[i][j] = 0

            res = max_area_of_island(matrix1)
            x = res[1]
            y = res[2]
            max_area = res[0]

            result = ""

            if check_perfect_square(max_area) and not check_horizontal_rect(matrix, x, y, r, c, max_area) and not check_vertical_rect(matrix, x, y, r, c, max_area):
                result += "square" + " "
            elif check_horizontal_rect(matrix, x, y, r, c, max_area):
                result += "horizontal rectangle" + " "
            elif check_vertical_rect(matrix, x, y, r, c, max_area):
                result += "vertical rectangle" + " "
            else:
                result += "polygon" + " "

            location = find_location(x, y, r, c)

            return result,location


        variables_to_test = ["G", "M", "B", "N"]
        final_res={}
        for variable in variables_to_test:
            result,location = run_with_variable(variable,layout_data)
            final_res[variable] = {'shape': result, 'location': location}

        # Return the result as a JSON response
        response_data = final_res
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
