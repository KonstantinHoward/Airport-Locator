from locator import locator


good_coords = [[41.75307, -85.130366], [41.75307, -84.901802], [41.628527, -85.130366], [41.628527, -84.901802]]
bad_coords_bounds = good_coords + [[-90.1, 181.4]]
bad_coords_len = good_coords[0:2]
bad_coords_dup = [good_coords[3], good_coords[3], good_coords[3], good_coords[2]]

good_airports = ['OJO', 'ANQ', 'OEB']
bad_airports = good_coords + [["WPFW"]]

# Test good init
good_locator = locator(good_coords)
good_locator.update_coords(bad_coords_len)


bad_locator = locator(bad_coords_bounds)
bad_locator.update_coords(bad_coords_dup)
bad_locator.update_coords(good_coords)


