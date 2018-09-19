from excelEdit import excelEdit
from teams import teams
from scores import scores
from wins import wins

fileName = 'Alumni_Fantasy_League.xlsx'
resultsFileName = 'Alumni_Fantasy_League_Results.xlsx'
num_teams = 10
num_weeks = 2
resultArray = []

seasonResults = excelEdit().reader(num_teams, num_weeks, fileName)

teamList = teams().getTeams(num_teams, seasonResults)

teamScores = scores().teamScores(seasonResults, teamList)

totalScores = scores().totalScores(teamScores)

averageScores = scores().avgScores(teamScores)

medianScores = scores().medianScores(teamScores)

rangeScores = scores().rangeScores(teamScores)

stdDevScores = scores().stdDevScores(teamScores)

winsAgainstEveryone = wins().totalWinsAgainstEveryone(teamScores)

normalizedWinsAgainstEveryone = wins().normalizedWinsAgainstEveryone(winsAgainstEveryone)

trueWins = wins().trueWins(seasonResults, teamList)

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

excelEdit().writer(resultArray, fileName, resultsFileName)
print(resultArray)


