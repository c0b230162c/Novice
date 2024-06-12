add_library('minim')

p = 15
ModeGame = False
ModeMenu = False
ModeTitle = True
ModeLibrary = False
M = False
ov = 0
correct = 0
flag = 0


add_library('minim')

p = 15
page = 0
ModeGame = False
ModeMenu = False
ModeTitle = True
ModeLibrary = False
ov = 0
correct = 0
flag = 0
my_x = 0
my_y = 0
flag_a1 = 0
flag_a2 = 0
flag_a3 = 0
flag_a4 = 0
flag_a5 = 0
flag_a6 = 0
flag_a7 = 0
flag_a8 = 0
flag_a9 = 0
flag_a10 = 0
flag_a11 = 0
flag_a12 = 0
page = 0
cc = 0
name_num = 0


yoko_lst = [10, 35, 47, 87, 97, 180, 180, 220, 250, 350, 375, #yagi
           800, 810, 815, 855, 945, 970, 975, 1005, 965, 1040, 1035, 1275, 1050, 1075, 1087, 1125, 1205, 1230, 1300, 1215, 1235, #ite
           1710, 1745, 1775, 1795, 1800, 1900, 1985, 1990, 1995, 2040, 2085, 2130, 2215, 2235, 2235, 2240, #sasori
           2420, 2515, 2620, 2645, 2685, 2750, #tennbinn
           3005, 3030, 3055, 3060, 3070, 3065, 3100, 3100, 3110, 3115, 3140, 3135, 3133, 3170, 3185, #otome
           3530, 3575, 3650, 3635, 3670, 3670, 3850, 3885, 3950, 4045, 3945, 3900, 3985, 4020, 4070, #sisi　
           4320, 4320, 4465, 4480, 4560, 4570, 4680, #kani
           5000, 5050, 5045, 5060, 5080, 5040, 5110, 5270, 5160, 5230, 5170, 5200, 5220, 5250, #hutago
           5570, 5600, 5680, 5700, 5680, 5690, 5710, 5750, 5760, 5735, 5790, 5850, 5880, 5810, 5860, #ousi
           6160, 6350, 6380, 6420, #ohituzi
           6630, 6650, 6665, 6680, 6720, 6780, 6775, 6760, 6785, 6760, 6800, 6900, 6950, 6980, 7000, 7010, 7050, 6945, 6985, #uo
           7330, 7340, 7380, 7395, 7397, 7430, 7385, 7420, 7415, 7440, 7500, 7480, 7510, 7570, 7590, 7680] #mizugame
tate_lst = [250, 245, 210, 150, 247, 245, 90, 50, 100, 290, 350,
           475, 300, 290, 165, 670, 205, 130, 605, 650, 590, 465, 595,415, 610, 485, 475, 505, 405, 390, 325, 275,
           770, 705, 725, 785, 650, 660, 690, 785, 870, 1010, 1055, 1070, 1210, 1140, 1045, 975,
           0, 50, 180, -55, -175, 25,
           425, 550, 590, 210, 300, 435, 355, 575, 510, 460, 395, 265, 215, 270, 365,
           890, 640, 750, 820, 890, 975, 800, 970, 840, 820, 910, 1040, 1080, 1045, 1040,
           70, 300, 255, 190, 210, 270, 325,
           570, 720, 620, 580, 500, 480, 730, 490, 660, 645, 570, 520, 500, 480,
           420, 470, 370, 400, 320, 300, 360, 400, 320, 280, 440, 330, 290, 250, 220,
           550, 520, 600, 560,
           20, 22, 100, 50, 180, 240, 280, 315, 345, 80, 75, 65, 50, 60, 50, 30, 40, 20, 15,
           300, 220, 110, 100, 80, 105, 210, 250, 310, 320, 350, 70, 160, 200, 80, 70]
r_lst = [10, 7, 4, 7, 7, 7, 4, 7, 4, 10, 7,
         4, 4, 7, 7, 7, 7, 7, 10, 4, 7, 10, 7, 10, 4, 15, 10, 10, 10, 10, 15, 10,
         10, 10, 15, 15, 15, 10, 7, 10, 15, 10, 15, 10, 10, 15, 10, 4,
         7, 4, 10, 4, 10, 10, 
         10, 7, 7, 7, 7, 10, 10, 7, 7, 10, 7, 7, 7, 7, 15,
         10, 7, 7, 7, 7, 10, 7, 10, 15, 7, 7, 7, 7, 10, 7, 
         10, 10, 10, 7, 4, 7, 10,
         4, 15, 4, 4, 15, 10, 15, 4, 7, 10, 10, 10, 7, 7,
         7, 15, 10, 4, 7, 4, 4, 10, 10, 15, 4, 7, 4, 4, 4,
         15, 15, 7, 7,
         17, 8, 7, 8, 20, 8, 10, 8, 8, 12, 10, 12, 7, 7, 8, 15, 12, 10, 7,
         8, 7, 9, 12, 8, 10, 8, 15, 7, 8, 20, 15, 10, 7, 12, 8]


def setup():
    global img
    size(1200, 800)
    img = loadImage("picture/utyuu.png")
    background(0)
    stroke(255, 255, 0)
    font = createFont(u'MS ゴシック',100)
    textFont(font)
    minim = Minim(this)
    main_sound = minim.loadFile("sound/main_sound.mp3")
    main_sound.loop()
    
    
def draw():
    global ov
    if ModeLibrary:
        draw_library()
    elif ModeGame:
        draw_space()
        draw_sky()
        move_space()
        draw_game()
    elif ModeLibrary:
        draw_library()
    elif ModeMenu:
        if ModeGame:
            draw_menu()
    
    elif ModeTitle:
        if frameCount % 100 == 0:
            ov += 0.5
        textSize(40)
        fill(255,255,0,ov)
        
        #タイトル背景用
        text(u"星間旅行～星が導くままに～",340,300)
        draw_Pixels()
        draw_title()


def draw_space():
    global my_x
    background(30, 30, 55)
    stroke(255, 255, 0)
    for i in range(len(r_lst)):
        strokeWeight(r_lst[i]/2)
        cX = yoko_lst[i]*0.75 + my_x
        cY = tate_lst[i]*0.75 + my_y
        point(cX + 50, 600 - cY)
        
def move_space():
    global my_x, my_y
    if keyPressed:
        if keyCode == UP:
            my_y -= 5
        if keyCode == DOWN:
            my_y += 5
        if keyCode == LEFT:
            my_x += 10
        if keyCode == RIGHT:
            my_x-= 5
    if my_x <= -6500:
        my_x = 1000
    if my_x >= 1000:
        my_x = -6500
    if my_y >= 200:
        my_y = 200
    if my_y <= -350:
        my_y = -350
        
            
#ピクセルアート（背景）の処理
def draw_Pixels():
    global img, p
    x = int(random(img.width))
    y = int(random(img.height))

    l = x + y * img.width

    loadPixels()

    Red = red(img.pixels[l])
    Green = green(img.pixels[l])
    Blue = blue(img.pixels[l])
    noStroke()

    fill(Red,Green,Blue,100)
    ellipse(x,y,p,p)

#タイトルの操作方法の記述
def draw_title():
    stroke(255)
    fill(0,0,0)
    rect (400,410,400,350)
    textSize(25)
    fill(255)
    text(u"☆操作方法☆",410,450)
    textSize(25)
    text(u"ｓキー  　Start/Continue",450,500)
    text(u"mキー  　Menu",450,540)
    text(u"↑キー　  上に移動",450,590)
    text(u"↓キー  　下に移動",450,640)
    text(u"→キー  　右に移動",450,690)
    text(u"←キー  　左に移動",450,740)

def draw_menu():
    
    size(1200,800)
    textSize(50)
    fill(255,255,255,100)
    rect(150,100,900,600)
    text("Library",200,210)
    text("Continue",200,310)
    #text("Correct",200,410)
    text("Exit",200,610)
    
    text(u"lキー",500,210)
    text(u"sキー",500,310)
    text(u"eキー",500,610)

    

#図鑑表示
def draw_library():
    background(255)
    global page
    L_crick()
    
    img1 = loadImage("picture/a1.png")
    img2 = loadImage("picture/a2.png")
    img3 = loadImage("picture/a3.png")
    img4 = loadImage("picture/a4.png")
    img5 = loadImage("picture/a5.png")
    img6 = loadImage("picture/a6.png")
    img7 = loadImage("picture/a7.png")
    img8 = loadImage("picture/a8.png")
    img9 = loadImage("picture/a9.png")
    img10 = loadImage("picture/a10.png")
    img11 = loadImage("picture/a11.png")
    img12 = loadImage("picture/a12.png")
    picture = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12]
    
    

    fill(255)
    rect(100,100,600,600)
    
    image(picture[page],0,0,1200,800)
    
def L_crick():
    global page, cc
    if cc == 0:
        if mouseX > width/2:
            if mouseButton:
                if page == 11:
                    page = 11
                else:
                    page += 1
                    cc += 1
                    minim = Minim(this)
                    Book_sound = minim.loadFile("sound/page.mp3")
                    Book_sound.play()
                    
                    
        if mouseX < width/2:
            if mouseButton:
                if page == 0:
                    page = 0
                else:
                    page -= 1
                    cc += 1
                    minim = Minim(this)
                    Book_sound = minim.loadFile("sound/page.mp3")
                    Book_sound.play()
    else:
        cc = 0
    
#ここにゲームモード
def draw_game():
    global ModeTitle, ModeLibrary, M
    crick_ster()
    
    #Complate時の処理
    if correct >= 12:
        corrrect = 12
        
        if M == False:
            minim = Minim(this)
            clear_sound = minim.loadFile("sound/clear.mp3")
            clear_sound.play()
            M = True
            
        textSize(25)
        fill(255,255,0)
        text(u"Complate!　　素敵な旅を!",270,30)
        noStroke()
        fill(30, 30, 55)  
        rect(400,7000,600,55)
        
    
    else:
        text(u"星座をクリックしてみよう",400,750,50)
    
        if mouseButton:
            noStroke()
            fill(30, 30, 55)  
            rect(390,700,400,55)
        
    
    fill(255,255,255)
    print(correct)
    textSize(25)
    text(u"集めた星の数",30,30)
    c_w = str(correct)
    text(c_w,190,30)
    text(u"/12",220,30)
    if name_num == 1:
        text(u"やぎ座", 100, 100)
    if name_num == 2:
        text(u"いて座", 100, 100)
    if name_num == 3:
        text(u"さそり座", 100, 100)
    if name_num == 4:
        text(u"てんびん座", 100, 100)
    if name_num == 5:
        text(u"おとめ座", 100, 100)
    if name_num == 6:
        text(u"しし座", 100, 100)
    if name_num == 7:
        text(u"かに座", 100, 100)
    if name_num == 8:
        text(u"ふたご座", 100, 100)
    if name_num == 9:
        text(u"おうし座", 100, 100)
    if name_num == 10:
        text(u"おひつじ座", 100, 100)
    if name_num == 11:
        text(u"うお座", 100, 100)
    if name_num == 12:
        text(u"みずがめ座", 100, 100)
    
    
    
    if key == "m":
        draw_menu()
        noStroke()
        fill(30,30,55)
        rect(150,700,900,100)
        ModeLibrary = False
    
        
def keyPressed():
    global ModeGame, ModeTitle, page, ModeLibrary
    
    if key == "s":
        ModeGame = True
        ModeTitle = False
        ModeLibrary = False
        minim = Minim(this)
        Ster_sound = minim.loadFile("sound/st1.mp3")
        Ster_sound.play()
        
    if key == "e":
        background(0)
        ModeGame = False
        ModeTitle = True
        ModeLibrary = False
    
    if key == "l":
        if ModeTitle == False:
            ModeLibrary = True
            page = 0
            minim = Minim(this)
            Book_sound = minim.loadFile("sound/page.mp3")
            Book_sound.play()

#星をクリックしたときの判定
def crick_ster():
    global correct, name_tag, flag_a1, flag_a2, flag_a3, flag_a4, flag_a5, flag_a6, flag_a7, flag_a8, flag_a9, flag_a10, flag_a11, flag_a12, flag, name_num
    my_X = my_x
    if flag == 1:
        minim = Minim(this)
        ster_sound = minim.loadFile("sound/ster.mp3")
        ster_sound.play()
        flag = 0
        correct += 1 
    if flag_a1 == 0:
        if 10 + my_X <= mouseX <= 350 + my_X and 350 + my_y <= mouseY <= 600 + my_y:
            if mousePressed:
                flag = 1
                flag_a1 = 1
                name_num = 1
    if flag_a2 == 0:
        if 650 + my_X <= mouseX <= 1025 + my_X and 153.75 + my_y <= mouseY <= 502.5 + my_y:
            if mousePressed:
                flag = 1
                flag_a2 = 1
                name_num = 2
    if flag_a3 == 0:
        if 1332.5 + my_X <= mouseX <= 1730 + my_X and -307.5 - my_y <= mouseY <= 112.5 - my_y:
            if mousePressed:
                flag = 1
                flag_a3 = 1
                name_num = 3
    if flag_a4 == 0:
        if 1865 + my_X <= mouseX <= 2126.25 + my_X and 465 - my_y <= mouseY <= 731.5 - my_y:
            if mousePressed:
                flag = 1
                flag_a4 = 1
                name_num = 4
    if flag_a5 == 0:
        if 2303.75 + my_X <= mouseX <= 2438.75 + my_X and 157.5 - my_y <= mouseY <= 442.5 - my_y:
            if mousePressed:
                flag = 1
                flag_a5 = 1
                name_num = 5
    if flag_a6 == 0:
        if 2697.5 + my_X <= mouseX <= 3102.5 + my_X and -210 - my_y <= mouseY <= 120 - my_y:
            if mousePressed:
                flag = 1
                flag_a6 = 1
                name_num = 6
    if flag_a7 == 0:
        if 3290 + my_X <= mouseX <= 3560 + my_X and 356.25 - my_y <= mouseY <= 547.5 - my_y:
            if mousePressed:
                flag = 1
                flag_a7 = 1
                name_num = 7
    if flag_a8 == 0:
        if 3800 + my_X <= mouseX <= 4002.5 + my_X and 52.5 - my_y <= mouseY <= 240 - my_y:
            if mousePressed:
                flag = 1
                flag_a8 = 1
                name_num = 8
    if flag_a9 == 0:
        if 4227.5 + my_X <= mouseX <= 4460 + my_X and 247.5 - my_y <= mouseY <= 435 - my_y:
            if mousePressed:
                flag = 1
                flag_a9 = 1
                name_num = 9
    if flag_a10 == 0:
        if 4670 + my_X <= mouseX <= 4865 + my_X and 150 - my_y <= mouseY <= 210 - my_y:
            if mousePressed:
                flag = 1
                flag_a10 = 1
                name_num = 10
    if flag_a11 == 0:
        if 5022.5 + my_X <= mouseX <= 5337.5 + my_X and 341.25 - my_y <= mouseY <= 588.75 - my_y:
            if mousePressed:
                flag = 1
                flag_a11 = 1
                name_num = 11
    if flag_a12 == 0:
        if 5547.5 + my_X <= mouseX <= 5810 + my_X and 337.5 - my_y <= mouseY <= 547.5 - my_y:
            if mousePressed:
                flag = 1
                flag_a12 = 1
                name_num = 12
        
def draw_sky():
    for j in range(1000):
        noStroke()
        fill(255,128)
        x = random(-6500, 2200)
        y = random(-300, 1000)
        ellipse(x, y, 2, 2)
    
