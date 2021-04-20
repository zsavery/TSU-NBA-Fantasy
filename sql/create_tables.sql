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

#drop table `player_stats`.`average_stats`;