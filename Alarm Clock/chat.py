import time
import pygame

def set_alarm(alarm_time):
    current_time = time.strftime("%H:%M:%S")
    print(f"Alarm set for {alarm_time}. Current time is {current_time}")

    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            play_alarm_sound()
            break
        time.sleep(1)

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # Replace with the path to your alarm sound file
    pygame.mixer.music.play()

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
