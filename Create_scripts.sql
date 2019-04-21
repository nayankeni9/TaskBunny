create table user(
    id int Primary Key NOT NULL AUTO_INCREMENT,
    firstname varchar(40) NOT NULL,
    lastname varchar(40) NOT NULL,
    email varchar(40) NOT NULL,
    password varchar(100) NOT NULL,
    contact_number varchar(20),
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
    is_active boolean,
    service_rate int default 10
);

CREATE TABLE jsckp5HTKU.Service(
    Service_Id int NOT NULL,
    Service_Name Varchar(20) NOT NULL,
    CONSTRAINT PRIMARY KEY (Service_Id)
    );
CREATE TABLE jsckp5HTKU.Sub_Service(
    Service_Id int NOT NULL,
    Sub_Service_Name Varchar(20) NOT NULL,
    CONSTRAINT FOREIGN KEY (Service_Id) REFERENCES Service(Service_Id)
    );
    
CREATE TABLE  jsckp5HTKU.Order(
    Order_Id int NOT NULL AUTO_INCREMENT,
    User_Id int NOT NULL,
    Service_Id int NOT NULL,
    Order_Date DATE NOT NULL,
    Service_Type Varchar(10) NOT NULL,
    Service_Description Varchar(100) NOT NULL,
    Service_Date DATE NOT NULL,
    Service_Time Varchar(10) NOT NULL,
    CONSTRAINT PRIMARY KEY (Order_Id),
    CONSTRAINT FOREIGN KEY (User_Id) REFERENCES user(id),
    CONSTRAINT FOREIGN KEY (Service_Id) REFERENCES Service(Service_Id)
);

CREATE TABLE  jsckp5HTKU.Task_Assignment(
    Tasker_Id int NOT NULL,
    Order_Id int NOT NULL,
    Task_Status Varchar(10) NOT NULL,
    CONSTRAINT PRIMARY KEY (Tasker_ID,Order_Id),
    CONSTRAINT FOREIGN KEY (Tasker_Id) REFERENCES tasker(id),
    CONSTRAINT FOREIGN KEY (Order_ID) REFERENCES Order(Order_Id)
);

INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Plumbing');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Carpentry');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Painting');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Bathroom Cleaning');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Carpet Cleaning');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Home Deep Cleaning');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Pest Control');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Yard Work');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (1,'Furniture Assembly');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Pet Sitting');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Vacation Visits');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Overnight Stay');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Poop Scooping');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Pet Grooming');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (2,'Pet Training');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'Light Installation');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'General Electrician');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'AC Service & Repair');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'Washing Machine Repair');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'Refrigerator Repair');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'Microwave Repair');

INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (3,'Mobile Repair');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Salon at Home');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Massage');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Makeup & Hairstyling');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Haircut & Grooming');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Home Tutor');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Lawyer');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Event Photographer');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Packers & Movers');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (4,'Income Tax filing');	
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Event Decoration');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Event Staffing');

INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Party Planning');

INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Entertainer');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Bartending');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Event Help & Wait Staff');
INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Shop & Install Decoration');

INSERT INTO `Sub_Service`(`Service_Id`, `Sub_Service_Name`) VALUES (5,'Cooking & Food Service');