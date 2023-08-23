import subprocess


def stop():
    applescript_code = f"""
    tell application "Music"
        stop
    end tell
    """

    subprocess.call(['osascript', '-e', applescript_code])
