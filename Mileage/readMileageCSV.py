# Import csv functions
import csv

# Open file
mileageFile = open('Mileage\\static\\Mileage\\files\\District_Mileage_Chart.csv')

# Reads file as a csv
mileageReader = csv.reader(mileageFile)

# Inputs data from file into list
mileageData = list(mileageReader)

# Finds row number of location
def rowLocationValue(locationName):
	rowNumber = 0
	for eachRow in mileageData:
		if eachRow[0] == locationName:
			# print("The row location of {} is: {}".format(locationName, rowNumber))
			return rowNumber
		else:
			rowNumber += 1
	return 1000

# Finds column number of location
def columnLocationValue(locationName):
	columnNumber = 0
	for eachColumn in mileageData[0]:
		if eachColumn == locationName:
			# print("The column location of {} is: {}".format(locationName, columnNumber))
			return columnNumber
		else:
			columnNumber += 1
	return 1000

print("")
print("")

# Calculate distance between two locations
def mileageDistance(locationOne, locationTwo):
	sourceRow = rowLocationValue(locationOne)
	destinationColumn = columnLocationValue(locationTwo)

	if locationTwo == '':
		return 0.0
	if mileageData[sourceRow][destinationColumn] == '':
		return 0.0
	else:
		return float(mileageData[sourceRow][destinationColumn])

# Calculate total distance between a list of locations
def calculateTotalDisance(locationList):
	totalDistance= 0
	try:
		for i in range(len(locationList)):
			totalDistance += mileageDistance(locationList[i], locationList[i+1])
	except IndexError:
		pass
	return round(totalDistance,1)

# print("The total distance between these locations: {} is: {}".format(locationList, calculateTotalDisance(locationList)))

def findAllLocations():
	allLocations = []
	for eachLocation in mileageData[0]:
		allLocations.append(eachLocation)
	return allLocations


# Converts list of locations to printable format
def convertLocationsToPrint(listOfLocations):
	listUpdated = []
	printLocation = ''
	for eachLocation in listOfLocations:
		if eachLocation != '':
			listUpdated.append(eachLocation)
	for locationIndex in range(len(listUpdated)):
		printLocation += listUpdated[locationIndex]
		if locationIndex != len(listUpdated) - 1:
			printLocation += ' -> '

	return printLocation

# Converts location query to location list
def convertLocationQueryToLocationList(myPrintQuery):
	location_as_list = []
	for each in myPrintQuery:
		unformated_string1 = each.locations
		unformated_string2 = unformated_string1.strip('[')
		unformated_string1 = unformated_string2.strip(']')
		unformated_string2 = unformated_string1.strip('\'')
		location_as_list.append(unformated_string2.split('\', \''))
	return location_as_list

# Converts date query to date
def convertDateQueryToDateList(query):
	listUpdated = []
	for eachItem in query:
		eachEntryFixed1 = str(eachItem).replace("(", "")
		eachEntryFixed2 = eachEntryFixed1.replace(")", "")
		eachEntryFixed3 = eachEntryFixed2.replace(",", "")
		eachEntryFixed4 = eachEntryFixed3.replace("(", "")
		eachEntryFixed5 = eachEntryFixed4.lstrip()
		eachEntryFixed6 = eachEntryFixed5.replace("\'", "")

		listUpdated.append(eachEntryFixed6)
	return listUpdated

# Converts Miles Driven query to list
def convertMilesQueryToMilesList(query):
	listUpdated = []
	for eachItem in query:
		eachEntryFixed1 = str(eachItem).replace("(", "")
		eachEntryFixed2 = eachEntryFixed1.replace(")", "")
		eachEntryFixed3 = eachEntryFixed2.replace(",", "")
		eachEntryFixed4 = eachEntryFixed3.replace("(", "")
		eachEntryFixed5 = eachEntryFixed4.lstrip()
		eachEntryFixed6 = eachEntryFixed5.replace("\'", "")

		listUpdated.append(float(eachEntryFixed6))
	return listUpdated
