#!/usr/bin/env python

if __name__ == '__main__':
    from argparse import ArgumentParser
    from datetime import datetime
    import random

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from create_sqlalchemy_db import City, Measurement, Base

    arg_parser = ArgumentParser(description='create tables in database')
    arg_parser.add_argument('db_name', help='name of DB to create')
    options = arg_parser.parse_args()

    engine = create_engine('sqlite:///{0}'.format(options.db_name))
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    db_session = DBSession()
    city_names = ['New York', 'London', 'Paris']
    city_map = {}
    for city_name in city_names:
        city = City(name=city_name)
        city_map[city_name] = city
        db_session.add(city)
    db_session.commit()
    year = 2015
    month = 1
    hour = 10
    minutes = 0
    for day in xrange(1, 16):
        date = datetime(year, month, day, hour, minutes)
        for city in city_map.itervalues():
            temperature = random.uniform(0.0, 30.0)
            measurement = Measurement(time=date, temperature=temperature,
                                      city=city)
            db_session.add(measurement)
    db_session.commit()