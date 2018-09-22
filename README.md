## TODO ##
- conditional formatting
- averages for each column
- Ranks - wea, nwea, true wins
- Rank diff - true wins and wea, true wins and nwea
- Charts?
- Predictions individual matchups
- predictions on total score
- playoff predictions

## Project Prereqs ##
* Python 3.7, pip, virtualenv (pip and virtualenv should be included with a python install)
* Python in your PATH
* geckodriver in your PATH (for firefox webscraping)
* * this is not necessary if you're only going to run the excel version

## Project Setup ##
* clone
* virtualenv venv
* activate venv
  * On Windows, venv\Scripts\activate
  * On Mac/Linux, source venv/bin/activate
* pip install -r requirements.txt

## Running Project ##
### Using a formatted excel spreadsheet ###
* Add/update excel workbook to project folder
* python runProgram.py <weekNum> <teamCount> "<filename>" "<sheetname>"
* * weekNum is num of weeks you want evaluated, starting with week 1
* * * weeks that haven't happened will causing confusing results
* * teamCount is the number of teams in your league
* * filename is the path of your input file
* * sheetname is the name of the sheet with your matchup data

### Using data scraped from your espn league ###
* python runProgram.py <weekNum> <teamCount> "<username>" "<password>" "<weekOneUrl>"
* * weekNum is num of weeks you want evaluated, starting with week 1
* * * weeks that haven't happened will causing confusing results
* * teamCount is the number of teams in your league
* * username is your espn account username
* * password if your espn account password
* * weekOneUrl is the url for the week one scoreboard for your league
