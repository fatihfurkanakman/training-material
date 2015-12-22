#!/usr/bin/env python

from datetime import datetime


def convert2date(date_str):
    '''convert a string representation 'yyyy-mm-dd' to a Python
       datetime object'''
    year, month, day = list(map(int, date_str.split('-')))
    return datetime(year, month, day)

if __name__ == '__main__':
    from argparse import ArgumentParser
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from experiments import Experiment, Researcher, Base
    arg_parser = ArgumentParser(description='create tables in database')
    arg_parser.add_argument('db_name', help='name of DB to create')
    arg_parser.add_argument('--first_name',
                            help='search for researcher by first name')
    arg_parser.add_argument('--started_after',
                            help='search experiments with a start date '
                                 'later than the given one')
    options = arg_parser.parse_args()

    engine = create_engine('sqlite:///{0}'.format(options.db_name))
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    db_session = DBSession()
    if options.first_name:
        researchers = db_session.query(Researcher).\
                                 filter_by(first_name=options.first_name).\
                                 all()
        for researcher in researchers:
            print(researcher)
    elif options.started_after:
        date_after = convert2date(options.started_after)
        experiments = db_session.query(Experiment).\
                         filter(Experiment.start_date > date_after).\
                         all()
        for experiment in experiments:
            print(experiment)
