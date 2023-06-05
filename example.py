from minigpt4 import MiniGPT4
from blip_processor import Blip2ImageEvalProcessor
from conversation import Chat, CONV_VISION

import torch
import time

print("Loading models...")

t0 = time.time()

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

t1 = time.time()

print("Models loaded in {} seconds".format(t1-t0))

for i in range(5):
    print("Loading image...")

    t0 = time.time()

    chat_state = CONV_VISION.copy()
    img_list = []
    chat.upload_img("icbm_bicycle.png", chat_state, img_list)

    t1 = time.time()

    print("Image loaded in {} seconds".format(t1-t0))

    t0 = time.time()

    num_beams = 1
    temperature = 0.01

    chat.ask("Tell me what you see on the road.", chat_state)

    llm_message = chat.answer(conv=chat_state,
                                img_list=img_list,
                                num_beams=num_beams,
                                temperature=temperature,
                                max_new_tokens=1024,
                                max_length=2048)[0]

    t1 = time.time()

    print(chat_state)
    print("Generated LLM response in {} seconds".format(t1-t0))
