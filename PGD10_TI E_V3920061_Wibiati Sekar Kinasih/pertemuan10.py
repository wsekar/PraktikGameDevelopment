# menghitung pergerakan kamera
from math import pi, sin, cos
# mengambil dan menampilkan image dari framework ShowBase. ShowBase juga digunakan unruk memberikan inputan dan gerakan
from direct.showbase.ShowBase import ShowBase
# manajemen kegiatan/fungsi pada python (event handling)
from direct.task import Task
# meload kelas aktor yang digunakan
from direct.actor.Actor import Actor
# memanipulasi waktu/durasi movement pada suatu nilai tertentu
from direct.interval.IntervalGlobal import Sequence
# mengatur koordinat aktor
from panda3d.core import Point3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)  # menginisialisasi modul ShowBase

        # load image sesuai dengan direktori penyimpanan file
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)  # merender image yang telah di load
        self.scene.setScale(0.25, 0.25, 0.25)  # mengatur skala image di layar
        self.scene.setPos(-8, 42, 0)  # mengatur posisi image di layar

        # mengatur pergerakan dan posisi kamera berdasar fungsi yang dibuat
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # load image yang dijadikan aktor.
        # image yang digunakan untuk pergerakan yaitu image ketika aktor diam dan image ketika aktor bergerak
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)

        # melakukan iterasi image fungsi pergerakan
        self.pandaActor.loop("walk")

        # fungsi pergerakan aktor saat bergerak dari posisi A ke B.
        # posInterval berisi nilai dan interval ketika kator akan bergerak
        # aktor akan bergerak selama 13 detik menuju koordinat (0,-10,0) dengan starting poin (0,10,0)
        posInterval1 = self.pandaActor.posInterval(
            13, Point3(0, -10, 0), startPos=Point3(0, 10, 0))
        # aktor akan bergerak selama 13 detik menuju koordinat (0,10,0) dengan starting poin (0,-10,0)
        posInterval2 = self.pandaActor.posInterval(
            13, Point3(0, 10, 0), startPos=Point3(0, -10, 0))
        # aktor akan bergerak selama 3 detik menuju koordinat (180,0,0) dengan starting poin (0,0,0)
        hprInterval1 = self.pandaActor.hprInterval(
            3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0))
        # aktor akan bergerak selama 3 detik menuju koordinat (0,0,0) dengan starting poin (180,0,0)
        hprInterval2 = self.pandaActor.hprInterval(
            3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0))

        # sequence untuk menentukan waktu dan urutan interval yang akan dijalankan
        self.pandaPace = Sequence(
            posInterval1, hprInterval1, posInterval2, hprInterval2, name="pandaPace")
        self.pandaPace.loop()

        # mengatur musik yang digunakan berdasarkan fungsi yang dibuat
        self.loadMusic()

    def spinCameraTask(self, task):
        # task.time untuk mengembalikan nilai(float) yang menunjukkan berapa lama fungsi tugas ini berjalan sejak pertama dieksekusi.
        # timer berjalan bahkan saat fungsi tidak dijalankan
        # angleDegrees untuk mencari sudut kamera
        angleDegrees = task.time * 6.0
        # angleRadians untuk mendapatkan nilai radian dari sudut kamera tsb.
        angleRadians = angleDegrees * (pi/180.0)
        # setPos merupakan fungsi awal pergerakan kamera dimulai
        # setHpr mengembalikan kamera ke koordinat semula
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def loadMusic(self):
        # load music/sound sesuai direktori penyimpanan file tsb
        self.music = self.loader.loadMusic(
            "models/audio/running-on-pavement-loop.wav")
        # membuat sound terus berulang selama program dijalankan
        self.music.setLoop(True)
        self.music.play()  # musik menyala
        self.music.setVolume(1)  # mengatur volume


app = MyApp()  # inisialisasi Function MyApp() ke variabel app
app.run()  # menjalankan aplikasi
