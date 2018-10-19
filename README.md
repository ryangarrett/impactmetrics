# ids-script
Script to generate some observations to impact data service


## PagerDuty Setup:

Fetch an user API token from pagerduty.com.
```
-> Go to pagerduty app
-> Go to User profile
-> Go to User Settings tab
-> Under API Access, create User API Token
```

### Pre reqs

-> brew (https://docs.brew.sh/Installation) 
-> Xcode (Apple App Store) 

### Setup

```
$ brew install python
$ brew install pip
$ brew install pipenv
$ vi ~/.bash_profile --> Add the below aliases. DO NOT UNINSTALL PYTHON 2.x<-- 
	alias python='python3' 
	alias pip='pip3'
$ pipenv install requests
$ pip install python-dateutil
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
startTime = parser.parse('2018-09-28T20:58:01Z')
endTime = parser.parse('2018-09-28T21:20:01Z') # summit end
```


### Run the script
```
$ PD_API_KEY=XXXXX pipenv run python script.py
```
