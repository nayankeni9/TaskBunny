create table user(
    id int Primary Key NOT NULL AUTO_INCREMENT,
    firstname varchar(40) NOT NULL,
    lastname varchar(40) NOT NULL,
    email varchar(40) NOT NULL,
    password varchar(100) NOT NULL,
    contact_number int,
    street_address varchar(100),
    city varchar(30),
    state varchar(20),
    zip varchar(20),
    reward int,
    is_active boolean
);

create table tasker(
    id int primary key NOT NULL AUTO_INCREMENT,
    firstname varchar(40) NOT NULL,
    lastname varchar(40) NOT NULL,
    contact_number varchar(20) NOT NULL,
    email varchar(40) NOT NULL,
    password varchar(100) NOT NULL,
    street_address varchar(50),
    city varchar(20),
    state varchar(20),
    zip varchar(20),
    primary_skill varchar(20),
    tasker_age int,
    about_me varchar(1000),
    vehicle_owned boolean,
    reward int,
    is_active boolean
);