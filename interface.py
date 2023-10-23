from locator import locator
import sys

def get_region() -> list[list[float]] :
    region = []
    print("Type your coordinates in the form: 'x.x,x.x' one at a time, then press enter. Type 'q' when done.")
    
    while True :
        rd = input("->")
        if rd == "exit" :
            sys.exit()
        if rd == 'q' :
            break
        try :
            point = list(map(float, rd.strip().split(",")))
        except ValueError:
            print("Coordinates must be of form 'x.x,x.x'.")
            continue
        region.append(point)
    return region

def get_airports() -> list[str] :
    airports = []
    print("Type the FAA airpot identifier, then press enter. Type 'q' when done.")
    while True :
        rd = input("->")
        if rd == "exit" :
            sys.exit()
        if rd == 'q' :
            break
        airports.append(rd.strip())
    return airports

def main() :
    print("Type 'exit' at anytime to quit.")
    region = get_region()
    loc = locator(region)
    
    airports = get_airports()
    res = loc.check_locations(airports)
    print("Result: ", res)

    while True :
        print("Enter '1' to update region. Enter '2' to enter more airport identifiers.")
        rd = input("->")
        if rd == 'exit' :
            sys.exit()
        if rd == "1" :
            loc.update_coords(get_region())
        elif rd == "2" :
            airports = get_airports()
        else : 
            print("Enter '1' to update region. Enter '2' to enter more airport identifiers.")
        res = loc.check_locations(airports)
        print("Result: ", res)

if __name__ == "__main__":
        main()