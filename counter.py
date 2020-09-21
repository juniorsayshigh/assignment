def main():
    """
    The Range Program

    This program asks the user to give:
    start number
    end number
    step number

    Return:
    A range of numbers using the perameters given by the user.

    
    """

    try:
        start = int(input('Please enter a start number.'
                          + 'If no number is entered, the default number will be 0.:'))
    except ValueError:
        start = 0


    while True:
        try:
            end = int(input('Please enter an end number.'
                            + ' End number is required to move on.:'))
            if end > 0 and end >= start:
                break
            if end <= start:
                print('End number must be larger than start number.')
        except ValueError:
            print('Please enter a number. ')

    dif = end - start

    try:
        while True:
            step = int(input('Please enter a step number.'
                             + ' If no number is enetered, the default number will be 1.:'))
            if step > dif:
                print(('Step number must be less than '
                       + 'the end number but more than the start number.'))
            elif step < dif:
                break
            elif step == dif:
                break
    except ValueError:
        step = 1

    for num in range(start, end, step):
        print(num)

    print(end)

if __name__ == "__main__":
    main()
