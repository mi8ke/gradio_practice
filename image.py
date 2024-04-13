# https://note.com/npaka/n/nb9d4902f8f4d
import numpy as np
import gradio as gr

# セピア化の関数
def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

# Interfaceの作成
demo = gr.Interface(
    fn=sepia, 
    inputs=gr.Image(), 
    outputs="image"
)

# 起動
demo.launch()