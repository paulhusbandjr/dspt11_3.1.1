import sqlite3
import pandas as pd
import rpg_queries

# setting connection and creating cursor for queries.
conn = sqlite3.connect('../rpg_db.sqlite3')
conn.row_factory = sqlite3.Row
curs = conn.cursor()

""" Testing of total character count query (DONE)"""
# total_characters_results = curs.execute(queries.TOTAL_CHARACTERS).fetchall()
# total_characters_df = pd.DataFrame(total_characters_results)
# print(total_characters_results[0][0])

"""Testing of subclass count query"""
# total_subclass_results = curs.execute(queries.TOTAL_SUBCLASS).fetchall()
# total_subclass_df = pd.DataFrame(total_subclass_results)

""" Testing of total item count query"""
total_items_results = curs.execute(rpg_queries.TOTAL_ITEMS).fetchall()
total_items_df = pd.DataFrame(total_items_results)

# Close the connection after query pulled
conn.close()

""" Print statements to review results"""
# print(len(total_characters_df))
# print(total_subclass_df.head())
# print(total_items_df)

"""Work from lecture - used as template for query writing"""
select_weapon_query = """select * from armory_weapon
                         left join armory_item ai 
                         on armory_weapon.item_ptr_id = ai.item_id"""

# weapon_results = curs.execute(select_weapon_query).fetchall()
# weapon_df = pd.DataFrame(weapon_results)
# weapon_df.drop(columns=[weapon_df.columns[2]], inplace=True)
# print(weapon_df.head())
