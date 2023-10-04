import json



class MapsJson():
    """ JSON Utils:
        Variables:
            jsonData (dict): Full read json file
    """
    def __init__(self, json_filepath):
        """Loads the json file first

        Args:
            json_filepath (str): JSON path.
        """
        self.jsonData:dict = self.__load_json(json_filepath)
        
    
    def __load_json(self, filepath) -> dict:
        """Loads json file

        Args:
            filepath (str): File path of the json

        Returns:
            dict: Data grabbed from python.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    
    def get_wad_name(self, wad_filename):
        """Gets wad name from a given wad.

        Args:
            wad_filename (_type_): Wad file. Like ATTACK.WAD

        Returns:
            str: Wad Name
            None: If wat not found. (TODO: Make a better error output!)
        """
        for item in self.jsonData["maps"]:
            if item["WAD"] == wad_filename:
                return item["Name"]              
        return None # Wad Not found!

    def get_from_filename(self, wad_filename, itemtype):
        """Gets any data by giving the wad filename 

        Args:
            wad_filename (str): Wad filename. (Like CATWALK.WAD)
            itemtype (_type_): What you want to look for:
                'Name', 'PC', 'PSX', 'Xbox', 'PSN'

        Returns:
            str, int: Return depending on user input.
        """
        for item in self.jsonData["maps"]:
            if item["WAD"] == wad_filename:
                return item[itemtype]              
        return None # Wad Not found!
    
    def get_all_wads_ordered(self, order='A-Z') -> list:
        wads = []
        for item in self.jsonData["maps"]:
                    wads.append(item["WAD"])

        match order:
            case 'A-Z': 
                wads = sorted(wads)  
            case 'Z-A':
                wads = sorted(wads, reverse=True)   
            case 'PSN':
                wads = sorted(wads, key= lambda x: self.get_from_filename(x, 'PSN'))
       
        return wads