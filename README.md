# minigpt4

This is a simplified version of MiniGPT-4 that can be used much more easily than the official repo.

It's a better starting point for people trying to integrate MiniGPT-4 into their own hobby projects.  May require some tweaking to get it to work with your specific use case, but it should be much easier than starting from scratch.

Designed to be integrated into https://github.com/catid/aiwebcam

## Setup

This is designed to run on an Ubuntu Linux server with an RTX 4090 installed.  It should also work with an RTX 3090 or maybe even an RTX 3080, but I haven't tested these other options.

```bash
conda create -n minigpt4 python=3.10

sudo apt install git-lfs

git clone https://github.com/catid/minigpt4
cd minigpt4

git lfs install
git submodule update --init --recursive

pip install -r requirements.txt
```

## Example Usage

```bash
conda activate minigpt4
python example.py
```
