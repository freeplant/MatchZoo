from pathlib import Path

USER_DIR = Path.expanduser(Path('~')).joinpath('.matchzoo')
if not USER_DIR.exists():
    USER_DIR.mkdir()
USER_DATA_DIR = USER_DIR.joinpath('datasets')
if not USER_DATA_DIR.exists():
    USER_DATA_DIR.mkdir()
USER_TUNED_MODELS_DIR = USER_DIR.joinpath('tuned_models')

from .logger import logger
from .version import __version__

from .utils import *
from . import processor_units
from .processor_units import chain_transform, ProcessorUnit

from .data_pack import DataPack
from .data_pack import pack
from .data_pack import load_data_pack
from .data_pack import build_unit_from_data_pack
from .data_pack import build_vocab_unit

from . import data_generator
from .data_generator import DataGenerator

from . import tasks
from . import metrics
from . import losses
from . import engine
from . import preprocessors
from . import models
from . import embedding
from . import datasets
from . import layers
from . import contrib

from .engine import hyper_spaces
from .engine import load_model
from .engine import load_preprocessor
from .engine import callbacks

from .embedding import Embedding

from . import auto
from .auto import tuner
from .auto import ZooKeeper
from .auto import Tuner
