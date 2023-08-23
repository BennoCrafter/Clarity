import subprocess



def play(song_name):
    applescript_code = f"""
    tell application "Music"
        play track "{song_name}"
    end tell
    """

    subprocess.call(['osascript', '-e', applescript_code])

