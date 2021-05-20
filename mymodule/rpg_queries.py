import sqlite3
import pandas as pd


def execute_query(query):
    results = curs.execute(query)
    return pd.DataFrame(results)


# set up the query variables

TOTAL_CHARACTERS = """select count(character_id) 
                      from charactercreator_character"""
TOTAL_SUBCLASS = """select count(mage_ptr_id) 
                    from charactercreator_necromancer"""
TOTAL_ITEMS = """select count(item_id) from armory_item"""
WEAPONS = """select count(item_ptr_id) from armory_weapon"""
NON_WEAPONS = """select count(item_id) from armory_item ai
                 left join armory_weapon aw
                 on ai.item_id = aw.item_ptr_id
                 where aw.item_ptr_id is null"""
CHARACTER_ITEMS = """select character_id, count(item_id) 
                     from charactercreator_character_inventory
                     group by character_id 
                     limit 20"""
CHARACTER_WEAPONS = """select character_id, count(item_id) 
                       from charactercreator_character_inventory 
                       left join armory_weapon aw
                       where item_id = aw.item_ptr_id
                       group by character_id
                       limit 20"""
AVG_CHARACTER_ITEMS = """select avg(count) from (
                         select character_id, count(item_id) as count
                         from charactercreator_character_inventory
                         group by character_id 
                         limit 20)"""
AVG_CHARACTER_WEAPONS = """select avg(count) from(select character_id, count(item_id) as count
                           from charactercreator_character_inventory 
                           left join armory_weapon aw
                           where item_id = aw.item_ptr_id
                           group by character_id
                           limit 20)"""

# set up the connection
con = sqlite3.connect('../rpg_db.sqlite3')
con_rowfactory = sqlite3.Row
curs = con.cursor()

# process through the variables
print(execute_query(TOTAL_CHARACTERS))
print(execute_query(TOTAL_SUBCLASS))
print(execute_query(TOTAL_ITEMS))
print(execute_query(WEAPONS))
print(execute_query(NON_WEAPONS))
print(execute_query(CHARACTER_ITEMS))
print(execute_query(CHARACTER_WEAPONS))
print(execute_query(AVG_CHARACTER_ITEMS))
print(execute_query(AVG_CHARACTER_WEAPONS))

con.close()
