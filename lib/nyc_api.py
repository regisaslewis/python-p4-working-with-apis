import requests
import json

class GetPrograms:
    
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content
  
    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for n in programs:
            programs_list.append(n["agency"])

        return programs_list

# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for n in sorted(set(programs_schools)):
    print(n)