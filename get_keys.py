import keyboard
while True:
    print(keyboard.read_key())

    try:
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            break
    except:
        break