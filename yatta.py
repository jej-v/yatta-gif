from PIL import Image, ImageSequence


#yatta gif
im1 = Image.open('yatta.gif')
# profile pic
im2 = Image.open('elysia.png').resize((200,200))

img = Image.new("RGB", im1.size, (255, 255, 255))
img.paste(im2, (210,60))


def senti():
    frames = []
    for frame in ImageSequence.Iterator(im1):
        if len(frames) < 35:
            mask_im = Image.open(f'fmask/senti{len(frames)}.png').resize(im1.size).convert('1')
            frame = Image.composite(im1, img, mask_im)
            frame = frame.copy()
            frames.append(frame)
        else:
            frame = frame.copy()
            frames.append(frame)
    frames[0].save('result.gif', save_all=True, append_images=frames[1:], duration=30, loop=0)

senti()
