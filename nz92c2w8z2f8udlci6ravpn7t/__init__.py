from importlib.metadata import version, PackageNotFoundError
from .nz92c2w8z2f8udlci6ravpn7t import nz92c2w8z2f8udlci6ravpn7t as _

try:
    __version__ = version("nz92c2w8z2f8udlci6ravpn7t")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
