# Text to Speech (TTS) for ComfyUI

# Description

## What This Is
ComfyUI-TTS is a tool that allows you to convert strings within ComfyUI to audio so you can hear what's written.  My objective with this one was to be able to use it with LLM AI models, but I wanted to leave the door open for way more other uses.

## Where This Fits
- TTS is "text to speech", which converts the written word to sound you can hear.  It does not
do the other thing, converting audio to text.
- Piper-tts was the first TTS program I chose to implement because it's meant to be easy to do so.  The feature set is less complete, but it works simple and easy.
- ONNX models are used by Piper-tts, along with a JSON file which should be named the same as the onnx, but with a .json extension.  I noticed some of the downloadables are not this way, and it's up to you to fix that (sorry)
- [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) lets us use Stable Diffusion using a flow graph layout.

## Why I Made This
- I wanted to integrate text generation and image generation AI in one interface and see what other people can come up with to use them.  TTS is just one aspect of being able to use text generation.

## Features:
- Currently let's you load ONNX models in a consistent fashion with other ComfyUI models and can use them to generate audio output from text.

## Upcoming Features:
- Intend to expand the Piper-tts function options
- Then going to start working on implementing basic XTTSv2

# Installation

## What you need first:
- [Python](https://github.com/python)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Highly Recommended
- [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

## Steps if using Comfy Manager:
1. Visit your Install Custom Nodes page, and search for ComfyUI-TTS.
2. Hit Install and restart when prompted.
3. Copy your ONNX and JSON files into ```./ComfyUI/custom_nodes/ComfyUI-TTS/models/*```
4. Hit Ctrl+F5 to hard reload the browser window.
5. The nodes should be in the TTS menu.

## Steps if installing manually:
1. Clone this repo into `custom_nodes` folder.
2. Install [piper-tts](https://github.com/rhasspy/piper) using the python methods!
3. Copy your ONNX and JSON files into ```./ComfyUI/custom_nodes/ComfyUI-TTS/models/*```
4. Hit Ctrl+F5 to hard reload the browser window.
5. The nodes should be in the TTS menu.

## If you can't install:
Either post an issue on github, or ask [on Element in Comfy's channel](https://matrix.to/#/#comfyui:matrix.org)

# Usage

## Instructions:
1. Download ONNX and JSON files for the models, which can be found [here](https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0). You will need at least 1. Different models produce different results.

2. Ensure the JSON file is named identically to the ONNX, but with `.json` appended.

3. Place models in ```ComfyUI/custom_nodes/ComfyUI-TTS/models```. They can be renamed if you want.

3. Fire up/Restart ComfyUI and allow it to finish restarting.

4. Hit Ctrl+F5 to ensure the browser is refreshed.

5. Check your ComfyUI available nodes and find the TTS menu.

6. Load TTS Model

7. Call Speak Text

## If you get errors:
Either post an issue on github, or ask [on Element in Comfy's channel](https://matrix.to/#/#comfyui:matrix.org)

## Examples

![image](https://github.com/daniel-lewis-ab/ComfyUI-TTS/blob/main/example1.png)

# For Possible Contributors

## Known Issues
- This is a very recent release.  Only basic functionality is probable.

# Conclusion

We appreciate your interest in TTS for ComfyUI. Feel free to explore and provide feedback or report any issues you encounter. Your contributions and suggestions are valuable to the project.




