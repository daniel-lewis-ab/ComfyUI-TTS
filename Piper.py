
import sys
import os
import folder_paths
from typing import List
from .logger import logger


# Folder path and venv
piper_dir = os.path.dirname(os.path.realpath(__file__))
venv_site_packages = os.path.join(folder_paths.base_path, 'venv', 'Lib', 'site-packages')
sys.path.append(venv_site_packages)


# Attempt to get piper-tts if it doesn't exist
try:
    from piper import voice
except ImportError:

    logger.warn("Unable to find piper-tts, attempting to fix.")
    # Determine the correct path based on the operating system
    if os.name == 'posix':
        site_packages = os.path.join(sys.prefix, 'lib', 'python{}.{}/site-packages'.format(sys.version_info.major, sys.version_info.minor))
    else:  # For Windows
        site_packages = os.path.join(sys.prefix, 'Lib', 'site-packages')

    sys.path.append(site_packages)
    try:
        from piper import voice
        logger.info("Successfully acquired piper-tts.")
    except ImportError:
        logger.exception("Nope.  Actually unable to find piper-tts.")

# Inject 'llm' to folder_paths ourselves, so we can use it like we belong there and have behavioral consistency
supported_file_extensions = set(['.onnx'])
models_dir = os.path.join(piper_dir, "models")
folder_paths.folder_names_and_paths["tts"] = ([models_dir], supported_file_extensions)


class Load_Piper_Model:
    """
    Load a piper-tts model by name.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Model": (folder_paths.get_filename_list("tts"), ), 
            },
        }

    # ComfyUI will effectively return the Llama class instanciation provided by execute() and call it an LLM
    RETURN_TYPES = ("TTS",)
    FUNCTION = "execute"
    CATEGORY = "TTS"

    def execute(self, Model:str):

        # basically just calls __init__ on the Llama class
        model_path = folder_paths.get_full_path("tts", Model)

        try:
            tts = PiperVoice.load(
                model_path=model_path
            )

        except ValueError:
            logger.exception("The model path does not exist.  Perhaps hit Ctrl+F5 and try reloading it.")

        return (tts,)


class Piper_Speak_Text:
    """
    Use a piper-tts PiperVoice object to speak text
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TTS":("TTS", ), 
                "text":("STRING", {"default":"", "forceInput":True,}),
            },
        }

    # ComfyUI will effectively return the Llama class instanciation provided by execute() and call it an LLM
    RETURN_TYPES = ()
    FUNCTION = "execute"
    CATEGORY = "TTS"
    OUTPUT_NODE = True

    def execute(self, TTS, text:str):

        tts = TTS.synthesize_stream_raw(text)

        return ()


NODE_CLASS_MAPPINGS = {
    "Load_Piper_Model": Load_Piper_Model,
    "Piper_Speak_Text": Piper_Speak_Text,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Load_Piper_Model": "Load Piper Model",
    "Piper_Speak_Text": "Piper Speak Text",
}


