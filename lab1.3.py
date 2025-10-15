def draw_function():
    width = 21
    height = 21
    x_min , x_max = -10 , 10
    y_min , y_max = -20 , 20



    for screen_y in range(height):
        line = ""
        math_y = y_max - (screen_y * (y_max - y_min))//(height-1)
        for screen_x in range(width):
            math_x = x_min +(screen_x *(x_max - x_min))//(width -1)

            y = math_x * 2

            if abs(y - math_y)<2:

                line += "*"
            else :
                line += " "
        print(line)



if __name__ =="__main__":
    draw_function()