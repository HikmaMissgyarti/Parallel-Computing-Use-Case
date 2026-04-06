# Quiz - Parallel Computing Use Case (Image Brightness Analysis)

## Nama
Nur Hikma Missgyarti

## NRP
152024098

## Deskripsi
Project ini merupakan implementasi **Data Parallelism** menggunakan Python.

Program memproses beberapa file gambar secara bersamaan untuk menghitung **rata-rata brightness** dari setiap gambar.

## Konsep Parallelism
Program ini menggunakan **Data Parallelism**, karena:
- task yang dijalankan sama
- data yang diproses berbeda

Setiap proses menjalankan tugas:
- membuka gambar
- mengubah ke grayscale
- menghitung brightness

Tetapi tiap proses mengerjakan **gambar yang berbeda**.

## Cara Menjalankan
1. Install library:
```bash
pip install -r requirements.txt