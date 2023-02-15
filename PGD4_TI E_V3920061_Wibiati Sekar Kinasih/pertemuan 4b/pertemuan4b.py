# PART E
import pygame, sys #mengimport modul pygame dan modul sys
from pygame.locals import *

WIDTH, HEIGHT = 400, 400 #konstanta width dan height digunakan untuk mengatur ukuran lebar dan tinggi display windows dengan ukuran 400 x 400
TITLE = "Smooth Movement - Wibi" #mengatur judul pada display windows yaitu "Smooth Movement - Wibi"

pygame.init() #menginisialisasikan semua modul pygame yang diimport
win = pygame.display.set_mode((WIDTH,HEIGHT)) #fungsi yang digunakan pada variabel win yaitu pygame.display.set_mode((WIDTH,HEIGHT)),
#digunakan untuk mengatur mode tampilan dan mengembalikan nilai pada fungsi variabel win
#parameter width dan height merupakan konstanta width dan height yang telah diberikan nilai sebelumnya
pygame.display.set_caption(TITLE) #digunakan untuk mengatur judul display Windows
#parameter title merupakan karakter title yang telah ditentukan sebelumnya

clock = pygame.time.Clock() #membuat objek untuk melacak waktu

# PART D
class Player: #membuat class player, dimana class ini untuk mendefinisikan object
    def __init__(self, x, y): #membuat fungsi constructor dengan parameter self,x,y
        #parameter self ini digunakan untuk mengetahui object mana yang digunakan, dalam kasus ini object yang digunakan adalah "Player"
        self.x = int(x) #dari parameter x yang telah disebutkan di atas maka terdapat properti x di mana ini dideklarasikan dengan tipe data x integer.
        self.y = int(y) #dari parameter y yang telah disebutkan di atas maka terdapat properti y di mana ini dideklarasikan dengan tipe data y integer.
        self.rect = pygame.Rect(self.x , self.y, 32, 32) #membuat object rectangle berukuran 32 x 32
        self.color = (245, 183, 177) #memberikan warna pada object
        self.velX = 0 #memberikan arah gerak pada object yaitu secara horizontal, dimulai dari titik 0
        self.velY = 0 #memberikan arah gerak pada object yaitu secara vertical, dimulai dari titik 0
        self.left_pressed = False #mendeklarasikan jika tombol kiri di tekan maka posisinya akan berubah (bukan di titik 0/default lagi)
        self.right_pressed = False #mendeklarasikan jika tombol kanan di tekan maka posisinya akan berubah (bukan di titik 0/default lagi)
        self.up_pressed = False #mendeklarasikan jika tombol atas di tekan maka posisinya akan berubah (bukan di titik 0/default lagi)
        self.down_pressed = False #mendeklarasikan jika tombol bawah di tekan maka posisinya akan berubah (bukan di titik 0/default lagi)
        self.speed = 4 #memberikan kecepatan pada object
    
    # PART F
    def draw(self, win): #fungsi draw digunakan untuk menggambar object pada display windows dengan warna dan ukuran yang telah ditentukan
        pygame.draw.rect(win, self.color, self.rect)

    # PART A
    def update(self): #fungsi update digunakan untuk mengupdate properti-properti pada object
        self.velX = 0 #memberikan arah gerak pada object yaitu secara horizontal, dimulai dari titik 0
        self.velY = 0 #memberikan arah gerak pada object yaitu secara vertical, dimulai dari titik 0
        if self.left_pressed and not self.right_pressed: #jika yang ditekan adalah tombol kiri dan bukan tombol kanan maka arah gerak menuju arah kiri (koordinat x negatif)
            if self.x >0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = -self.speed
        if self.right_pressed and not self.left_pressed: #jika yang ditekan adalah tombol kanan dan bukan tombol kiri maka arah gerak menuju arah kanan (koordinat x positif)
            if self.x < 400 -32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = self.speed
        if self.up_pressed and not self.down_pressed: #jika yang ditekan adalah tombol atas dan bukan tombol bawah maka arah gerak menuju arah atas (koordinat y positif)
            if self.y > 0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = -self.speed
        if self.down_pressed and not self.up_pressed: #jika yang ditekan adalah tombol bawah dan bukan tombol atas maka arah gerak menuju arah bawah (koordinat y negatif)
            if self.y < 400 - 32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = self.speed

        #nilai koordinat akan bertambah seiring dengan pergerakan object
        self.x += self.velX 
        self.y += self.velY 

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

# PART B
player = Player(WIDTH/2, HEIGHT/2)
#menggunakan perulangan while, jika true (benar) maka perintah-perintah di dalamnya akan di-execute
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #menjalankan object, jika ditekan nanti akan menghasilkan kondisi pergerakan object yang seperti apa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

# PART C
    win.fill ((12, 24,36)) #membuat warna backround yaitu black pearl

#menampilkan teks nama lengkap
    font_color = (233,150,122) #memberi warna dark salmon
    font_obj=pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf", 25) #mengatur jenis dan ukuran font
    text_obj=font_obj.render("Wibiati Sekar Kinasih", True, font_color) #pada fungsi render terdapat 4 parameter
    #parameter 1 berisi teks yang akan ditampilkan pada pygame display window
    #parameter 2 merupakan antialising memiliki nilai tru
    #parameter 3 merupakan warna
    #parameter 4 untuk menentukan background
    win.blit(text_obj,(22,0)) #merender (menampilkan) teks pada display window dengan koordinat yang ditentukan 

    player.draw(win) #menggambar warna background untuk object player
    player.update() #mengupdate semua pada object player
    pygame.display.flip() #menampilkan display window
    clock.tick(120) #mengatur kecepatan frame maksimum yaitu 120 frame/detik sehingga tidak akan memakan banyak sumber daya

pygame.quit()