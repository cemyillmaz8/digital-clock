from tkinter import Label, Tk
import time

app_windows = Tk()

#başlığı dijital saat olarak değiştiriyor
app_windows.title("dijital saat") 

#pencerenin şeklini belirliyor
app_windows.geometry("500x200")

#pencerenin şeklini mause ile değiştiremezsin
app_windows.resizable(0,0)

#pencerenin arka planı renk seçimi
app_windows.configure(bg="black")

#yazı tipi
text_font = ("boulder",36, 'bold') 
#bicim büyüklük kalınlık

#arkaplan
background = "black"

#önplan
foreground = "white"

#pencerenin köşelerinin yumuşak olması
border_witdh = 20

#saat etiketi
label = Label(app_windows,font=text_font, bg=background, fg=foreground)

#eklediğimiz alanın biçimini
label.grid(row=0,column=1,padx=border_witdh,pady=10)
#row satır column sutun padx yanlar 10 satır boşluk pady üst ve alt 10 satır boşluk

#tarih etiketi
date_label = Label(app_windows,font=text_font, bg=background, fg=foreground)
date_label.grid(row=1,column=1,padx=border_witdh,pady=10)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    #tarih etiketi
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    #saat güncellemesi 200 mili saniyede
    label.after(200,digital_clock)


digital_clock()






app_windows.mainloop()