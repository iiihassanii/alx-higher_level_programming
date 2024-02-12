SHOW databases
CREATE DATABASE IF NOT EXISTS `hbtn_0c_0`
DROP DATABASE IF EXISTS `hbtn_0c_0`;
SHOW TABLES
CREATE TABLE IF NOT EXISTS `first_table` ( `id` INT, `name` VARCHAR(256));
SHOW CREATE TABLE `first_table`;
SELECT * FROM `first_table`;
INSETR INTO `first_table` (`id` , `name`) VALUES  (1, 'hassan');
SELECT COUNT(*) `fist_table` WHERE `id` = 89;
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT , `name` VARCHAR(256), `score` INT );
INSETR INTO `second_table` (`id`, `name`, `score`) VALUES
(1, 'afs', 10),
(2, ',sdajkd', 120),
(3, 'dsadafs', 14),
(4, 'hassan', 302);
SELECT `score`, `name` FROM `second_table` ORDER BY `score` DESC;
SELECT `score`, `name` FROM `second_table` ORDER BY `score` DESC;
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BU `score` DESC;
UPDATE `second_table` SET VALUES `score` = 10 WHERE `name` = 'Bob'