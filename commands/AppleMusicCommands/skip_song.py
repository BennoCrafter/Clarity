import subprocess


def skip():
    applescript_code = '''
    tell application "Music"
        next track
    end tell
    '''

    subprocess.call(['osascript', '-e', applescript_code])

