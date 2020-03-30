from IPython.display import Video


class GoodMorning:

    REESE = "/Users/good_morning_reese.mp4"

    def play_video(self):
        """Play video in Jupyter notdbook"""

        return Video(data=GoodMorning.REESE, embed=True)
