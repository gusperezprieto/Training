COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def label(colors):
    
    ohms = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10**COLORS.index(colors[2])

    label = " ohms"
    if ohms//1000 > 0:
        ohms //= 1000
        label = " kiloohms"
    if ohms//1000 > 0:
        ohms //= 1000
        label = " megaohms"
    if ohms//1000 > 0:
        ohms //= 1000
        label = " gigaohms"

    return str(ohms) + label
