import re


from commands.AppleMusicCommands.play_song import play
from commands.AppleMusicCommands.stop_song import stop
from commands.AppleMusicCommands.current_song import current_song
from commands.AppleMusicCommands.skip_song import skip
from commands.quit import quit


running = True
while running:
    user_input = input("Enter a command: ")
    tokens = [part.strip('"') for part in re.findall(r'"[^"]+"|\S+', user_input)]
    print(tokens)
    command = tokens[0]

    if len(tokens) >= 2:
        attribute = tokens[1]
        # Check if the command exists as a function
        if command in globals() and callable(globals()[command]):
            function_to_call = globals()[command]
            if len(tokens) >= 2:
                print(function_to_call(attribute))
        else:
            print("Command not recognized")

    else:
        print(globals()[command]())