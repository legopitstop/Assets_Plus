# Removes comments in all JSON files
import commentjson
import json
import glob
import os

PATH = os.path.dirname(os.path.realpath(__file__))

def parse(dir:str, name:str):
    for fp in glob.glob(PATH+f'/{dir}/**', recursive=True):
        print(fp)
        if os.path.isfile(fp):
            try:
                with open(fp, 'r') as r:
                    dat = commentjson.load(r)
            except Exception as e:
                print(e)
                return 0

            with open(fp, 'w') as w:
                w.write(json.dumps(dat, indent=2))

parse('biomes', 'biome')
parse('blocks', 'block')
parse('cameras', 'camera')
parse('entities', 'entity')
parse('feature_rules', 'feature_rule')
parse('features', 'feature')
parse('items', 'item')
parse('loot_tables', 'loot_table')
parse('recipes', 'recipe')
parse('spawn_rules', 'spawn_rule')
parse('trading', 'trading')

print('Done!')