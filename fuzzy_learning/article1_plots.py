import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.fuzzy_clause import FuzzyClause
from fuzzy_system.type1_fuzzy_set import Type1FuzzySet


def plot_art1_fig1():
    rc('text', usetex=True)

    x = np.arange(0,20,0.0001)
    y = np.logical_and(x>=4, x<=12)*1

    plt.plot(x,y)
    plt.title('Indicator function plot of values $A = 12\leq x \leq 4$')
    plt.grid(True, which='both', alpha=0.4)
    plt.xlabel('x')
    plt.ylabel('$1_A(x)$')


    plt.show()

def plot_art1_fig2():
    rc('text', usetex=True)

    x = np.arange(0,20,0.0001)
    a = np.logical_and(x>=4, x<=12)*1
    b = np.logical_and(x>=10, x<=15)*1

    fig, axs = plt.subplots(4,2)
    # fig.suptitle('Set Operations')

    fig.tight_layout(pad=1.0)
    axs[-1, -1].axis('off')
    axs[-2, -1].axis('off')


    axs[0,0].plot(x,a)
    axs[0,0].set_title('Indicator function plot of values $A = 12\leq x \leq 4$')
    axs[0,0].grid(True, which='both', alpha=0.4)
    axs[0,0].set(xlabel='x', ylabel='$1_A(x)$')

    axs[1,0].plot(x,b, 'tab:orange')
    axs[1,0].set_title('Indicator function plot of values $B = 15\leq x \leq 10$')
    axs[1,0].grid(True, which='both', alpha=0.4)
    axs[1,0].set(xlabel='x', ylabel='$1_B(x)$')


    axs[0,1].plot(x,1-a)
    axs[0,1].set_title('Indicator function plot of values $ \overline{A}$')
    axs[0,1].grid(True, which='both', alpha=0.4)
    axs[0,1].set(xlabel='x', ylabel='$1_{\overline{A}}(x)$')

    axs[1,1].plot(x,1-b, 'tab:orange')
    axs[1,1].set_title('Indicator function plot of values $ \overline{B}$')
    axs[1,1].grid(True, which='both', alpha=0.4)
    axs[1,1].set(xlabel='x', ylabel='$1_{\overline{B}}(x)$')

    axs[2,0].plot(x, np.maximum(a,b), 'tab:green')
    axs[2,0].set_title('Indicator function plot of values $ A \cap B$')
    axs[2,0].grid(True, which='both', alpha=0.4)
    axs[2,0].set(xlabel='x', ylabel='$1_{A \cap B}(x)$')

    axs[3,0].plot(x,a*b, 'tab:green')
    axs[3,0].set_title('Indicator function plot of values $ A \cup B$')
    axs[3,0].grid(True, which='both', alpha=0.4)
    axs[3,0].set(xlabel='x', ylabel='$1_{A \cup B}(x)$')


    plt.show()

def plot_art1_fig3():
    
    x1 = Type1FuzzyVariable(0, 100, 100, 'x1')
    x1.add_triangular('v_cold', 0, 0, 25)
    x1.add_triangular('cold', 0, 25, 50)
    x1.add_triangular('medium', 25, 50, 75)
    x1.add_triangular('hot', 50, 75, 100)
    x1.add_triangular('v_hot', 75, 100, 100)

    x1.plot_variable()


def plot_art1_fig6():
    rc('text', usetex=True)


    a = Type1FuzzySet.create_triangular(0, 10, 1000, 2, 4, 6, 'A')
    b = Type1FuzzySet.create_triangular(0, 10, 1000, 4, 6, 8, 'B')
    
    u = a.union(b)
    u._name = '$A \cup B$'
    i = a.intersection(b)
    i._name = '$A \cap B$'

    c_a = a.complement()
    c_a._name = '$\overline{A}$'

    c_b = b.complement()
    c_b._name = '$\overline{B}$'

    fig, axs = plt.subplots(4,2)
    fig.tight_layout(pad=1.0)
    axs[-1, -1].axis('off')
    axs[-2, -1].axis('off')

    a.plot_set(axs[0,0])
    b.plot_set(axs[1,0])

    c_a.plot_set(axs[0,1], 'tab:orange')
    c_a.plot_set(axs[1,1], 'tab:orange')

    u.plot_set(axs[2,0], 'tab:green')
    i.plot_set(axs[3,0], 'tab:green')


    plt.show()

if __name__ == "__main__":
    # plot_art1_fig3()
    plot_art1_fig6()
    pass