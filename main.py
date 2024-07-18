]import random
def number_guessing_game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  lower_boundery = 1
  upper_boundery = 100
  target_number = random.randint(lower_boundery, upper_boundery)
  attempt = 0
  guessed = False
  while not guessed:
    while True:
      try:
        player_guess = int(input(f"Guess the number between {lower_boundery} and {upper_boundery}: "))
        break
      except ValueError:
          print("Invalid input! Please enter a valid number.")

    attempt += 1
    if player_guess < target_number:
      print("too low try guess higher")

    if player_guess > target_number:
      print("too high try guess lower")

    if player_guess == target_number:
      print(f"you guessed the number in {attempt} attempts!")

number_guessing_game()
