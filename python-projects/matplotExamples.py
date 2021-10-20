import matplotlib.pyplot as plt
import numpy as np


def example_1():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    save(fname="asd")


def example_2():
    fig = plt.figure()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots(2, 2)
    plt.show()


def example_3():
    x = np.linspace(0, 2, 100)
    fig, axis = plt.subplots()
    axis.plot(x, x, label="linear")
    axis.plot(x, x ** 2, label="quadratic")
    axis.plot(x, x ** 3, label="cubic")
    axis.set_title("Simple plot")
    axis.set_xlabel("X linear")
    axis.set_ylabel("Y linear")
    axis.legend()
    plt.show()


def example_4():
    x = np.asarray([0, 60])
    y = x * 3
    fig, axis = plt.subplots()
    axis.plot(x, y, label='linear')
    axis.set_title('Draw a line')
    axis.set_xlabel('x - axis')
    axis.set_ylabel('y - axis')
    axis.legend()
    plt.show()


def example_5():
    x = np.asarray([1, 2, 3])
    y = np.asarray([2, 4, 0])
    fig, axis = plt.subplots()
    axis.plot(x, y, label='linear')
    axis.set_title('Sample graph!')
    axis.set_xlabel('x - axis')
    axis.set_ylabel('y - axis')
    axis.legend()
    plt.show()


def writeFile():
    with open('coord.txt', 'w') as file:
        file.write('Title:Graph!!!\n')
        file.write('x:x label\n')
        file.write('y:y label\n')
        file.write('0 1\n')
        file.write('8 7\n')
        file.write('3 5\n')
        file.write('12 17\n')
        file.write('5 11\n')


def readFile(fileName: str):
    ret = {}
    with open(fileName, 'r') as file:
        i = 0
        for line in file:
            line=line.rstrip('\n')
            parts=[]
            if line.find(':') != -1:
                parts = line.split(':')
            else:
                parts = line.split(' ')
            print('line:',line)
            print('parts:',parts)
            if len(parts) == 2:
                if parts[0] == 'Title':
                    ret['title'] = parts[1]
                if parts[0] == 'x':
                    ret['x'] = parts[1]
                if parts[0] == 'y':
                    ret['y'] = parts[1]
                if parts[0].isnumeric() and parts[1].isnumeric():
                    ret[i] = (int(parts[0]), int(parts[1]))
                    i = i + 1
        ret['n'] = i
    return ret


def example_6():
    data = readFile('coord.txt')
    print(data)
    x = [value[0] for (key, value) in data.items() if type(key) == int]
    y = [value[1] for (key, value) in data.items() if type(key) == int]
    fig, axis = plt.subplots()
    axis.plot(x, y, label='linear')
    axis.set_title(data['title'])
    axis.set_xlabel(data['x'])
    axis.set_ylabel(data['y'])
    axis.legend()
    plt.show()


def save(file_name):
    plt.savefig(fname=file_name)


# Main
example_6()
