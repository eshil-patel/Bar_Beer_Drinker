from sqlalchemy import create_engine
from sqlalchemy import sql
from sqlalchemy import sql 
from BarBeerDrinker import config

engine=create_engine(config.database_uri)


def get_bars():
        with engine.connect() as con:    
                rs=con.execute("SELECT barName, license, city, phone, address FROM bars;")
                #rs=con.execute("SELECT name, license, city, phone, addr FROM bars")
                return [dict(row) for row in rs]

        
def find_bar(name):
    with engine.connect() as con:
        query = sql.text("SELECT barName,license, city, phone,address FROM bars WHERE barName= :name;")
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)
def filter_beers(max_price):
    with engine.connect() as con:
        query = sql.text( "SELECT * FROM sells WHERE price < :max_price;")
        rs = con.execute(query, max_price=max_price)
        results = [dict(row) for row in rs]
        for r in results:
            r['price'] = float(r['price'])
        return results







