create database Loteria;
use Loteria;

SHOW FULL COLUMNS from LotoFacil;

create table MeusJogos(
	codigo int(11) primary key auto_increment,
	tipoJogo int(11),
	numConcurso	int(4),
	codigoAposta varchar(25),
	diaAposta varchar(10),
    quantJogos int(11),
	quantNum int(2),
	surpresinha varchar(4),
	teimosinha varchar(4),
	utilizaTeimo int(2)
)engine=innodb;

create table MegaSena(
	codigo int(11) primary key auto_increment,
	codJogo	int(11),
    constraint foreign key (codJogo) references MeusJogos(codigo),
	Num1 int(11),
	Num2 int(11),
	Num3 int(11),
	Num4 int(11),
	Num5 int(11),
	Num6 int(11),
	Num7 int(11),
	Num8 int(11),
	Num9 int(11),
	Num10 int(11),
	Num11 int(11),
	Num12 int(11),
	Num13 int(11),
	Num14 int(11),
	Num15 int(11)
)engine=innodb;

create table LotoFacil(
	codigo int(11) primary key auto_increment,
	codJogo	int(11),
    constraint foreign key (codJogo) references MeusJogos(codigo),
	Num1 int(11),
	Num2 int(11),
	Num3 int(11),
	Num4 int(11),
	Num5 int(11),
	Num6 int(11),
	Num7 int(11),
	Num8 int(11),
	Num9 int(11),
	Num10 int(11),
	Num11 int(11),
	Num12 int(11),
	Num13 int(11),
	Num14 int(11),
	Num15 int(11),
	Num16 int(11),
	Num17 int(11),
	Num18 int(11),
    Num19 int(11),
    Num20 int(11)
)engine=innodb;

create table SorteiosOficialMegaSena(
	codigo int(11) primary key auto_increment,
    tipoJogo int(11),
    concurso int(11),
    dataSorteio varchar(10),
    Num1 int(11),
	Num2 int(11),
	Num3 int(11),
	Num4 int(11),
	Num5 int(11),
	Num6 int(11)
)engine=innodb;

create table SorteiosOficialLotoFacil(
	codigo int(11) primary key auto_increment,
    tipoJogo int(11),
    concurso int(11),
    dataSorteio varchar(10),
    Num1 int(11),
	Num2 int(11),
	Num3 int(11),
	Num4 int(11),
	Num5 int(11),
	Num6 int(11),
	Num7 int(11),
	Num8 int(11),
	Num9 int(11),
	Num10 int(11),
	Num11 int(11),
	Num12 int(11),
	Num13 int(11),
	Num14 int(11),
	Num15 int(11)
)engine=innodb;