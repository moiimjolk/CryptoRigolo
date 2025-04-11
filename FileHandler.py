import os
import tkinter as tk
from tkinter import filedialog

class FileHandler:
    def __init__(self):
        self.file_path = None
        self.file_content = None
    
    def select_file(self):
        """Open a file dialog and return the selected file path"""
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        self.file_path = filedialog.askopenfilename(
            title="Select a file to encrypt/decrypt",
            filetypes=[("All files", "*.*")]
        )
        
        return self.file_path
    
    def read_file(self, file_path=None):
        """Read the contents of the file"""
        if file_path:
            self.file_path = file_path
            
        if not self.file_path or not os.path.isfile(self.file_path):
            return "Error: Invalid file path."
        
        try:
            with open(self.file_path, 'rb') as file:
                self.file_content = file.read()
            return self.file_content
        except Exception as e:
            return f"Error reading file: {e}"
    
    def save_file(self, content, output_path=None):
        """Save content to a file"""
        if not output_path:
            root = tk.Tk()
            root.withdraw()
            output_path = filedialog.asksaveasfilename(
                title="Save encrypted/decrypted file",
                filetypes=[("All files", "*.*")]
            )
        
        if not output_path:
            return "Error: No output path provided."
        
        try:
            with open(output_path, 'wb') as file:
                file.write(content)
            return True
        except Exception as e:
            return f"Error saving file: {e}"