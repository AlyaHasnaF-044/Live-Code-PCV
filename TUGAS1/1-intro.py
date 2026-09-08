# import cv2
# from matplotlib import pyplot as plt

#TUGAS NO 1.
#gambar = cv2.imread("foto alya.jpg")

# Cek apakah gambar berhasil dibaca
#if gambar is None:
#    print("Gambar tidak ditemukan!")
#else:
    #print("Gambar berhasil dibaca!")

    # Menampilkan gambar
    #cv2.imshow("Foto Saya", gambar)

    # Menunggu tombol ditekan
   # cv2.waitKey(0)

    # Menutup semua window OpenCV
  #  cv2.destroyAllWindows()

#TUGAS NO 2.
# terang = cv2.imread("citra terang.jpg")
# gelap = cv2.imread("citra gelap.jpg")
# kontras = cv2.imread("kontras rendah.jpg")

# print("=== CITRA TERANG ===")
# print("Shape     :", terang.shape)
# print("Dtype     :", terang.dtype)
# print("Min       :", terang.min())
# print("Max       :", terang.max())
# print("Rata-rata :", terang.mean())

# print("\n=== CITRA GELAP ===")
# print("Shape     :", gelap.shape)
# print("Dtype     :", gelap.dtype)
# print("Min       :", gelap.min())
# print("Max       :", gelap.max())
# print("Rata-rata :", gelap.mean())

# print("\n=== CITRA KONTRAS RENDAH ===")
# print("Shape     :", kontras.shape)
# print("Dtype     :", kontras.dtype)
# print("Min       :", kontras.min())
# print("Max       :", kontras.max())
# print("Rata-rata :", kontras.mean())

# gambar = cv2.imread("citra terang.jpg")

# # Ubah ke grayscale
# gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# # Ambil area 8 x 8
# potongan = gray[100:108, 100:108]

# print(potongan)

# gelap = gray[300:308, 200:208]
# print("Area gelap:")
# print(gelap)

# terang = gray[50:58, 500:508]
# print("Area terang:")
# print(terang)

# print("Area gelap:")
# print(gelap)
# print("Min:", gelap.min())
# print("Max:", gelap.max())

# print("\nArea terang:")
# print(terang)
# print("Min:", terang.min())
# print("Max:", terang.max())

#BAGIAN IMAGE TUGAS DI KELAS
# image = cv2.imread("citra terang.jpg")
# [h,w,c] = image.shape

# for i in range(h):
#     for j in range(w):
#         image[i,j,0] = 0
#         image[i,j,2] = 0


# cv2.imshow("image hijau", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows
# cv2.waitKey(1)

# #BAGIAN VIDEO TUGAS DI KELAS
# import cv2

# kamera = cv2.VideoCapture(0)

# while True:
#     ret, image = kamera.read()

#     if ret == False:
#         break

#     h, w, c = image.shape

#     i = 0

#     while i < h:
#         j = 0

#         while j < w:
#             image[i, j, 0] = 0
#             image[i, j, 2] = 0

#             j = j + 1

#         i = i + 1

#     cv2.imshow("Kamera Hijau", image)

#     tombol = cv2.waitKey(1)

#     if tombol == ord('q'):
#         break

# kamera.release()
# cv2.destroyAllWindows()



