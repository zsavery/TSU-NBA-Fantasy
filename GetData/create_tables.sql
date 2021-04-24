create user if not exists `admin`@`NBA` identified by 'tigers';
grant all privileges on *.* to `admin`@`NBA`;

create user if not exists `admin`@`localhost` identified by 'tigers';
grant all privileges on *.* to `admin`@`localhost`;

create user if not exists `admin`@`192.168.68.101` identified by 'tigers';
grant all privileges on *.* to `admin`@`192.168.68.101`;

flush privileges;



create database if not exists player_stats;
create table if not exists `player_stats`.`average_stats`(
	`playerId` varchar(10) unique not null,
	`firstName` varchar(30),
    `lastName` varchar(30),
    `teamId` varchar(10),
    `pos` varchar(10),
    `points` decimal(4, 2),
    `totReb` decimal(4, 2),
    `assists` decimal(4, 2),
    `steals` decimal(4, 2),
    `blocks` decimal(4, 2),
    `turnovers` dec(4, 2),
    `fantasyPoints` decimal(4, 2),
    primary key(`playerId`)
);

-- show global variables like 'local_infile';
-- set global local_infile=1;

-- LOAD DATA LOCAL INFILE "/average_stats.csv" 
-- INTO TABLE tsu_nba.average_stats
-- FIELDS TERMINATED BY ','
-- LINES TERMINATED BY '\n'
-- IGNORE 1 rows;
-- (playerId, firstName, lastName, teamId, pos, points, totReb, assists, steals, blocks, turnovers, fantasyPoints);
drop table `player_stats`.`average_stats`;
