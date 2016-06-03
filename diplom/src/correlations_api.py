from matplotlib import rc, mlab
import numpy
import pylab
font = {'family': 'Verdana',
        'weight': 'normal'}
rc('font', **font)


def plot_theory_and_practice(x_list,
                             practice_list,
                             theory_list,
                             string_name,
                             picture_name):
    dx = x_list[1] - x_list[0]
    practice = pylab.bar(x_list, practice_list, width = 0.7 * dx, align = "center", color="gray")
    theory = pylab.plot(x_list, theory_list, color="black", linewidth = 3)
    ylim = pylab.ylim(0.0, pylab.ylim()[1] * 1.15)
    if string_name == r"p":
        xlabel_ = pylab.xlabel(r"$p/q_0$")
    else:
        xlabel_ = pylab.xlabel(r"$" +  string_name + r"$")
    ylabel_ = pylab.ylabel(r"$\rho_{" + string_name + r"} \left( " + string_name + r"\right)$")
    practice[0].set_label(u"Компьютерное вычисление")
    theory[0].set_label(u"Аналитическое выражение")

    xlabel_.set_size(20)
    ylabel_.set_rotation(1)
    ylabel_.set_size(20)
    ylabel_.set_horizontalalignment("right")
    #pylab.show()
    pylab.legend()
    pylab.savefig(picture_name + ".png", bbox_inches='tight')
    pylab.close()


def plot_distribution(*,
                      string_name,
                      calculate_function,
                      theory_function,
                      left_bound,
                      right_bound,
                      da,
                      N,
                      picture_name):
    a_list = numpy.array([left_bound + i * da
                          for i in range(int((right_bound - left_bound) / da) + 1)])
    dN_list = numpy.zeros(a_list.shape)
    for i in range(N):
        a = calculate_function()
        n = round((a - left_bound) / da)
        if 0 <= n < len(dN_list):
            dN_list[n] += 1
    dN_list[0] *= 2
   
    rho_a_practice = dN_list / (da * N)
    rho_a_theory = numpy.array([theory_function(a) for a in a_list])
    plot_theory_and_practice(a_list, rho_a_practice, rho_a_theory, string_name, picture_name + "_" + str(N))
