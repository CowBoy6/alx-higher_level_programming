-- creates a table second_table in the database hbtn_0c_0 in my MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS `second_table`(`id` INT,`name` VARCHAR(256), `score` INT);INSERT INTO `second_table`(`id`,`name`,`score`) VALUES(1,'JOHN',10);
INSERT INTO `second_table`(`id`,`name`,`score`) VALUES(2,'Alex',3); 
INSERT INTO `second_table`(`id`,`name`,`score`) VALUES(3,'bob',14);