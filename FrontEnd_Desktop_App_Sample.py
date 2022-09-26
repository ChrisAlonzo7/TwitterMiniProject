import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()
window.title("SW Mini Project")
window.geometry("700x500")

def button_handler():
    twitter_handle_input = entry.get()
    text = tk.Text(master=window,height=1,width=10)
    text.grid(column=1,row=5)
    text.insert(tk.END,twitter_handle_input)

label1 = tk.Label(text ="Botometer and Sentiment Analysis", font=("Times new roman",20))
label1.grid(column=0,row=0, padx=20, pady=20)

label2 = tk.Label(text ="Enter the twitter handle: ", font=("Times new roman",15))
label2.grid(column=0,row=1, padx=10, pady=10)

button=tk.Button(window,text="Check (Bots/Sentiment)",command=button_handler,bg="red")
button.grid(column=0,row=2, padx=10, pady=10)

entry = tk.Entry()
entry.grid(column=1,row=1, padx=20, pady=20)

image=Image.open('twitter_image.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=0,row=5)

window.mainloop()
