-- needs to be run as root user to make accounts and give privileges
create user if not exists `admin`@`NBA` identified by 'tigers';
grant all privileges on *.* to `admin`@`NBA`;

create user if not exists `admin`@`localhost` identified by 'tigers';
grant all privileges on *.* to `admin`@`localhost`;
-- i believe this allows for a remote connection
create user if not exists `admin`@`192.168.68.101` identified by 'tigers';
grant all privileges on *.* to `admin`@`192.168.68.101`;

flush privileges;

-- what our table looks like
# create database if not exists player_stats;
# create table if not exists `player_stats`.`average_stats`(
# 	`playerId` decimal(4, 2) unique not null,
# 	`firstName` varchar(30),
#     `lastName` varchar(30),
#     `teamId` decimal(4, 2),
#     `pos` varchar(10),
#     `points` decimal(4, 2),
#     `totReb` decimal(4, 2),
#     `assists` decimal(4, 2),
#     `steals` decimal(4, 2),
#     `blocks` decimal(4, 2),
#     `turnovers` dec(4, 2),
#     `fantasyPoints` decimal(4, 2),
#     primary key(`playerId`)
# );

