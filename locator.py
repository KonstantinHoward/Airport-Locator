from shapely.geometry import Point, Polygon
import pandas as pd


class locator :
    ''' Class encapsulates a given region in lat, long described
    as the vertices of a polygon. Region can be updated. Evaluation
    on a list of airport identifiers returns results but does not 
    change state.
    '''
    def __init__(self, coords: list[list[float]]) :
        ''' Creates locator object with region on given coords.
        Loads airport locations from csv to dictionary.
        :param coords: list of pairs of floats describing 
        lat,long vertices of the region
        '''
        self.region = None
        self.update_coords(coords)
        df = pd.read_csv("t.csv", header=None, names=["ID", "Coords"])
        self.airport_dict = df.set_index("ID").to_dict()["Coords"]
        del df
        

    def update_coords(self, coords: list[list[float]]) :
        ''' Updates polygon region contained by object. Checks
        for valid lat, long values and valid polygon shape. If
        failure, locator region will be None.
        :param coords: list of pairs of floats describing 
        lat,long vertices of the region
        '''
        for v in coords :
            if abs(v[0]) > 90 or abs(v[1]) > 180 :
                print("Coordinates are not valid in latitude, longitude.")
                return
        temp = self.region
        try :
            self.region = Polygon(coords)
        except ValueError :
            print("Coordinates provided do not describe a valid polygon.")
            self.region = temp


    def check_locations(self, airports: list[str]) -> list[bool] : 
        ''' Retrieves lat, long coordinates of each airport, checks
        if in region, and returns bool in same order as provided airport ids.
        An invalid airport id will notify user but appear as False in list.
        :param airports: list of FAA public airport identifiers
        :return: list of bools describing whether respective id is in region
        '''
        result = []
        if self.region is None :
            print("No region saved.")
            return result
        for id in airports :
            loc = self.get_coords(id)
            if loc == [0,0] :
                result.append(False)
            else :
                p = Point(loc)
                result.append(self.region.contains(p))
        return result
    
    def get_coords(self, id: str) -> list[float] :
        ''' Retrieves coordinates of given airport as pair of floats.
        Returns [0,0] if airport id is invalid.
        :param id: FAA public airport identifier
        :return: given airport's lat, long coordinates
        '''
        if id not in self.airport_dict:
            print(id + " is not a valid FAA public airport ID. Result will be False.")
            return [0,0]
        return list(map(float, self.airport_dict[id]))



def main():
    points = [[41.75307, -85.130366], [41.75307, -84.901802], [41.628527, -85.130366], [41.628527, -84.901802]]
    airports = ['I58', 'ANQ', 'OEB']
    

if __name__ == "__main__":
    main()