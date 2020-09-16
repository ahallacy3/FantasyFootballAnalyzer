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


def runProgramWithLogin(weekNum, userName, passWord, weekOneUrl, resultFileName):
    dataCrawler = espnSpider(weekOneUrl)
    dataCrawler.loadInitialPage()
    dataCrawler.login(userName, passWord)
    seasonResults = dataCrawler.getData(weekNum)
    compileResults(seasonResults, weekNum, resultFileName)

def runProgramWithoutLogin(weekNum, weekOneUrl, resultFileName):
    dataCrawler = espnSpider(weekOneUrl)
    dataCrawler.loadInitialPage()
    seasonResults = dataCrawler.getData(weekNum)
    compileResults(seasonResults, weekNum, resultFileName)


def runProgramWithSpreadsheet(weekNum, teamCount, fileName, sheetName, resultFileName):
    seasonResults = excelEdit().reader(teamCount, weekNum, fileName, sheetName)
    compileResults(seasonResults, weekNum, resultFileName)


def compileResults(seasonResults, weekNum, resultsFileName):
    resultArray = []

    teamList = teams().getTeams(seasonResults)

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

    resultArray = dataSort(resultArray)

    resultArray[0].append('')
    resultArray[0].append('Averages')

    resultArray = addAverage(resultArray)

    excelEdit().writer(resultArray, resultsFileName)


def addAverage(resultArray):
    for i in range(1, len(resultArray)):
        total = 0
        for j in range(1, len(resultArray[i])):
            total += resultArray[i][j]
        resultArray[i].append('')
        resultArray[i].append(total / (len(resultArray[i]) - 2))
    return resultArray


def dataSort(results):
    sortedResults = []
    sortOrder = []
    for i in range(0, len(results)):
        if results[i][0] == "How bad has your schedule fucked you?":
            sortArray = results[i][1:len(results[i])]
            for j in range(0, len(sortArray)):
                sortOrder.append(sortArray.index(max(sortArray)))
                sortArray.remove(max(sortArray))
    for i in range(0, len(results)):
        sortedResults.append([])
        sortedResults[i].append(results[i][0])
        results[i].remove(results[i][0])
        for j in range(0, len(sortOrder)):
            sortedResults[i].append(results[i][sortOrder[j]])
            results[i].pop(sortOrder[j])
    return sortedResults


if __name__ == "__main__":
    if len(sys.argv) == 5:
        runProgramWithSpreadsheet(int(sys.argv[1]), int(sys.argv[2]),sys.argv[3],sys.argv[4])
    elif len(sys.argv) == 7:
        if sys.argv[6] != 'False':
            runProgramWithLogin(int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        else:
            runProgramWithoutLogin(int(sys.argv[1]), sys.argv[4], sys.argv[5])
    else:
        print('Invalid number of arguments')