# minigpt4

This is a simplified version of MiniGPT-4 that can be used much more easily than the official repo.

Official MiniGPT-4 repo here: https://minigpt-4.github.io/

It's a better starting point for people trying to integrate MiniGPT-4 into their own hobby projects.  May require some tweaking to get it to work with your specific use case, but it should be much easier than starting from scratch.

Designed to be integrated into https://github.com/catid/aiwebcam

## Setup

This is designed to run on an Ubuntu Linux server with an RTX 4090 installed.  Please fork the project or submit a PR to support other platforms.

```bash
conda create -n minigpt4 python=3.10

sudo apt install git-lfs

git clone https://github.com/catid/minigpt4
cd minigpt4

git lfs install
git submodule update --init --recursive

conda activate minigpt4
pip install -r requirements.txt
```

## Example Usage

This uses about 18.2 GB of VRAM to run.  Note that the first question/answer will be very slow because it is compiling the model.  Subsequent questions will be much faster.

![Example Image](icbm_bicycle.png)

```bash
conda activate minigpt4
(mg4) ➜  minigpt4 git:(main) ✗ CUDA_VISIBLE_DEVICES=0 python example.py

Loading models...
Loading VIT
Loading VIT Done
Loading Q-Former
Loading Q-Former Done
Loading LLAMA

...

Loading image...
Image loaded in 0.03974032402038574 seconds
Live output: <s>I see a large, white missile on the road. It appears to be made of metal and has a pointed nose and tail. It is sitting on the ground, leaning against a road sign. The sign says "Danger: Missile Ahead". There is a cloudy sky in the background.###
LLM response: I see a large, white missile on the road. It appears to be made of metal and has a pointed nose and tail. It is sitting on the ground, leaning against a road sign. The sign says "Danger: Missile Ahead". There is a cloudy sky in the background.
Conversation(system='Human provides a photo and asks questions.  Assistant answers the questions honestly and simply.', roles=('Human', 'Assistant'), messages=[['Human', '<Img><ImageHere></Img> Tell me what you see on the road.'], ['Assistant', 'I see a large, white missile on the road. It appears to be made of metal and has a pointed nose and tail. It is sitting on the ground, leaning against a road sign. The sign says "Danger: Missile Ahead". There is a cloudy sky in the background.']], offset=2, sep_style=<SeparatorStyle.SINGLE: 1>, sep='###', sep2=None, skip_next=False, conv_id=None)
Generated LLM response in 5.6917641162872314 seconds
```
