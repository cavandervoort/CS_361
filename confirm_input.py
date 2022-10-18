def confirm_input(curr_input):
    user_input = ''
    while user_input.lower() != 'yes' and user_input.lower() != 'no':
        user_input = input(f"You input '{curr_input}'. Is this what you meant to"
                           " input? (Yes/No): ")
        if user_input.lower() != 'yes' and user_input.lower() != 'no':
            print("Oops! Your input was not 'Yes' or 'No'. Please try again.")

    if user_input.lower() == 'yes':
        return curr_input

    return 'invalid_input'
