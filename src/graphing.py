import matplotlib
matplotlib.use("Agg") #thread safe
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import math
import io

import Tos2Info

def drawFancyBar(ax, left, width, height, colour, alpha):
    bar = FancyBboxPatch((left, -height/2), width, height, boxstyle=f"round,pad=0,rounding_size=0.5", linewidth=0, facecolor=colour, alpha=alpha)
    ax.add_patch(bar)

def changeColBrightness (colour, changeFactor):
    r = (colour >> 16) & 0xFF
    g = (colour >> 8) & 0xFF
    b = (colour) &0xFF

    r = min(255, max(0, int(r*changeFactor)))
    g = min(255, max(0, int(g*changeFactor)))
    b = min(255, max(0, int(b*changeFactor)))

    return (r << 16) | (g << 8) | b

def genStackedProgressBarRoleBased (roles, nums, totalNum):
    fig, ax = plt.subplots(figsize=(8, 0.5))

    gapSize = 0.3
    usableWidth = 100 - gapSize * (len(roles) - 1)

    drawFancyBar(ax, 0, 100, 1, "#2b2b2b", 1)

    left = 0

    coloursUsed = []

    for role, num in zip(roles, nums):
        width = (num/totalNum) * usableWidth
        widthRemaining = ((25/totalNum)*usableWidth) - width

        colour = Tos2Info.getRoleColour(role)

        recolourCount = 0
        while colour in coloursUsed:
            recolourCount += 1
            
            colour = changeColBrightness(colour, 1 + 0.6 * math.sin(recolourCount * 2.1))
            print(colour)

        coloursUsed.append(colour)

        colour = f"#{colour:06X}" #pain because this func wasn't designed to return hex codes           

        drawFancyBar(ax, left, width, 1, colour, 1)
        left += width

        drawFancyBar(ax, left, widthRemaining, 1, colour, 0.2)
        left += widthRemaining + gapSize


    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.5)
    ax.axis("off")

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=200, transparent=True)
    plt.close(fig)
    buffer.seek(0)

    return buffer
