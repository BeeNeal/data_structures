import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(level=logging.CRITICAL)
logging.debug('Start of program')

def isBadVersion(num):

    if num >= 4:
        return True
    return False


def firstBadVersion(n):

    low = 0
    high = n
    
    while low < high:
        guess = (high + low) // 2
        logging.debug('guess is {}'.format(guess))
        is_bad = isBadVersion(guess)
        # bad version must be higher
        if is_bad is False:
            # why not hitting this?
            low = guess
            logging.debug('low is {}'.format(guess))

        elif is_bad is True:
            if isBadVersion(guess - 1) is False:
                logging.debug('guess is {} and prior version is {}'.format(guess, guess-1))
                return guess
            else:
                high = guess
                logging.debug('high is {}'.format(guess))



firstBadVersion(10)

# can't name a variable inside the control if/else flow