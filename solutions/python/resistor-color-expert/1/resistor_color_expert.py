COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
TOLERANCE = {"grey":"0.05%","violet":"0.1%","blue":"0.25%","green":"0.5%","brown":"1%","red":"2%","gold":"5%","silve":"10%"}

def resistor_label(colors):

    def format_number(num):
        # Convert to string, strip trailing zeros and dot if needed
        s = ('%f' % num).rstrip('0').rstrip('.')
        return s

    if len(colors) == 1:
        return str(COLORS.index(colors[0])) + " ohms"

    ohms = 0

    for index in range(0, len(colors)-2):
        ohms *= 10
        ohms += COLORS.index(colors[index])

    ohms *= 10**COLORS.index(colors[-2])
    

    modifier = ""
    if ohms >= 1000:
        ohms /= 1000
        modifier = "kilo"
    if  ohms >= 1000 > 0:
        ohms /= 1000
        modifier = "mega"
    if  ohms >= 1000 > 0:
        ohms /= 1000
        modifier = "giga"

    return f"{str(format_number(ohms))} {modifier}ohms ±{TOLERANCE[colors[-1]]}"
