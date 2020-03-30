from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

from IPython import display
from pathlib import Path


def peter_rabbit_winking():
    """
    Source:  https://tenor.com/search/peter-rabbit-gifs

    """

    gif = Path("/Users/d3y010/Desktop/tenor.gif")

    # Display GIF in Jupyter, CoLab, IPython
    with open(gif,'rb') as f:

        display.Image(data=f.read(), format='png')
