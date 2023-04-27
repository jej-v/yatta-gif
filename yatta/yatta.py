from PIL import Image, ImageSequence
from io import BytesIO

def senti(image):
    #yatta gif
    im1 = Image.open('/yatta/yatta.gif')
    # pfp
    im2 = Image.open(image).resize((200,200))
    
    img = Image.new("RGB", im1.size, (255, 255, 255))
    img.paste(im2, (210,60))
    
    frames = []
    for frame in ImageSequence.Iterator(im1):
        if len(frames) < 35:
            mask_im = Image.open(f'/yatta/fmask/senti{len(frames)}.png').resize(im1.size).convert('1')
            frame = Image.composite(im1, img, mask_im)
            frame = frame.copy()
            frames.append(frame)
        else:
            frame = frame.copy()
            frames.append(frame)

    animated_gif = BytesIO()

    frames[0].save(animated_gif, format='gif', save_all=True, append_images=frames[1:], duration=30, loop=0)
    animated_gif.seek(0)
    
    return animated_gif
