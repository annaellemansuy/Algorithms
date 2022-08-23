#Scenario : you want to use certain radio stations to broadcast a message to as many ppl as possible in certain places

Places_Needed = set(["Paris", "New York", "Hong Kong", "London", "Toronto", "Rome", "Beijing"])
stations = {}
stations["BBC"] = set(["London", "Hong Kong", "New York"])
stations["TV5Monde"] = set(["Paris", "Rome", "Toronto"])
stations["SCMP"] = set(["Hong Kong", "Beijing"])
stations["CNN"] = set(["New York", "London"])
final_stations = set()


while len(Places_Needed) > 0:
  best_station = None
  places_covered = set()
  for station, stations_for_places in stations.items():
    covered = Places_Needed & stations_for_places #set intersection
    if len(covered) > len(places_covered):
      print(Places_Needed)
      best_station = station
      places_covered = covered
      Places_Needed = Places_Needed - places_covered
      final_stations.add(best_station)


print(final_stations) # stations needed so all the places covered
print(Places_Needed)

