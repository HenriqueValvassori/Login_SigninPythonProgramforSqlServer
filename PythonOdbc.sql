create database Odbc;
use Odbc;

create table Cadastro(
id int primary key identity(1,1),
Usuario varchar(50) null,
Email varchar(250) null,
Password varchar(72));
insert into Cadastro(Usuario,Email,Password) values ('Henrique','@henrqie.com.br','Her123');
select * from Cadastro;


