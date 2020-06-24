import json
import os

class SigHelper:
    
    here = os.path.dirname(__file__)
    
    def __init__(self):
        pass

    def getAllBossData(self, tier, difficulty):
        with open(os.path.join(self.here,'prog.json')) as json_file:
            return_data = ''
            data = json.load(json_file)
            for boss, value in data['tiers'][tier][difficulty].items():
                #return_data += boss + '\t\t' + value['best'] + '\t' + value['wipes'] + ' wipes\n'
                return_data += ('{} {} {} wipes\n').format(boss, value['best'],value['wipes'])
            return return_data
    
    def getBossData(self, tier, difficulty, boss):
        with open(os.path.join(self.here,'prog.json')) as json_file:
            data = json.load(json_file)
            return_data = {}
            return_data['wipes'] = data['tiers'][tier][difficulty][boss]['wipes']
            return_data['best'] = data['tiers'][tier][difficulty][boss]['best']
            return_data['log'] = data['tiers'][tier][difficulty][boss]['log']
            return return_data
    
    def getAllBossNames(self, tier):
        with open(os.path.join(self.here,'prog.json')) as json_file:
            data = json.load(json_file)
            return_data = {'bosses':[]}
            for boss in data['tiers'][tier]['mythic']:
                return_data['bosses'].append(boss)
            return return_data

    def getAllTierNames(self):
        with open(os.path.join(self.here,'prog.json')) as json_file:
            data = json.load(json_file)
            return_data = {'tiers':[]}
            for tier in data['tiers']:
                return_data['tiers'].append(tier)
            return return_data