def noisy_line(m, b, x):
    return m * x + b + 0.5 * (random() - 0.5)

slope = 1.0
intercept = -0.5
x_coords = [random() for t in range(50)]
y_coords = [noisy_line(slope, intercept, x) for x in x_coords]
sp = scatter_plot(zip(x_coords, y_coords))
sp += line([(0.0, intercept), (1.0, slope+intercept)], color='red')
sp.show()
# Use list_plot to visualize digital signals
# Undersampling and oversampling a cosine signal
sample_times_1 = srange(0, 6*pi, 4*pi/5)
sample_times_2 = srange(0, 6*pi, pi/3)
data1 = [cos(t) for t in sample_times_1]
data2 = [cos(t) for t in sample_times_2]

plot1 = list_plot(zip(sample_times_1, data1), color='blue')
plot1.axes_range(0, 18, -1, 1)
plot1 += text("Undersampled", (9, 1.1), color='blue', fontsize=12)
plot2 = list_plot(zip(sample_times_2, data2), color='red')
plot2.axes_range(0, 18, -1, 1)
plot2 += text("Oversampled", (9, 1.1), color='red', fontsize=12)

g = graphics_array([plot1, plot2], 2, 1) # 2 rows, 1 column
g.show(gridlines=["minor", False])
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(-2 * numpy.pi, 2 * numpy.pi, 0.1)
func1 = numpy.sin(x)
func2 = numpy.cos(x)

plt.figure(figsize=(5.5, 3.7)) # size in inches
plt.plot(x, func1, linewidth=2.0, color=(0.5, 1,0),
label='$f(x)=sin(x)$')
plt.plot(x, func2, linewidth=3.0, color='purple', alpha=0.5,
label='$f(x)=cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('Plotting with matplotlib')
plt.legend(loc='lower left')
plt.savefig('demo1.png')
plt.close()
