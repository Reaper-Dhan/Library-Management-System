CREATE database library;
use library;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+05:30";
CREATE TABLE `book` (
  `id` int(10) NOT NULL,
  `title` char(60) DEFAULT NULL,
  `author` char(50) DEFAULT NULL,
  `pages` int(10) DEFAULT NULL,
  `price` float(6,2) DEFAULT NULL,
  `status` char(10) DEFAULT NULL,
  `publisher` char(60) DEFAULT NULL,
  `edition` char(15) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
INSERT INTO `book` (`id`, `title`, `author`, `pages`, `price`, `status`, `publisher`, `edition`) VALUES
(1, 'Python', 'Benten', 120, 300.00, 'available', 'RRpublishers', '1');
CREATE TABLE `member` (
  `id` int(11) NOT NULL,
  `name` char(30) DEFAULT NULL,
  `class` char(15) DEFAULT NULL,
  `address` char(100) DEFAULT NULL,
  `phone` char(15) DEFAULT NULL,
  `email` char(60) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
INSERT INTO `member` (`id`, `name`, `class`, `address`, `phone`, `email`) VALUES
(1, 'Rabikiran', '9th standard', 'kingkoti', '9879879879', 'koti@gmail.com');
CREATE TABLE `transaction` (
  `tid` int(11) NOT NULL,
  `b_id` int(11) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL,
  `doi` date DEFAULT NULL,
  `dor` date DEFAULT NULL,
  `fine` float(5,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`tid`);
ALTER TABLE `book`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
ALTER TABLE `member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
ALTER TABLE `transaction`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;