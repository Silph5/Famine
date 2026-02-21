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

def differColours(coloursList):

    outList = []
    
    for col in range(len(coloursList)):
            
            colour = coloursList[col]
            
            recolourCount = 0
            while colour in outList:
                recolourCount += 1
                colour = changeColBrightness(colour, 1 + 0.35 * math.sin(recolourCount * 2.1))

            outList.append(colour)

    return outList

def genStackedProgressBarRoleBased (rolesList, numsList, maxNumsList, coloursList):

    differColours(coloursList)

    maxTotal = sum(maxNumsList)
    total = sum(numsList)
    
    fig = plt.figure(figsize=(8, 0.6))
    axRoles = fig.add_axes([0.05, 0.05, 0.9, 0.36])
    axOverview = fig.add_axes([0.05, 0.6, 0.9, 0.03])

    left = 0

    drawFancyBar(axOverview, 0, 100, 1, "#354f6c", 1)
    drawFancyBar(axOverview, 0, (total/maxTotal)*100, 1, "#2886f1", 1)

    axOverview.set_xlim(0, 100)
    axOverview.set_ylim(-0.5, 0.5)
    axOverview.axis("off")

    gapSize = 0.3
    usableWidth = 100 - gapSize * (len(rolesList) - 1)

    drawFancyBar(axRoles, 0, 100, 1, "#2b2b2b", 1)

    left = 0

    for b in range(len(rolesList)):

        width = (numsList[b]/maxTotal) * usableWidth
        widthRemaining = ((25/maxTotal)*usableWidth) - width        

        colour = f"#{coloursList[b]:06X}" #pain because this func wasn't designed to return hex codes           

        drawFancyBar(axRoles, left, width, 1, colour, 1)
        left += width

        drawFancyBar(axRoles, left, widthRemaining, 1, colour, 0.2)
        left += widthRemaining + gapSize


    axRoles.set_xlim(0, 100)
    axRoles.set_ylim(-0.5, 0.5)
    axRoles.axis("off")

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=200, transparent=True)
    plt.close(fig)
    buffer.seek(0)

    return buffer
