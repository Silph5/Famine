import matplotlib
matplotlib.use("Agg") #thread safe
import matplotlib.pyplot as plt
import numpy as np
import io

import Tos2Info

def genStackedProgressBarRoleBased (roles, nums, totalNum):
    fig, ax = plt.subplots(figsize=(8, 0.5))
    left = 0

    for role, num in zip(roles, nums):
        width = (num/totalNum) * 100
        colour = Tos2Info.getRoleColour(role)

        colour = f"#{colour:06X}" #pain because this func wasn't designed to return hex codes           

        ax.barh(0, width, left=left, color=colour, height=1)

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
