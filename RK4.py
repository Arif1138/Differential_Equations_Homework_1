import matplotlib.pyplot as plt


def f_x(x,y):
    return x-x*y


def f_y(x,y):
    return x*y-y


def main():
    x = 4
    y = 0.2
    t = 0.0
    h = 0.01

    t_values = [t]
    x_values = [x]
    y_values = [y]


    while t < 40:
        k_1=f_x(x,y)
        l_1=f_y(x,y)

        k_2 = f_x(x+k_1*h/2,y+l_1*h/2)
        l_2 = f_y(x+k_1*h/2,y+l_1*h/2)

        k_3 = f_x(x+k_2*h/2,y+l_2*h/2)
        l_3 = f_y(x+k_2*h/2,y+l_2*h/2)

        k_4 = f_x(x+h*k_3,y+h*l_3)
        l_4 = f_y(x+h*k_3,y+h*l_3)

        x,y=(
            x+(h/6)*(k_1+2*k_2+2*k_3+k_4),
            y+(h/6)*(l_1+2*l_2+2*l_3+l_4)

        )
        t+=h
        t_values.append(t)
        x_values.append(x)
        y_values.append(y)



    plt.plot(t_values, x_values, label="Rabbit (x)")
    plt.plot(t_values, y_values, label="Wolf (y)")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("RK4")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()