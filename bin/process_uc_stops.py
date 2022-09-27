#!/usr/bin/env python

"""
Download the SEPTA buses GTFS data and unzip stops, stop_times, and trips into
the /data/ folder.
"""

import csv
import json
from collections import defaultdict
from shapely.geometry import mapping, shape, Point
from os.path import abspath, dirname

root = dirname(dirname(abspath(__file__)))
stops_file = f'{root}/data/stops.txt'
stop_times_file = f'{root}/data/stop_times.txt'
trips_file = f'{root}/data/trips.txt'
neighborhoods_file = f'{root}/data/Neighborhoods_Philadelphia.geojson'

with open(stops_file) as infile:
    reader = csv.DictReader(infile)
    stops = [
        {
            'stop_id': row['stop_id'],
            'stop_name': row['stop_name'],
            'wheelchair_boarding': row['wheelchair_boarding'],
            'geom': Point(float(row['stop_lon']), float(row['stop_lat']))
        }
        for row in reader
    ]

with open(neighborhoods_file) as infile:
    neighborhoods = json.load(infile)
    for feature in neighborhoods['features']:
        if feature['properties']['name'] == 'UNIVERSITY_CITY':
            uc = shape(feature['geometry'])
            break
    else:
        raise Exception('University City not found.')

uc_stops = {
    stop['stop_id']: {**stop, 'route_ids': set()}
    for stop in stops
    if uc.contains(stop['geom'])
}
uc_trip_stops = defaultdict(set)

with open(stop_times_file) as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        trip_id = row['trip_id']
        stop_id = row['stop_id']
        if stop_id in uc_stops:
            uc_trip_stops[trip_id].add(stop_id)

with open(trips_file) as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        route_id = row['route_id']
        trip_id = row['trip_id']
        if trip_id in uc_trip_stops:
            for stop_id in uc_trip_stops[trip_id]:
                uc_stops[stop_id]['route_ids'].add(route_id)

uc_stop_features = [
    {
        'type': 'Feature',
        'id': stop['stop_id'],
        'properties': {
            'stop_id': stop['stop_id'],
            'stop_name': stop['stop_name'],
            'wheelchair_boarding': stop['wheelchair_boarding'],
        },
        'geometry': mapping(stop['geom'])
    }
    for stop in uc_stops.values()
]

print(json.dumps([
    {
        'stop_id': stop['stop_id'],
        'stop_name': stop['stop_name'],
        'wheelchair_boarding': stop['wheelchair_boarding'],
        'routes_ids': list(sorted(stop['route_ids'])),
        'geom': mapping(stop['geom'])
    }
    for stop in uc_stops.values()
], indent=2))