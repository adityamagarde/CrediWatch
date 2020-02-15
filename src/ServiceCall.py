from utils_ab import companyValidation
from UrbanRural_tarun import findCityTier
from NewsAnalysis import newsAnalysor


def calculateIndividualOtherScore(address,cin,companyName,state,activityDescription):
	individualScore = []
	
	#city tier score calculation
	tierCityScore = findCityTier(address)
	if tierCityScore == 1:
		individualScore.append(0.3)
	elif tierCityScore == 2:
		individualScore.append(0.2)
	elif tierCityScore == 3:
		individualScore.append(0.1)

	#companyValidation score
	companyNameValidation = companyValidation(cin,companyName)
	if companyNameValidation == 10:
		individualScore.append(0.3)
	elif companyNameValidation == 8:
		individualScore.append(0.2)

	#News Analysis
	newsAnalysisScore = (newsAnalysor(state)+newsAnalysor(activityDescription))/2
	individualScore.append(newsAnalysisScore)
	return individualScore

def calculateTotalOtherScore(individualScore):
	sum = 0.0
	for value in individualScore:
		sum += value
	return sum

if __name__ == "__main__":	
	print(calculateTotalOtherScore(calculateIndividualOtherScore("Room 1116, Homi Bhabha Block, Tata Memorial Hospital, Dr.Borges Road, Parel MUMBAI Mumbai City-400012 Maharashtra","U85100MH2020NPL335745","HEMATOLOGY CANCER CONSORTIUM - ASSOCIATION","Maharashtra","Community, personal & Social Services")))
