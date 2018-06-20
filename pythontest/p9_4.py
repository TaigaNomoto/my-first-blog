import matplotlib.pyplot as plt

steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.title('Number of steps walked(by )')
plt.pie(steps, labels=labels, autopct=make_autopct(steps),
        startangle=90, wedgeprops={'linewidth': 2,'edgecolor':"white"})
plt.axis('equal')

plt.grid()
plt.show()
