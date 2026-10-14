
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
        x,y=(
             x+h*f_x(x,y),
             y+h*f_y(x,y)

        )
        t=t+h
        t_values.append(t)
        x_values.append(x)
        y_values.append(y)


    plt.plot(t_values, x_values, label="Prey (Rabbit - x)")
    plt.plot(t_values, y_values, label="Predator (Wolf - y)")
    plt.xlabel("Time (t)")
    plt.ylabel("Population")
    plt.title("Lotka-Volterra - Euler Method")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()