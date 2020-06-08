print("\nPrime Numbers Between 1 and 100")

for PrimeN in range (1, 101):              # LOOP: Numbers 1-100 will be processed.
    CountN = 0
    for i in range(2, (PrimeN//2 + 1)):    # IF the number is 'Between 2' and the 'PrimeN Divide by 2, plus 1'.
        if(PrimeN % i == 0):               # Checks for a remainder / Decimal place. Proceed if 0
            CountN = CountN + 1            # Adds 1 to CountN to stop the next if statement from functioning.
            break                          # Breaks the loop to then move onto the next statement.

        
    if (CountN == 0 and PrimeN != 1):      # IF CountN is 0, it is a prime number. PrimeN: exclude 1 from printing.
        print("%d" %PrimeN, end = '  ')


