import pkg_resources

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

from IPython import display


class PeterRabbitGif:

    # Source:  https://tenor.com/view/smile-wink-peter-rabbit-peter-rabbit-gifs-gif-11787571
    WINKING = pkg_resources.resource_filename('kids_math', 'img/peter_rabbit_winking.gif')

    # Source:  https://tenor.com/view/no-nope-dont-beg-peter-rabbit-gif-11782011
    NOPE = pkg_resources.resource_filename('kids_math', 'img/peter_rabbit_no.gif')

    @staticmethod
    def display_gif(gif):
        """Display GIF in a Jupyter, CoLab, or IPython Notebook"""

        with open(gif, 'rb') as f:

            return display.Image(data=f.read(), format='png')

    def wink(self):
        """Display Peter Rabbit winking GIF"""

        return self.display_gif(PeterRabbitGif.WINKING)

    def nope(self):
        """Display Peter Rabbit saying no GIF"""

        return self.display_gif(PeterRabbitGif.NOPE)


class FrozenGif:

    # Source:  https://tenor.com/view/disney-princess-its-me-frozen-elsa-gif-15403239
    ELSA_WALKING = pkg_resources.resource_filename('kids_math', 'img/frozen_walking.gif')

    # Source:  https://media.tenor.com/images/69d62f9ebd55c45d08ab6af501cbfa47/tenor.gif
    OLAF_HEART = pkg_resources.resource_filename('kids_math', 'img/frozen_olaf_heart.gif')

    @staticmethod
    def display_gif(gif):
        """Display GIF in a Jupyter, CoLab, or IPython Notebook"""

        with open(gif, 'rb') as f:

            return display.Image(data=f.read(), format='png')

    def walking(self):
        """Display Peter Rabbit winking GIF"""

        return self.display_gif(FrozenGif.ELSA_WALKING)

    def olaf_heart(self):
        """Display Peter Rabbit saying no GIF"""

        return self.display_gif(FrozenGif.OLAF_HEART)


class RapunzelGif:

    # Source:  https://media.giphy.com/media/14rbfgZ6aTgwAo/giphy.gif
    SWINGING = pkg_resources.resource_filename('kids_math', 'img/rapunzel_swinging.gif')

    @staticmethod
    def display_gif(gif):
        """Display GIF in a Jupyter, CoLab, or IPython Notebook"""

        with open(gif, 'rb') as f:

            return display.Image(data=f.read(), format='png')

    def swinging(self):
        """Display Peter Rabbit winking GIF"""

        return self.display_gif(RapunzelGif.SWINGING)
