import pkg_resources


class RabbitImg:

    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F559783428674901803%2F&psig=AOvVaw2_nraiVWQeMHhkEa2IR3K3&ust=1585677594411000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDxnsLjwugCFQAAAAAdAAAAABAO
    RUNNING = pkg_resources.resource_filename('kids_math', '/img/rabbit_running.jpeg')

    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fthenounproject.com%2Fterm%2Frabbit%2F29549%2F&psig=AOvVaw2_nraiVWQeMHhkEa2IR3K3&ust=1585677594411000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDxnsLjwugCFQAAAAAdAAAAABAa
    SITTING = pkg_resources.resource_filename('kids_math', '/img/rabbit_sitting.png')

    def display_img(self):
        """Fill in."""
        pass
