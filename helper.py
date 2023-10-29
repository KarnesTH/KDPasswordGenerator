import os
import json


class Paths():
    base = os.path.dirname(__file__)
    images = os.path.join(base, "data/images")
    icons = os.path.join(images, "icons")
    datas = os.path.join(base, "data")

    # File loaders.
    @classmethod
    def icon(cls, filename):
        return os.path.join(cls.icons, filename)

    @classmethod
    def image(cls, filname):
        return os.path.join(cls.images, filname)

    @classmethod
    def data(cls, filename):
        return os.path.join(cls.datas, filename)


class Locations():
    @classmethod
    def getData(cls, locale):
        data = json.load(
            open(Paths.data("./locale/" + locale + ".json"), "r", encoding="utf-8"))

        return data
