#Simple Alarm Clock in Python using pygame for audio playback
# This script sets an alarm that plays a sound at a specified time.
import time
import datetime
import pygame

def set_alarm(alarm_time):
    # Validate the alarm time format
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"  # Path to your alarm sound file
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Alarm ringing!")
            
            #Initialize pygame mixer to play sound
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Wait for the music to finish playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        # Sleep for a short duration to avoid busy waiting
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)