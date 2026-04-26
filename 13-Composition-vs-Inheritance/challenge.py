# Music Player System

class StreamingService:
    def play(self):
        print("Streaming from internet")
        

class LocalFileService:
    def play(self):
        print("Playing from local storage")
        
        
class MusicPlayer:
    def __init__(self, service: object):
        self.service = service
        
    def play_music(self):
        self.service.play()
        
        
spotify = MusicPlayer(StreamingService())
local = MusicPlayer(LocalFileService())

spotify.play_music()
local.play_music()

# player with dynamic runtime behavior

player = MusicPlayer( StreamingService() )  # originally it streams music online
player.play_music()

# switching behavior of the player

player.service = LocalFileService()
player.play_music()
