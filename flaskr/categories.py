import requests
import datetime

from flask import (
    Blueprint, request, jsonify
)
testJson = {
"category": [
"featured_tours_and_tickets",
"recommended_experiences",
"cruises,_sailing_&_water_tours",
"recommended_experiences",
"walking_&_biking_tours",
"outdoor_activities",
"cruises,_sailing_&_water_tours",
"cruises,_sailing_&_water_tours"
],
"image": [
None,
None,
None,
None,
None,
None,
None,
None
],
"location": [
[
49.1978340149,
-123.064994812
],
[
50.1133308411,
-122.9547576904
],
[
48.4265937805,
-123.3709182739
],
[
49.7491493225,
-123.1333770752
],
[
49.2914733887,
-123.1424026489
],
[
50.1133766174,
-122.9542617798
],
[
48.422203064,
-123.3796234131
],
[
48.4227218628,
-123.3689804077
]
],
"name": [
"whistler_small-group_day_trip_from_vancouver",
"whistler_sasquatch_zipline",
"summer_whale_watching_on_vancouver_island",
"overnight_camping_and_river-rafting_trip_in_squamish",
"vancouver_biking_and_hiking_tour_including_lunch",
"call_of_the_wild_atv_tour",
"victoria_whale_watching_tour_on_a_covered_vessel",
"half-day_whale_watching_adventure_from_vancouver"
],
"price": [
145.0,
135.45,
145.95,
425.24,
135.5,
156.45,
122.0,
181.13
],
"rating": [
5.0,
5.0,
5.0,
5.0,
5.0,
5.0,
4.0,
4.5
],
"timeofday": [
"Morning",
"Morning",
"Evening",
"Evening",
"Morning",
"Morning",
"Evening",
"Evening"
]
}
bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/get_categories', methods=('GET', 'POST'))
def get_categories():
    res = requests.post("http://127.0.0.1:5003/get_recommadations", json = request.get_json());
    return convertToRequiredFormat(res.json())

        
def convertToRequiredFormat(reponseBody):

    totalDays =  datetime.datetime.strptime(request.get_json().get('end_date'), '%Y-%m-%d').date().day - datetime.datetime.strptime(request.get_json().get('begin_date'), '%Y-%m-%d').date().day
    responseBodyToReturn = {}
    print(totalDays)
    for i in range(totalDays+1):
        responseBodyToReturn.update({i+1 : []})

    day = 0
    for i in range((totalDays + 1) * 4):
        place = {}
        place['category'] = reponseBody.get('category')[i] 
        place['image'] = reponseBody.get('image')[i]
        place['location'] = reponseBody.get('location')[i]
        place['timeofday'] = reponseBody.get('timeofday')[i]
        place['rating'] = reponseBody.get('rating')[i]
        place['name'] = reponseBody.get('name')[i]
        place['price'] = reponseBody.get('price')[i]
        responseBodyToReturn.get(((int)((day/4) + 1))).append(place)
        day += 1

    return responseBodyToReturn