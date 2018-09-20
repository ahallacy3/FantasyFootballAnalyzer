from excelEdit import excelEdit
from teams import teams
from scores import scores
from truewins import trueWins
from waeWins import waeWins

fileName = 'Alumni_Fantasy_League.xlsx'
resultsFileName = 'Alumni_Fantasy_League_Results.xlsx'
num_teams = 10
num_weeks_played = 2
num_weeks_total = 13
resultArray = []

seasonResults = excelEdit().reader(num_teams, num_weeks_played, fileName)

teamList = teams().getTeams(num_teams, seasonResults)

teamScores = scores().teamScores(seasonResults, teamList)

totalScores = scores().totalScores(teamScores)

averageScores = scores().avgScores(teamScores)

medianScores = scores().medianScores(teamScores)

rangeScores = scores().rangeScores(teamScores)

stdDevScores = scores().stdDevScores(teamScores)

winsAgainstEveryone = waeWins().totalWinsAgainstEveryone(teamScores)

normalizedWinsAgainstEveryone = waeWins().normalizedWinsAgainstEveryone(winsAgainstEveryone)

waeStrengthOfSchedule = waeWins().strengthOfSchedule(seasonResults, teamScores)

trueWins = trueWins().trueWins(seasonResults, teamList)

teamList.insert(0, 'Team Name')

resultArray.append(teamList)
resultArray.append(totalScores)
resultArray.append(averageScores)
resultArray.append(medianScores)
resultArray.append(rangeScores)
resultArray.append(stdDevScores)
resultArray.append(trueWins)
resultArray.append(winsAgainstEveryone)
resultArray.append(normalizedWinsAgainstEveryone)
resultArray.append(waeStrengthOfSchedule)

excelEdit().writer(resultArray, fileName, resultsFileName)
print(resultArray)


