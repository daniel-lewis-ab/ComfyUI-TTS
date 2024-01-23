
import sys
import os
import folder_paths
from typing import List
from .logger import logger


# Folder path and venv
piper_dir = os.path.dirname(os.path.realpath(__file__))
venv_site_packages = os.path.join(folder_paths.base_path, 'venv', 'Lib', 'site-packages')
sys.path.append(venv_site_packages)


# Attempt to get llama_cpp if it doesn't exist
try:
    from piper import Piper
except ImportError:

    logger.warn("Unable to find piper-tts, attempting to fix.")
    # Determine the correct path based on the operating system
    if os.name == 'posix':
        site_packages = os.path.join(sys.prefix, 'lib', 'python{}.{}/site-packages'.format(sys.version_info.major, sys.version_info.minor))
    else:  # For Windows
        site_packages = os.path.join(sys.prefix, 'Lib', 'site-packages')

    sys.path.append(site_packages)
    try:
        from piper import Piper
        logger.info("Successfully acquired piper-tts.")
    except ImportError:
        logger.exception("Nope.  Actually unable to find piper-tts.")


NODE_CLASS_MAPPINGS = {
}

NODE_DISPLAY_NAME_MAPPINGS = {
}


