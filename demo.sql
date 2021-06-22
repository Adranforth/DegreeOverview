-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2021-05-31 12:24:58
-- 服务器版本： 10.4.18-MariaDB
-- PHP 版本： 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `demo`
--

-- --------------------------------------------------------

--
-- 表的结构 `assessment`
--

CREATE TABLE `assessment` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `course` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cilos` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `assessment`
--

INSERT INTO `assessment` (`create_time`, `status`, `id`, `course`, `weight`, `name`, `cilos`) VALUES
(1622439527, 1, 1, 1, 15, 'Assignments/ Quizzes', '1'),
(1622439527, 1, 2, 1, 25, 'Labs', '2'),
(1622439527, 1, 3, 1, 10, 'Projects', '1-2'),
(1622439527, 1, 4, 1, 50, 'Examination', '1-2'),
(1622439862, 1, 5, 2, 15, 'Programming Exercise', '1'),
(1622439862, 1, 6, 2, 20, 'Programming Assignment', '1'),
(1622439862, 1, 7, 2, 25, 'Project', '2'),
(1622439862, 1, 8, 2, 10, 'Quizzes', '1-2'),
(1622439862, 1, 9, 2, 30, 'Final Examination', '1-2'),
(1622443693, 1, 10, 3, 15, 'Programming Exercise', '1'),
(1622443693, 1, 11, 3, 20, 'Programming Assignment', '1'),
(1622443693, 1, 12, 3, 25, 'Project', '2'),
(1622443693, 1, 13, 3, 10, 'Quizzes', '1-2'),
(1622443693, 1, 14, 3, 30, 'Final Examination', '1-2'),
(1622443733, 1, 15, 3, 15, 'Programming Exercise', '1'),
(1622443733, 1, 16, 3, 20, 'Programming Assignment', '1'),
(1622443733, 1, 17, 3, 25, 'Project', '2'),
(1622443733, 1, 18, 3, 5, 'Quizzes', '1-2'),
(1622443733, 1, 19, 3, 35, 'Final Examination', '1-2');

-- --------------------------------------------------------

--
-- 表的结构 `cilo`
--

CREATE TABLE `cilo` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `pre_cilo1` int(11) DEFAULT NULL,
  `pre_cilo2` int(11) DEFAULT NULL,
  `pre_cilo3` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `cilo`
--

INSERT INTO `cilo` (`create_time`, `status`, `id`, `pre_cilo1`, `pre_cilo2`, `pre_cilo3`, `name`) VALUES
(1622439527, 1, 1, NULL, NULL, NULL, 'Learn bootstrap'),
(1622439527, 1, 2, NULL, NULL, NULL, 'Use Python'),
(1622439862, 1, 3, 2, NULL, NULL, 'Explain the conceptual framework of object-oriented programming'),
(1622439862, 1, 4, NULL, NULL, NULL, 'Programme in JAVA to enable the solution of non-elementary programming tasks'),
(1622443693, 1, 5, NULL, NULL, NULL, 'Opencv'),
(1622443693, 1, 6, NULL, NULL, NULL, 'Use html');

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(100) NOT NULL,
  `academic_year` varchar(100) NOT NULL,
  `programme` varchar(100) NOT NULL,
  `_type` varchar(100) NOT NULL,
  `cilo1_id` int(11) DEFAULT NULL,
  `cilo2_id` int(11) DEFAULT NULL,
  `cilo3_id` int(11) DEFAULT NULL,
  `pre_course1_id` int(11) DEFAULT NULL,
  `pre_course2_id` int(11) DEFAULT NULL,
  `pre_course3_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`create_time`, `status`, `id`, `name`, `code`, `academic_year`, `programme`, `_type`, `cilo1_id`, `cilo2_id`, `cilo3_id`, `pre_course1_id`, `pre_course2_id`, `pre_course3_id`) VALUES
(1622439527, 1, 1, 'Software Engineering', 'COMP3013', '2021S2', 'CST', 'MR', 1, 2, NULL, 2, NULL, NULL),
(1622439862, 1, 2, 'OOP', 'COMP1002', '1920S1', 'CST', 'MR', 3, 4, NULL, 3, NULL, NULL),
(1622443693, 1, 3, 'IT', 'COMP1001', '1819S2', 'CST', 'MR', 5, 6, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `coursedesigner`
--

CREATE TABLE `coursedesigner` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `ID_num` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `coursedesigner`
--

INSERT INTO `coursedesigner` (`create_time`, `status`, `ID_num`, `Name`, `Username`, `password`, `programme`, `id`) VALUES
(0, 1, 'c830026123', 'Judy', 'Judy123', '123456', 'CST', 1);

-- --------------------------------------------------------

--
-- 表的结构 `grade`
--

CREATE TABLE `grade` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `Student_ID` varchar(100) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `EvaluationMethod` varchar(100) DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `grade`
--

INSERT INTO `grade` (`create_time`, `status`, `id`, `Student_ID`, `course_id`, `EvaluationMethod`, `value`) VALUES
(1629999999, 1, 1, 's830026039', 1, 'Assignments/ Quizzes', 14.71),
(1629999999, 1, 2, 's830026039', 1, 'Labs', 23.5),
(1629999999, 1, 3, 's830026039', 1, 'Projects', 9.63),
(1629999999, 1, 4, 's830026039', 1, 'Examination', 49.75);

-- --------------------------------------------------------

--
-- 表的结构 `lecturer`
--

CREATE TABLE `lecturer` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `ID_num` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `lecturer`
--

INSERT INTO `lecturer` (`create_time`, `status`, `ID_num`, `Name`, `Username`, `password`, `programme`, `id`) VALUES
(0, 1, 'l830026000', 'Nina', 'Nina000', '123456', 'CST', 1);

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE `student` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `ID_num` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `Student_ID` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`create_time`, `status`, `ID_num`, `Name`, `Username`, `password`, `programme`, `id`, `Student_ID`) VALUES
(0, 1, 's830026039', 'Gabriel', 'Gab039', '123456', 'CST', 1, 's830026039');

--
-- 转储表的索引
--

--
-- 表的索引 `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `course` (`course`);

--
-- 表的索引 `cilo`
--
ALTER TABLE `cilo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pre_cilo1` (`pre_cilo1`),
  ADD KEY `pre_cilo2` (`pre_cilo2`),
  ADD KEY `pre_cilo3` (`pre_cilo3`);

--
-- 表的索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cilo1_id` (`cilo1_id`),
  ADD KEY `cilo2_id` (`cilo2_id`),
  ADD KEY `cilo3_id` (`cilo3_id`),
  ADD KEY `pre_course1_id` (`pre_course1_id`),
  ADD KEY `pre_course2_id` (`pre_course2_id`),
  ADD KEY `pre_course3_id` (`pre_course3_id`);

--
-- 表的索引 `coursedesigner`
--
ALTER TABLE `coursedesigner`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- 表的索引 `grade`
--
ALTER TABLE `grade`
  ADD PRIMARY KEY (`id`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- 表的索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `assessment`
--
ALTER TABLE `assessment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- 使用表AUTO_INCREMENT `cilo`
--
ALTER TABLE `cilo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- 使用表AUTO_INCREMENT `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- 使用表AUTO_INCREMENT `coursedesigner`
--
ALTER TABLE `coursedesigner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `grade`
--
ALTER TABLE `grade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 限制导出的表
--

--
-- 限制表 `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`course`) REFERENCES `course` (`id`);

--
-- 限制表 `cilo`
--
ALTER TABLE `cilo`
  ADD CONSTRAINT `cilo_ibfk_1` FOREIGN KEY (`pre_cilo1`) REFERENCES `cilo` (`id`),
  ADD CONSTRAINT `cilo_ibfk_2` FOREIGN KEY (`pre_cilo2`) REFERENCES `cilo` (`id`),
  ADD CONSTRAINT `cilo_ibfk_3` FOREIGN KEY (`pre_cilo3`) REFERENCES `cilo` (`id`);

--
-- 限制表 `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`cilo1_id`) REFERENCES `cilo` (`id`),
  ADD CONSTRAINT `course_ibfk_2` FOREIGN KEY (`cilo2_id`) REFERENCES `cilo` (`id`),
  ADD CONSTRAINT `course_ibfk_3` FOREIGN KEY (`cilo3_id`) REFERENCES `cilo` (`id`),
  ADD CONSTRAINT `course_ibfk_4` FOREIGN KEY (`pre_course1_id`) REFERENCES `course` (`id`),
  ADD CONSTRAINT `course_ibfk_5` FOREIGN KEY (`pre_course2_id`) REFERENCES `course` (`id`),
  ADD CONSTRAINT `course_ibfk_6` FOREIGN KEY (`pre_course3_id`) REFERENCES `course` (`id`);

--
-- 限制表 `grade`
--
ALTER TABLE `grade`
  ADD CONSTRAINT `grade_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
