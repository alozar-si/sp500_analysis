import matplotlib.pyplot as plt

def candlesticks(ax, quotes, width=0.2, colorup='g', colordown='r', 
                 ochl=False, linewidth=1):
    lines = []
    openlines = []
    closelines = []
    for q in quotes:
        if ochl:
            t, open, close, high, low = q[:5]
        else:
            t, open, high, low, close = q[:5]

        if close >= open:
            color = colorup
        else:
            color = colordown

        vlineup = plt.Line2D(xdata=(t,t), ydata=(max(close, open), high), color='k', linewidth=linewidth, antialiased=True)
        vlinedown = plt.Line2D(xdata=(t,t), ydata=(low, min(close, open)), color='k', linewidth=linewidth, antialiased=True)
        
        lines.append(vlineup)
        lines.append(vlinedown)
        bar = ax.bar(t, max(close, open) - min(close, open), bottom=min(close, open), width=0.8, align='center', color=color)

        ax.add_line(vlineup)
        ax.add_line(vlinedown)
        #ax.add_line(bar)
    ax.autoscale_view()
    ax.set_ylabel("Price", fontsize=14)
    ax.set_xlabel("Date", fontsize=14)
    ax.grid(True)


    return lines, openlines, closelines