from excelEdit import excelEdit
from teams import teams
from scores import scores
from trueWins import trueWins
from waeWins import waeWins
from espnSpider import espnSpider
import sys

fileName = 'Alumni_Fantasy_League.xlsx'

weekOneUrl = 'http://games.espn.com/ffl/scoreboard?leagueId=1322187&matchupPeriodId=1'
num_weeks_total = 13

def runProgramWithLogin(weekNum, teamCount, userName, passWord, weekOneUrl):
    dataCrawler = espnSpider(weekOneUrl)
    dataCrawler.login(userName, passWord)
    seasonResults = dataCrawler.getData(weekNum, teamCount)
    compileResults(teamCount, seasonResults, weekNum)

def runProgramWithSpreadsheet(weekNum, teamCount, fileName, sheetName):
    seasonResults = excelEdit().reader(teamCount, weekNum, fileName, sheetName)
    compileResults(teamCount, seasonResults, weekNum)

def compileResults(teamCount, seasonResults, weekNum):
    resultArray = []

    teamList = teams().getTeams(teamCount, seasonResults)

    teamScores = scores().teamScores(seasonResults, teamList)

    totalScores = scores().totalScores(teamScores)

    averageScores = scores().avgScores(teamScores)

    medianScores = scores().medianScores(teamScores)

    rangeScores = scores().rangeScores(teamScores)

    stdDevScores = scores().stdDevScores(teamScores)

    winsAgainstEveryone = waeWins().totalWinsAgainstEveryone(teamScores)

    normalizedWinsAgainstEveryone = waeWins().normalizedWinsAgainstEveryone(winsAgainstEveryone)

    waeStrengthOfSchedule = waeWins().strengthOfSchedule(seasonResults, teamScores)

    actualWins = trueWins().getTrueWins(seasonResults, teamList)

    winDiff = waeWins().winDiff(normalizedWinsAgainstEveryone, actualWins)

    nStrengthOfSchedule = waeWins().normalizedLosses(waeStrengthOfSchedule)

    lossDiff = waeWins().lossDiff(nStrengthOfSchedule, actualWins, weekNum)

    expectedWins = waeWins().expectedWins(winsAgainstEveryone, waeStrengthOfSchedule, weekNum)

    scheduleLuck = waeWins().scheduleLuck(actualWins, expectedWins)

    teamList.insert(0, 'Team Name')
    teamList.append('')
    teamList.append('Averages')

    resultArray.append(teamList)
    resultArray.append(totalScores)
    resultArray.append(averageScores)
    resultArray.append(medianScores)
    resultArray.append(rangeScores)
    resultArray.append(stdDevScores)
    resultArray.append(actualWins)
    resultArray.append(winsAgainstEveryone)
    resultArray.append(normalizedWinsAgainstEveryone)
    resultArray.append(winDiff)
    resultArray.append(waeStrengthOfSchedule)
    resultArray.append(nStrengthOfSchedule)
    resultArray.append(lossDiff)
    resultArray.append(expectedWins)
    resultArray.append(scheduleLuck)

    resultArray = addAverage(resultArray)

    excelEdit().writer(resultArray, 'Analysis_Results.xlsx')


def addAverage(resultArray):
    for i in range(1, len(resultArray)):
        total = 0
        for j in range(1, len(resultArray[i])):
            total += resultArray[i][j]
        resultArray[i].append('')
        resultArray[i].append(total / (len(resultArray[i]) - 2))
    return resultArray

if __name__ == "__main__":
    if len(sys.argv) == 5:
        runProgramWithSpreadsheet(int(sys.argv[1]), int(sys.argv[2]),sys.argv[3],sys.argv[4])
    elif len(sys.argv) == 6:
        runProgramWithLogin(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print('Invalid number of arguments')