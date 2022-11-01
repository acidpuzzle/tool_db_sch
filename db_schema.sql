/*
 *
 *
 */


-- SCHOOLS
CREATE TABLE "school"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "short_name" VARCHAR(255) NULL,
    "full_name" VARCHAR(255) NULL,
    "address" VARCHAR(255) NULL,
    "district_id" INTEGER NOT NULL,
    "wlc_id" INTEGER NULL,
    "prime_id" INTEGER NULL,
    "project_id" INTEGER NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "active" BOOLEAN NULL
);
ALTER TABLE
    "school" ADD PRIMARY KEY("id");
ALTER TABLE
    "school" ADD CONSTRAINT "school_name_unique" UNIQUE("name");

-- ROUTERS
CREATE TABLE "router"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "sn" VARCHAR(255) NOT NULL,
    "ip" INET NOT NULL,
    "model_id" INTEGER NULL,
    "os_version" VARCHAR(255) NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "available" TIMESTAMP NULL
);
ALTER TABLE
    "router" ADD PRIMARY KEY("id");
ALTER TABLE
    "router" ADD CONSTRAINT "router_name_sn_ip_unique" UNIQUE("name","sn", "ip");

-- VENDORS
CREATE TABLE "vendor"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL
);
ALTER TABLE
    "vendor" ADD PRIMARY KEY("id");
ALTER TABLE
    "vendor" ADD CONSTRAINT "vendor_name_unique" UNIQUE("name");

-- SWITCHES
CREATE TABLE "switch"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "sn" VARCHAR(255) NOT NULL,
    "ip" INET NOT NULL,
    "mac" MACADDR NULL,
    "model_id" INTEGER NULL,
    "os_version" VARCHAR(255) NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "available" TIMESTAMP NULL
);
ALTER TABLE
    "switch" ADD PRIMARY KEY("id");
ALTER TABLE
    "switch" ADD CONSTRAINT "switch_name_unique" UNIQUE("name");
ALTER TABLE
    "switch" ADD CONSTRAINT "switch_sn_unique" UNIQUE("sn");
ALTER TABLE
    "switch" ADD CONSTRAINT "switch_ip_unique" UNIQUE("ip");

-- DEVICE MODEL
CREATE TABLE "model"(
    "id" SERIAL NOT NULL,
    "vendor_id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "credentials_id" INTEGER NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL
);
ALTER TABLE
    "model" ADD PRIMARY KEY("id");
ALTER TABLE
    "model" ADD CONSTRAINT "model_name_unique" UNIQUE("name");

-- DISTRICT AND DOMAIN
CREATE TABLE "district"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "name_en" VARCHAR(255) NOT NULL,
    "full_name" VARCHAR(255) NOT NULL,
    "fqdn" VARCHAR(255) NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL
);
ALTER TABLE
    "district" ADD PRIMARY KEY("id");
ALTER TABLE
    "district" ADD CONSTRAINT "district_name_unique" UNIQUE("name");
ALTER TABLE
    "district" ADD CONSTRAINT "district_name_en_unique" UNIQUE("name_en");
ALTER TABLE
    "district" ADD CONSTRAINT "district_full_name_unique" UNIQUE("full_name");

-- KMS NETWORKS
CREATE TABLE "kms_net"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "network" CIDR NOT NULL,
    "vlan30" CIDR NULL,
    "vlan60" CIDR NULL,
    "vlan70" CIDR NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    UNIQUE ("school_id", "network")
);
ALTER TABLE
    "kms_net" ADD PRIMARY KEY("id");
ALTER TABLE
    "kms_net" ADD CONSTRAINT "kms_net_school_id_network_unique" UNIQUE("school_id", "network");

-- MES USERS NETWORK
CREATE TABLE "users_net"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "network" CIDR NOT NULL,
    "vlan40" CIDR NULL,
    "vlan50" CIDR NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    UNIQUE ("school_id", "network")
);
ALTER TABLE
    "users_net" ADD CONSTRAINT "users_net_school_id_network_unique" UNIQUE("school_id", "network");
ALTER TABLE
    "users_net" ADD PRIMARY KEY("id");

-- RT NETWORK
CREATE TABLE "rt_net"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "network" CIDR NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    UNIQUE ("school_id", "network")
);
ALTER TABLE
    "rt_net" ADD PRIMARY KEY("id");
ALTER TABLE
    "rt_net" ADD CONSTRAINT "rt_net_school_id_network_unique" UNIQUE("school_id", "network");

-- MGTS NETWORK
CREATE TABLE "mgts_net"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "network" CIDR NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    UNIQUE ("school_id", "network")
);
ALTER TABLE
    "mgts_net" ADD PRIMARY KEY("id");
ALTER TABLE
    "mgts_net" ADD CONSTRAINT "mgts_school_id_network_unique" UNIQUE("school_id", "network");

-- WIRELESS LAN CONTROLLER
CREATE TABLE "wlc"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "ip" INET NOT NULL,
    "option_43" VARCHAR(255) NOT NULL,
    "mgmt_ip" INET NOT NULL,
    "os_version" VARCHAR(255) NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "available" TIMESTAMP NULL
);
ALTER TABLE
    "wlc" ADD PRIMARY KEY("id");
ALTER TABLE
    "wlc" ADD CONSTRAINT "wlc_name_unique" UNIQUE("name");
ALTER TABLE
    "wlc" ADD CONSTRAINT "wlc_ip_unique" UNIQUE("ip");
ALTER TABLE
    "wlc" ADD CONSTRAINT "wlc_option_43_unique" UNIQUE("option_43");
ALTER TABLE
    "wlc" ADD CONSTRAINT "wlc_mgmt_ip_unique" UNIQUE("mgmt_ip");

-- CISCO PRIME CONTROLLER
CREATE TABLE "prime"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "ip" INET NOT NULL,
    "stack_master_id" INTEGER NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "available" TIMESTAMP NULL
);
ALTER TABLE
    "prime" ADD PRIMARY KEY("id");
ALTER TABLE
    "prime" ADD CONSTRAINT "prime_name_unique" UNIQUE("name");
ALTER TABLE
    "prime" ADD CONSTRAINT "prime_ip_unique" UNIQUE("ip");

-- ACCESS POINTS
CREATE TABLE "ap"(
    "id" SERIAL NOT NULL,
    "mac" MACADDR NOT NULL,
    "sn" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "ip" INET NULL,
    "school_id" INTEGER NOT NULL,
    "model_id" INTEGER NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    "available" TIMESTAMP NULL
);
ALTER TABLE
    "ap" ADD PRIMARY KEY("id");
ALTER TABLE
    "ap" ADD CONSTRAINT "ap_mac_unique" UNIQUE("mac");
ALTER TABLE
    "ap" ADD CONSTRAINT "ap_sn_unique" UNIQUE("sn");

-- PROJECT NAME
CREATE TABLE "project"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL
);
ALTER TABLE
    "project" ADD PRIMARY KEY("id");
ALTER TABLE
    "project" ADD CONSTRAINT "project_name_unique" UNIQUE("name");

-- SCHOOL, NOT MES, NETWORKS
CREATE TABLE "sch_net"(
    "id" SERIAL NOT NULL,
    "school_id" INTEGER NOT NULL,
    "network" INET NOT NULL,
    "description" VARCHAR(255) NULL,
    "kms" BOOLEAN DEFAULT FALSE NOT NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL,
    UNIQUE ("school_id", "network")
);
ALTER TABLE
    "sch_net" ADD CONSTRAINT "sch_net_school_id_network_unique" UNIQUE("school_id", "network");
ALTER TABLE
    "sch_net" ADD PRIMARY KEY("id");

-- PARAMS FOR REMOTE CONNECTION
CREATE TABLE "credentials"(
    "id" SERIAL NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "enable_pass" VARCHAR(255) NULL,
    "netmiko_device" VARCHAR(255) NULL,
    "scrapli_driver" VARCHAR(255) NULL,
    "scrapli_transport" VARCHAR(255) NULL,
    "created" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "updated" TIMESTAMP NULL
);
ALTER TABLE
    "credentials" ADD PRIMARY KEY("id");

-- TABLE RELATIONSHIPS
ALTER TABLE
    "switch" ADD CONSTRAINT "switch_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "school" ADD CONSTRAINT "school_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "district"("id");
ALTER TABLE
    "school" ADD CONSTRAINT "school_prime_id_foreign" FOREIGN KEY("prime_id") REFERENCES "prime"("id");
ALTER TABLE
    "school" ADD CONSTRAINT "school_project_id_foreign" FOREIGN KEY("project_id") REFERENCES "project"("id");
ALTER TABLE
    "router" ADD CONSTRAINT "router_model_id_foreign" FOREIGN KEY("model_id") REFERENCES "model"("id");
ALTER TABLE
    "router" ADD CONSTRAINT "router_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "model" ADD CONSTRAINT "model_vendor_id_foreign" FOREIGN KEY("vendor_id") REFERENCES "vendor"("id");
ALTER TABLE
    "model" ADD CONSTRAINT "model_credentials_id_foreign" FOREIGN KEY("credentials_id") REFERENCES "credentials"("id");
ALTER TABLE
    "switch" ADD CONSTRAINT "switch_model_id_foreign" FOREIGN KEY("model_id") REFERENCES "model"("id");
ALTER TABLE
    "kms_net" ADD CONSTRAINT "kms_net_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "users_net" ADD CONSTRAINT "users_net_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "rt_net" ADD CONSTRAINT "rt_net_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "mgts_net" ADD CONSTRAINT "mgts_net_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "school" ADD CONSTRAINT "school_wlc_id_foreign" FOREIGN KEY("wlc_id") REFERENCES "wlc"("id");
ALTER TABLE
    "prime" ADD CONSTRAINT "prime_stack_master_id_foreign" FOREIGN KEY("stack_master_id") REFERENCES "prime"("id");
ALTER TABLE
    "ap" ADD CONSTRAINT "ap_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");
ALTER TABLE
    "ap" ADD CONSTRAINT "ap_model_id_foreign" FOREIGN KEY("model_id") REFERENCES "model"("id");
ALTER TABLE
    "sch_net" ADD CONSTRAINT "sch_net_school_id_foreign" FOREIGN KEY("school_id") REFERENCES "school"("id");

-- UPDATE TRIGGER
create function trigger_set_timestamp() returns trigger
    language plpgsql
as
$$
BEGIN

  NEW.updated = NOW();

  RETURN NEW;

END;

$$;
alter function trigger_set_timestamp() owner to sch_db_admin;

-- UPDATE TRIGGER TO TABLE
create trigger set_timestamp
    before update
    of id, name, short_name, full_name, address, district_id, wlc_id, prime_id, project_id
    on school
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, school_id, name, sn, ip, model_id, os_version
    on router
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on vendor
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, school_id, name, sn, ip, mac, model_id, os_version
    on switch
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on model
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on district
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on kms_net
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on users_net
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on rt_net
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on mgts_net
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, name, ip, option_43, mgmt_ip, os_version
    on wlc
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, mac, sn, name, ip, school_id, model_id
    on ap
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, name, ip, stack_master_id
    on prime
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on project
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    on sch_net
    for each row
execute procedure trigger_set_timestamp();

create trigger set_timestamp
    before update
    of id, username, password, enable_pass, netmiko_device, scrapli_driver, scrapli_transport
    on credentials
    for each row
execute procedure trigger_set_timestamp();


-- USER sch_db_admin database admin
ALTER DATABASE sch_db owner to sch_db_admin ;
