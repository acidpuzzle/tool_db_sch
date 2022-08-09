# -*- coding: utf-8 -*-
import os

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey


"""
Database URLs
dialect+driver://username:password@host:port/database
psycopg2 example: 'postgresql+psycopg2://scott:qwerty@localhost/mydatabase'
do not store the login with the password in textual form in the script or on github, get them from the OS environment.
"""
old_db_url = os.environ.get("OLD_SCHOOL_DATABASE")

old_db_engine = create_engine(old_db_url)
old_base = declarative_base(old_db_engine)


class OldSchool(old_base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    district = Column(String)
    address = Column(String)
    school = Column(String, unique=True, nullable=False)
    mgts = Column(String)
    rt = Column(String)
    net_pak = Column(String)
    net_inner = Column(String)
    vwlc = Column(String)
    old_mgts = Column(String)
    prime = Column(String)
    dszn = Column(String)
    project = Column(String)
    sw_count = Column(Integer)
    ap_count = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    former_id = Column(Integer, default=0)
    sch_sw_count = Column(Integer)
    edu_dc_id = Column(Integer)
    pnr = Column(DateTime)
    finish = Column(DateTime)
    parent_id = Column(Integer)
    crt_generated = Column(Boolean)
    school_full_name = Column(String)
    school_building_full_address = Column(String)
    ekis = Column(String)
    panels_count = Column(Integer)
    unique_address_id = Column(Integer)
    zbf = Column(Boolean, default=False)
    sch_all_pak_nets = Column(String)

    def __init__(self, *args, **kwargs):
        super(OldSchool, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<School: {}, address: {}>'.format(self.name, self.address)

    router = relationship("OldRouter",  backref='schools', uselist=False)


class OldRouter(old_base):
    __tablename__ = 'router'
    serial = Column(String, nullable=False)
    school = Column(String)
    model = Column(String)
    name = Column(String)
    location = Column(String)
    ip = Column(String)
    os = Column(String)
    z_hostid = Column(String)
    vendor = Column(String)
    type = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('schools.id'))

    def __init__(self, *args, **kwargs):
        super(OldRouter, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<Router: {}, name: {}, ip: {}>'.format(self.model, self.name, self.ip)

    # schools = relationship("OldSchool", backref='router', uselist=False)


class OldSwitch(old_base):
    __tablename__ = 'switch'
    serial = Column(String, nullable=False)
    school = Column(String)
    model = Column(String)
    name = Column(String)
    location = Column(String)
    ip = Column(String)
    os = Column(String)
    z_hostid = Column(String)
    type = Column(String)
    vendor = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    school_id = Column(String)
    crt_generated = Column(Boolean)

    def __init__(self, *args, **kwargs):
        super(OldSwitch, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<Switch: {}, ip: {}>'.format(self.name, self.ip)


class OldWLC(old_base):
    __tablename__ = 'wlc'
    name = Column(String, primary_key=True)
    wlc_ip = Column(String)
    wlc_option = Column(String)
    radius_primary = Column(Integer)
    radius_secondary = Column(Integer)

    def __init__(self, *args, **kwargs):
        super(OldWLC, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<WLC: {}, ip: {}>'.format(self.name, self.wlc_ip)


class OldDidtrict(old_base):
    __tablename__ = 'domains'
    district = Column(String, unique=True)
    domain = Column(String, primary_key=True)
    shortname = Column(String)

    def __init__(self, *args, **kwargs):
        super(OldDidtrict, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<OldDidtrict: {}, ip: {}>'.format(self.name, self.domain)


class OldPrime(old_base):
    __tablename__ = 'prime'
    name = Column(String)
    ip = Column(String)
    id = Column(Integer, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(OldPrime, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<OldPrime: {}, ip: {}>'.format(self.name, self.ip)


old_db_session = Session(bind=old_db_engine)

if __name__ == "__main__":
    pass
