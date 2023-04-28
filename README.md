
VMA’S VOTING WEBSITE – Kirk Cheataa-Laryea, Bhavana Bandaru

Application Login Credentials

With this web application there is the user login and the admin login, 
| Username             | Password | Role        |
|----------------------|----------|-------------|
| curt@gmail.com       | 12345    | Admin       |
| cheatak@clarkson.edu | 12345    | User/Viewer |

the user/viewer can only view and vote, the admin can add a nominee and delete a nominee(can also place a vote). 

Purpose

The VMA voting website is a platform where users can vote for their favorite music videos. The website allows users to register, login, and vote for their favorite videos in different categories such as Best Hip Hop, Best Pop, and Best Video of the Year. The website also displays the nominees in each category and allows users to view and vote.

Database and Class Description

This VMA voting web application imports modules such as Flask, render_template, request, session, redirect, url_for, escape, send_from_directory, and make_response. It also imports classes for the User, Student, Nominee, and Vote.
This web app creates a Flask application instance and sets the configuration for server-side sessions, including the secret key and session type. It also sets up a route for the home page, which displays the results of the votes and enables or disables voting based on whether a user is signed in or not, It also sets up a route for submitting votes, which gets the database connection, retrieves data from the request, and inserts the vote into the database.It sets up a route for the sign-in page, which handles both GET and POST requests. If the request method is GET, it renders the sign-in template, otherwise, it retrieves the email and password from the request, checks if the email and password match the database records, and if so, sets the session for the user and renders the home page template. Otherwise, it renders the sign-in template with an error message. It sets up a route for the admin page, which is only accessible to users with the admin role. It retrieves the results of the votes and nominee objects and handles POST requests for deleting or adding nominees to the database.
It also sets up a route for managing users, which can handle both GET and POST requests and can insert or update user data into the database.
In the baseobject.py file, there are three classes defined to represent each of these tables. The User class represents the users table, while the Video class represents the videos table. The Vote class represents the votes table. Each class contains attributes that map to the columns in the corresponding table.

Highlighted Custom SELECT Queries

In the nominee class, the getNomineeById function is a custom select query that fetches a single nominee from the database based on their ID. The getNominees function is another custom select query that fetches all nominees from the database. In the vote class, the getVotes function is a custom select query that fetches the number of votes each nominee has received from the database, also in the user class, the checkSignedIn function is a custom select query that fetches a single user from the database based on their email and password also the getUsers function is another custom select query that fetches all users from the database.

SQL Schema File

-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 27, 2023 at 11:15 PM
-- Server version: 5.6.33-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `is437`
--

-- --------------------------------------------------------

--
-- Table structure for table `vmas_ceremony`
--

CREATE TABLE IF NOT EXISTS `vmas_ceremony` (
  `cid` int(11) NOT NULL,
  `ceremonylocation` varchar(25) NOT NULL,
  `ceremonyhost` varchar(25) NOT NULL,
  `ceremonyvenue` varchar(25) NOT NULL,
  `yearofceremony` int(11) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vmas_media`
--

CREATE TABLE IF NOT EXISTS `vmas_media` (
  `mediaid` int(11) NOT NULL,
  `objectkey` int(11) NOT NULL,
  `objectname` varchar(255) NOT NULL,
  `filename` varchar(255) NOT NULL,
  PRIMARY KEY (`mediaid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vmas_nominee`
--

CREATE TABLE IF NOT EXISTS `vmas_nominee` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `nomineename` varchar(25) NOT NULL,
  `nomineecountry` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL,
  `musicname` varchar(25) NOT NULL,
  `awardcategory` varchar(25) NOT NULL,
  `nominatedyear` int(11) NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=38 ;

--
-- Dumping data for table `vmas_nominee`
--

INSERT INTO `vmas_nominee` (`nid`, `nomineename`, `nomineecountry`, `status`, `musicname`, `awardcategory`, `nominatedyear`) VALUES
(1, 'BTS', 'South Korea', 'Won', 'Butter', 'Best K-Pop', 2023),
(2, 'Lisa', 'South Korea', 'Loss', 'Lalisa', 'Best K-Pop', 2023),
(3, 'BlackPink', 'South Korea', 'Loss', 'How you like that', 'Best K-Pop', 2023),
(4, 'Lady Gaga', 'USA', 'Loss', 'Bad Romance', 'Artist of the year', 2023),
(5, 'Miley Cyrus', 'USA', 'Won', 'Flowers', 'Best New Single', 2023),
(6, 'Rihanna', 'USA', 'Loss', 'Umbrella', 'Best New Single', 2023),
(32, 'Weeknd', 'Canada', 'Loss', 'Blinding Lights', 'Best Music Video', 2023),
(33, 'Taylor Swift', 'USA', 'Loss', 'Gorgeous', 'Best New Single', 2023),
(34, 'Meghan Trainor', 'USA', 'Loss', 'Made you look', 'Best Music Video', 2023),
(35, 'Public band', 'USA', 'Loss', 'Make you mine', 'Artist of the year', 2023),
(36, 'One Direction', 'UK', 'Won', 'Night changes', 'Artist of the year', 2023),
(37, 'Dua Lipa', 'UK', 'Won', 'One Kiss', 'Best Music Video', 2023);

-- --------------------------------------------------------

--
-- Table structure for table `vmas_participation`
--

CREATE TABLE IF NOT EXISTS `vmas_participation` (
  `pid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `nid` int(11) NOT NULL,
  PRIMARY KEY (`pid`),
  KEY `cid` (`cid`),
  KEY `nid` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vmas_user`
--

CREATE TABLE IF NOT EXISTS `vmas_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(132) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` varchar(132) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=32 ;

--
-- Dumping data for table `vmas_user`
--

INSERT INTO `vmas_user` (`id`, `email`, `password`, `role`, `name`) VALUES
(3, 'bandarb@clarkson.edu', 'e5c5ec94023c839c53ab88bd7c184100', 'admin', 'Bhavana'),
(12, 'cheatak@clarkson.edu', 'e5c5ec94023c839c53ab88bd7c184100', 'viewer', 'Kirk'),
(23, 'flow@gmail.com', 'e5c5ec94023c839c53ab88bd7c184100', 'viewer', 'flow'),
(28, 'aabrams@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 'admin', 'Augustus Abrams'),
(29, 'curt@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 'admin', 'curt'),
(30, 'kirk@kirk.com', '827ccb0eea8a706c4c34a16891f84e7b', 'user', 'kirk'),
(31, 'bhavana@clarkson.edu', '827ccb0eea8a706c4c34a16891f84e7b', 'admin', 'Bhavana');

-- --------------------------------------------------------

--
-- Table structure for table `vmas_votes`
--

CREATE TABLE IF NOT EXISTS `vmas_votes` (
  `voteid` int(11) NOT NULL AUTO_INCREMENT,
  `nid` int(11) NOT NULL,
  `emailid` varchar(25) NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`voteid`),
  UNIQUE KEY `voteid` (`voteid`),
  KEY `emailid` (`emailid`),
  KEY `nid` (`nid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `vmas_votes`
--

INSERT INTO `vmas_votes` (`voteid`, `nid`, `emailid`, `userid`) VALUES
(17, 1, 'aabrams@gmail.com', 26),
(21, 1, 'aabrams@gmail.com', 26),
(25, 2, 'aabrams@gmail.com', 28),
(27, 4, 'curt@gmail.com', 29),
(28, 1, 'kirk@kirk.com', 30),
(29, 2, 'kirk@kirk.com', 30),
(30, 3, 'kirk@kirk.com', 30),
(33, 35, 'bhavana@clarkson.edu', 31),
(34, 1, 'bhavana@clarkson.edu', 31),
(35, 37, 'bhavana@clarkson.edu', 31),
(36, 33, 'bhavana@clarkson.edu', 31);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `vmas_participation`
--
ALTER TABLE `vmas_participation`
  ADD CONSTRAINT `vmas_participation_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `vmas_ceremony` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `vmas_participation_ibfk_2` FOREIGN KEY (`nid`) REFERENCES `vmas_nominee` (`nid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vmas_votes`
--
ALTER TABLE `vmas_votes`
  ADD CONSTRAINT `vmas_votes_ibfk_1` FOREIGN KEY (`nid`) REFERENCES `vmas_nominee` (`nid`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
