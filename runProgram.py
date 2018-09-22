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
    compileResults(teamCount, seasonResults)

def runProgramWithSpreadsheet(weekNum, teamCount, fileName, sheetName):
    seasonResults = excelEdit().reader(teamCount, weekNum, fileName, sheetName)
    print(seasonResults)
    compileResults(teamCount, seasonResults)

def compileResults(teamCount, seasonResults):
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
    resultArray.append(waeStrengthOfSchedule)

    excelEdit().writer(resultArray, 'result.xlsx')


if __name__ == "__main__":
    if len(sys.argv) == 5:
        runProgramWithSpreadsheet(int(sys.argv[1]), int(sys.argv[2]),sys.argv[3],sys.argv[4])
    elif len(sys.argv) == 6:
        runProgramWithLogin(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print('Invalid number of arguments')