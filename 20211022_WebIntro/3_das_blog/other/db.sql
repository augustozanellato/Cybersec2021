-- Database: blog
-- Table structure for table `users`
-- Table structure for table `posts`
-- NeverLAN CTF <info@neverlanctf.com>
-- Author : Zane Durkin

-- Create user for web
CREATE USER 'blog'@'localhost' IDENTIFIED BY '<password_web>';
CREATE USER 'blog'@'%' IDENTIFIED BY '<password_web>';
GRANT SELECT ON blog.* To 'blog'@'localhost' WITH GRANT OPTION;
GRANT UPDATE ON blog.* To 'blog'@'localhost' WITH GRANT OPTION;
GRANT UPDATE ON blog.* To 'blog'@'%' WITH GRANT OPTION;
GRANT SELECT ON blog.* To 'blog'@'%' WITH GRANT OPTION;


-- Add password for root user
USE `mysql`;
UPDATE user set password=PASSWORD('<password_root>') where User='root';

-- Create blog database
CREATE DATABASE `blog`;
USE `blog`;

DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `permissions` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

LOCK TABLES `posts` WRITE;
INSERT INTO `posts` VALUES (1,'The Key, Oh my, The Key','<p>I know this post is only available for admins, and since I am the only admin on the blog, I decided to start keeping my passwords on here for quick access.<br>Everyone says that it isin\'t a good idea, but I don\'t care, nobody reads this blog anyway...<br> <ul><li><p>flag{C00ki3s_c4n_b33_ch4ng3d_?}</p></li></ul>','ADMIN'),(2,'The First Entry','<p>This is my first time writing a blog for my very own, custom made, website!!!!</p><p>I can set posts to only show for users with special permissions!</p>','OPEN'),(3,'Yet another log entry that you probably won\'t read','<p>so... it turns out not a whole lot of people actually visit my blog... maybe I should host it on a public server?</p>','OPEN');
UNLOCK TABLES;

-- Create users table
--   In real Practive, you never leave passwords in plain text.
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `permissions` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'JohnsTestUser','user','AT3stAccountForT3sting');
UNLOCK TABLES;
