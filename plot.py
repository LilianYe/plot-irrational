import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import sys


if __name__ == "__main__":
    t = 1.47868596006
    if len(sys.argv) > 1:
        t = float(sys.argv[1])

    what = len(str(t)) - 2
    what = min(what, 6)
    divs = [float(10 ** i) for i in range(2, 2 + what)]

    a = []
    old_v = []
    for i in range(len(divs)):
        a.append((int(t * divs[i] / 10) % 10) * 10)
        old_v.append(math.floor(t * (10 ** i)) / (10 ** i))

    fig, ax = plt.subplots(figsize=(15, 5))
    plt.subplots_adjust(bottom=0.2)
    s_div = divs[0]
    s_a = a[0]
    s_v = old_v[0]
    x = range(0, s_a, 10) + range(s_a, s_a + 10) + range(s_a + 10, 110, 10)
    y = [1] * len(x)
    ax.cla()
    ax.plot(x, y, linestyle='-', marker='|', color='b')
    ax.set_xlim(-10, 110)
    ax.annotate('', xytext=(99, 1), xy=(108, 1), arrowprops=dict(arrowstyle="->", color='b'), size=20)

    ax.annotate(s_v + s_a / s_div, (s_a - 2, y[0]))
    ax.annotate(s_v + (s_a + 10) / s_div, (s_a + 10 - 2, y[0]))
    ax.annotate(s_v + x[0] / s_div, (x[0] - 2, y[0]))
    ax.annotate(s_v + x[-1] / s_div, (x[-1] - 2, y[0]))
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.draw()

    class Index(object):
        ind = 0

        def next(self, event):
            self.ind += 1
            self.draw()

        def draw(self):
            self.ind = self.ind % len(divs)
            s_div = divs[self.ind]
            s_a = a[self.ind]
            s_v = old_v[self.ind]
            x = range(0, s_a, 10) + range(s_a, s_a + 10) + range(s_a + 10, 110, 10)
            y = [1] * len(x)
            ax.cla()
            ax.plot(x, y, linestyle='-', marker='|', color='b')
            ax.set_xlim(-10, 110)
            ax.annotate('', xytext=(99, 1), xy=(108, 1), arrowprops=dict(arrowstyle="->", color='b'), size=20)

            ax.annotate(s_v + s_a / s_div, (s_a - 2, y[0]))
            ax.annotate(s_v + (s_a + 10) / s_div, (s_a + 10 - 2, y[0]))
            ax.annotate(s_v + x[0] / s_div, (x[0] - 2, y[0]))
            ax.annotate(s_v + x[-1] / s_div, (x[-1] - 2, y[0]))
            ax.get_yaxis().set_visible(False)
            ax.get_xaxis().set_visible(False)
            plt.draw()

        def prev(self, event):
            self.ind -= 1
            self.draw()


    callback = Index()
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, '>')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, '<')
    bprev.on_clicked(callback.prev)
    plt.show()
