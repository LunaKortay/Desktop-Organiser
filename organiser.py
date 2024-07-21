import os
import shutil


audio = (
    ".3ga",
    ".aac",
    ".ac3",
    ".aif",
    ".aiff",
    ".alac",
    ".amr",
    ".ape",
    ".au",
    ".dss",
    ".flac",
    ".flv",
    ".m4a",
    ".m4b",
    ".m4p",
    ".mp3",
    ".mpga",
    ".ogg",
    ".oga",
    ".mogg",
    ".opus",
    ".qcp",
    ".tta",
    ".voc",
    ".wav",
    ".wma",
    ".wv",
)

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf")

img = (
    ".jpg",
    ".jpeg",
    ".jfif",
    ".pjpeg",
    ".pjp",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".apng",
    ".avif",
)


excluded_items = [
    "Everything",
    "Trash",
    "Recycle Bin",
    "My PC",
    "This PC",
    "Geri Dönüşüm Kutusu",
]


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
everything_folder = os.path.join(desktop_path, "Everything")


os.chdir(desktop_path)


if not os.path.exists(everything_folder):
    os.makedirs(everything_folder)

img_folder = os.path.join(everything_folder, "img")
audio_folder = os.path.join(everything_folder, "audio")
video_folder = os.path.join(everything_folder, "video")
other_folder = os.path.join(everything_folder, "other")

for folder in [img_folder, audio_folder, video_folder, other_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)


def is_audio(file):
    return os.path.splitext(file)[1].lower() in audio


def is_video(file):
    return os.path.splitext(file)[1].lower() in video


def is_image(file):
    return os.path.splitext(file)[1].lower() in img


for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)

    # Skip excluded items
    if item in excluded_items:
        continue

    if os.path.isfile(item_path):
        if is_image(item):
            shutil.move(item_path, os.path.join(img_folder, item))
        elif is_audio(item):
            shutil.move(item_path, os.path.join(audio_folder, item))
        elif is_video(item):
            shutil.move(item_path, os.path.join(video_folder, item))
        else:
            shutil.move(item_path, os.path.join(other_folder, item))

    elif os.path.isdir(item_path) and item != "Everything":
        shutil.move(item_path, os.path.join(everything_folder, item))
