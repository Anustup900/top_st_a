import streamlit as st
import os
from PIL import Image


def load_images(folder):
    image_files = ['product.png', 'base.png', 'tryon3.png', 'tryon_n.png']
    images = []
    for img in image_files:
        img_path = os.path.join(folder, img)
        if os.path.exists(img_path):
            image = Image.open(img_path)
            images.append((img, image))
        else:
            images.append((img, None))
    return images


# Root directory where images are stored
root_folder = "Testing_set_tops_alle"

st.title("Tops Tryon View <> Pinterest Flow")

if os.path.exists(root_folder):
    subfolders = sorted(os.listdir(root_folder))

    for subfolder in subfolders:
        folder_path = os.path.join(root_folder, subfolder)
        if os.path.isdir(folder_path):
            st.subheader(f"Experiment: {subfolder}")
            images = load_images(folder_path)

            cols = st.columns(len(images))

            for col, (filename, img) in zip(cols, images):
                if img:
                    col.image(img, use_container_width=True)
                    col.write(f"{filename}")
                else:
                    col.write(f"**{filename}** (Not Found)")
else:
    st.error("No images found. Please run the image download script first.")
