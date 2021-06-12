"""
A collection of function for doing my project.

"""


# Import modules
from random import randint
import time

# Start the game. Introduction and kicks to generate function.
def start():
    """
    Starts and introduces the game: Digital Mastermind.
    
    --------
    Parameters
    None
        No parameters as it serves to call other functions
    
    --------
    Returns
    str : string
        Returns ending message after the run_game function.
    
    """
        
    print('Hello and welcome to Digital Mastermind!')
    time.sleep(2)
    print('Mastermind is a classic game where one player creates a predetermined pattern of colors  and the other player tries to guess the correct order.')
    time.sleep(3)
    print('In Digital Mastermind, the colors are replaced with non-repeating numbers 0-9 and the computer generates the secret code.')
    time.sleep(5)
    print('After each guess the player makes, the computer will tell the player how many numbers were guessed correctly and in the correct position, how many were guessed correctly and in the incorrect position, and how many numbers were guessed incorrectly.')
    time.sleep(0)
    
    answer = generate()
    return(run_game(answer))

#############################################################################

# Generate a numerical code with the length of 1 to 10 based on user input.
def generate():
    """
    Generates the code that user will have to guess.
    
    --------
    Parameters
    integer: int
        This number determines the length of the generated code.
        
    --------    
    Returns
    list : []
        Returns a list of integers with the length of 1 to 10 based on integer input.
    
    """
    
    digits = 0
    i = 0
    num = [-1]
    
    while True:
        
        # User input of length of code they would like.
        digits = input('Enter number of digits (1 to 10): ')
        
        # Get ready for errors and catch them.
        try:
            
            # Checks if input value is an integer -> Line 76 if not.
            digits = int(digits)
            
            # Length of code must be 1 to 9 digits and unique (no reps).
            if (digits < 1) or (digits > 10):
                print('Please enter a number from 1 to 10.')
            else:
                break
                
        except ValueError:
            print('Please enter your number as an integer.')

    while i < digits:
        
        # Generates random digit.
        dig = randint(0,9)
        # Allows the loop to decide whether to make new number or continue to next digit.
        iterate = True
        
        # Checks to see if digit has been generated.
        if (num[0]) != -1:
            
            # Checks is generated digit has appeared yet.
            for j in range (len(num)):
                if dig == num[j]:
                    iterate = False
                    break
                    
            # If digit has not appeared yet -> could still append new digit on.      
            if iterate == True:
                num.append(dig)
                i += 1
                
        else:
            num[0] = dig
            i +=1
            
    return num

#############################################################################

# Run the game. Bulk of where the game occurs.
# Users inputs guess and function checks.
def run_game(answer):
    """
    Users inputs a numerical value as a guess and the functions checks if it exists within the generated code.
    
    --------
    Parameters
    integer: int
        The guessed number that will be determined if it is within the genereated code or if it is the generated code.
        
    --------
    Returns
    str : string
        Returns a string that is a message of whether the guessed code is correct or incorrect and the game statistics.
   
    """
    
    incorrect = 0
    correct = 0
    right_digit = 0
    tries = 0
    hints = 0
    length = len(answer)
    revealed_digits = []
    
    # Loop will keep running until the generated code is guessed correctly.
    while True:
        
        str_guess = input('Enter your guess (enter \'hint\' if you would like to reveal a digit): ')
        
        # Checks if user would like a hint.
        if str_guess == 'hint':
            temp = hint(answer, revealed_digits)
            hints += temp[0]
            if (temp[1]) != -1:
                revealed_digits.append(temp[1])
            continue
            
        try:
            
            # Makes sure the guess is an integer.
            int(str_guess)
            
            # Makes sure the length of the guess is equal to the length of the genereated code (answer).
            if (len(str_guess)) != length:
                print('Please enter a guess that is ' + str(length) + ' digit(s)')
                continue
             
            # Input function returns a string, so we convert to ints and store into array.
            guess = []
            for i in range(length):
                guess.append(int(str_guess[i]))
                
            tries += 1
     
            # Checks for how correct the guess is and adds it to clue provided at the end of each guess.
            for i in range(length):
                for j in range(length):
                    if guess[i] == answer[j]:
                        if i == j:
                            correct += 1
                        else:
                            right_digit += 1
                        break
                    elif j == length - 1:
                        incorrect += 1
            
            # Same lengte and correct location is the correct guess and returns a completion message (str).
            if correct == length:
                if tries == 1 and hints == 0:
                    return ('You just got the answer in only 1 try and no hints! How?!')
                elif tries == 1 and hints >= length:
                    return ('Even though you technically got it in one try, you had us reveal ALL the digits for you... for SHAME!')
                elif tries == 1:
                    return ('You got it in 1 try, but you used hints so it\'\s not as immpressive. Sorry :/')
                else:
                    return ('Congrats! You got the answer in ' + str(tries) + ' tries with ' + str(hints) + ' hint(s)!')
                
            print(str(correct) + ' digit(s) are in the correct location.')
            print(str(right_digit) + ' digit(s) are in the correct but wrong position.')
            print(str(incorrect) + ' digit(s) are not part of the answer.')
            
            # Resets the variables to prepare for the next guess.
            correct = 0
            right_digit = 0
            incorrect = 0
         
        # Runs when the guess is not numerical (int).
        except ValueError:
            print('Please enter your guess as a number (the 1st digit can be "0" in this case).')
            
#############################################################################

# Gives a hint.
def hint(answer, revealed):
    """
    Prints the digit based of the requested location with 1 being the left most placement and returns a tuple. 
    
    --------
    Parameters
    integer: int
        The location/ placement of the genereated digit. 
        '1' is the fist index of the code.
        
    --------
    Returns
    tuple : ()
        First element of tuple incraments run_game.hints by 0 or 1
        Secont element of tuple appends the revealed digit to run_game.reveal_digits, unless it is -1.
   
    """
    # Loop is run until appropriate response is entered.
    while True:
        digit = input('Which digit would you like revealed (1 refers to the left most digit)?  Enter \'thanks\' to exit the hint section.: ')
        
        # No hint is used. 
        if digit == 'thanks':
            return 0,-1
        
        try:
            
            # Convert str input into int and check if a number was entered.
            digit = int(digit)
            if (digit > 0) and (digit < len(answer) + 1):
                revealed_digit = answer[digit - 1]
                
                # Checks if digit has been revealed.
                # If digit has already been revealed, no hint is used.
                for i in range (len(revealed)):
                    if revealed_digit == revealed[i]:
                        print('This digit was already revealed. It is ' + str(revealed_digit) + '.')
                        return 0, -1
                    
                print('That digit is ' + str(revealed_digit) + '.')
                return 1, revealed_digit
            
            # Statement is run if the selected digit is beyond the bounds of the length of the answer.
            else:
                print('Please enter a number between 1 and ' + str(len(answer)))
                
        # Run if entered value is not a number.        
        except ValueError:
            print('Please enter a number between 1 and ' + str(len(answer)))
                    
                      
                           
                              




































      
