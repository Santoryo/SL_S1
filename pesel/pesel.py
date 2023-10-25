i = 0
correct = 0
female = 0
male = 0
incorrect = 0


def checkLength(pesel):
    '''Checks the length of PESEL number'''
    if len(pesel) != 11:
        return False
    else:
        return True


def checkChecksum(pesel):
    '''Checking the checksum number (last digit in PESEL)'''
    PESEL_LENGTH = 11
    PESEL_WEIGHT = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = 0

    for i in range(PESEL_LENGTH - 1):
        checksum += PESEL_WEIGHT[i] * int(pesel[i])

    checksum = (10 - (checksum % 10)) % 10

    if checksum == int(pesel[10]):
        return True
    else:
        return False


def checkDigits(pesel):
    '''Checking if the data is numbers-only'''
    if pesel.isdigit():
        return True
    else:
        return False


def checkDates(pesel):
    '''Checks the validation of date to prevent nonsensical checksum'''
    YEAR = int(pesel[:2])
    MONTH = int(pesel[2:4])
    DAY = int(pesel[4:6])
    month = 0

    # Check the century and then calculate month using helper function
    if (MONTH >= 81 and MONTH <= 92):
        month = checkMonthHelper(MONTH, 80)
    elif (MONTH >= 1 and MONTH <= 12):
        month = checkMonthHelper(MONTH, 0)
    elif (MONTH >= 21 and MONTH <= 32):
        month = checkMonthHelper(MONTH, 20)
    elif (MONTH >= 41 and MONTH <= 52):
        month = checkMonthHelper(MONTH, 40)
    elif (MONTH >= 61 and MONTH <= 72):
        month = checkMonthHelper(MONTH, 60)
    else:
        return False

    if not (month >= 1 and month <= 12):
        return False

    if month == 2:
        if (YEAR % 4 == 0 and YEAR % 100 != 0) or (YEAR % 400 == 0):
            if not (DAY <= 29 and DAY >= 1):
                return False
        else:
            if not (DAY <= 28 and DAY >= 1):
                return False
    elif month in (1, 3, 5, 7, 8, 10, 12):
        if not (DAY <= 31 and DAY >= 1):
            return False
    elif month in (4, 6, 9, 11):
        if not (DAY <= 30 and DAY >= 1):
            return False

    return True


def checkMonthHelper(month, centuryVariable):
    '''Helper expression to calculate month'''
    return month - centuryVariable


def checkGender(pesel):
    GENDER = int(pesel[9:10])
    if (GENDER % 2 == 0):
        return True
    else:
        return False


file = open('1e6.dat')
invalid_length, invalid_digit, invalid_date, invalid_checksum = 0, 0, 0, 0

for pesel in file:
    i += 1
    pesel = pesel.strip()

    # Step 1 - Check length
    if not (checkLength(pesel)):
        invalid_length += 1
        incorrect += 1
        continue

    # Step 2 - Check if Digit
    if not (checkDigits(pesel)):
        invalid_digit += 1
        incorrect += 1
        continue

    # Step 3 - Check if invalid dates and increase sex counter
    if not (checkDates(pesel)):
        invalid_date += 1
        incorrect += 1
        continue

    # Step 4 - Check if invalid checksum
    if not (checkChecksum(pesel)):
        invalid_checksum += 1
        incorrect += 1
        continue

    if (checkGender(pesel)):
        female += 1
    else:
        male += 1

    correct += 1

print(correct + incorrect, correct, female, male)
print(invalid_length, invalid_digit, invalid_date, invalid_checksum)
