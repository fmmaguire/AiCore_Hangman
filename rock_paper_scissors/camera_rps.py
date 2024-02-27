import cv2
from keras.models import load_model
import numpy as np
import time
import random

def get_prediction():

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    timer = 5

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        count_down = timer - (time.time() - start_time)
        # Press q to close the window
        print(prediction)
        print(count_down)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        if count_down <= 0:
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    prediction = prediction[0]
    labels = ['rock', 'paper', 'scissors', 'nothing']
    prediction_dict = dict(zip(labels, prediction))
    pred_user_choice = max(prediction_dict, key=prediction_dict.get)

    return pred_user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def get_winner(computer_choice, user_choice):
    print(f"User choice:{user_choice}, Computer choice:{computer_choice}")
    if computer_choice == user_choice:
        print("It's a tie")
        return "tie"
    elif (computer_choice == "rock" and user_choice == "scissors"):
        print("You lost.")
        return "computer"
    elif (computer_choice == "paper" and user_choice == "rock"):
        print("You lost.")
        return "computer"
    elif (computer_choice == "scissors" and user_choice == "paper"):
        print("You lost.")
        return "computer"
    else:
        print("You won!")
        return "user"

def play():
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user_choice = get_prediction()
        computer_choice = get_computer_choice()
        winner = get_winner(computer_choice, user_choice)

        if winner == "tie":
            print("tie")
            print(f"User wins:{user_wins}, Computer wins:{computer_wins}")
        elif winner == "computer":
            computer_wins += 1
            print(f"User wins:{user_wins}, Computer wins:{computer_wins}")
        else:
            user_wins += 1
            print(f"User wins:{user_wins}, Computer wins:{computer_wins}")

    if user_wins == 3:
        print("You won the game!")
    else:
        print("womp womp the computer won the game.")

play()