from .logger_addons import LoggerAddons

class GeoToolsCore(LoggerAddons):

    def __init__(self, logger_dir):
        super().__init__(logger_dir=logger_dir)
        self.info_title(self.__class__.__name__)