from multiprocessing import Pool, cpu_count
from PIL import Image
import os
import time

# Folder tempat gambar disimpan
IMAGE_FOLDER = "images"

def process_image(image_name):
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    start_time = time.time()

    # Membuka gambar lalu ubah ke grayscale
    img = Image.open(image_path).convert("L")

    # Ambil semua pixel
    pixels = list(img.getdata())

    # Hitung rata-rata brightness
    avg_brightness = sum(pixels) / len(pixels)

    end_time = time.time()
    execution_time = end_time - start_time

    return {
        "image": image_name,
        "brightness": round(avg_brightness, 2),
        "time": round(execution_time, 4)
    }

if __name__ == "__main__":
    start_total = time.time()

    # Ambil semua file gambar
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    print("=== DATA PARALLELISM: IMAGE BRIGHTNESS ANALYSIS ===")
    print(f"Jumlah CPU yang tersedia: {cpu_count()}")
    print(f"Jumlah gambar: {len(image_files)}\n")

    # Proses paralel
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_image, image_files)

    print("=== HASIL ===")
    for result in results:
        print(f"Gambar: {result['image']}")
        print(f"Brightness rata-rata: {result['brightness']}")
        print(f"Waktu eksekusi: {result['time']} detik")
        print("-" * 40)

    end_total = time.time()
    print(f"\nTotal waktu eksekusi paralel: {round(end_total - start_total, 4)} detik")

    