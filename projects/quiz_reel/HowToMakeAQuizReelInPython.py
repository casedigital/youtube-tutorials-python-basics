# How to make a quiz reel in python

import os
import random
import textwrap

import cv2
import moviepy.editor as mp
import numpy as np
from PIL import Image, ImageDraw


def wrap_text(txt, width):
    wrapped_text = '\n'.join(textwrap.wrap(txt, width))
    return wrapped_text

def create_gradiant_image(size:tuple, color1, color2):
    width, height = size
    img = np.zeros((height, width, 4), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            r = color1[0] + (color2[0] - color1[0]) * (x+y) / (width + height)
            g = color1[1] + (color2[1] - color1[1]) * (x+y) / (width + height)
            b = color1[2] + (color2[2] - color1[2]) * (x+y) / (width + height)
            img[y, x] = (int(r), int(g), int(b), 255)
    return img

def create_rounded_rectangle(size, radius, color, border_color=(255, 255, 255, 255), border_thickness=10):
    width, height = size
    total_width = width + 2 * border_thickness
    total_height = height + 2 * border_thickness
    image = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, width, height), fill=color, outline=border_color, width=border_thickness, radius=radius)

    image = pil_to_cv2(image)
    return image

def pil_to_cv2(image):
    np_img = np.array(image)
    # opencv_img = cv2.cvtColor(np_img, cv2.COLOR_RGBA2BGRA)
    return np_img

def generate_confetti_clip(duration, size, num_particels=200):

    def make_particle():
        x = np.random.randint(0, size[0])
        y = np.random.randint(-size[1], 0)
        radius = np.random.randint(5, 15)
        color = tuple(map(int, np.random.randint(0, 256, size=3)))
        return {'pos': [x, y], 'radius': radius, 'color': color}

    particles = [make_particle() for _ in range(num_particels)]

    print(len(particles))

    def make_frame(t):
        frame = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        for p in particles:
            x, y = p['pos']
            radius = p['radius']
            color = p['color']
            cv2.circle(frame, (x, y + int(t * size[1] / duration)), radius, color + (255, ), -1)
        return frame
        
    return mp.VideoClip(make_frame, duration=duration).add_mask()

def blend_confetti(main_clip, confetti):

    def make_frame(t):
        frame = main_clip.get_frame(t)
        if main_clip.duration - confetti.duration <= t <= main_clip.duration:
            confetti_frame = confetti.get_frame(t - (main_clip.duration - confetti.duration))
            frame = cv2.addWeighted(frame, 1.0, confetti_frame, 1.0, 0)
        return frame
    return mp.VideoClip(make_frame, duration=main_clip.duration)

if __name__ == "__main__":
    question = "Which mode is used to open a file for reading in python"
    choices = ["r", "w", "a", "x"]
    answer = choices[0]
    print(f"{choices = }")
    random.shuffle(choices)
    print(f"{choices = }")

    total_duration = 9
    video_size = (1080, 1920)

    wrapped_question = wrap_text(question, 20)
    print(wrapped_question)

    question_clip = mp.TextClip(
        wrapped_question, fontsize=100, color="white", size=(800, None), bg_color="black"
    )
    question_clip = question_clip.set_position(("center", 300)).set_duration(total_duration)


    gradiant_img = create_gradiant_image(video_size, (255, 211, 67), (54, 119, 174))
    gradiant_clip = mp.ImageClip(gradiant_img, ismask=False).set_duration(total_duration)


    choice_clips = []
    rounded_rect_clips = []
    answer_pos = None
    choice_start_y = 1000
    choice_w_h = (800, 150)
    choice_space = choice_w_h[-1] + 25
    for i, choice in enumerate(choices):
        rounded_rect_img = create_rounded_rectangle(choice_w_h, 20, (54, 119, 174, 255))

        choice_clip = mp.TextClip(
            choice,
            fontsize=100,
            color ='#ffd343',
            size = choice_w_h
        )
        choice_clip = choice_clip.set_position(("center", choice_start_y + i * choice_space))

        rounded_rect_clip = mp.ImageClip(rounded_rect_img)
        rounded_rect_clip = rounded_rect_clip.set_position(("center", choice_start_y + i * choice_space))
        

        if choice == answer:
            answer_pos = choice_start_y + i * choice_space
            rounded_rect_clip = rounded_rect_clip.set_duration(total_duration-3)
            choice_clip = choice_clip.set_duration(total_duration-3)
        else:
            rounded_rect_clip = rounded_rect_clip.set_duration(total_duration)
            choice_clip = choice_clip.set_duration(total_duration)

        choice_clip = choice_clip.set_duration(total_duration)
        choice_clips.append(choice_clip)
        rounded_rect_clips.append(rounded_rect_clip)


    answer_rect_img = create_rounded_rectangle(choice_w_h, 20, (0, 255, 0, 255))
    answer_clip = mp.TextClip(
        answer,
        fontsize=100,
        color ='black',
        size = choice_w_h
    )
    answer_clip = answer_clip.set_position(("center", answer_pos))
    answer_rect_clip = mp.ImageClip(answer_rect_img)
    answer_rect_clip = answer_rect_clip.set_position(("center", answer_pos))
    answer_rect_clip = answer_rect_clip.set_duration(3).set_start(total_duration -3)
    answer_clip = answer_clip.set_duration(3).set_start(total_duration -3)


    countdown_clips = []
    for i in range(5, 0, -1):
        countdown_clip = mp.TextClip(
            str(i),
            fontsize=200,
            color ='white',
            bg_color="transparent",
            size = (400, 400)
        )
        countdown_clip = countdown_clip.set_position((1080 / 2 - 200, 1920 / 2 -400))
        countdown_clip = countdown_clip.set_duration(1)
        countdown_clip = countdown_clip.set_start(1 + (5 - i))
        countdown_clips.append(countdown_clip)


    use_clips = [gradiant_clip, question_clip] + rounded_rect_clips + countdown_clips+ choice_clips + [answer_rect_clip, answer_clip]

    final_clip = mp.CompositeVideoClip(use_clips, bg_color=(0, 0, 0, 0))
    final_clip = final_clip.set_duration(total_duration)


    confetti_clip = generate_confetti_clip(duration=3, size=video_size)
    blended_clip = blend_confetti(final_clip, confetti_clip)

    blended_clip.write_videofile("./QuizReel.mp4", fps=24, codec="libx264")


