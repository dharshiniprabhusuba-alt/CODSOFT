import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors")
        master.geometry("400x400")
        master.config(bg="#f0f0f0")

        self.user_score = 0
        self.computer_score = 0
        self.options = ["rock", "paper", "scissors"]

        # --- Widgets ---
        self.title_label = tk.Label(master, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(master, text="Choose your move:", font=("Arial", 12), bg="#f0f0f0")
        self.instruction_label.pack()

        # Frame for buttons
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Buttons for player choices
        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play_round("rock"), font=("Arial", 10), width=10)
        self.rock_button.pack(side="left", padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play_round("paper"), font=("Arial", 10), width=10)
        self.paper_button.pack(side="left", padx=5)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play_round("scissors"), font=("Arial", 10), width=10)
        self.scissors_button.pack(side="left", padx=5)

        # Labels to display results
        self.choice_label = tk.Label(master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.choice_label.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(master, text=f"Score: You {self.user_score} | Computer {self.computer_score}", font=("Arial", 12), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # Play Again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, state="disabled", font=("Arial", 10), width=20)
        self.play_again_button.pack(pady=10)

    def play_round(self, player_choice):
        """
        Main logic for a single round of the game.
        """
        computer_choice = random.choice(self.options)
        
        self.choice_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}")

        result_text, winner = self.check_win(player_choice, computer_choice)
        self.result_label.config(text=result_text)

        self.update_score(winner)
        self.play_again_button.config(state="normal")

    def check_win(self, player, computer):
        """
        Determines the winner of the game.
        Returns the result string and the winner ("user", "computer", or "tie").
        """
        if player == computer:
            return "It's a tie!", "tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "You win!", "user"
        else:
            return "You lose!", "computer"

    def update_score(self, winner):
        """
        Updates the score based on the winner of the round.
        """
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1
        
        self.score_label.config(text=f"Score: You {self.user_score} | Computer {self.computer_score}")

    def reset_game(self):
        """
        Resets the display for a new round.
        """
        self.choice_label.config(text="")
        self.result_label.config(text="")
        self.play_again_button.config(state="disabled")

# --- Main application loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()