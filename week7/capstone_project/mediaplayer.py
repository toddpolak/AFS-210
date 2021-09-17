from queue import Queue
import random

# Song Class
#region
class Song():
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
#endregion

class Queue:
    def __init__(self):
        self.items = []

    def add_song(self, song):
        self.items.insert(0, song)
        
    def size(self):
        return len(self.items)
        
    def play(self, song_index):
        print(self.items[song_index])
        
    def removeSong(self, title):
        song_index = 0
        
        for item in self.items:
            if item.title == title:
                break   
            song_index += 1
        
        self.items.pop(song_index)

# Menu 
#region 
def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
#endregion
    

media_player = Queue()

# Default Playlist
media_player.add_song(Song('The Walk', 'Mayer Hawthorne'))
media_player.add_song(Song('What Lovers Do', 'Maroon 5'))
media_player.add_song(Song('Heartbreaker', 'Mariah Carey'))
media_player.add_song(Song('24K Magic', 'Bruno Mars'))
media_player.add_song(Song('Wifey', 'Next'))

# Set the default song index
current_song_index = 0

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        artist = input('Enter the Song Artist:')
        title = input('Enter Song title: ')

        # Add song to playlist
        song = Song(title=title, artist=artist)
        media_player.add_song(song)
        
        print("New Song Added to Playlist")
        
    elif choice == 2:
        # Prompt user for Song Title 
        title = input('Enter the song title to be removed: ')
        
        # remove song from playlist
        media_player.removeSong(title)
        
        print("Song Removed from Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        
        print("Playing....")
        
        media_player.play(current_song_index)
        
        
        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")  
        
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        
        random.shuffle(media_player.items)
        
        print("Shuffling....")
        
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")

    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        
        for item in media_player.items:
            print(item)
        
    elif choice == 0:
        print("Goodbye.")
        break