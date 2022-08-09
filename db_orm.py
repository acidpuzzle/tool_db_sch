# -*- coding: utf-8 -*-
import os
import logging

from datetime import datetime
from ipaddress import ip_network, ip_address

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import INET, CIDR, MACADDR
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, UniqueConstraint


logger = logging.getLogger(__name__)


db_url = os.environ.get("NEW_SCHOOL_DATABASE")
db_engine = create_engine(db_url)
database = declarative_base(db_engine)


class School(database):
    """
    School table map
    """
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)             # VARCHAR(255) NOT NULL,
    short_name = Column(String(255))                                    # VARCHAR(255) NULL
    full_name = Column(String(255))                                     # VARCHAR(255) NULL
    address = Column(String(255))                                       # VARCHAR(255) NULL,
    district_id = Column(Integer, ForeignKey('district.id'))            # INTEGER NULL,
    wlc_id = Column(Integer, ForeignKey('wlc.id'))                      # INTEGER NULL,
    prime_id = Column(Integer, ForeignKey('prime.id'))                  # INTEGER NOT NULL,
    project_id = Column(Integer, ForeignKey('project.id'))              # INTEGER NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(School, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"School(name='{self.name}', address='{self.address}')"

    district = relationship("District", back_populates="school")
    wlc = relationship("WLC", back_populates="schools", uselist=False)
    router = relationship("Router",  back_populates="school")
    switches = relationship("Switch", back_populates="school")
    prime = relationship("Prime", back_populates="schools", uselist=False)
    ap = relationship("AP", back_populates="school")
    project = relationship("Project", back_populates="schools", uselist=False)

    kms_net = relationship("KMSNet", back_populates="school", uselist=False)
    users_net = relationship("UsersNet", back_populates="school", uselist=False)
    rt_net = relationship("RTNet", back_populates="school", uselist=False)
    mgts_net = relationship("MGTSNet", back_populates="school", uselist=False)
    sch_net = relationship("SchNet", back_populates="school")


class Router(database):
    """
    Routers table map
    """
    __tablename__ = 'router'
    id = Column(Integer, primary_key=True)                               # SERIAL NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    name = Column(String(255), unique=True, nullable=False)              # VARCHAR(255) NULL,
    sn = Column(String(255), unique=True, nullable=False)                # VARCHAR(255) NULL,
    ip = Column(INET, unique=True, nullable=False)                       # INET NOT NULL,
    model_id = Column(Integer, ForeignKey('model.id'))                   # INTEGER NULL,
    os_version = Column(String(255))                                     # VARCHAR(255) NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)   # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                           # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Router, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Router(name='{self.name}', ip='{self.ip}')"

    school = relationship("School", back_populates="router")
    model = relationship("Model", back_populates="router")


class Vendor(database):
    """
    Device Vedors table map
    """
    __tablename__ = 'vendor'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)             # VARCHAR(255) NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Vendor, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Vendor(name='{self.name}')"

    model = relationship("Model", back_populates="vendor")


class Switch(database):
    """
    Switches table map
    """
    __tablename__ = 'switch'
    id = Column(Integer, primary_key=True)                               # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)              # VARCHAR(255) NULL,
    sn = Column(String(255), unique=True, nullable=False)                # VARCHAR(255) NULL,
    ip = Column(INET, unique=True, nullable=False)                       # INET NOT NULL,
    mac = Column(MACADDR)                                                # MACADDR NULL,
    model_id = Column(Integer, ForeignKey('model.id'))                   # INTEGER NULL,
    os_version = Column(String(255))                                     # VARCHAR(255) NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)   # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                           # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Switch, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Switch(name='{self.name}', ip='{self.ip}')"

    school = relationship("School", back_populates="switches")
    model = relationship("Model", back_populates="switch")


class Model(database):
    """
    Device model table map
    """
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)                                # SERIAL NOT NULL,
    vendor_id = Column(Integer, ForeignKey('vendor.id'), nullable=False)  # INTEGER NOT NULL,
    name = Column(String(255), unique=True, nullable=False)               # VARCHAR(255) NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)    # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    updated = Column(DateTime)                                            # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Model(name='{self.name}')"

    vendor = relationship("Vendor", back_populates="model")
    router = relationship("Router", back_populates="model")
    switch = relationship("Switch", back_populates="model")
    ap = relationship("AP", back_populates="model")


class District(database):
    """
    District table map
    """
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)             # VARCHAR(255) NOT NULL,
    name_en = Column(String(255), unique=True, nullable=False)          # VARCHAR(255) NOT NULL,
    full_name = Column(String(255), unique=True, nullable=False)        # VARCHAR(255) NULL,
    fqdn = Column(String(255))                                          # VARCHAR(255) NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(District, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"District(name='{self.name}')"

    school = relationship("School", back_populates="district")


class KMSNet(database):
    """
    KMS Networl table map
    """
    __tablename__ = 'kms_net'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    network = Column(CIDR, unique=True, nullable=False)                 # CIDR NOT NULL,
    vlan30 = Column(CIDR)                                               # CIDR NULL,
    vlan60 = Column(CIDR)                                               # CIDR NULL,
    vlan70 = Column(CIDR)                                               # CIDR NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(KMSNet, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"KMSNet(network='{self.network}')"

    school = relationship("School", back_populates="kms_net")


class UsersNet(database):
    """
    Inner school networl table map
    """
    __tablename__ = 'users_net'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    network = Column(CIDR, nullable=False)                              # CIDR NOT NULL,
    vlan40 = Column(CIDR)                                               # CIDR NULL,
    vlan50 = Column(CIDR)                                               # CIDR NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(UsersNet, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"UsersNet(network='{self.network}')"

    school = relationship("School", back_populates="users_net")


class RTNet(database):
    """
    RT Networl tablr map
    """
    __tablename__ = 'rt_net'
    id = Column(Integer, primary_key=True)                                # SERIAL NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    network = Column(CIDR, unique=True, nullable=False)                   # CIDR NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)    # timestamp default now() NOT NULL,
    updated = Column(DateTime)                                            # timestamp NULL

    def __init__(self, *args, **kwargs):
        super(RTNet, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"RTNet(network='{self.network}')"

    school = relationship("School", back_populates="rt_net")


class MGTSNet(database):
    """
    MGTS table network
    """
    __tablename__ = 'mgts_net'
    id = Column(Integer, primary_key=True)                                # SERIAL NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    network = Column(CIDR, unique=True, nullable=False)                   # CIDR NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)    # timestamp default now() NOT NULL,
    updated = Column(DateTime)                                            # timestamp NULL

    def __init__(self, *args, **kwargs):
        super(MGTSNet, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"MGTSNet(network='{self.network}')"

    school = relationship("School", back_populates="mgts_net")


class WLC(database):
    """
    WLC table map
    """
    __tablename__ = 'wlc'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)             # VARCHAR(255) NOT NULL,
    ip = Column(INET, unique=True, nullable=False)                      # INET NOT NULL,
    option_43 = Column(String(255), unique=True, nullable=False)        # VARCHAR(255) NOT NULL,
    mgmt_ip = Column(INET, unique=True, nullable=False)                 # INET NOT NULL,
    os_version = Column(String(60))                                     # VARCHAR(255) NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(WLC, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"WLC(name='{self.name}', ip='{self.ip}')"

    schools = relationship("School", back_populates="wlc")


class Prime(database):
    """
    Prime controller table map
    """
    __tablename__ = 'prime'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    name = Column(String(255), unique=True, nullable=False)             # VARCHAR(255) NOT NULL,
    ip = Column(INET, unique=True, nullable=False)                      # INET NOT NULL,
    stack_master_id = Column(Integer, ForeignKey('prime.id'))           # INTEGER NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Prime, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Prime(name='{self.name}', ip='{self.ip}')"

    schools = relationship("School", back_populates="prime")
    stack_master = relationship("Prime")


class AP(database):
    """
    Access Point table map
    """
    __tablename__ = 'ap'
    id = Column(Integer, primary_key=True)                              # SERIAL NOT NULL,
    mac = Column(MACADDR, unique=True, nullable=False)                  # MACADDR NOT NULL,
    sn = Column(String(255), unique=True, nullable=False)               # VARCHAR(255) NOT NULL,
    name = Column(String(255), nullable=False)                          # VARCHAR(255) NOT NULL,
    ip = Column(INET)                                                   # INET NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'))                # INTEGER NOT NULL,
    model_id = Column(Integer, ForeignKey('model.id'))                  # INTEGER NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                          # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(AP, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"AP(name='{self.name}', mac='{self.mac}')"

    school = relationship("School", back_populates="ap")
    model = relationship("Model", back_populates="ap")


class Project(database):
    """
    Project year table map
    """
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)                               # INTEGER NOT NULL,
    name = Column(String(255), unique=True, nullable=False)              # CHAR(255) NOT NULL,
    created = Column(DateTime, default=datetime.now(), nullable=False)   # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                           # TIMESTAMP NULL

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"Project(name='{self.name}')"

    schools = relationship("School", back_populates="project")


class SchNet(database):
    """
    Project year table map
    """
    __tablename__ = 'sch_net'
    id = Column(Integer, primary_key=True)                               # INTEGER NOT NULL,
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)  # INTEGER NOT NULL,
    network = Column(INET, nullable=False)                               # INET NOT NULL,
    description = Column(String(255))                                    # VARCHAR(255) NULL,
    kms = Column(Boolean, default=False)                                 # BOOLEAN DEFAULT FALSE NOT NULL,
    created = Column(DateTime, default=datetime.now())                   # TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated = Column(DateTime)                                           # TIMESTAMP NULL

    UniqueConstraint("school_id", "network", name="sch_net_school_id_network_unique")

    def __init__(self, *args, **kwargs):
        super(SchNet, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"SchNet(network='{self.network}')"

    school = relationship("School", back_populates="sch_net")


db_session = Session(bind=db_engine)


def create(entity, session=db_session, commit=False, **kwargs):
    """
    Creates a new object of the specified type, with the specified parameters
    :param entity: SQLAlchemy ORM object
    :param session: SQLAlchemy sesion to database 'sqlalchemy.orm.session.Session'
    :param commit: Write to database if True, else need commit() outside.
    :return: Newly created object
    """
    logger.debug(f"Trying create new object {entity}, with parametrs {kwargs}")
    try:
        new_entity = entity(**kwargs)
        session.add(new_entity)
        if commit:
            session.commit()
        logger.debug(f"Successful create new object {entity}, with parametrs {kwargs}")
        return new_entity
    except SQLAlchemyError as error:
        logger.error(error)


def exist(entity, session=db_session, **kwargs):
    """
    Searches for already existing objects with the given parameters
    :param entity: SQLAlchemy ORM object
    :param session: SQLAlchemy sesion to database 'sqlalchemy.orm.session.Session'
    :return: existing object or None
    """
    logger.debug(f"Check for exist {entity=}, {kwargs=}")
    exist_entity = session.query(entity).filter_by(**kwargs).first()
    if exist_entity:
        logger.debug(f"Already exists {entity}(id={exist_entity.id}, "
                     f"params={exist_entity.__dict__})")
        return exist_entity
    else:
        logger.debug(f"{entity}({kwargs}) not exist.")


def exist_or_create(entity, session=db_session, commit=False, **kwargs):
    """
    :param entity: SQLAlchemy ORM object
    :param session: SQLAlchemy sesion to database 'sqlalchemy.orm.session.Session'
    :param commit: Write to database if True, else need commit() outside.
    :return: Newly or existing object
    """
    exist_entity = exist(entity, session, **kwargs)
    if exist_entity:
        return exist_entity
    else:
        new_entity = create(entity, session, commit, **kwargs)
        return new_entity


def update(entity, session=db_session, commit=False, **kwargs):
    """
    Updates the attributes of an existing object
    :param entity: SQLAlchemy ORM object
    :param session: SQLAlchemy sesion to database 'sqlalchemy.orm.session.Session'
    :param commit: Write to database if True, else need commit() outside.
    :return: Updated object
    """
    for attr, value in kwargs.items():
        try:
            logger.debug(f"Update: {entity=}, {attr=}, {value=}")
            setattr(entity, attr, value)
        except AttributeError as error:
            logger.error(f"Error update {attr=}, {value=}, {error=}")
    if commit:
        session.commit()
    return entity


def isnet(network: str) -> str:
    """
    Checking if the network prefix is correct
    :param network: Network "10.10.10.8/30"
    :return: if network correct, return network, else None
    """
    try:
        net = str(ip_network(network.strip(), strict=False)) if network else None
        if net:
            logger.debug(f"Correct prefix: {net}")
            return net
        else:
            logger.error(f"Incorrect prefix: {net}")
    except ValueError as error:
        logger.error(error)


def isip(ipaddr: str) -> str:
    """
    Checking if the ip address is correct
    :param ipaddr: ip address in textual representation, for example "192.168.1.1"
    :return: if ip address correct, return ip address, else None
    """
    try:
        ip = str(ip_address(ipaddr.strip())) if ipaddr else None
        if ip:
            logger.debug(f"Correct ip address: {ip}")
            return ip
        else:
            logger.error(f"Incorrect ip address: {ip}")
    except ValueError as error:
        logger.error(error)


if __name__ == "__main__":
    pass
