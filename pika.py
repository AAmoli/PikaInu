import numpy as np
import os
from PIL import Image
import pandas as pd
import os


os.chdir(r"C:\Users\AmirA\Desktop\Programming\Phyton-Skript\Pixel_Fotos\Pikachu")


df = pd.read_excel("pika_final.xlsx")


def mein_pix(x_von, x_bis, y_von, y_bis, size, Farbe):
    for x in range(x_von * size, x_bis * size): # X-Achse
        for y in range(y_von * size, y_bis * size): # Y-Achse
            data[y, x] = Farbe


def mein_pixel(rechts, unten, Farbe):
    for x in range(rechts * 2 , rechts * 2+20): # X-Achse
        for y in range(unten * 2, unten * 2+20): # Y-Achse
            data[y, x] = Farbe 



# =============================================================================
# layout
# =============================================================================


def layout_funktion(color):
    data = np.zeros((1200, 1200, 3), dtype=np.uint8)
    
    if color == "Turquois":
        my_color = [102,204,255] #turquois

    
        for x in range(0,1200): # X-Achse
            for y in range(0,1200): # Y-Achse
                data[y, x] = my_color


    if color == "Pink":
        my_color = [255,102,204] # pink

    
        for x in range(0,1200): # X-Achse
            for y in range(0,1200): # Y-Achse
                data[y, x] = my_color


    if color == "Purple":
        my_color = [144,67,201] #purple

    
        for x in range(0,1200): # X-Achse
            for y in range(0,1200): # Y-Achse
                data[y, x] = my_color



    if color == "Green":
        my_color = [38,238,105] #green

    
        for x in range(0,1200): # X-Achse
            for y in range(0,1200): # Y-Achse
                data[y, x] = my_color



    if color == "Blue":
        my_color = [75,135,255] #blue

    
        for x in range(0,1200): # X-Achse
            for y in range(0,1200): # Y-Achse
                data[y, x] = my_color


    return data




size = 20

# =============================================================================
# Füllung
# =============================================================================


def fuellung_funktion(color_fuellung):
    
       
    if color_fuellung == "Yellow": #yellow
        my_fill = [243, 231, 29]

        mein_pix(x_von = 40, x_bis = 41, y_von = 34, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 21, x_bis = 40, y_von = 14, y_bis = 44, size = size, Farbe = my_fill)    
        mein_pix(x_von = 15, x_bis = 21, y_von = 13, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 39, x_bis = 43, y_von = 10, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 37, x_bis = 40, y_von = 12, y_bis = 15, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 16, y_von = 25, y_bis = 26, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 16, y_von = 26, y_bis = 27, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 17, y_von = 27, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 18, y_von = 28, y_bis = 29, size = size, Farbe = my_fill)    
        mein_pix(x_von = 11, x_bis = 18, y_von = 29, y_bis = 30, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 30, y_bis = 31, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 31, y_bis = 32, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 32, y_bis = 33, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 33, y_bis = 34, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 34, y_bis = 35, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 20, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 32, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 40, x_bis = 41, y_von = 20, y_bis = 27, size = size, Farbe = my_fill)    
        
        mein_pix(x_von = 22, x_bis = 38, y_von = 44, y_bis = 45, size = size, Farbe = my_fill)    
        mein_pix(x_von = 22, x_bis = 25, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
        mein_pix(x_von = 35, x_bis = 39, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 14, y_von = 24, y_bis = 25, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 13, y_von = 23, y_bis = 24, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 12, y_von = 22, y_bis = 23, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 11, y_von = 21, y_bis = 22, size = size, Farbe = my_fill)    
        mein_pix(x_von = 13, x_bis = 16, y_von = 35, y_bis = 36, size = size, Farbe = my_fill)    


        # =============================================================================
        # Schatten 1
        # =============================================================================

        mein_pixel(70 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(80 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])
        mein_pixel(90 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])
        mein_pixel(340 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(130 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        mein_pixel(330 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])           
        mein_pixel(340 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
    
        mein_pixel(100 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])           
        mein_pixel(170 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(270 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(320 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(330 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(100 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(110 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(120 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(300 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(310 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(320 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(110 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(120 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(130 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(140 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(150 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(290 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(310 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        
        mein_pixel(130 +80, 90 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(300 +80, 90 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(20 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(130 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(310 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        
        mein_pixel(30 +80, 130 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(40 +80, 140 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(50 +80, 150 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(60 +80, 160 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(70 +80, 170 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(80 +80, 180 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(90 +80, 190 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
    
        mein_pixel(130 +80, 200 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(310 +80, 200 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        
        mein_pixel(130 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(210 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(220 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(230 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(240 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(310 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(220 +80, 230 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(230 +80, 230 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
    
        mein_pixel(80 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
        mein_pixel(90 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        
        mein_pixel(70 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(80 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        mein_pixel(90 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
    
        mein_pixel(80 +80, 290 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(120 +80, 320 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(130 +80, 340 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
            
        mein_pixel(200 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(210 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(220 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(230 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(240 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(150 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(170 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(180 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
        mein_pixel(260 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(270 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(290 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 


        
        # =============================================================================
        # Schatten 2
        # =============================================================================

        mein_pixel(80 +80, 50 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 60 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])   
        mein_pixel(100 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])     
        mein_pixel(90 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])      
        mein_pixel(100 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])    
        mein_pixel(70 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
        mein_pixel(80 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(100 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(80 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(100 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])
        mein_pixel(100 +80, 320 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])



    if color_fuellung == "Orange": #orange
        my_fill = [255,102,0]

        mein_pix(x_von = 40, x_bis = 41, y_von = 34, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 21, x_bis = 40, y_von = 14, y_bis = 44, size = size, Farbe = my_fill)    
        mein_pix(x_von = 15, x_bis = 21, y_von = 13, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 39, x_bis = 43, y_von = 10, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 37, x_bis = 40, y_von = 12, y_bis = 15, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 16, y_von = 25, y_bis = 26, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 16, y_von = 26, y_bis = 27, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 17, y_von = 27, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 18, y_von = 28, y_bis = 29, size = size, Farbe = my_fill)    
        mein_pix(x_von = 11, x_bis = 18, y_von = 29, y_bis = 30, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 30, y_bis = 31, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 31, y_bis = 32, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 32, y_bis = 33, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 33, y_bis = 34, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 34, y_bis = 35, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 20, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 32, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 40, x_bis = 41, y_von = 20, y_bis = 27, size = size, Farbe = my_fill)    
        
        mein_pix(x_von = 22, x_bis = 38, y_von = 44, y_bis = 45, size = size, Farbe = my_fill)    
        mein_pix(x_von = 22, x_bis = 25, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
        mein_pix(x_von = 35, x_bis = 39, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 14, y_von = 24, y_bis = 25, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 13, y_von = 23, y_bis = 24, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 12, y_von = 22, y_bis = 23, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 11, y_von = 21, y_bis = 22, size = size, Farbe = my_fill)    
        mein_pix(x_von = 13, x_bis = 16, y_von = 35, y_bis = 36, size = size, Farbe = my_fill)    


        # =============================================================================
        # Schatten 1
        # =============================================================================

        mein_pixel(70 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(80 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])
        mein_pixel(90 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])
        mein_pixel(340 +80, 40 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(130 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        mein_pixel(330 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])           
        mein_pixel(340 +80, 50 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
    
        mein_pixel(100 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])           
        mein_pixel(170 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(270 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(320 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(330 +80, 60 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(100 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(110 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(120 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(300 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(310 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(320 +80, 70 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(110 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(120 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(130 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(140 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(150 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(290 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(310 +80, 80 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        
        mein_pixel(130 +80, 90 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(300 +80, 90 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(20 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(130 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(310 +80, 120 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        
        mein_pixel(30 +80, 130 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(40 +80, 140 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(50 +80, 150 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(60 +80, 160 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(70 +80, 170 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(80 +80, 180 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(90 +80, 190 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
    
        mein_pixel(130 +80, 200 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(310 +80, 200 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        
        mein_pixel(130 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(210 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(220 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(230 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(240 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(310 +80, 220 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])    
        
        mein_pixel(220 +80, 230 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(230 +80, 230 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
    
        mein_pixel(80 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
        mein_pixel(90 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        
        mein_pixel(70 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(80 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])       
        mein_pixel(90 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
    
        mein_pixel(80 +80, 290 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(120 +80, 320 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(130 +80, 340 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
            
        mein_pixel(200 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])     
        mein_pixel(210 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(220 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(230 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])      
        mein_pixel(240 +80, 350 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(150 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(170 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(180 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
        mein_pixel(260 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(270 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(290 +80, 360 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 


        
        # =============================================================================
        # Schatten 2
        # =============================================================================

        mein_pixel(80 +80, 50 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 60 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])   
        mein_pixel(100 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])     
        mein_pixel(90 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])      
        mein_pixel(100 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])    
        mein_pixel(70 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
        mein_pixel(80 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(100 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(80 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(90 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(100 +80, 310 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])
        mein_pixel(100 +80, 320 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])





    if color_fuellung == "Beige": #beige
        my_fill = [249,228,183]

        mein_pix(x_von = 40, x_bis = 41, y_von = 34, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 21, x_bis = 40, y_von = 14, y_bis = 44, size = size, Farbe = my_fill)    
        mein_pix(x_von = 15, x_bis = 21, y_von = 13, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 39, x_bis = 43, y_von = 10, y_bis = 15, size = size, Farbe = my_fill)    
        mein_pix(x_von = 37, x_bis = 40, y_von = 12, y_bis = 15, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 16, y_von = 25, y_bis = 26, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 16, y_von = 26, y_bis = 27, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 17, y_von = 27, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 18, y_von = 28, y_bis = 29, size = size, Farbe = my_fill)    
        mein_pix(x_von = 11, x_bis = 18, y_von = 29, y_bis = 30, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 30, y_bis = 31, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 31, y_bis = 32, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 17, y_von = 32, y_bis = 33, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 33, y_bis = 34, size = size, Farbe = my_fill)    
        mein_pix(x_von = 12, x_bis = 18, y_von = 34, y_bis = 35, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 20, y_bis = 28, size = size, Farbe = my_fill)    
        mein_pix(x_von = 20, x_bis = 21, y_von = 32, y_bis = 41, size = size, Farbe = my_fill)    
        mein_pix(x_von = 40, x_bis = 41, y_von = 20, y_bis = 27, size = size, Farbe = my_fill)    
        
        mein_pix(x_von = 22, x_bis = 38, y_von = 44, y_bis = 45, size = size, Farbe = my_fill)    
        mein_pix(x_von = 22, x_bis = 25, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
        mein_pix(x_von = 35, x_bis = 39, y_von = 45, y_bis = 46, size = size, Farbe = my_fill)    
       
        mein_pix(x_von = 10, x_bis = 14, y_von = 24, y_bis = 25, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 13, y_von = 23, y_bis = 24, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 12, y_von = 22, y_bis = 23, size = size, Farbe = my_fill)    
        mein_pix(x_von = 10, x_bis = 11, y_von = 21, y_bis = 22, size = size, Farbe = my_fill)    
        mein_pix(x_von = 13, x_bis = 16, y_von = 35, y_bis = 36, size = size, Farbe = my_fill)    


        # =============================================================================
        # Schatten 1
        # =============================================================================

        mein_pixel(70 +80, 40 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(80 +80, 40 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])
        mein_pixel(90 +80, 40 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])
        mein_pixel(340 +80, 40 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])    
        
        mein_pixel(130 +80, 50 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])       
        mein_pixel(330 +80, 50 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])           
        mein_pixel(340 +80, 50 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])    
    
        mein_pixel(100 +80, 60 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])           
        mein_pixel(170 +80, 60 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(270 +80, 60 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(320 +80, 60 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(330 +80, 60 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
    
        mein_pixel(100 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(110 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(120 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(300 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(310 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(320 +80, 70 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
    
        mein_pixel(110 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(120 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(130 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(140 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(150 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(290 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(310 +80, 80 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        
        mein_pixel(130 +80, 90 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(300 +80, 90 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])    
        
        mein_pixel(20 +80, 120 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(130 +80, 120 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(310 +80, 120 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        
        mein_pixel(30 +80, 130 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(40 +80, 140 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(50 +80, 150 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(60 +80, 160 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(70 +80, 170 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(80 +80, 180 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(90 +80, 190 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
    
        mein_pixel(130 +80, 200 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(310 +80, 200 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        
        mein_pixel(130 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(210 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(220 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(230 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(240 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(310 +80, 220 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])    
        
        mein_pixel(220 +80, 230 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(230 +80, 230 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
    
        mein_pixel(80 +80, 270 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])   
        mein_pixel(90 +80, 270 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])       
        
        mein_pixel(70 +80, 280 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(80 +80, 280 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])       
        mein_pixel(90 +80, 280 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])   
    
        mein_pixel(80 +80, 290 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
    
        mein_pixel(120 +80, 320 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(130 +80, 340 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
            
        mein_pixel(200 +80, 350 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])     
        mein_pixel(210 +80, 350 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(220 +80, 350 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(230 +80, 350 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])      
        mein_pixel(240 +80, 350 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
    
        mein_pixel(150 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(170 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(180 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])   
        mein_pixel(260 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]])  
        mein_pixel(270 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 
        mein_pixel(290 +80, 360 +80, [my_fill[0], my_fill[1] -35, my_fill[2]]) 


        
        # =============================================================================
        # Schatten 2
        # =============================================================================

        mein_pixel(80 +80, 50 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(90 +80, 60 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])   
        mein_pixel(100 +80, 270 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])     
        mein_pixel(90 +80, 290 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])      
        mein_pixel(100 +80, 290 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])    
        mein_pixel(70 +80, 300 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])  
        mein_pixel(80 +80, 300 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(90 +80, 300 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(100 +80, 300 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(80 +80, 310 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(90 +80, 310 +80, [my_fill[0], my_fill[1] -25, my_fill[2]]) 
        mein_pixel(100 +80, 310 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])
        mein_pixel(100 +80, 320 +80, [my_fill[0], my_fill[1] -25, my_fill[2]])






# =============================================================================
# Umriss
# =============================================================================
def umriss_funktion():

    mein_pix(x_von = 17, x_bis = 18, y_von = 27, y_bis = 31, size = size, Farbe = [0,0,0])    

    mein_pixel(330 +80, 250 +80, [0,0,0])

    mein_pixel(320 +80, 10 +80, [0,0,0])
    mein_pixel(330 +80, 10 +80, [0,0,0])
    mein_pixel(340 +80, 10 +80, [0,0,0])
    mein_pixel(350 +80, 10 +80, [0,0,0])
    mein_pixel(360 +80, 10 +80, [0,0,0])
    mein_pixel(370 +80, 10 +80, [0,0,0])
    
    mein_pixel(310 +80, 20 +80, [0,0,0])
    mein_pixel(350 +80, 20 +80, [0,0,0])
    mein_pixel(360 +80, 20 +80, [0,0,0])
    mein_pixel(370 +80, 20 +80, [0,0,0])
    
    mein_pixel(40 +80, 30 +80, [0,0,0])   
    mein_pixel(50 +80, 30 +80, [0,0,0]) 
    mein_pixel(60 +80, 30 +80, [0,0,0]) 
    mein_pixel(70 +80, 30 +80, [0,0,0]) 
    mein_pixel(80 +80, 30 +80, [0,0,0]) 
    mein_pixel(90 +80, 30 +80, [0,0,0]) 
    mein_pixel(300 +80, 30 +80, [0,0,0])  
    mein_pixel(350 +80, 30 +80, [0,0,0])   
    mein_pixel(360 +80, 30 +80, [0,0,0])   
    
    mein_pixel(40 +80, 40 +80, [0,0,0])     
    mein_pixel(50 +80, 40 +80, [0,0,0])     
    mein_pixel(60 +80, 40 +80, [0,0,0])     
    mein_pixel(100 +80, 40 +80, [0,0,0])    
    mein_pixel(110 +80, 40 +80, [0,0,0])    
    mein_pixel(120 +80, 40 +80, [0,0,0])    
    mein_pixel(130 +80, 40 +80, [0,0,0])    
    mein_pixel(290 +80, 40 +80, [0,0,0])
    mein_pixel(350 +80, 40 +80, [0,0,0]) 
    mein_pixel(360 +80, 40 +80, [0,0,0]) 
    
    mein_pixel(60 +80, 50 +80, [0,0,0]) 
    mein_pixel(70 +80, 50 +80, [0,0,0])
    mein_pixel(140 +80, 50 +80, [0,0,0]) 
    mein_pixel(150 +80, 50 +80, [0,0,0])
    mein_pixel(160 +80, 50 +80, [0,0,0]) 
    mein_pixel(170 +80, 50 +80, [0,0,0]) 
    mein_pixel(190 +80, 50 +80, [0,0,0])
    mein_pixel(200 +80, 50 +80, [0,0,0])
    mein_pixel(210 +80, 50 +80, [0,0,0])
    mein_pixel(220 +80, 50 +80, [0,0,0])
    mein_pixel(230 +80, 50 +80, [0,0,0])
    mein_pixel(240 +80, 50 +80, [0,0,0])
    mein_pixel(250 +80, 50 +80, [0,0,0])
    mein_pixel(270 +80, 50 +80, [0,0,0])
    mein_pixel(280 +80, 50 +80, [0,0,0])
    mein_pixel(350 +80, 50 +80, [0,0,0])
    
    mein_pixel(70 +80, 60 +80, [0,0,0])
    mein_pixel(80 +80, 60 +80, [0,0,0])
    mein_pixel(180 +80, 60 +80, [0,0,0])
    mein_pixel(260 +80, 60 +80, [0,0,0])
    mein_pixel(340 +80, 60 +80, [0,0,0])
    
    mein_pixel(80 +80, 70 +80, [0,0,0])
    mein_pixel(90 +80, 70 +80, [0,0,0])
    mein_pixel(330 +80, 70 +80, [0,0,0])
    
    mein_pixel(90 +80, 80 +80, [0,0,0])
    mein_pixel(100 +80, 80 +80, [0,0,0])
    mein_pixel(320 +80, 80 +80, [0,0,0])
    
    mein_pixel(110 +80, 90 +80, [0,0,0])
    mein_pixel(120 +80, 90 +80, [0,0,0])
    mein_pixel(310 +80, 90 +80, [0,0,0])

    mein_pixel(10 +80, 100 +80, [0,0,0])
    mein_pixel(130 +80, 100 +80, [0,0,0])
    mein_pixel(310 +80, 100 +80, [0,0,0])
    
    mein_pixel(10 +80, 110 +80, [0,0,0])
    mein_pixel(20 +80, 110 +80, [0,0,0])
    mein_pixel(130 +80, 110 +80, [0,0,0])
    mein_pixel(310 +80, 110 +80, [0,0,0])    
    
    mein_pixel(10 +80, 120 +80, [0,0,0])
    mein_pixel(30 +80, 120 +80, [0,0,0])    
    mein_pixel(120 +80, 120 +80, [0,0,0]) 
    mein_pixel(320 +80, 120 +80, [0,0,0])   

    mein_pixel(10 +80, 130 +80, [0,0,0])
    mein_pixel(40 +80, 130 +80, [0,0,0])   
    mein_pixel(120 +80, 130 +80, [0,0,0])      
    mein_pixel(320 +80, 130 +80, [0,0,0])   

    mein_pixel(10 +80, 140 +80, [0,0,0])
    mein_pixel(50 +80, 140 +80, [0,0,0])    
    mein_pixel(120 +80, 140 +80, [0,0,0])        
    mein_pixel(320 +80, 140 +80, [0,0,0])        
    
    mein_pixel(10 +80, 150 +80, [0,0,0])    
    mein_pixel(60 +80, 150 +80, [0,0,0])     
    mein_pixel(110 +80, 150 +80, [0,0,0])        
    mein_pixel(220 +80, 150 +80, [0,0,0])        
    mein_pixel(230 +80, 150 +80, [0,0,0])        
    mein_pixel(330 +80, 150 +80, [0,0,0])    
    
    mein_pixel(10 +80, 160 +80, [0,0,0])  
    mein_pixel(70 +80, 160 +80, [0,0,0])      
    mein_pixel(110 +80, 160 +80, [0,0,0])          
    mein_pixel(330 +80, 160 +80, [0,0,0])   

    mein_pixel(10 +80, 170 +80, [0,0,0])
    mein_pixel(80 +80, 170 +80, [0,0,0])
    mein_pixel(110 +80, 170 +80, [0,0,0])
    mein_pixel(330 +80, 170 +80, [0,0,0]) 

    mein_pixel(10 +80, 180 +80, [0,0,0])
    mein_pixel(90 +80, 180 +80, [0,0,0])
    mein_pixel(110 +80, 180 +80, [0,0,0])
    mein_pixel(330 +80, 180 +80, [0,0,0])

    
    mein_pixel(10 +80, 190 +80, [0,0,0])  
    mein_pixel(110 +80, 190 +80, [0,0,0])  
    mein_pixel(120 +80, 190 +80, [0,0,0])    
    mein_pixel(320 +80, 190 +80, [0,0,0])  
    mein_pixel(320 +80, 200 +80, [0,0,0])  
    
    mein_pixel(10 +80, 200 +80, [0,0,0]) 
    mein_pixel(120 +80, 200 +80, [0,0,0])   
    mein_pixel(310 +80, 200 +80, [0,0,0])       
    
    mein_pixel(20 +80, 210 +80, [0,0,0])
    mein_pixel(130 +80, 210 +80, [0,0,0])   
    mein_pixel(310 +80, 210 +80, [0,0,0])    
    
    mein_pixel(30 +80, 220 +80, [0,0,0])
    mein_pixel(120 +80, 220 +80, [0,0,0])
    mein_pixel(130 +80, 220 +80, [0,0,0]) 
    mein_pixel(320 +80, 220 +80, [0,0,0])  
    
    mein_pixel(40 +80, 230 +80, [0,0,0])    
    mein_pixel(90 +80, 230 +80, [0,0,0])        
    mein_pixel(120 +80, 230 +80, [0,0,0])        
    mein_pixel(130 +80, 230 +80, [0,0,0])        
    mein_pixel(320 +80, 230 +80, [0,0,0])        
    
    mein_pixel(30 +80, 240 +80, [0,0,0])   
    mein_pixel(80 +80, 240 +80, [0,0,0])  
    mein_pixel(120 +80, 240 +80, [0,0,0])  
    mein_pixel(320 +80, 240 +80, [0,0,0])       
    
    mein_pixel(30 +80, 250 +80, [0,0,0])    
    mein_pixel(90 +80, 250 +80, [0,0,0])   
    mein_pixel(110 +80, 250 +80, [0,0,0])   
    mein_pixel(320 +80, 250 +80, [0,0,0])    
    
    mein_pixel(40 +80, 260 +80, [0,0,0])      
    mein_pixel(100 +80, 260 +80, [0,0,0])         
    mein_pixel(110 +80, 260 +80, [0,0,0])       
    mein_pixel(330 +80, 260 +80, [0,0,0]) 

    mein_pixel(50 +80, 270 +80, [0,0,0]) 
    mein_pixel(110 +80, 270 +80, [0,0,0]) 
    mein_pixel(330 +80, 270 +80, [0,0,0]) 
    
    mein_pixel(60 +80, 280 +80, [0,0,0])     
    mein_pixel(100 +80, 280 +80, [0,0,0])      
    mein_pixel(110 +80, 280 +80, [0,0,0])      
    mein_pixel(330 +80, 280 +80, [0,0,0])     
    
    mein_pixel(70 +80, 290 +80, [0,0,0])     
    mein_pixel(110 +80, 290 +80, [0,0,0])       
    mein_pixel(330 +80, 290 +80, [0,0,0]) 

    mein_pixel(60 +80, 300 +80, [0,0,0]) 
    mein_pixel(110 +80, 300 +80, [0,0,0])  
    mein_pixel(330 +80, 300 +80, [0,0,0])     
    
    mein_pixel(70 +80, 310 +80, [0,0,0])     
    mein_pixel(110 +80, 310 +80, [0,0,0])        
    mein_pixel(330 +80, 310 +80, [0,0,0])  
    
    mein_pixel(80 +80, 320 +80, [0,0,0])     
    mein_pixel(90 +80, 320 +80, [0,0,0])  
    mein_pixel(110 +80, 320 +80, [0,0,0])  
    mein_pixel(330 +80, 320 +80, [0,0,0])  

    mein_pixel(100 +80, 330 +80, [0,0,0])
    mein_pixel(110 +80, 330 +80, [0,0,0])
    mein_pixel(120 +80, 330 +80, [0,0,0])
    mein_pixel(320 +80, 330 +80, [0,0,0])
    
    mein_pixel(120 +80, 340 +80, [0,0,0])
    mein_pixel(320 +80, 340 +80, [0,0,0])

    mein_pixel(130 +80, 350 +80, [0,0,0])
    mein_pixel(310 +80, 350 +80, [0,0,0])

    mein_pixel(140 +80, 360 +80, [0,0,0])
    mein_pixel(190 +80, 360 +80, [0,0,0])
    mein_pixel(200 +80, 360 +80, [0,0,0])
    mein_pixel(210 +80, 360 +80, [0,0,0])
    mein_pixel(220 +80, 360 +80, [0,0,0])
    mein_pixel(230 +80, 360 +80, [0,0,0])
    mein_pixel(240 +80, 360 +80, [0,0,0])
    mein_pixel(250 +80, 360 +80, [0,0,0])
    mein_pixel(300 +80, 360 +80, [0,0,0])    
    
    mein_pixel(130 +80, 370 +80, [0,0,0])    
    mein_pixel(170 +80, 370 +80, [0,0,0])  
    mein_pixel(180 +80, 370 +80, [0,0,0])  
    mein_pixel(190 +80, 370 +80, [0,0,0])  
    mein_pixel(260 +80, 370 +80, [0,0,0])  
    mein_pixel(270 +80, 370 +80, [0,0,0])  
    mein_pixel(310 +80, 370 +80, [0,0,0])  
    
    mein_pixel(130 +80, 380 +80, [0,0,0])
    mein_pixel(140 +80, 380 +80, [0,0,0]) 
    mein_pixel(150 +80, 380 +80, [0,0,0]) 
    mein_pixel(160 +80, 380 +80, [0,0,0]) 
    mein_pixel(170 +80, 380 +80, [0,0,0]) 
    mein_pixel(270 +80, 380 +80, [0,0,0]) 
    mein_pixel(280 +80, 380 +80, [0,0,0]) 
    mein_pixel(290 +80, 380 +80, [0,0,0]) 
    mein_pixel(300 +80, 380 +80, [0,0,0]) 
    mein_pixel(310 +80, 380 +80, [0,0,0]) 


# =============================================================================
# Jacke
# =============================================================================

def kleidung_funktion(cloth):
    
    if cloth == "Blue Jacket":
        mein_pix(21, 40, 31, 41, size, [0, 91, 226])
        mein_pix(20, 21, 33, 41, size, [0, 91, 226])
        mein_pix(40, 41, 33, 41, size, [0, 91, 226])
    
    if cloth == "Blue Pants":
        mein_pix(22, 39, 36, 44, size, [0, 91, 226])
        mein_pix(20, 21, 36, 41, size, [0, 91, 226])
        mein_pix(21, 22, 36, 43, size, [0, 91, 226])
        mein_pix(39, 40, 36, 43, size, [0, 91, 226])
        mein_pix(40, 41, 36, 41, size, [0, 91, 226])


    if cloth == "Pink Jacket":
        mein_pix(21, 40, 31, 41, size, [255,153,255])
        mein_pix(20, 21, 33, 41, size, [255,153,255])
        mein_pix(40, 41, 33, 41, size, [255,153,255])
    
    if cloth == "Pink Pants":
        mein_pix(22, 39, 36, 44, size, [255,153,255])
        mein_pix(20, 21, 36, 41, size, [255,153,255])
        mein_pix(21, 22, 36, 43, size, [255,153,255])
        mein_pix(39, 40, 36, 43, size, [255,153,255])
        mein_pix(40, 41, 36, 41, size, [255,153,255])


    if cloth == "Grey Jacket":
        mein_pix(21, 40, 31, 41, size, [40,40,40])
        mein_pix(20, 21, 33, 41, size, [40,40,40])
        mein_pix(40, 41, 33, 41, size, [40,40,40])
    
    if cloth == "Grey Pants":
        mein_pix(22, 39, 36, 44, size, [40,40,40])
        mein_pix(20, 21, 36, 41, size, [40,40,40])
        mein_pix(21, 22, 36, 43, size, [40,40,40])
        mein_pix(39, 40, 36, 43, size, [40,40,40])
        mein_pix(40, 41, 36, 41, size, [40,40,40])



# =============================================================================
# Arme
# =============================================================================
def arm_funktion(color_fuellung):
    
    if color_fuellung == "Orange": #orange
        my_fill = [255,102,0]

        mein_pix(24, 28, 35, 38, size, my_fill)
        mein_pix(34, 38, 35, 38, size, my_fill)
        
    
        mein_pixel(150 +80, 250 +80, [0,0,0]) 
        mein_pixel(190 +80, 250 +80, [0,0,0]) 
        mein_pixel(260 +80, 250 +80, [0,0,0]) 
        mein_pixel(300 +80, 250 +80, [0,0,0]) 
    
        mein_pixel(150 +80, 260 +80, [0,0,0])      
        mein_pixel(200 +80, 260 +80, [0,0,0])      
        mein_pixel(250 +80, 260 +80, [0,0,0]) 
        mein_pixel(300 +80, 260 +80, [0,0,0]) 
    
        mein_pixel(160 +80, 270 +80, [0,0,0]) 
        mein_pixel(200 +80, 270 +80, [0,0,0]) 
        mein_pixel(250 +80, 270 +80, [0,0,0]) 
        mein_pixel(290 +80, 270 +80, [0,0,0])     
    
        mein_pixel(160 +80, 280 +80, [0,0,0]) 
        mein_pixel(200 +80, 280 +80, [0,0,0]) 
        mein_pixel(250 +80, 280 +80, [0,0,0])     
        mein_pixel(290 +80, 280 +80, [0,0,0])     
    
        mein_pix(50, 52, 75, 76, 10, [0,0,0])
        mein_pixel(200 +80, 290 +80, [0,0,0]) 
        mein_pixel(250 +80, 290 +80, [0,0,0]) 
        mein_pixel(280 +80, 290 +80, [0,0,0]) 
    
        mein_pixel(180 +80, 300 +80, [0,0,0])  
        mein_pixel(190 +80, 300 +80, [0,0,0])  
        mein_pixel(260 +80, 300 +80, [0,0,0])  
        mein_pixel(270 +80, 300 +80, [0,0,0])      
    
        mein_pixel(150 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
        mein_pixel(300 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
    
        mein_pixel(150 +80, 280 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])   
        mein_pixel(300 +80, 280 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
    
        mein_pixel(160 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(290 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
    
        mein_pixel(170 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(280 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 



    if color_fuellung == "Beige": #beige
        my_fill = [249,228,183]
        
        
        mein_pix(24, 28, 35, 38, size, my_fill)
        mein_pix(34, 38, 35, 38, size, my_fill)
        
    
        mein_pixel(150 +80, 250 +80, [0,0,0]) 
        mein_pixel(190 +80, 250 +80, [0,0,0]) 
        mein_pixel(260 +80, 250 +80, [0,0,0]) 
        mein_pixel(300 +80, 250 +80, [0,0,0]) 
    
        mein_pixel(150 +80, 260 +80, [0,0,0])      
        mein_pixel(200 +80, 260 +80, [0,0,0])      
        mein_pixel(250 +80, 260 +80, [0,0,0]) 
        mein_pixel(300 +80, 260 +80, [0,0,0]) 
    
        mein_pixel(160 +80, 270 +80, [0,0,0]) 
        mein_pixel(200 +80, 270 +80, [0,0,0]) 
        mein_pixel(250 +80, 270 +80, [0,0,0]) 
        mein_pixel(290 +80, 270 +80, [0,0,0])     
    
        mein_pixel(160 +80, 280 +80, [0,0,0]) 
        mein_pixel(200 +80, 280 +80, [0,0,0]) 
        mein_pixel(250 +80, 280 +80, [0,0,0])     
        mein_pixel(290 +80, 280 +80, [0,0,0])     
    
        mein_pix(50, 52, 75, 76, 10, [0,0,0])
        mein_pixel(200 +80, 290 +80, [0,0,0]) 
        mein_pixel(250 +80, 290 +80, [0,0,0]) 
        mein_pixel(280 +80, 290 +80, [0,0,0]) 
    
        mein_pixel(180 +80, 300 +80, [0,0,0])  
        mein_pixel(190 +80, 300 +80, [0,0,0])  
        mein_pixel(260 +80, 300 +80, [0,0,0])  
        mein_pixel(270 +80, 300 +80, [0,0,0])      
    
        mein_pixel(150 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
        mein_pixel(300 +80, 270 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])  
    
        mein_pixel(150 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]])   
        mein_pixel(300 +80, 280 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
    
        mein_pixel(160 +80, 290 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(290 +80, 290 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
    
        mein_pixel(170 +80, 300 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        mein_pixel(280 +80, 300 +80, [my_fill[0], my_fill[1] -50, my_fill[2]]) 
        
        
        
    
    if color_fuellung == "Yellow": #yellow
        my_fill = [243, 231, 29]
    
        mein_pix(24, 28, 35, 38, size, my_fill)
        mein_pix(34, 38, 35, 38, size, my_fill)
        
    
        mein_pixel(150 +80, 250 +80, [0,0,0]) 
        mein_pixel(190 +80, 250 +80, [0,0,0]) 
        mein_pixel(260 +80, 250 +80, [0,0,0]) 
        mein_pixel(300 +80, 250 +80, [0,0,0]) 
    
        mein_pixel(150 +80, 260 +80, [0,0,0])      
        mein_pixel(200 +80, 260 +80, [0,0,0])      
        mein_pixel(250 +80, 260 +80, [0,0,0]) 
        mein_pixel(300 +80, 260 +80, [0,0,0]) 
    
        mein_pixel(160 +80, 270 +80, [0,0,0]) 
        mein_pixel(200 +80, 270 +80, [0,0,0]) 
        mein_pixel(250 +80, 270 +80, [0,0,0]) 
        mein_pixel(290 +80, 270 +80, [0,0,0])     
    
        mein_pixel(160 +80, 280 +80, [0,0,0]) 
        mein_pixel(200 +80, 280 +80, [0,0,0]) 
        mein_pixel(250 +80, 280 +80, [0,0,0])     
        mein_pixel(290 +80, 280 +80, [0,0,0])     
    
        mein_pix(50, 52, 75, 76, 10, [0,0,0])
        mein_pixel(200 +80, 290 +80, [0,0,0]) 
        mein_pixel(250 +80, 290 +80, [0,0,0]) 
        mein_pixel(280 +80, 290 +80, [0,0,0]) 
    
        mein_pixel(180 +80, 300 +80, [0,0,0])  
        mein_pixel(190 +80, 300 +80, [0,0,0])  
        mein_pixel(260 +80, 300 +80, [0,0,0])  
        mein_pixel(270 +80, 300 +80, [0,0,0])      
    
        mein_pixel(150 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
        mein_pixel(300 +80, 270 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])  
    
        mein_pixel(150 +80, 280 +80, [my_fill[0], my_fill[1] -100, my_fill[2]])   
        mein_pixel(300 +80, 280 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
    
        mein_pixel(160 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(290 +80, 290 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
    
        mein_pixel(170 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 
        mein_pixel(280 +80, 300 +80, [my_fill[0], my_fill[1] -100, my_fill[2]]) 




# =============================================================================
# Uhr
# =============================================================================
def watch_funktion(zahl):
    if zahl == "Silver Watch 3":

        # =============================================================================
        # 3 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [192,192,192])
        mein_pix(102, 110, 141, 149, 5, [192,192,192])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])
        mein_pix(105, 108, 144, 146, 5, [0,0,0])

    if zahl == "Silver Watch 6":

        # =============================================================================
        # 6 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [192,192,192])
        mein_pix(102, 110, 141, 149, 5, [192,192,192])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 148, 5, [0,0,0])

    if zahl == "Silver Watch 9":

        # =============================================================================
        # 9 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [192,192,192])
        mein_pix(102, 110, 141, 149, 5, [192,192,192])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])
        mein_pix(104, 107, 144, 146, 5, [0,0,0])


    if zahl == "Silver Watch 12":
    
        # =============================================================================
        # 12 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [192,192,192])
        mein_pix(102, 110, 141, 149, 5, [192,192,192])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])


    if zahl == "Golden Watch 3":

        # =============================================================================
        # 3 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [211,175,55])
        mein_pix(102, 110, 141, 149, 5, [211,175,55])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])
        mein_pix(105, 108, 144, 146, 5, [0,0,0])

    if zahl == "Golden Watch 6":

        # =============================================================================
        # 6 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [211,175,55])
        mein_pix(102, 110, 141, 149, 5, [211,175,55])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 148, 5, [0,0,0])

    if zahl == "Golden Watch 9":

        # =============================================================================
        # 9 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [211,175,55])
        mein_pix(102, 110, 141, 149, 5, [211,175,55])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])
        mein_pix(104, 107, 144, 146, 5, [0,0,0])


    if zahl == "Golden Watch 12":
    
        # =============================================================================
        # 12 Uhr
        # =============================================================================        

        mein_pix(96, 116, 143, 147, 5, [211,175,55])
        mein_pix(102, 110, 141, 149, 5, [211,175,55])
        mein_pix(52, 54, 71, 74, 10, [255,255,255])
        
        mein_pix(105, 107, 142, 145, 5, [0,0,0])




def kette_funktion(zahl):
    if zahl == "Silver Necklace USD": #USD
    
        fuellung = [200,200,200]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
   
        
        
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 120, x_bis = 127, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 120, x_bis = 121, y_von = 145, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 120, x_bis = 127, y_von = 149, y_bis = 150, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 126, x_bis = 127, y_von = 149, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 120, x_bis = 127, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        
        mein_pix(x_von = 122, x_bis = 123, y_von = 144, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 124, x_bis = 125, y_von = 144, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])


    if zahl == "Silver Necklace EUR": #EUR
    
        fuellung = [200,200,200]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
        
   
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 122, x_bis = 127, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 121, x_bis = 122, y_von = 146, y_bis = 147, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 120, x_bis = 121, y_von = 147, y_bis = 152, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 121, x_bis = 122, y_von = 152, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 122, x_bis = 127, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        
        mein_pix(x_von = 119, x_bis = 125, y_von = 150, y_bis = 151, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 119, x_bis = 125, y_von = 148, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])



    if zahl == "Silver Necklace BTC": #BTC
    
        fuellung = [200,200,200]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
        
  
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 120, x_bis = 126, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 121, x_bis = 126, y_von = 149, y_bis = 150, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 120, x_bis = 126, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        
        mein_pix(x_von = 126, x_bis = 127, y_von = 146, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 126, x_bis = 127, y_von = 150, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(x_von = 121, x_bis = 122, y_von = 145, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        
        
        mein_pix(x_von = 122, x_bis = 123, y_von = 144, y_bis = 145, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 122, x_bis = 123, y_von = 154, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(x_von = 124, x_bis = 125, y_von = 144, y_bis = 145, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(x_von = 124, x_bis = 125, y_von = 154, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])


    if zahl == "Silver Necklace ETH": #ETH
    
        fuellung = [200,200,200]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
        
   
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        for x in range(9):
            mein_pix(301+x, 303+x, y_von = 5+ 370-x-x, y_bis = 5+ 372, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        for x in range(9):
            mein_pix(309+x, 311+x, y_von = 5+ 354+x+x, y_bis = 5+ 372, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
            
        mein_pix(309, 310, y_von = 5+ 354, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])


        for x in range(5):
            mein_pix(301+x+x, 303+x+x, y_von = 5+ 370, y_bis = 5+ 372+x, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])
        for x in range(5):
            mein_pix(309+x+x, 311+x+x, y_von = 5+ 370, y_bis = 5+ 376-x, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2] - 150])


        mein_pix(310, 319, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])
        mein_pix(301, 310, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])

        mein_pix(310, 317, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2] - 150])
        mein_pix(303, 310, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])

        mein_pix(310, 315, y_von = 5+ 369, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2] - 150])
        mein_pix(305, 310, y_von = 5+ 369, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])

        mein_pix(310, 313, y_von = 5+ 368, y_bis = 5+ 369, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2] - 150])
        mein_pix(307, 310, y_von = 5+ 368, y_bis = 5+ 369, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])

        mein_pix(310, 311, y_von = 5+ 367, y_bis = 5+ 368, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2] - 150])
        mein_pix(309, 310, y_von = 5+ 367, y_bis = 5+ 368, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])

        mein_pix(309, 310, y_von = 5+ 367, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2] - 125])

        mein_pix(301, 302, y_von = 5+ 373, y_bis = 5+ 374, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(318, 319, y_von = 5+ 373, y_bis = 5+ 374, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(302, 304, y_von = 5+ 374, y_bis = 5+ 375, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(316, 318, y_von = 5+ 374, y_bis = 5+ 375, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(303, 306, y_von = 5+ 375, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(314, 317, y_von = 5+ 375, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(303, 308, y_von = 5+ 376, y_bis = 5+ 377, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(312, 317, y_von = 5+ 376, y_bis = 5+ 377, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(304, 310, y_von = 5+ 377, y_bis = 5+ 378, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 316, y_von = 5+ 377, y_bis = 5+ 378, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(305, 310, y_von = 5+ 378, y_bis = 5+ 379, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 315, y_von = 5+ 378, y_bis = 5+ 379, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(306, 310, y_von = 5+ 379, y_bis = 5+ 380, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 314, y_von = 5+ 379, y_bis = 5+ 380, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(307, 310, y_von = 5+ 380, y_bis = 5+ 382, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 313, y_von = 5+ 380, y_bis = 5+ 382, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(308, 310, y_von = 5+ 381, y_bis = 5+ 383, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 312, y_von = 5+ 381, y_bis = 5+ 383, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])

        mein_pix(309, 310, y_von = 5+ 382, y_bis = 5+ 384, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2] - 50])
        mein_pix(310, 311, y_von = 5+ 382, y_bis = 5+ 384, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2] - 100])





    if zahl == "Golden Necklace USD": #USD
    
        fuellung = [211,175,55]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])

        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 120, x_bis = 127, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 120, x_bis = 121, y_von = 145, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 120, x_bis = 127, y_von = 149, y_bis = 150, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 126, x_bis = 127, y_von = 149, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 120, x_bis = 127, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        
        mein_pix(x_von = 122, x_bis = 123, y_von = 144, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 124, x_bis = 125, y_von = 144, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])


    if zahl == "Golden Necklace EUR": #EUR
    
        fuellung = [211,175,55]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
        
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 122, x_bis = 127, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 121, x_bis = 122, y_von = 146, y_bis = 147, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 120, x_bis = 121, y_von = 147, y_bis = 152, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 121, x_bis = 122, y_von = 152, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 122, x_bis = 127, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        
        mein_pix(x_von = 119, x_bis = 125, y_von = 150, y_bis = 151, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 119, x_bis = 125, y_von = 148, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])


    if zahl == "Golden Necklace BTC": #BTC
    
        fuellung = [211,175,55]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])
        
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        mein_pix(x_von = 120, x_bis = 126, y_von = 145, y_bis = 146, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 121, x_bis = 126, y_von = 149, y_bis = 150, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 120, x_bis = 126, y_von = 153, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        
        mein_pix(x_von = 126, x_bis = 127, y_von = 146, y_bis = 149, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 126, x_bis = 127, y_von = 150, y_bis = 153, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(x_von = 121, x_bis = 122, y_von = 145, y_bis = 154, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        
        
        mein_pix(x_von = 122, x_bis = 123, y_von = 144, y_bis = 145, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 122, x_bis = 123, y_von = 154, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(x_von = 124, x_bis = 125, y_von = 144, y_bis = 145, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(x_von = 124, x_bis = 125, y_von = 154, y_bis = 155, size = 5, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])


    if zahl == "Golden Necklace ETH": #ETH
    
        fuellung = [211,175,55]
        mein_pix(x_von = 20, x_bis = 21, y_von = 29, y_bis = 30, size = size, Farbe = fuellung) 

        for x in range(20, 120, 20):
            
            mein_pixel(190 + x, 280 + int(x / 2), fuellung)
            mein_pixel(190 + x + 10, 280 + int(x / 2), fuellung)
            
            
            mein_pixel(410 - x, 280 + int(x / 2), fuellung)
            mein_pixel(410 - x + 10, 280 + int(x / 2), fuellung)
                
        mein_pixel(410, 270, [0,0,0])

    
        #Anhänger
        mein_pix(x_von = 123, x_bis = 125, y_von = 136, y_bis = 142, size = 5, Farbe = fuellung)
        
        for x in range(15):        
            mein_pix(292, 328, 360+x+x, 362+x+x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 360-x-x, 362-x-x, 2, fuellung)
        
        for x in range(5):
            mein_pix(292+x, 328-x, 390+x+x, 392+x+x, 2, fuellung)


        for x in range(9):
            mein_pix(301+x, 303+x, y_von = 5+ 370-x-x, y_bis = 5+ 372, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        for x in range(9):
            mein_pix(309+x, 311+x, y_von = 5+ 354+x+x, y_bis = 5+ 372, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
            
        mein_pix(309, 310, y_von = 5+ 354, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])


        for x in range(5):
            mein_pix(301+x+x, 303+x+x, y_von = 5+ 370, y_bis = 5+ 372+x, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])
        for x in range(5):
            mein_pix(309+x+x, 311+x+x, y_von = 5+ 370, y_bis = 5+ 376-x, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2]])


        mein_pix(310, 319, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])
        mein_pix(301, 310, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])

        mein_pix(310, 317, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2]])
        mein_pix(303, 310, y_von = 5+ 370, y_bis = 5+ 371, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])

        mein_pix(310, 315, y_von = 5+ 369, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2]])
        mein_pix(305, 310, y_von = 5+ 369, y_bis = 5+ 370, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])

        mein_pix(310, 313, y_von = 5+ 368, y_bis = 5+ 369, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2]])
        mein_pix(307, 310, y_von = 5+ 368, y_bis = 5+ 369, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])

        mein_pix(310, 311, y_von = 5+ 367, y_bis = 5+ 368, size = 2, Farbe = [fuellung[0] -150, fuellung[1] -150, fuellung[2]])
        mein_pix(309, 310, y_von = 5+ 367, y_bis = 5+ 368, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])

        mein_pix(309, 310, y_von = 5+ 367, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -125, fuellung[1] -125, fuellung[2]])

        mein_pix(301, 302, y_von = 5+ 373, y_bis = 5+ 374, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(318, 319, y_von = 5+ 373, y_bis = 5+ 374, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(302, 304, y_von = 5+ 374, y_bis = 5+ 375, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(316, 318, y_von = 5+ 374, y_bis = 5+ 375, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(303, 306, y_von = 5+ 375, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(314, 317, y_von = 5+ 375, y_bis = 5+ 376, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(303, 308, y_von = 5+ 376, y_bis = 5+ 377, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(312, 317, y_von = 5+ 376, y_bis = 5+ 377, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(304, 310, y_von = 5+ 377, y_bis = 5+ 378, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 316, y_von = 5+ 377, y_bis = 5+ 378, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(305, 310, y_von = 5+ 378, y_bis = 5+ 379, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 315, y_von = 5+ 378, y_bis = 5+ 379, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(306, 310, y_von = 5+ 379, y_bis = 5+ 380, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 314, y_von = 5+ 379, y_bis = 5+ 380, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(307, 310, y_von = 5+ 380, y_bis = 5+ 382, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 313, y_von = 5+ 380, y_bis = 5+ 382, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(308, 310, y_von = 5+ 381, y_bis = 5+ 383, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 312, y_von = 5+ 381, y_bis = 5+ 383, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])

        mein_pix(309, 310, y_von = 5+ 382, y_bis = 5+ 384, size = 2, Farbe = [fuellung[0] -50, fuellung[1] -50, fuellung[2]])
        mein_pix(310, 311, y_von = 5+ 382, y_bis = 5+ 384, size = 2, Farbe = [fuellung[0] -100, fuellung[1] -100, fuellung[2]])



# =============================================================================
# Mund
# =============================================================================
def mund_funktion(zahl):
    if zahl == "Happy":
        mein_pixel(190 +80, 170 +80, [0,0,0])
        mein_pixel(220 +80, 170 +80, [0,0,0])
        mein_pixel(230 +80, 170 +80, [0,0,0])   
        mein_pixel(260 +80, 170 +80, [0,0,0])   
        mein_pixel(200 +80, 180 +80, [0,0,0])
        mein_pixel(210 +80, 180 +80, [0,0,0]) 
        mein_pixel(240 +80, 180 +80, [0,0,0])
        mein_pixel(250 +80, 180 +80, [0,0,0])

    if zahl == "Happy Tongue":
        mein_pixel(190 +80, 170 +80, [0,0,0])
        mein_pixel(220 +80, 170 +80, [0,0,0])
        mein_pixel(230 +80, 170 +80, [0,0,0])   
        mein_pixel(260 +80, 170 +80, [0,0,0])   
        mein_pixel(200 +80, 180 +80, [0,0,0])
        mein_pixel(210 +80, 180 +80, [0,0,0]) 
        mein_pixel(240 +80, 180 +80, [0,0,0])
        mein_pixel(250 +80, 180 +80, [0,0,0])
        mein_pixel(220 +80, 180 +80, [255,144,142])
        mein_pixel(230 +80, 180 +80, [255,144,142])
        for x in range(8):
            mein_pix(x_von = 290+x, x_bis = 330-x, y_von = 270+x+x, y_bis = 272+x+x, size = 2, Farbe = [255,144,142])
       
        
    if zahl == "Sad": #traurig
        mein_pix(x_von = 29, x_bis = 33, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 28, x_bis = 29, y_von = 27, y_bis = 28, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 33, x_bis = 34, y_von = 27, y_bis = 28, size = size, Farbe = [0,0,0])    

    if zahl == "Cold": #neutral
        mein_pix(x_von = 29, x_bis = 33, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    

    if zahl == "Dirty": #checka1
        mein_pix(x_von = 29, x_bis = 33, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 33, x_bis = 34, y_von = 25, y_bis = 26, size = size, Farbe = [0,0,0])    

    if zahl == "Cigarette": #zigarette
        mein_pix(x_von = 34, x_bis = 36, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 36, x_bis = 37, y_von = 26, y_bis = 27, size = size, Farbe = [255,192,0])    
        mein_pix(x_von = 37, x_bis = 43, y_von = 26, y_bis = 27, size = size, Farbe = [240,240,240])    
        mein_pix(x_von = 43, x_bis = 44, y_von = 26, y_bis = 27, size = size, Farbe = [255,37,1])    
        mein_pix(x_von = 43, x_bis = 44, y_von = 20, y_bis = 25, size = size, Farbe = [190,190,190])    

    if zahl == "Joint": #joint
        mein_pix(x_von = 34, x_bis = 36, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    


        joint_start = 1
        for x in range(10,120,10):
            mein_pix(x_von = 350+x, x_bis = 430, y_von = 264-joint_start, y_bis = 266-joint_start, size = 2, Farbe = [191,253,194])    
            joint_start = joint_start + 1
        joint_start = 1
        for x in range(10,120,10):
            mein_pix(x_von = 350+x, x_bis = 430, y_von = 264+joint_start, y_bis = 266+joint_start, size = 2, Farbe = [191,253,194])    
            joint_start = joint_start + 1

        mein_pix(x_von = 430, x_bis = 440, y_von = 257, y_bis = 273, size = 2, Farbe = [255,37,1])    

        mein_pix(x_von = 43, x_bis = 44, y_von = 20, y_bis = 25, size = size, Farbe = [190,190,190])    


    if zahl == "Pipe": #Pfeife
        mein_pix(x_von = 34, x_bis = 36, y_von = 26, y_bis = 27, size = size, Farbe = [0,0,0])    


        for x in range(6):
            mein_pix(x_von = 36+x, x_bis = 37+x, y_von = 26+x, y_bis = 27+x, size = size, Farbe = [150,69,13])    
        
        for x in range(6):
            mein_pix(x_von = 37+x, x_bis = 38+x, y_von = 26+x, y_bis = 27+x, size = size, Farbe = [0,0,0])    
        
        for x in range(7):
            mein_pix(x_von = 36+x, x_bis = 37+x, y_von = 27+x, y_bis = 28+x, size = size, Farbe = [0,0,0])    
        
        mein_pix(x_von = 42, x_bis = 47, y_von = 32, y_bis = 33, size = size, Farbe = [150,69,13])    
        mein_pix(x_von = 44, x_bis = 48, y_von = 30, y_bis = 32, size = size, Farbe = [150,69,13])    
        
        mein_pix(x_von = 42, x_bis = 47, y_von = 33, y_bis = 34, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 46, x_bis = 47, y_von = 32, y_bis = 33, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 47, x_bis = 48, y_von = 30, y_bis = 32, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 44, x_bis = 48, y_von = 29, y_bis = 30, size = size, Farbe = [0,0,0])    
        mein_pix(x_von = 43, x_bis = 44, y_von = 29, y_bis = 32, size = size, Farbe = [0,0,0])    

        mein_pix(x_von = 45, x_bis = 46, y_von = 27, y_bis = 28, size = size, Farbe = [190,190,190])    
        mein_pix(x_von = 45, x_bis = 46, y_von = 25, y_bis = 26, size = size, Farbe = [190,190,190])    
        
        mein_pix(x_von = 44, x_bis = 47, y_von = 22, y_bis = 24, size = size, Farbe = [190,190,190])    
        mein_pix(x_von = 45, x_bis = 46, y_von = 21, y_bis = 22, size = size, Farbe = [190,190,190])    




# =============================================================================
# Cap
# =============================================================================
def head(zahl, color):
    if zahl == "Chinese Hat" and color == "Turquois":
        mein_pix(x_von = 24, x_bis = 36, y_von = 13, y_bis = 14, size = size, Farbe = [0,0,0])
        for x in range(10):
            mein_pix(x_von = 290+x, x_bis = 310-x, y_von = 87+x, y_bis = 88+x, size = 2, Farbe = [0,0,255])
        for x in range(9):
            mein_pix(x_von = 298-x, x_bis = 302+x, y_von = 73+x, y_bis = 79+x, size = 2, Farbe = [0,0,255])
        for x in range(0, 18):
            mein_pix(x_von = 250+x, x_bis = 350-x, y_von = 147-x-x-x, y_bis = 150-x-x-x, size = 2, Farbe = [0,0,255])
        mein_pix(x_von = 280, x_bis = 320, y_von = 105, y_bis = 110, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 275, x_bis = 325, y_von = 120, y_bis = 125, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 265, x_bis = 335, y_von = 135, y_bis = 140, size = 2, Farbe = [255,0,0])


    if zahl == "Chinese Hat" and color == "Pink":
        mein_pix(x_von = 24, x_bis = 36, y_von = 13, y_bis = 14, size = size, Farbe = [0,0,0])
        for x in range(10):
            mein_pix(x_von = 290+x, x_bis = 310-x, y_von = 87+x, y_bis = 88+x, size = 2, Farbe = [0,0,255])
        for x in range(9):
            mein_pix(x_von = 298-x, x_bis = 302+x, y_von = 73+x, y_bis = 79+x, size = 2, Farbe = [0,0,255])
        for x in range(0, 18):
            mein_pix(x_von = 250+x, x_bis = 350-x, y_von = 147-x-x-x, y_bis = 150-x-x-x, size = 2, Farbe = [0,0,255])
        mein_pix(x_von = 280, x_bis = 320, y_von = 105, y_bis = 110, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 275, x_bis = 325, y_von = 120, y_bis = 125, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 265, x_bis = 335, y_von = 135, y_bis = 140, size = 2, Farbe = [255,0,0])


    if zahl == "Chinese Hat" and color == "Purple":
        mein_pix(x_von = 24, x_bis = 36, y_von = 13, y_bis = 14, size = size, Farbe = [0,0,0])
        for x in range(10):
            mein_pix(x_von = 290+x, x_bis = 310-x, y_von = 87+x, y_bis = 88+x, size = 2, Farbe = [0,0,255])
        for x in range(9):
            mein_pix(x_von = 298-x, x_bis = 302+x, y_von = 73+x, y_bis = 79+x, size = 2, Farbe = [0,0,255])
        for x in range(0, 18):
            mein_pix(x_von = 250+x, x_bis = 350-x, y_von = 147-x-x-x, y_bis = 150-x-x-x, size = 2, Farbe = [0,0,255])
        mein_pix(x_von = 280, x_bis = 320, y_von = 105, y_bis = 110, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 275, x_bis = 325, y_von = 120, y_bis = 125, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 265, x_bis = 335, y_von = 135, y_bis = 140, size = 2, Farbe = [255,0,0])

        
    if zahl == "Chinese Hat" and color == "Green":
        mein_pix(x_von = 24, x_bis = 36, y_von = 13, y_bis = 14, size = size, Farbe = [0,0,0])
        for x in range(10):
            mein_pix(x_von = 290+x, x_bis = 310-x, y_von = 87+x, y_bis = 88+x, size = 2, Farbe = [0,0,255])
        for x in range(9):
            mein_pix(x_von = 298-x, x_bis = 302+x, y_von = 73+x, y_bis = 79+x, size = 2, Farbe = [0,0,255])
        for x in range(0, 18):
            mein_pix(x_von = 250+x, x_bis = 350-x, y_von = 147-x-x-x, y_bis = 150-x-x-x, size = 2, Farbe = [0,0,255])
        mein_pix(x_von = 280, x_bis = 320, y_von = 105, y_bis = 110, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 275, x_bis = 325, y_von = 120, y_bis = 125, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 265, x_bis = 335, y_von = 135, y_bis = 140, size = 2, Farbe = [255,0,0])


    if zahl == "Chinese Hat" and color == "Blue":
        mein_pix(x_von = 24, x_bis = 36, y_von = 13, y_bis = 14, size = size, Farbe = [0,0,0])
        for x in range(10):
            mein_pix(x_von = 290+x, x_bis = 310-x, y_von = 87+x, y_bis = 88+x, size = 2, Farbe = [0,0,255])
        for x in range(9):
            mein_pix(x_von = 298-x, x_bis = 302+x, y_von = 73+x, y_bis = 79+x, size = 2, Farbe = [0,0,255])
        for x in range(0, 18):
            mein_pix(x_von = 250+x, x_bis = 350-x, y_von = 147-x-x-x, y_bis = 150-x-x-x, size = 2, Farbe = [0,0,255])
        mein_pix(x_von = 280, x_bis = 320, y_von = 105, y_bis = 110, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 275, x_bis = 325, y_von = 120, y_bis = 125, size = 2, Farbe = [255,0,0])
        mein_pix(x_von = 265, x_bis = 335, y_von = 135, y_bis = 140, size = 2, Farbe = [255,0,0])


    if zahl == "Headband":
        mein_pix(x_von = 21, x_bis = 40, y_von = 17, y_bis = 18, size = size, Farbe = [255,0,0]) 
        mein_pix(x_von = 84, x_bis = 160, y_von = 72, y_bis = 75, size = 5, Farbe = [255,0,0]) 
        mein_pix(x_von = 100, x_bis = 144, y_von = 73, y_bis = 74, size = 5, Farbe = [255,255,255]) 
        mein_pix(x_von = 100, x_bis = 144, y_von = 71, y_bis = 72, size = 5, Farbe = [255,255,255]) 
        mein_pix(x_von = 100, x_bis = 144, y_von = 69, y_bis = 70, size = 5, Farbe = [255,255,255]) 
        
    if zahl == "Nippon Headband":
        mein_pix(x_von = 21, x_bis = 40, y_von = 17, y_bis = 18, size = size, Farbe = [255,255,255]) 
        mein_pix(x_von = 84, x_bis = 160, y_von = 72, y_bis = 77, size = 5, Farbe = [255,255,255]) 
        mein_pix(x_von = 121, x_bis = 126, y_von = 70, y_bis = 75, size = 5, Farbe = [255,0,0]) 
        
        mein_pix(x_von = 120, x_bis = 121, y_von = 71, y_bis = 74, size = 5, Farbe = [255,0,0]) 
        mein_pix(x_von = 126, x_bis = 127, y_von = 71, y_bis = 74, size = 5, Farbe = [255,0,0]) 
        
        mein_pix(x_von = 122, x_bis = 125, y_von = 69, y_bis = 70, size = 5, Farbe = [255,0,0]) 
        mein_pix(x_von = 122, x_bis = 125, y_von = 75, y_bis = 76, size = 5, Farbe = [255,0,0]) 

        
        
        
        

# =============================================================================
# Augen
# =============================================================================


def augen_funktion(zahl):
    if zahl == "Sweet": #Normal
   
        mein_pixel(180 +80, 120 +80, [0,0,0])
        mein_pixel(280 +80, 120 +80, [0,0,0])
        
        mein_pixel(170 +80, 110 +80, [0,0,0])
        mein_pixel(180 +80, 110 +80, [0,0,0])
        mein_pixel(270 +80, 110 +80, [0,0,0])
        mein_pixel(280 +80, 110 +80, [0,0,0])
        
        mein_pixel(160 +80, 120 +80, [0,0,0])
        mein_pixel(170 +80, 120 +80, [0,0,0])
        mein_pixel(190 +80, 120 +80, [0,0,0])
        mein_pixel(260 +80, 120 +80, [0,0,0])    
        mein_pixel(270 +80, 120 +80, [0,0,0])  
        mein_pixel(290 +80, 120 +80, [0,0,0])  
        
        mein_pixel(160 +80, 130 +80, [0,0,0])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [0,0,0])
        mein_pixel(190 +80, 130 +80, [0,0,0])    
        mein_pixel(260 +80, 130 +80, [0,0,0])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [0,0,0])
        mein_pixel(290 +80, 130 +80, [0,0,0])  
        
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])

        mein_pixel(180 +80, 120 +80, [255, 255, 255])
        mein_pixel(280 +80, 120 +80, [255, 255, 255])



    if zahl == "Cry Baby":
        
        mein_pixel(180 +80, 120 +80, [0,0,0])
        mein_pixel(280 +80, 120 +80, [0,0,0])
        mein_pixel(170 +80, 120 +80, [0,0,0])
        mein_pixel(270 +80, 120 +80, [0,0,0])  
        
        mein_pixel(160 +80, 130 +80, [0,0,0])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [0,0,0])
        mein_pixel(190 +80, 130 +80, [0,0,0])    
        mein_pixel(260 +80, 130 +80, [0,0,0])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [0,0,0])
        mein_pixel(290 +80, 130 +80, [0,0,0])  
        
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])
        
        mein_pixel(180 +80, 130 +80, [255, 255, 255])
        mein_pixel(270 +80, 130 +80, [255, 255, 255])
        
        mein_pix(26, 27, 23, 30, size, [255,255,255])
        mein_pix(35, 36, 23, 30, size, [255,255,255])
        
    if zahl == "Stoned":
        
        mein_pixel(160 +80, 130 +80, [0,0,0])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [0,0,0])
        mein_pixel(190 +80, 130 +80, [0,0,0])    
        mein_pixel(260 +80, 130 +80, [0,0,0])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [0,0,0])
        mein_pixel(290 +80, 130 +80, [0,0,0])  
        
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])
        
        mein_pixel(180 +80, 130 +80, [255, 255, 255])
        mein_pixel(280 +80, 130 +80, [255, 255, 255])
        

    if zahl == "VR": ## virtual reality
        
        mein_pix(24, 37, 16, 21, size, [0,0,0])
        mein_pix(25, 36, 17, 20, size, [255, 255, 255])
        mein_pix(24, 37, 15, 16, size, [100,100,100])
        mein_pix(23, 38, 21, 22, size, [100,100,100])
        
        mein_pix(23, 24, 15, 21, size, [100,100,100])
        mein_pix(37, 38, 15, 21, size, [100,100,100])

        mein_pix(21, 22, 17, 18, size, [0,0,0])
        mein_pix(22, 23, 16, 17, size, [0,0,0])
        mein_pix(22, 23, 17, 20, size, [100,100,100])
        mein_pix(38, 39, 17, 20, size, [100,100,100])
        mein_pix(38, 39, 16, 17, size, [0,0,0])


    if zahl == "Sweet Eye Patch": #Augenklappe1
   
        mein_pixel(180 +80, 120 +80, [0,0,0])
        mein_pixel(280 +80, 120 +80, [0,0,0])
        
        mein_pixel(170 +80, 110 +80, [0,0,0])
        mein_pixel(180 +80, 110 +80, [0,0,0])
        mein_pixel(270 +80, 110 +80, [0,0,0])
        mein_pixel(280 +80, 110 +80, [0,0,0])
        
        mein_pixel(160 +80, 120 +80, [0,0,0])
        mein_pixel(170 +80, 120 +80, [0,0,0])
        mein_pixel(190 +80, 120 +80, [0,0,0])
        mein_pixel(260 +80, 120 +80, [0,0,0])    
        mein_pixel(270 +80, 120 +80, [0,0,0])  
        mein_pixel(290 +80, 120 +80, [0,0,0])  
        
        mein_pixel(160 +80, 130 +80, [0,0,0])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [0,0,0])
        mein_pixel(190 +80, 130 +80, [0,0,0])    
        mein_pixel(260 +80, 130 +80, [0,0,0])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [0,0,0])
        mein_pixel(290 +80, 130 +80, [0,0,0])  
        
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])

        mein_pixel(180 +80, 120 +80, [255, 255, 255])
        mein_pixel(280 +80, 120 +80, [255, 255, 255])

        
        mein_pix(x_von = 19, x_bis = 39, y_von = 17, y_bis = 18, size = size, Farbe = [0,0,0]) 
        mein_pix(x_von = 21, x_bis = 30, y_von = 18, y_bis = 19, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 21, x_bis = 30, y_von = 19, y_bis = 20, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 22, x_bis = 29, y_von = 20, y_bis = 21, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 23, x_bis = 28, y_von = 21, y_bis = 22, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 24, x_bis = 26, y_von = 22, y_bis = 23, size = size, Farbe = [0,0,0])


    if zahl == "Stoned Eye Patch": #Augenklappe3
        
        mein_pixel(160 +80, 130 +80, [0,0,0])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [0,0,0])
        mein_pixel(190 +80, 130 +80, [0,0,0])    
        mein_pixel(260 +80, 130 +80, [0,0,0])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [0,0,0])
        mein_pixel(290 +80, 130 +80, [0,0,0])  
        
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])
        
        mein_pixel(180 +80, 130 +80, [255, 255, 255])
        mein_pixel(280 +80, 130 +80, [255, 255, 255])
        
        
        mein_pix(x_von = 19, x_bis = 39, y_von = 17, y_bis = 18, size = size, Farbe = [0,0,0]) 
        mein_pix(x_von = 21, x_bis = 30, y_von = 18, y_bis = 19, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 21, x_bis = 30, y_von = 19, y_bis = 20, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 22, x_bis = 29, y_von = 20, y_bis = 21, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 23, x_bis = 28, y_von = 21, y_bis = 22, size = size, Farbe = [0,0,0])
        mein_pix(x_von = 24, x_bis = 26, y_von = 22, y_bis = 23, size = size, Farbe = [0,0,0])


    if zahl == "3D": # 3D Brille
        #Umriss
        mein_pix(x_von = 19, x_bis = 41, y_von = 18, y_bis = 19, size = size, Farbe = [205,205,205]) 
        
        mein_pixel(130 +80, 110 +80, [205,205,205])
        mein_pixel(140 +80, 110 +80, [205,205,205])
        mein_pixel(220 +80, 110 +80, [205,205,205])
        mein_pixel(230 +80, 110 +80, [205,205,205])
        mein_pixel(310 +80, 110 +80, [205,205,205])
        mein_pixel(320 +80, 110 +80, [205,205,205])
        
        mein_pixel(130 +80, 120 +80, [205,205,205])
        mein_pixel(140 +80, 120 +80, [205,205,205])
        mein_pixel(220 +80, 120 +80, [205,205,205])
        mein_pixel(230 +80, 120 +80, [205,205,205])
        mein_pixel(310 +80, 120 +80, [205,205,205])
        mein_pixel(320 +80, 120 +80, [205,205,205])
        
        mein_pixel(130 +80, 130 +80, [205,205,205])
        mein_pixel(140 +80, 130 +80, [205,205,205])
        mein_pixel(220 +80, 130 +80, [205,205,205])
        mein_pixel(230 +80, 130 +80, [205,205,205])
        mein_pixel(310 +80, 130 +80, [205,205,205])
        mein_pixel(320 +80, 130 +80, [205,205,205])
        
        mein_pixel(130 +80, 140 +80, [205,205,205])
        mein_pixel(140 +80, 140 +80, [205,205,205])
        mein_pixel(220 +80, 140 +80, [205,205,205])
        mein_pixel(230 +80, 140 +80, [205,205,205])
        mein_pixel(310 +80, 140 +80, [205,205,205])
        mein_pixel(320 +80, 140 +80, [205,205,205])
        
        mein_pix(x_von = 21, x_bis = 41, y_von = 22, y_bis = 23, size = size, Farbe = [205,205,205]) 
        
        
        #Glasfarbe
        mein_pix(x_von = 23, x_bis = 30, y_von = 19, y_bis = 20, size = size, Farbe = [5,148,245])
        mein_pix(x_von = 23, x_bis = 30, y_von = 20, y_bis = 21, size = size, Farbe = [5,148,245])
        mein_pix(x_von = 23, x_bis = 30, y_von = 21, y_bis = 22, size = size, Farbe = [5,148,245])
        
        
        mein_pix(x_von = 32, x_bis = 39, y_von = 19, y_bis = 20, size = size, Farbe = [252,16,16])
        mein_pix(x_von = 32, x_bis = 39, y_von = 20, y_bis = 21, size = size, Farbe = [252,16,16])
        mein_pix(x_von = 32, x_bis = 39, y_von = 21, y_bis = 22, size = size, Farbe = [252,16,16])

    if zahl == "Sunglasses": # 3D Brille

        #Umriss
        mein_pix(x_von = 19, x_bis = 40, y_von = 18, y_bis = 19, size = size, Farbe = [0,0,0]) 
        
        mein_pixel(230 +80, 110 +80, [0,0,0])
        mein_pixel(230 +80, 110 +80, [0,0,0])
        mein_pixel(130 +80, 110 +80, [0,0,0])
        mein_pixel(140 +80, 110 +80, [255,255,255])
        mein_pixel(150 +80, 110 +80, [0,0,0])
        mein_pixel(160 +80, 110 +80, [255,255,255])
        mein_pixel(170 +80, 110 +80, [0,0,0])
        mein_pixel(180 +80, 110 +80, [0,0,0])
        mein_pixel(190 +80, 110 +80, [0,0,0])
        mein_pixel(200 +80, 110 +80, [0,0,0])
        mein_pixel(210 +80, 110 +80, [0,0,0])
        
        mein_pixel(240 +80, 110 +80, [255,255,255])
        mein_pixel(250 +80, 110 +80, [0,0,0])
        mein_pixel(260 +80, 110 +80, [255,255,255])
        mein_pixel(270 +80, 110 +80, [0,0,0])
        mein_pixel(280 +80, 110 +80, [0,0,0])
        mein_pixel(290 +80, 110 +80, [0,0,0])
        mein_pixel(300 +80, 110 +80, [0,0,0])
        mein_pixel(310 +80, 110 +80, [0,0,0])
        
        
        
        mein_pixel(140 +80, 120 +80, [0,0,0])
        mein_pixel(150 +80, 120 +80, [255,255,255])
        mein_pixel(160 +80, 120 +80, [0,0,0])
        mein_pixel(170 +80, 120 +80, [255,255,255])
        mein_pixel(180 +80, 120 +80, [0,0,0])
        mein_pixel(190 +80, 120 +80, [0,0,0])
        mein_pixel(200 +80, 120 +80, [0,0,0])
        mein_pixel(210 +80, 120 +80, [0,0,0])
        
        mein_pixel(240 +80, 120 +80, [0,0,0])
        mein_pixel(250 +80, 120 +80, [255,255,255])
        mein_pixel(260 +80, 120 +80, [0,0,0])
        mein_pixel(270 +80, 120 +80, [255,255,255])
        mein_pixel(280 +80, 120 +80, [0,0,0])
        mein_pixel(290 +80, 120 +80, [0,0,0])
        mein_pixel(300 +80, 120 +80, [0,0,0])
        
        
        mein_pixel(150 +80, 130 +80, [0,0,0])
        mein_pixel(160 +80, 130 +80, [255,255,255])
        mein_pixel(170 +80, 130 +80, [0,0,0])
        mein_pixel(180 +80, 130 +80, [255,255,255])
        mein_pixel(190 +80, 130 +80, [0,0,0])
        mein_pixel(200 +80, 130 +80, [0,0,0])
        
        mein_pixel(250 +80, 130 +80, [0,0,0])
        mein_pixel(260 +80, 130 +80, [255,255,255])
        mein_pixel(270 +80, 130 +80, [0,0,0])
        mein_pixel(280 +80, 130 +80, [255,255,255])
        mein_pixel(290 +80, 130 +80, [0,0,0])
        mein_pixel(300 +80, 130 +80, [0,0,0])
        
        
        mein_pixel(160 +80, 140 +80, [0,0,0])
        mein_pixel(170 +80, 140 +80, [0,0,0])
        mein_pixel(180 +80, 140 +80, [0,0,0])
        mein_pixel(190 +80, 140 +80, [0,0,0])
        
        mein_pixel(260 +80, 140 +80, [0,0,0])
        mein_pixel(270 +80, 140 +80, [0,0,0])
        mein_pixel(280 +80, 140 +80, [0,0,0])
        mein_pixel(290 +80, 140 +80, [0,0,0])
        


# =============================================================================
# baeckchen
# =============================================================================
def baeckchen_funktion():
    mein_pixel(140 +80, 150 +80, [231, 25, 3])     
    mein_pixel(150 +80, 150 +80, [231, 25, 3])      
    mein_pixel(300 +80, 150 +80, [231, 25, 3])     
    mein_pixel(310 +80, 150 +80, [231, 25, 3]) 

    mein_pixel(130 +80, 160 +80, [231, 25, 3])
    mein_pixel(140 +80, 160 +80, [231, 25, 3])
    mein_pixel(150 +80, 160 +80, [231, 25, 3])    
    mein_pixel(160 +80, 160 +80, [231, 25, 3])  
    mein_pixel(290 +80, 160 +80, [231, 25, 3])
    mein_pixel(300 +80, 160 +80, [231, 25, 3])
    mein_pixel(310 +80, 160 +80, [231, 25, 3])    
    mein_pixel(320 +80, 160 +80, [231, 25, 3])    
    
    mein_pixel(130 +80, 170 +80, [231, 25, 3])
    mein_pixel(140 +80, 170 +80, [231, 25, 3])
    mein_pixel(150 +80, 170 +80, [231, 25, 3])    
    mein_pixel(160 +80, 170 +80, [231, 25, 3])  
    mein_pixel(290 +80, 170 +80, [231, 25, 3])
    mein_pixel(300 +80, 170 +80, [231, 25, 3])
    mein_pixel(310 +80, 170 +80, [231, 25, 3])    
    mein_pixel(320 +80, 170 +80, [231, 25, 3])    
    
    mein_pixel(140 +80, 180 +80, [231, 25, 3])     
    mein_pixel(150 +80, 180 +80, [231, 25, 3])      
    mein_pixel(300 +80, 180 +80, [231, 25, 3])     
    mein_pixel(310 +80, 180 +80, [231, 25, 3]) 
    
    
    




#%%

os.chdir(r"C:\Users\AmirA\Desktop\Programming\Phyton-Skript\Pixel_Fotos\Pikachu\Bilder")


for x in range(0, 25000):
    print(x)

    # =============================================================================
    # Background - ohne Kombi
    # =============================================================================
    ["Turquois", "Pink", "Purple", "Green", "Blue"]
    data = layout_funktion(df.loc[x, "Background"])
    
    
    # =============================================================================
    # Füllung - ohne Kombi
    # =============================================================================
    fuellung = ["Yellow", "Yellow", "Yellow", "Yellow", "Yellow",
                "Yellow", "Yellow", "Yellow", "Orange", "Beige"]
    fuellung_funktion(df.loc[x, "Body"])
    
    
    umriss_funktion()
    baeckchen_funktion()
    
    
    # =============================================================================
    # Augen - mit Kombi
    # =============================================================================
    ["Sweet", "Cry Baby", "Stoned", "VR", "Sweet Eye Patch", "Stoned Eye Patch", "3D", "Sunglasses"]
    augen_funktion(df.loc[x, "Eyes"])
    
    
    # =============================================================================
    # Kleidung - mit Kombi
    # =============================================================================
    ["None", "Blue Jacket", "Blue Pants", "Pink Jacket", "Pink Pants", "Grey Jacket", "Grey Pants"]
    kleidung_funktion(df.loc[x, "Clothing"])
    
    # =============================================================================
    # Arme - ohne Kombi
    # =============================================================================
    fuellung = ["Yellow", "Yellow", "Yellow", "Yellow", "Yellow",
                "Yellow", "Yellow", "Yellow", "Orange", "Beige"]
    arm_funktion(df.loc[x, "Body"]) # arm ist wie fuellung ["Yellow", "Orange", "Beige"]
    
    
    # =============================================================================
    # Watch - mit Kombi
    # =============================================================================
    watch = ["None", "Silver Watch 3", "Silver Watch 9", "Golden Watch 3", "Golden watch 9"]
    watch_funktion(df.loc[x, "Watch"])
    
    
    # =============================================================================
    # Kette - mit Kombi
    # =============================================================================
    kette = ["None", "Silver Necklace USD", "Silver Necklace EUR", "Silver Necklace BTC", "Silver Necklace ETH",
             "Golden Necklace USD", "Golden Necklace EUR", "Golden Necklace BTC", "Golden Necklace ETH"]
    kette_funktion(df.loc[x, "Necklace"])
    
    
    # =============================================================================
    # Mund - mit Kombi
    # =============================================================================
    ["Happy", "Happy Tongue", "Sad", "Cold", "Dirty", "Joint", "Cigarette", "Pipe"]
    mund_funktion(df.loc[x, "Mouth"])
    
    
    # =============================================================================
    # verschiedene Mützen - mit Kombis
    # =============================================================================
    ["None", "Chinese Hat", "Headband", "Nippon Headband"]
    head(df.loc[x, "Head"], df.loc[x, "Background"])
    
    
    # =============================================================================
    # Logo
    # =============================================================================
    mein_pix(x_von = 111, x_bis = 118, y_von = 113, y_bis = 114, size = 10, Farbe = [0,0,0])
    mein_pix(x_von = 111, x_bis = 116, y_von = 115, y_bis = 116, size = 10, Farbe = [0,0,0])
    mein_pix(x_von = 111, x_bis = 114, y_von = 117, y_bis = 118, size = 10, Farbe = [0,0,0])
    
    
    
    
    image = Image.fromarray(data)
    # image.show()
     
    image.save(str(x) + ".png")
    

