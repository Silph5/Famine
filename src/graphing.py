import matplotlib
matplotlib.use("Agg") #thread safe
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import numpy as np
import io

import Tos2Info

def drawFancyBar(ax, left, width, height, colour):
    bar = FancyBboxPatch((left, -height/2), width, height, boxstyle=f"round,pad=0,rounding_size=0.4", linewidth=0, facecolor=colour)
    ax.add_patch(bar)

def genStackedProgressBarRoleBased (roles, nums, totalNum):
    fig, ax = plt.subplots(figsize=(8, 0.5))

    drawFancyBar(ax, 0, 100, 1, "#2b2b2b")

    left = 0
    for role, num in zip(roles, nums):
        width = (num/totalNum) * 100
        colour = Tos2Info.getRoleColour(role)

        colour = f"#{colour:06X}" #pain because this func wasn't designed to return hex codes           

        drawFancyBar(ax, left, width, 1, colour)

        if width > 8:
            ax.text(left + width/2, 0, f"{int(width)}%", ha="center", va="center", fontsize=8, color="white", weight="bold")

        left += width


    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.5)
    ax.axis("off")

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=200, transparent=True)
    plt.close(fig)
    buffer.seek(0)

    return buffer
