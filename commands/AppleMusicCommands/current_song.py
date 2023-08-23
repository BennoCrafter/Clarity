import subprocess
from rich.console import Console
from rich.progress import Progress
import time
from pynput import keyboard


def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def generate_progress_bar(current_time, total_time, length=20):
    progress = current_time / total_time
    bar_length = int(progress * length)
    return "[" + "=" * bar_length + "-" * (length - bar_length) + "]"


def get_current_song():
    applescript_code = '''
    tell application "Music"
        set currentTrackName to name of current track
        set currentArtistName to artist of current track
        set currentTime to player position
        set totalTime to duration of current track

        set currentMinutes to (currentTime div 60) as integer
        set currentSeconds to (currentTime mod 60) as integer

        set totalMinutes to (totalTime div 60) as integer
        set totalSeconds to (totalTime mod 60) as integer

        return {currentTrackName, currentArtistName, currentTime, totalTime}
    end tell
    '''

    result = subprocess.run(['osascript', '-e', applescript_code], capture_output=True, text=True)
    output = result.stdout.strip().split(",")
    print(output)
    if result.returncode == 0:
        song_name = output[0]
        artist_name = output[1].strip()
        current_time = float(output[2].strip())
        total_time = float(output[3].strip())
        return song_name, artist_name, current_time, total_time
    else:
        return None, None, None, None


def current_song():
    console = Console(width=80)  # Adjust the console width as needed
    progress = Progress(console=console)

    song_name, artist_name, current_time, total_time = get_current_song()

    if song_name is not None:
        task = progress.add_task("[cyan]Playing song...", total=total_time)
        with progress:
            while not progress.finished:
                progress.update(task, completed=current_time)

                current_time_formatted = format_time(current_time)
                total_time_formatted = format_time(total_time)

                console.clear()
                console.print(":musical_note: [bold]Now Playing:[/bold]", justify="center")
                console.print(f"[green]{song_name}[/green] by [blue]{artist_name}[/blue]", justify="center")
                console.print("\n")

                time.sleep(1)
                song_name, artist_name, current_time, total_time = get_current_song()
                with keyboard.Events() as events:
                    # Block for as much as possible
                    event = events.get(1e6)
                    if event.key == keyboard.KeyCode.from_char('q'):
                        progress.finished = True
    else:
        console.print("Error retrieving current song information")

