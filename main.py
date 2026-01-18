import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from text_generator import TextGenerator
from tts_engine import TTSEngine

class HearTextsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hear Texts - Language Learning")
        self.root.geometry("900x700")
        self.root.configure(bg="#2b2b2b")

        self.text_generator = TextGenerator()
        self.tts_engine = TTSEngine()

        self.current_text = ""
        self.current_questions = []
        self.current_language = "English"

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#2b2b2b")
        style.configure("TLabel", background="#2b2b2b", foreground="white", font=("Arial", 11))
        style.configure("Title.TLabel", font=("Arial", 18, "bold"), foreground="#4fc3f7")
        style.configure("TButton", font=("Arial", 10), padding=10)
        style.configure("TRadiobutton", background="#2b2b2b", foreground="white", font=("Arial", 10))
        style.configure("TLabelframe", background="#2b2b2b", foreground="white")
        style.configure("TLabelframe.Label", background="#2b2b2b", foreground="#4fc3f7", font=("Arial", 12, "bold"))

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="Hear Texts - Language Learning", style="Title.TLabel")
        title_label.pack(pady=(0, 20))

        # Settings frame
        settings_frame = ttk.Frame(main_frame)
        settings_frame.pack(fill=tk.X, pady=(0, 15))

        # Language selection
        lang_frame = ttk.LabelFrame(settings_frame, text="Language", padding="10")
        lang_frame.pack(side=tk.LEFT, padx=(0, 20), fill=tk.Y)

        self.language_var = tk.StringVar(value="English")
        languages = [("English", "English"), ("French", "French"), ("German", "German")]
        for text, value in languages:
            rb = ttk.Radiobutton(lang_frame, text=text, value=value, variable=self.language_var)
            rb.pack(anchor=tk.W, pady=2)

        # Level selection
        level_frame = ttk.LabelFrame(settings_frame, text="Level", padding="10")
        level_frame.pack(side=tk.LEFT, padx=(0, 20), fill=tk.Y)

        self.level_var = tk.StringVar(value="beginner")
        levels = [
            ("Beginner (50-100 words)", "beginner"),
            ("Intermediate (100-200 words)", "intermediate"),
            ("Advanced (200-300 words)", "advanced")
        ]
        for text, value in levels:
            rb = ttk.Radiobutton(level_frame, text=text, value=value, variable=self.level_var)
            rb.pack(anchor=tk.W, pady=2)

        # Custom word count
        custom_frame = ttk.LabelFrame(settings_frame, text="Custom Word Count", padding="10")
        custom_frame.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(custom_frame, text="Words:").pack(side=tk.LEFT)
        self.word_count_var = tk.StringVar(value="")
        word_entry = ttk.Entry(custom_frame, textvariable=self.word_count_var, width=8)
        word_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(custom_frame, text="(overrides level)").pack(side=tk.LEFT)

        # Topic selection
        topic_frame = ttk.LabelFrame(settings_frame, text="Topic", padding="10")
        topic_frame.pack(side=tk.LEFT, padx=(20, 0), fill=tk.Y)

        self.topic_var = tk.StringVar(value="daily_life")
        topics = [
            ("Daily Life", "daily_life"),
            ("Travel", "travel"),
            ("Nature", "nature"),
            ("Technology", "technology")
        ]
        for text, value in topics:
            rb = ttk.Radiobutton(topic_frame, text=text, value=value, variable=self.topic_var)
            rb.pack(anchor=tk.W, pady=2)

        # Buttons frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=15)

        generate_btn = ttk.Button(btn_frame, text="Generate New Text", command=self.generate_text)
        generate_btn.pack(side=tk.LEFT, padx=5)

        listen_btn = ttk.Button(btn_frame, text="Listen to Text", command=self.listen_text)
        listen_btn.pack(side=tk.LEFT, padx=5)

        stop_btn = ttk.Button(btn_frame, text="Stop Audio", command=self.stop_audio)
        stop_btn.pack(side=tk.LEFT, padx=5)

        show_questions_btn = ttk.Button(btn_frame, text="Show Questions", command=self.show_questions)
        show_questions_btn.pack(side=tk.LEFT, padx=5)

        # Text display
        text_frame = ttk.LabelFrame(main_frame, text="Text", padding="10")
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        self.text_display = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 12),
                                     bg="#3c3c3c", fg="white", insertbackground="white",
                                     relief=tk.FLAT, padx=10, pady=10)
        self.text_display.pack(fill=tk.BOTH, expand=True)

        text_scrollbar = ttk.Scrollbar(self.text_display, orient=tk.VERTICAL, command=self.text_display.yview)
        self.text_display.configure(yscrollcommand=text_scrollbar.set)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Questions display
        questions_frame = ttk.LabelFrame(main_frame, text="Comprehension Questions", padding="10")
        questions_frame.pack(fill=tk.BOTH, expand=True)

        self.questions_display = tk.Text(questions_frame, wrap=tk.WORD, font=("Arial", 11),
                                          bg="#3c3c3c", fg="white", insertbackground="white",
                                          relief=tk.FLAT, padx=10, pady=10, height=8)
        self.questions_display.pack(fill=tk.BOTH, expand=True)

    def get_word_count(self):
        """Get word count from custom input or level selection"""
        custom = self.word_count_var.get().strip()
        if custom and custom.isdigit():
            return int(custom)

        level_counts = {
            "beginner": 75,
            "intermediate": 150,
            "advanced": 250
        }
        return level_counts.get(self.level_var.get(), 100)

    def generate_text(self):
        language = self.language_var.get()
        level = self.level_var.get()
        topic = self.topic_var.get()
        word_count = self.get_word_count()

        self.current_language = language

        result = self.text_generator.generate(language, level, topic, word_count)

        self.current_text = result["text"]
        self.current_questions = result["questions"]

        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, self.current_text)

        self.questions_display.delete(1.0, tk.END)
        self.questions_display.insert(tk.END, "Click 'Show Questions' to see comprehension questions.")

    def listen_text(self):
        if not self.current_text:
            messagebox.showwarning("No Text", "Please generate a text first!")
            return
        self.tts_engine.speak(self.current_text, self.current_language)

    def stop_audio(self):
        self.tts_engine.stop()

    def show_questions(self):
        if not self.current_questions:
            messagebox.showwarning("No Questions", "Please generate a text first!")
            return

        self.questions_display.delete(1.0, tk.END)
        for i, q in enumerate(self.current_questions, 1):
            self.questions_display.insert(tk.END, f"{i}. {q}\n\n")

def main():
    root = tk.Tk()
    app = HearTextsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
