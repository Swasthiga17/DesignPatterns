from abc import ABC, abstractmethod
import os

# Target Interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, filename: str, output_file=None):
        pass

# Adaptee 1 - Advanced Media Player
class AdvancedMediaPlayer:
    def play_vlc(self, filename: str, output_file=None):
        message = f"Playing VLC file: {filename}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def play_mp4(self, filename: str, output_file=None):
        message = f"Playing MP4 file: {filename}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)

# Adaptee 2 - Legacy Audio Player
class LegacyAudioPlayer:
    def play_mp3(self, filename: str, output_file=None):
        message = f"Playing MP3 file: {filename}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def play_wav(self, filename: str, output_file=None):
        message = f"Playing WAV file: {filename}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)

# Adapter for Advanced Media Player
class AdvancedMediaAdapter(MediaPlayer):
    def __init__(self):
        self.advanced_player = AdvancedMediaPlayer()
    
    def play(self, audio_type: str, filename: str, output_file=None):
        if audio_type.lower() == "vlc":
            self.advanced_player.play_vlc(filename, output_file)
        elif audio_type.lower() == "mp4":
            self.advanced_player.play_mp4(filename, output_file)
        else:
            message = f"Unsupported format: {audio_type}"
            if output_file:
                output_file.write(message + "\n")
            else:
                print(message)

# Adapter for Legacy Audio Player
class LegacyAudioAdapter(MediaPlayer):
    def __init__(self):
        self.legacy_player = LegacyAudioPlayer()
    
    def play(self, audio_type: str, filename: str, output_file=None):
        if audio_type.lower() == "mp3":
            self.legacy_player.play_mp3(filename, output_file)
        elif audio_type.lower() == "wav":
            self.legacy_player.play_wav(filename, output_file)
        else:
            message = f"Unsupported format: {audio_type}"
            if output_file:
                output_file.write(message + "\n")
            else:
                print(message)

# Media Player that uses adapters
class UniversalMediaPlayer(MediaPlayer):
    def __init__(self):
        self.advanced_adapter = AdvancedMediaAdapter()
        self.legacy_adapter = LegacyAudioAdapter()
    
    def play(self, audio_type: str, filename: str, output_file=None):
        message = f"Attempting to play {filename} as {audio_type}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
        
        if audio_type.lower() in ["mp3", "wav"]:
            self.legacy_adapter.play(audio_type, filename, output_file)
        elif audio_type.lower() in ["vlc", "mp4"]:
            self.advanced_adapter.play(audio_type, filename, output_file)
        else:
            message = f"Format {audio_type} not supported by any player"
            if output_file:
                output_file.write(message + "\n")
            else:
                print(message)

def demo_adapter(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/adapter_media.txt", "w") as f:
        f.write("=== Adapter Pattern: Media Players ===\n\n")
        
        player = UniversalMediaPlayer()
        
        # Play various formats
        formats = [
            ("mp3", "song.mp3"),
            ("mp4", "movie.mp4"),
            ("vlc", "presentation.vlc"),
            ("wav", "sound.wav"),
            ("avi", "video.avi")  # Unsupported format
        ]
        
        for audio_type, filename in formats:
            f.write(f"Format: {audio_type.upper()} -> ")
            player.play(audio_type, filename, f)
        
        f.write("\nAdapter pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_adapter()