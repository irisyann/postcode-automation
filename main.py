import csv

# open postcodes database and store into array postCodeDB
with open('postcodes.csv', newline='') as postCodeCSV:
    postCodeDB = list(csv.reader(postCodeCSV))

# open this file to put the states into it later
extractedStatesFile = open("extractedStates.txt", "a")

# open file of user postcodes (taken from excel report)
with open('userPostcodes.csv', 'r') as userPostCodeCSV:

    userPostcodes = csv.reader(userPostCodeCSV)

    # loop through every user postcode
    for userPostcode in userPostcodes:
        matchFound = 0

        # for every user postcode, loop through postcode database to find matching postcode
        for postcode in postCodeDB:

            # remove leading and trailing whitespace in user postcode
            userPostcode[0] = userPostcode[0].strip()
            
            # if match found
            # csv into array, first element of the row is the postcode
            if userPostcode[0] == postcode[0]:

                # write state to extractedStateFile
                # csv into array, second element of the row is the state
                extractedStatesFile.write(postcode[1] + "\n")
                matchFound = 1
                break
        
        # if match not found, put ***
        if matchFound == 0:
            extractedStatesFile.write("***\n")


print('done')

