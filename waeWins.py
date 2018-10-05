class waeWins:
    def winsAgainstEveryone(self, seasonResults, teamList):
        winArray = []
        for team in teamList:
            wins = 0
            for week in seasonResults:
                for match in week:
                    if team == match[0]:
                        if match[1] > match[2]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
                    elif team == match[3]:
                        if match[2] > match[1]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
            winArray.append(wins)
        return winArray

    def winsAgainstEveryoneByWeek(self, teamScores, team, week):
        score = 0
        wae = 0
        for teamScore in teamScores:
            if teamScore[0] == team:
                score = teamScore[week]
        for teamScore in teamScores:
            if score > teamScore[week]:
                wae += 1
        return wae

    def totalWinsAgainstEveryone(self, teamScores):
        waeArray = ['Wins Against Everyone']
        for team in teamScores:
            wae = 0
            for i in range(1, len(team)):
                wae += self.winsAgainstEveryoneByWeek(teamScores, team[0], i)
            waeArray.append(wae)
        return waeArray

    def normalizedWinsAgainstEveryone(self, wae):
        nwae = ['Normalized WAE']
        for i in range(1, len(wae)):
            nwae.append(float('%.1f' % (wae[i] / (len(wae) - 2))))
        return nwae

    def normalizedLosses(self, sos):
        nSos = ['Normalized Losses']
        for i in range(1, len(sos)):
            nSos.append(float('%.1f' % (sos[i] / (len(sos) - 2))))
        return nSos

    def strengthOfSchedule(self, seasonResults, teamScores):
        sosArray = ['SoS']
        for team in teamScores:
            sos = 0
            for i in range(1, len(seasonResults) + 1):
                for match in seasonResults[i - 1]:
                    if match[0] == team[0]:
                        sos += self.winsAgainstEveryoneByWeek(teamScores, match[3], i)
                    elif match[3] == team[0]:
                        sos += self.winsAgainstEveryoneByWeek(teamScores, match[0], i)
            sosArray.append(sos)
        return sosArray

    def winDiff(self, nWae, actualWins):
        winDiff = ['Win Diff']
        for i in range(1, len(nWae)):
            winDiff.append(nWae[i] - actualWins[i])
        return winDiff

    def lossDiff(self, nSos, actualWins, weekNum):
        lossDiff = ['Loss Diff']
        for i in range(1, len(nSos)):
            lossDiff.append(nSos[i] - (weekNum - actualWins[i]))
        return lossDiff

    def expectedWins(self, wae, waeSos, weekNum):
        expectedWins = ['Expected Wins So Far']
        for i in range(1, len(wae)):
            expectedWins.append(float('%.2f' % ((wae[i] - (len(wae) - 2) * weekNum / 2)/(len(wae) - 2) + weekNum / 2)))
        return expectedWins

    def scheduleLuck(self, actualWins, expectedWins):
        scheduleLuck = ['How bad has your schedule fucked you?']
        for i in range(1, len(actualWins)):
            scheduleLuck.append(actualWins[i] - expectedWins[i])
        return scheduleLuck