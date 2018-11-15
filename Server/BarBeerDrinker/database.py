from sqlalchemy import create_engine
from sqlalchemy import sql

from BarBeerDrinker import config

engine = create_engine(config.database_uri)

def get_bars():
    with engine.connect() as con:
        rs = con.execute("SELECT barId, barName, license, city, phone, address FROM bars;")
        return [dict(row) for row in rs]

def find_bar(barId):
    with engine.connect() as con:
        query = sql.text(
            "SELECT barId, barName,license, city, phone,address FROM bars WHERE barId= :barId;"
        )

        rs = con.execute(query, barId=barId)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def filter_beers(max_price):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM sells WHERE price < :max_price;"
        )

        rs = con.execute(query, max_price=max_price)
        results = [dict(row) for row in rs]
        for r in results:
            r['price'] = float(r['price'])
        return results


def get_bar_menu(barId):
    print(barId)
    with engine.connect() as con:
        query = sql.text(
            'SELECT a.barId, a.itemId, a.price, b.manufacturer, b.itemName, coalesce(c.like_count, 0) as likes \
                FROM sells as a \
                JOIN items AS b \
                ON a.itemId = b.itemId \
                LEFT OUTER JOIN (SELECT itemId, count(*) as like_count FROM likes GROUP BY itemid) as c \
                ON a.itemId = c.itemid \
                WHERE a.barId = :barId; \
            ')
        rs = con.execute(query, barId=barId)
        results = [dict(row) for row in rs]
        for i, _ in enumerate(results):
            if (results[i]['manufacturer'] == ""):
                results[i]['manufacturer'] = "N/A"
            results[i]['price'] = float(results[i]['price'])
        print("finished succesfully")
        return results


def get_bars_selling(beer):
    with engine.connect() as con:
        query = sql.text('SELECT a.barid, a.price, b.customers \
                FROM sells AS a \
                JOIN (SELECT barid, count(*) AS customers FROM frequents GROUP BY barid) as b \
                ON a.barid = b.barid \
                WHERE a.itemid = :beer \
                ORDER BY a.price; \
            ')
        rs = con.execute(query, beer=beer)
        results = [dict(row) for row in rs]
        for i, _ in enumerate(results):
            results[i]['price'] = float(results[i]['price'])
        return results


def get_bar_frequent_counts():
    with engine.connect() as con:
        query = sql.text('SELECT barid, count(*) as frequentCount \
                FROM frequents \
                GROUP BY barid; \
            ')
        rs = con.execute(query)
        results = [dict(row) for row in rs]
        return results


def get_bar_cities():
    with engine.connect() as con:
        rs = con.execute('SELECT DISTINCT city FROM bars;')
        return [row['city'] for row in rs]


def get_beers():
    print("Doing this....")
    """Gets a list of beer names from the beers table."""

    with engine.connect() as con:
        rs = con.execute('SELECT itemName, manufacturer FROM items;')
        return [dict(row) for row in rs]


def get_beer_manufacturers(itemId):
    print("Getting manufacturers")
    with engine.connect() as con:
        if itemId is None:
            rs = con.execute('SELECT DISTINCT manufacturer FROM items;')
            print("returning succesfully")
            return [row['manufacturer'] for row in rs]

        query = sql.text('SELECT manufacturer FROM items WHERE itemId = :itemId;')
        rs = con.execute(query, itemId=itemId)
        result = rs.first()
        if result is None:
            print("Returning none")
            return None
        print("Succesful")
        return result['manufacturer']


def get_drinkers():
    with engine.connect() as con:
        rs = con.execute('SELECT name, city, phone, address FROM drinkers;')
        return [dict(row) for row in rs]


def get_likes(drinker_name):
    """Gets a list of beers liked by the drinker provided."""

    with engine.connect() as con:
        query = sql.text('SELECT itemId FROM likes WHERE drinkerId = :name;')
        rs = con.execute(query, name=drinker_name)
        return [row['item'] for row in rs]


def get_drinker_info(drinker_name):
    with engine.connect() as con:
        query = sql.text('SELECT * FROM drinkers WHERE name = :name;')
        rs = con.execute(query, name=drinker_name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)