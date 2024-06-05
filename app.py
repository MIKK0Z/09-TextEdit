import tkinter as tk
from tkinter import filedialog, messagebox, Text
from tkinter.font import Font
from tkinter import ttk

class TextEditor:

    def __init__(self, root):
        self.root = root
        self.root.title("Prosty Edytor Tekstu")

        # Ustawienia głównego okna
        self.root.geometry("800x600")

        # Pasek menu
        self.create_menu()

        # Pasek narzędziowy
        self.create_toolbar()

        # Pole tekstowe
        self.text_area = Text(self.root, undo=True, wrap="word")
        self.text_area.pack(expand=1, fill='both')

        # Czcionki dla formatowania
        self.bold_font = Font(self.text_area, self.text_area.cget("font"))
        self.bold_font.configure(weight="bold")

        self.italic_font = Font(self.text_area, self.text_area.cget("font"))
        self.italic_font.configure(slant="italic")

        self.underline_font = Font(self.text_area, self.text_area.cget("font"))
        self.underline_font.configure(underline=True)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nowy", command=self.new_file)
        file_menu.add_command(label="Otwórz", command=self.open_file)
        file_menu.add_command(label="Zapisz", command=self.save_file)
        file_menu.add_command(label="Zamknij", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Pogrubienie", command=self.toggle_bold)
        edit_menu.add_command(label="Podkreślenie", command=self.toggle_underline)
        edit_menu.add_command(label="Pochylenie", command=self.toggle_italic)

        align_menu = tk.Menu(edit_menu, tearoff=0)
        align_menu.add_command(label="Lewa", command=lambda: self.align_text("left"))
        align_menu.add_command(label="Środek", command=lambda: self.align_text("center"))
        align_menu.add_command(label="Prawa", command=lambda: self.align_text("right"))
        edit_menu.add_cascade(label="Wyrównywanie", menu=align_menu)

        menu_bar.add_cascade(label="Plik", menu=file_menu)
        menu_bar.add_cascade(label="Edytuj", menu=edit_menu)

        self.root.config(menu=menu_bar)

    def create_toolbar(self):
        toolbar = ttk.Frame(self.root, relief="raised", borderwidth=2)
        toolbar.pack(side="top", fill="x")

        new_icon = tk.PhotoImage(file="icons/new_file.png")
        open_icon = tk.PhotoImage(file="icons/open_file.png")
        save_icon = tk.PhotoImage(file="icons/save_file.png")
        bold_icon = tk.PhotoImage(file="icons/bold.png")
        italic_icon = tk.PhotoImage(file="icons/italic.png")
        underline_icon = tk.PhotoImage(file="icons/underline.png")
        align_left_icon = tk.PhotoImage(file="icons/align_left.png")
        align_center_icon = tk.PhotoImage(file="icons/align_center.png")
        align_right_icon = tk.PhotoImage(file="icons/align_right.png")

        ttk.Button(toolbar, image=new_icon, command=self.new_file).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=open_icon, command=self.open_file).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=save_icon, command=self.save_file).pack(side="left", padx=2, pady=2)
        ttk.Separator(toolbar, orient='vertical').pack(side='left', fill='y', padx=5)

        ttk.Button(toolbar, image=bold_icon, command=self.toggle_bold).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=italic_icon, command=self.toggle_italic).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=underline_icon, command=self.toggle_underline).pack(side="left", padx=2, pady=2)
        ttk.Separator(toolbar, orient='vertical').pack(side='left', fill='y', padx=5)

        ttk.Button(toolbar, image=align_left_icon, command=lambda: self.align_text("left")).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=align_center_icon, command=lambda: self.align_text("center")).pack(side="left", padx=2, pady=2)
        ttk.Button(toolbar, image=align_right_icon, command=lambda: self.align_text("right")).pack(side="left", padx=2, pady=2)

        # Keep a reference to the icons to prevent garbage collection
        self.icons = [new_icon, open_icon, save_icon, bold_icon, italic_icon, underline_icon, align_left_icon, align_center_icon, align_right_icon]

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def toggle_bold(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "bold" in current_tags:
            self.text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("bold", "sel.first", "sel.last")
            self.text_area.tag_configure("bold", font=self.bold_font)

    def toggle_italic(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "italic" in current_tags:
            self.text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("italic", "sel.first", "sel.last")
            self.text_area.tag_configure("italic", font=self.italic_font)

    def toggle_underline(self):
        current_tags = self.text_area.tag_names("sel.first")
        if "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_configure("underline", font=self.underline_font)

    def align_text(self, align_type):
        self.text_area.tag_configure("left", justify='left')
        self.text_area.tag_configure("center", justify='center')
        self.text_area.tag_configure("right", justify='right')
        current_tags = self.text_area.tag_names("sel.first")
        for tag in ["left", "center", "right"]:
            self.text_area.tag_remove(tag, "sel.first", "sel.last")
        self.text_area.tag_add(align_type, "sel.first", "sel.last")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
