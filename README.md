# ids-script
Script to generate some observations to impact data service


## To Run:

Fetch an user API token from pagerduty.com.
```
-> Go to pagerduty app
-> Go to User profile
-> Go to User Settings tab
-> Under API Access, create User API Token
```

### Setup

Make sure [brew](https://brew.sh) is installed
```
$ brew install pipenv
$ pipenv install
```

### Things you will want to change in the script file (script.py):

Change the subdomain to the one you want metric data in:
```
subdomain = 'pdt-summit18'
```

Change the Impact Metrics ids to whichever ones you have created
```
P2U2I0P
PLQOINW
PHE0HY6
```

Change the start and end time for the data you want to fill in (times in UTC, can use: https://coderstoolbox.net/unixtimestamp/)

```
startTime = parser.parse('2018-09-12T10:00:00Z')
endTime = parser.parse('2018-09-13T07:00:00Z') # summit end
```


### Run the script
```
$ PD_API_KEY=XXXXX pipenv run python script.py
```
