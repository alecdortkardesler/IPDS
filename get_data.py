from pandas.io.html import read_html
import pickle

refresh = False

if refresh:
    page = 'html = https://en.wikipedia.org/wiki/Farebox_recovery_ratio'
    wikitables = read_html(page)
    table = wikitables [1]
    pickle.dump(table, open("wiki_table.pkl", "w"))
else:
    table = pickle.load(open("wiki_table.pkl", "r"))

continent = table[0]
country = table[1]
system = table[2]
rates = table[3]
ratios = table[3][1:]

for c in continent
    

def CleanRatio(raw_ratio):
    s = raw_ratio.split("%")
    return float(s[0])/100.00

clean_ratios = []
for ratio in ratios:
    clean_ratios.append(CleanRatio(ratio))
    
# Writing to SQLite Database

create_table_sql = """ CREATE TABLE IF NOT EXISTS sysyems (
                                        ratio REAL,
                                        ); """
cur = conn.cursor()
cur.execute(create_table_sql)

for r in zip clean_ratios:
    sql = """INSERT INTO systems VALUES (%s,%s);""" % r
    cur.execute(sql)
    conn.commit()

# python get_data.py (name of this file)
# sqlite3 rate.db

#for r in zip(clean_ratios, clean_countries):
#    sql = """INSERT INTO systems VALUES (%s,%s);""" % r
#    cur.execute(sql)
#    conn.commit()

for t in zip(rates, countries):
    print(t)
