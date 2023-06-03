from minigpt4 import MiniGPT4
from blip_processor import Blip2ImageEvalProcessor
from conversation import Chat

import torch

model = MiniGPT4(
    llama_model="/home/catid/sources/minigpt4/models/vicuna13b_v0/"
)

ckpt_path = "/home/catid/sources/minigpt4/models/pretrained_minigpt4.pth"

print("Load BLIP2-LLM Checkpoint: {}".format(ckpt_path))
ckpt = torch.load(ckpt_path, map_location="cpu")
model.load_state_dict(ckpt['model'], strict=False)

torch.compile(model)

vis_processor = Blip2ImageEvalProcessor()

chat = Chat(model, vis_processor, device='cuda:0')
