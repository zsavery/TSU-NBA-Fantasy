create user if not exists `tsu_admin`@`NBA` identified by 'tigers';
grant all privileges on *.* to `tsu_admin`@`NBA`;

create user if not exists `tsu_admin`@`localhost` identified by 'tigers';
grant all privileges on *.* to `tsu_admin`@`localhost`;
flush privileges;

create database if not exists player_stats;
create table if not exists `player_stats`.`average_stats`(
	`playerId` varchar(10) unique not null,
	`firstName` varchar(30) not null,
    `lastName` varchar(30) not null,
    `teamId` varchar(10),
    `pos` varchar(10),
    `points` dec,
    `totReb` dec,
    `assists` dec,
    `steals` dec,
    `blocks` dec,
    `turnovers` dec,
    `fantasyPoints` dec,
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