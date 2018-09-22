from openpyxl import load_workbook
from openpyxl import Workbook

class excelEdit:
    def reader(self, num_teams, num_weeks, fileName, sheetName):
        wb = load_workbook(fileName)
        dataSheet = wb[sheetName]

        num_rows = 3 + (num_teams / 2) * num_weeks + 1
        matchData = []
        weekData = []
        seasonData = []
        for row in dataSheet['A3:D'+str(int(num_rows))]:
            for cell in row:
                matchData.append(cell.value)
            if matchData[1] is not None:
                weekData.append(matchData)
                matchData = []
            else:
                seasonData.append(weekData)
                matchData = []
                weekData = []
        return seasonData

    def writer(self, results, resultsFileName):
        wb = Workbook()
        sheet = wb['Sheet']
        for col in range(1, len(results) + 1):
            for row in range(1, len(results[col - 1]) + 1):
                sheet.cell(column=col, row=row, value=results[col - 1][row - 1])
        wb.save(resultsFileName)
