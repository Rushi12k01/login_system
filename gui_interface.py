import customtkinter

# app looks
customtkinter.set_appearance_mode("blue")# dark for dark mode

# app theme
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
# app size
root.geometry("450x450")
root.title("login page")

# function for login
def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,fill="both",expand=True)

# checkbox for remember me
label = customtkinter.CTkLabel(master=frame,text="Login System")
label.pack(pady=12,padx=10)

# username and password entry and checkbox
entry1= customtkinter.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2= customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame,text="Remember me")
checkbox.pack(pady=12,padx=10)

root.mainloop()