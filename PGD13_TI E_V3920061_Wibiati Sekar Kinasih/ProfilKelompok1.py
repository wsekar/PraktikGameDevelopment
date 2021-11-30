import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame

numItemsVisible = 4
itemHeight = 0.11

myScrolledList = DirectScrolledList(
    decButton_pos=(0.35, 0, 0.53),
    decButton_text="Dec",
    decButton_text_scale=0.04,
    decButton_borderWidth=(0.005, 0.005),

    incButton_pos=(0.35, 0, -0.02),
    incButton_text="Inc",
    incButton_text_scale=0.04,
    incButton_borderWidth=(0.005, 0.005),

    frameSize=(0.0, 0.7, -0.05, 0.59),
    frameColor=(1,0,0,0.5),
    pos=(-0.06, 0, 0.15),
    numItemsVisible=numItemsVisible,
    forceHeight=itemHeight,
    itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
    itemFrame_pos=(0.35, 0, 0.4),
)


for fruit in ['Membaca', 'Olahraga', 'Pemrograman', 'Desain','Menggambar','Naik Sepeda']:
    l = DirectLabel(text=fruit, text_scale=0.1)
    myScrolledList.addItem(l)

# Add some text
bk_text = "Profil Kelompok 1"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.85), scale=0.07,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)

# Add some text
output = ""
textObject = OnscreenText(text=output, pos=(0.012, -0.40), scale=0.07,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)
# Callback function to set text
v = [0]

def itemSel(arg):
    if arg == "Pilih Disini Lihat Anggota":
        # Callback function to set  text
        # Add button
        # No need to add an element
        bk_text = "D3 Teknik Informatika PSDKU Kelas E"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
        image='selamat_datang.png', pos=(-0.5, 0, 0.02), scale=0.3,)
        
    if arg == "Anggota 1":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.50),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Muhammad Hanif Arafi Nim : V3920038"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
            image='hanif.png', pos=(-0.5, 0, 0.02), scale=0.3,)
    if arg == "Anggota 2":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.50),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Narutama Phinda Baskara Nim :(V3920042)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='baskara.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)

    if arg == "Anggota 3":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.50),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Oktarinia Rossa Atanaswati Nim : (V3920046)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='okta.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)

    if arg == "Anggota 4":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.50),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Wibiati Sekar Kinasih Nim : (V3920061)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='wibi.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)

# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                        items=["Pilih Disini Lihat Anggota", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4"],
                        highlightColor=(0.65, 0.1, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu


slider = DirectSlider(range=(0, 50), value=50, pageSize=3,
                      pos=(-0.20, 0, -0.70), command=showValue)

# Procedurally select a item
menu.set(0)

# Run the program
base.run()
