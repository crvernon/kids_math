import pkg_resources

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

from IPython import display


# class ImageQueue:
#
#     # https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRecycling_symbol&psig=AOvVaw2GNY83bu2O5H-QsZthasM5&ust=1585754401094000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIiP8s-BxegCFQAAAAAdAAAAABAG
#     RECYCLE = pkg_resources.resource_filename('kids_math', '/img/recycle.png')
#
#     # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.playprelude.com%2Fthe-star-enduring-symbol-of-excellence%2F&psig=AOvVaw1LADueQERSmgmCS2yccUr1&ust=1585755157140000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLCQsLqExegCFQAAAAAdAAAAABAD
#     STAR = pkg_resources.resource_filename('kids_math', '/img/star.jpeg')
#
#     # https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngimage.net%2Frectangle-black-png-2%2F&psig=AOvVaw1B-XrUOJkruAPEbWn0OKp9&ust=1585755215178000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODOs9qExegCFQAAAAAdAAAAABAH
#     RECTANGLE = pkg_resources.resource_filename('kids_math', '/img/rectangle.png')
#
#     # https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FConcave_polygon&psig=AOvVaw1eDb0BuktqWcCHy76p-IXK&ust=1585755302231000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKiz4IOFxegCFQAAAAAdAAAAABAD
#     CONCAVE_POLYGON = pkg_resources.resource_filename('kids_math', '/img/concave_polygon.png')
#
#     # https://www.google.com/url?sa=i&url=https%3A%2F%2Fetc.usf.edu%2Fclipart%2F42600%2F42616%2Firreghept_42616.htm&psig=AOvVaw0zPqcjZVCB3_DadMrAASSA&ust=1585755383000000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMDM46iFxegCFQAAAAAdAAAAABAI
#     IRREGULAR_POLYGON = pkg_resources.resource_filename('kids_math', '/img/irregular_polygon.gif')
#
#     @staticmethod
#     def display_img(img):
#         """Display image
#
#         :param img:                             string; Full path with file name and extension to the desired image
#
#         """
#         with open(img, 'rb') as f:
#             return display.Image(data=f.read(), format='png')


class RabbitImg:

    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F559783428674901803%2F&psig=AOvVaw2_nraiVWQeMHhkEa2IR3K3&ust=1585677594411000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDxnsLjwugCFQAAAAAdAAAAABAO
    RUNNING = pkg_resources.resource_filename('kids_math', '/img/rabbit_running.jpeg')

    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fthenounproject.com%2Fterm%2Frabbit%2F29549%2F&psig=AOvVaw2_nraiVWQeMHhkEa2IR3K3&ust=1585677594411000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDxnsLjwugCFQAAAAAdAAAAABAa
    SITTING = pkg_resources.resource_filename('kids_math', '/img/rabbit_sitting.png')

    def display_img(self):
        """Fill in."""
        pass

