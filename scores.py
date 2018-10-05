import numpy

class scores:
    def totalScores(self, teamScores):
        totalResult = ['Total']
        for team in teamScores:
            teamSub = 0
            for i in range(1, len(team)):
                teamSub += team[i]
            totalResult.append(float('%.1f' % teamSub))
        return totalResult

    def teamScores(self, seasonResults, teamList):
        teamScores = []
        for team in teamList:
            teamSub = [team]
            for week in seasonResults:
                for match in week:
                    if match[0] == team:
                        teamSub.append(match[1])
                    elif match[3] == team:
                        teamSub.append(match[2])
            teamScores.append(teamSub)
        return teamScores

    def avgScores(self, teamScores):
        totalResult = ['Average']
        for team in teamScores:
            teamSub = 0
            for i in range(1, len(team)):
                teamSub += team[i]
            totalResult.append(float('%.1f' % (teamSub / (len(team) - 1))))
        return totalResult

    def medianScores(self, teamScores):
        totalResult = ['Median']
        for team in teamScores:
            teamSub = []
            for i in range(1, len(team)):
                teamSub.append(team[i])
            totalResult.append(float('%.1f' % numpy.median(teamSub)))
        return totalResult

    def rangeScores(self, teamScores):
        totalResult = ['Range']
        for team in teamScores:
            teamSub = []
            for i in range(1, len(team)):
                teamSub.append(team[i])
            totalResult.append(float('%.1f' % (numpy.max(teamSub) - numpy.min(teamSub))))
        return totalResult

    def stdDevScores(self, teamScores):
        totalResult = ['STDEV']
        for team in teamScores:
            teamSub = []
            for i in range(1, len(team)):
                teamSub.append(team[i])
            totalResult.append(float('%.2f' % (numpy.std(teamSub, ddof=1))))
        return totalResult
