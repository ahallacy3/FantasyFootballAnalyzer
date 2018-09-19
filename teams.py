
class teams:
    def getTeams(self, num_teams, seasonResults):
        teams = []
        for match in seasonResults[0]:
            teams.append(match[0])
            teams.append(match[3])
        return teams
