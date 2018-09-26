import requests
from datetime import datetime, timedelta
from random import randint
from string import Template
from dateutil import parser
import os

def create_observations(startTime, metricId, values):
  subdomain = 'pdt-summit18'
  token = os.environ["PD_API_KEY"]

  tokenTemplate = Template('Token token=$token')
  headers = {'Content-Type': 'application/json', 'Authorization': tokenTemplate.substitute(token = token)}
  url = Template('https://$subdomain.pagerduty.com/api/v1/business_impact_metrics/$metricId/observations').substitute(subdomain = subdomain, metricId = metricId)
  # url = Template('http://localhost:4400/api/v1/business_impact_metrics/$metricId/observations').substitute(metricId = metricId)

  # Fill in values from start time before to 45min after.
  preSpikeEnd = values['preSpike']['length']
  for i in range(0, preSpikeEnd):
    timeToFill = startTime + timedelta(minutes = i)
    value = randint(values['preSpike']['range'][0], values['preSpike']['range'][-1]) # values from 0 to 3
    dateString = timeToFill.isoformat()
    r = requests.post(url, json = { 'observation': { 'value': value, 'observed_at': dateString} }, headers = headers)
    print(r.json())
    r.raise_for_status()

  # Fill in values for spike
  spikeEnd = preSpikeEnd + values['spike']['length']
  for i in range(values['preSpike']['length'], spikeEnd):
    timeToFill = startTime + timedelta(minutes = i)
    value = randint(values['spike']['range'][0], values['spike']['range'][-1])
    dateString = timeToFill.isoformat()
    r = requests.post(url, json = { 'observation': { 'value': value, 'observed_at': dateString} }, headers = headers)
    print(r.json())
    r.raise_for_status()

  # Fill in values after spike
  postSpikeStart = spikeEnd
  for i in range(postSpikeStart, 60):
    timeToFill = startTime + timedelta(minutes = i)
    right = int(values['postSpike']['range'][-1] * (60 - i) / (60 - postSpikeStart))
    left = int(right * 0.8)
    value = randint(left, right)
    print(value)
    dateString = timeToFill.isoformat()
    r = requests.post(url, json = { 'observation': { 'value': value, 'observed_at': dateString} }, headers = headers)
    print(r.json())
    r.raise_for_status()


metrics = {
  'P2U2I0P' : {
    'preSpike': {
      'range': range(0, 3), # values for the pre-spike duration
      'length': 45, # how long before the spike: 45min
    },
    'spike': {
      'range': range(25,35),
      'length': 10, # spike lasts for 10 min
    },
    'postSpike': {
      'range': range(0, 10),
      'length': 5,
    }
  },
  'PLQOINW' : {
    'preSpike': {
      'range': range(25, 50), # values for the pre-spike duration
      'length': 45, # how long before the spike: 45min
    },
    'spike': {
      'range': range(2000, 5000),
      'length': 3, # spike lasts for 3 min
    },
    'postSpike': {
      'range': range(0, 400),
      'length': 12,
    }
  },
  'PHE0HY6' : {
    'preSpike': {
      'range': range(500, 10000), # values for the pre-spike duration
      'length': 45, # how long before the spike: 45min
    },
    'spike': {
      'range': range(100000, 120000),
      'length': 3, # spike lasts for 3 min
    },
    'postSpike': {
      'range': range(0, 1),
      'length': 12,
    }
  }
}

# put times on :00 seconds so we can overwrite them by running script again
startTime = parser.parse('2018-09-12T10:00:00Z')
endTime = parser.parse('2018-09-13T07:00:00Z') # summit end

while (startTime < endTime):
  print(startTime)
  for key in metrics.keys():
    create_observations(startTime, key, metrics[key])
  startTime = startTime + timedelta(hours = 1)
