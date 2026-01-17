from PIL import Image
import struct


def convert_to_rgb565(image_path, output_path):
    img = Image.open(image_path).resize((240, 320))
    img = img.convert("RGB")
    with open(output_path, "wb") as f:
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                # Формула RGB888 -> RGB565
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                f.write(struct.pack(">H", rgb565))  # Сохраняем как big-endian


convert_to_rgb565("sabib.jpg", "sabiba.bin")
