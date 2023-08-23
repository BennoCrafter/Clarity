from rich.console import Console
from rich.progress import Progress
import time


def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def simulate_song_progress():
    total_time = 180  # Total song time in seconds
    song_name = "Awesome Song"
    artist_name = "Great Artist"

    console = Console(width=80)  # Adjust the console width as needed

    with Progress(console=console) as progress:
        task = progress.add_task("[cyan]Playing song...", total=total_time)
        for current_time in range(total_time + 1):
            progress.update(task, completed=current_time)

            current_time_formatted = format_time(current_time)
            total_time_formatted = format_time(total_time)

            console.clear()
            console.print(":musical_note: [bold]Now Playing:[/bold]", justify="center")
            console.print(f"[bold]{song_name}[/bold] by [bold]{artist_name}[/bold]", justify="center")
            console.print(f"Time: [green]{current_time_formatted}[/green] / {total_time_formatted}", justify="center")
            console.print("\n")
            time.sleep(1)


if __name__ == "__main__":
    simulate_song_progress()
