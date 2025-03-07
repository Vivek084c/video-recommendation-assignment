import json
from box import Box

class Json_Util:
    def convertToBox(jsonFile):
        """
        converts the json file into a box object
        """
        # Convert JSON to Python dictionary
        data_dict = json.loads(jsonFile)

        # Convert dictionary to Box object
        data_box = Box(data_dict)
        return data_box

