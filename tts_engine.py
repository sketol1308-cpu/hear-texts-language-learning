import threading

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

class TTSEngine:
    def __init__(self):
        self.engine = None
        self.speaking = False
        self.thread = None

        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)  # Speed of speech
                self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
            except Exception as e:
                print(f"TTS initialization error: {e}")
                self.engine = None

    def _get_voice_for_language(self, language):
        """Get appropriate voice for the selected language"""
        if not self.engine:
            return None

        voices = self.engine.getProperty('voices')

        language_codes = {
            "English": ["en", "english"],
            "French": ["fr", "french", "français"],
            "German": ["de", "german", "deutsch"]
        }

        target_codes = language_codes.get(language, ["en"])

        for voice in voices:
            voice_name = voice.name.lower()
            voice_id = voice.id.lower()

            for code in target_codes:
                if code in voice_name or code in voice_id:
                    return voice.id

        # Return first voice as fallback
        if voices:
            return voices[0].id
        return None

    def speak(self, text, language="English"):
        """Speak the given text in the specified language"""
        if not TTS_AVAILABLE:
            print("Text-to-speech is not available. Please install pyttsx3: pip install pyttsx3")
            return

        if not self.engine:
            print("TTS engine not initialized")
            return

        # Stop any current speech
        self.stop()

        def _speak_thread():
            try:
                voice_id = self._get_voice_for_language(language)
                if voice_id:
                    self.engine.setProperty('voice', voice_id)

                # Adjust rate based on language
                if language == "French":
                    self.engine.setProperty('rate', 140)
                elif language == "German":
                    self.engine.setProperty('rate', 145)
                else:
                    self.engine.setProperty('rate', 150)

                self.speaking = True
                self.engine.say(text)
                self.engine.runAndWait()
                self.speaking = False
            except Exception as e:
                print(f"TTS error: {e}")
                self.speaking = False

        self.thread = threading.Thread(target=_speak_thread, daemon=True)
        self.thread.start()

    def stop(self):
        """Stop current speech"""
        if self.engine and self.speaking:
            try:
                self.engine.stop()
                self.speaking = False
            except Exception as e:
                print(f"Error stopping TTS: {e}")

    def is_speaking(self):
        """Check if currently speaking"""
        return self.speaking
