from locator import locator
import pandas as pd
import random


# Correctness Tests and Error Handling
good_coords = [[30, -86.7], [44.5, -60], [30, -60], [44.5, -86.7]]
bad_coords_bounds = good_coords + [[-90.1, 181.4]]
bad_coords_len = good_coords[0:1]
bad_coords_dup = [[40.5, -86.7],[40.5, -86.7],[40.5, -86.7],[40.5, -86.7]]
good_airports = ["0J0", "67T", "D95", "53T"]
bad_airport = ["bogus", "0J0"]
brk = "----------------------------------------------------------"

print("\nUnit Tests and Error Handling")
print("Testing good initialization. No output should appear.")
good_locator = locator(good_coords)
print(brk)
print("Testing bad coords. Three msgs should appear.")
bad_locator = locator(bad_coords_bounds)
bad_locator.update_coords(bad_coords_dup)
bad_locator.update_coords(bad_coords_len)
print(brk)
print("Testing check_locations() with valid ids. Expect: [True, False, True, False]")
res = good_locator.check_locations(good_airports)
print(res)
print(brk)
print("Testing check_locations with invalid (None) region. Expect: msg and empty list.")
res = bad_locator.check_locations(good_airports)
print(res)
print(brk)
print("Fix region. Test check_locations. Expect [True, False, True, False]")
bad_locator.update_coords(good_coords)
res = bad_locator.check_locations(good_airports)
print(res)
print(brk)
print("Test bad id. Expect error message and output: [False, True]")
res = good_locator.check_locations(bad_airport)
print(res)
print(brk)
print("Test internal get_coords function. No output should appear.")
assert good_locator.get_coords("KBOK") == [42.0739444, -124.2897778]
assert good_locator.get_coords("KOGS")  == [44.6822500, -75.4632500]
assert good_locator.get_coords("45S")  == [43.1109725, -121.0941667]
assert good_locator.get_coords("KSJX")  == [45.6922222, -85.5666111]
assert good_locator.get_coords("64I")  == [38.6314417, -85.4434194]
assert good_locator.get_coords("KPGA")  == [36.9260694, -111.4483506]
print(brk)
print("Test internal get_coords function with abbreivated id. No output should appear.")
assert good_locator.get_coords("OEB") == good_locator.get_coords("KOEB")
assert good_locator.get_coords("DRP") == good_locator.get_coords("KDRP")
print(brk)
# Boundary Tests
airports_region = [[69.7328889, -163.0053333], [68.3487722, -166.7992611], [39.9461081, -122.1711167], [38.1435758, -122.5570914]]
ids = ["PPIZ", "PAPO", "0O4", "KDVO"]

print("\nBoundary Tests")
print("Test airports as vertices of region. Expect all False.")
loc = locator(airports_region)
res = loc.check_locations(ids)
print(res)
print(brk)

# Stress Tests
df = pd.read_csv("locations.csv", header=None, names=["ID", "Coords"])
all_ids = list(df["ID"])
del all_ids[0]
globe = [[-89.9,179.9], [-89.9,-179.9], [89.9,179.9], [89.9,-179.9]]

random_region = [[random.uniform(-89.9, 89.9) for i in range(2)] for k in range(4000)]
null = [0,0]


print("\nStress Tests")
print("Test all ids on full globe region. No output should appear.")
stress_locator = locator(globe)
res = stress_locator.check_locations(all_ids)
for val in res :
    assert val
print(brk)
print("Test region with randomly generated points.")
stress_locator.update_coords(random_region)
res = stress_locator.check_locations(all_ids)
print(sum(i==True for i in res), " aiports located within random region.")
print(brk)




