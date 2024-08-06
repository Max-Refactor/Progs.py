import customtkinter

class RegApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Reg App")

        # add widgets to app
        self.frame = customtkinter.CTkFrame(master=self)
        self.Label = customtkinter.CTkLabel(self.frame, text="Login", font=("Roboto", 24))
        self.userButton = customtkinter.CTkButton(self.frame, text="User", width=200, height=50)
        self.adminButton = customtkinter.CTkButton(self.frame, text="Admin", width=200, height=50)

        self.frame.pack(pady=20, padx=40, fill='both', expand=True)
        self.Label.pack(padx=20, pady=40, anchor="center")
        self.userButton.pack(padx=20, pady=80, anchor="center")
        self.adminButton.pack(padx=20, pady=80, anchor="center")

    # add methods to app
    def button_click(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
        Input = dialog.get_input()
        print("Number:", Input)


regApp = RegApp()
regApp.mainloop()