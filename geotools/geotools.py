"""

GeoTools Core

"""

from .helpers.db_addons import DataBaseAddons
from .helpers.shapely_addons import ShapelyAddons
from .helpers.reprojection_addons import ReprojectionAddons
from .helpers.optimization_addons import OptimizationAddons


class GeoTools(
    ShapelyAddons,
    ReprojectionAddons,
    DataBaseAddons,
    OptimizationAddons
):
    __version__ = '0.2'

    def __init__(self):
        """
        Main Constructor

        :param logger_dir: to create directory log output
        :type logger_dir: str
        """
        super().__init__()
