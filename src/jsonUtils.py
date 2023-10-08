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

    def get_avaliable_keys(self) -> list:
        keys = self.jsonData['maps'][0].keys()

        return keys

    def get_all_authors(self) -> list:
        """Gets all authors ordered A-Z in a list

        Returns:
            list: List of authors
        """
        authors = set(map['Author'] for map in self.jsonData['maps'])
        return sorted(authors)
    
    
    def get_from_data(self, i_valuetype, i_value, o_itemtype):
        """Gets any data from the json file

        Args:
            i_valuetype (str): What key is the given value:
                - Name, Author, WAD, PSN, PC, xbox
            i_value (any): Main value of the key you want to choose from.
            o_itemtype (str): What item do you want to know.

        Returns:
            _type_: Item that you want to know.

        Example:
            get_from_data('Name', 'Attack', 'WAD') -> 'ATTACK.WAD'
            get_from_data('Name', 'Attack', 'PSN') -> 1
            get_from_data('Name', 'Attack', 'Author') -> 'Tim Willits'

        """
        o_item = []
        for item in self.jsonData["maps"]:
            if item[i_valuetype] == i_value:
                try:
                    o_item.append(item[o_itemtype])
                    
                except KeyError:
                    print(f"Unknown itemtype: {o_itemtype}.")
                    print(f"Known itemtypes are: {self.get_avaliable_keys()}")
        return o_item
    
    def get_all_wads_ordered(self, order='A-Z', displayExtension=True) -> list:
        """Gets all wads in a given order.

        Args:
            order (str, optional): Selects speciffic order. Defaults to 'A-Z':
                'A-Z', 'Z-A', PSN'
            displayExtension (bool, optional): If true it will preserve the
                *.WAD file extension. Defaults to True.

        Returns:
            list: Wads in order
        """
        wads = []
        for item in self.jsonData["maps"]:
                    wads.append(item["WAD"])

        match order:
            case 'A-Z': 
                wads = sorted(wads)  
            case 'Z-A':
                wads = sorted(wads, reverse=True)   
            case 'PSN':
                wads = sorted(wads, key= lambda x: self.get_from_data(
                    'WAD', x, 'PSN'))
       
        if displayExtension != True:
            wads_noextension = []
            for item in wads:
                wads_noextension.append(item.rsplit('.', 1)[0])
            wads = wads_noextension
        return wads


if __name__ == '__main__':
    # Tests for debugging this module.
    maps = MapsJson('src/ml_info.json')
    print(f"\nWADS ORDERED:\n{maps.get_all_wads_ordered(displayExtension=False,order='PSN')}")
    print(f"\nALL AUTHORS: \n{maps.get_all_authors()}")
    print(f"\n GETTER TEXT: \n{maps.get_from_data('Author', 'Jim Flynn', 'WAD')}")