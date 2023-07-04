-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2023 at 02:25 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `time_tabling`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `number` varchar(9) NOT NULL,
  `name` varchar(255) NOT NULL,
  `max_numb_of_students` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`number`, `name`, `max_numb_of_students`) VALUES
('05501111', 'วิชาเลือกทางคอมพิวเตอร์2', 50),
('05502222', 'วิชาเลือกทางคอมพิวเตอร์3', 50),
('05506001', 'คณิตศาสตร์ดิสครีต', 50),
('05506001A', 'คณิตศาสตร์ดิสครีต', 60),
('05506002', 'กรรมวิธีคำนวณเชิงตัวเลข', 50),
('05506004', 'การเขียนโปรแกรมเชิงออบเจกต์', 50),
('05506004A', 'การเขียนโปรแกรมเชิงออบเจกต์', 60),
('05506008', 'โครงสร้างและสถาปัตยกรรม', 50),
('05506011', 'ปฏิสัมพันธ์ระหว่างมนุษย์และคอมพิวเตอร์', 50),
('05506014', 'คอมพิวเตอร์กราฟิกส์', 50),
('05506015', 'จรรยาบรรณทางวิชาชีพและเชิงสังคม', 50),
('05506018', 'สัมมนา', 50),
('05506019', 'จรรยาบรรณทางวิชาชีพและเชิงสังคมปี3', 50),
('05506099', 'ปัญหาพิเศษ', 50),
('05506113', 'การวิเคราะห์และออกแบบซอฟต์แวร์', 50),
('05506233', 'แคลคูลัสสำหรับวิทยาการคอมพิวเตอร์', 50),
('05506233A', 'แคลคูลัสสำหรับวิทยาการคอมพิวเตอร์', 60),
('05506236', 'การวิเคราะห์และการออกแบบขั้นตอนวิธี', 50),
('05506xxx', 'วิชาเลือกทางคอมพิวเตอร์', 50),
('90111111', '(วิชาเลือกกลุ่มภาษา)', 50),
('90641002', 'ความฉลาดทางดิจิทัล', 50),
('90644008', 'ภาษาอังกฤษพื้นฐาน', 50),
('90xxxxxx', 'วิชาเลือกตามเกณฑ์ของคณะวิทยาศาสตร์', 59),
('xxxxxxxx', 'วิชาเลือกเสรี', 70);

-- --------------------------------------------------------

--
-- Table structure for table `course_instructor`
--

CREATE TABLE `course_instructor` (
  `course_number` varchar(9) NOT NULL,
  `instructor_number` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course_instructor`
--

INSERT INTO `course_instructor` (`course_number`, `instructor_number`) VALUES
('90xxxxxx', 'I11'),
('05506113', 'I2'),
('05502222', 'I2'),
('05506002', 'I3'),
('xxxxxxxx', 'I3'),
('05506004', 'I3'),
('05506004A', 'I3'),
('05506xxx', 'I4'),
('05506008', 'I5'),
('05506015', 'I6'),
('05506019', 'I6'),
('05501111', 'I6'),
('90644008', 'I7'),
('05506011', 'I7'),
('05506014', 'I8'),
('05506236', 'I9'),
('05506099', 'I9'),
('05506233', 'I1'),
('05506233A', 'I4'),
('05506018', 'I1'),
('90641002', 'I1'),
('05501111', 'I1'),
('05506001', 'I2'),
('05506001A', 'I2');

-- --------------------------------------------------------

--
-- Table structure for table `dept`
--

CREATE TABLE `dept` (
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dept`
--

INSERT INTO `dept` (`name`) VALUES
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1'),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2'),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 3'),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 4');

-- --------------------------------------------------------

--
-- Table structure for table `dept_course`
--

CREATE TABLE `dept_course` (
  `name` varchar(255) NOT NULL,
  `course_numb` varchar(9) NOT NULL,
  `sec` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dept_course`
--

INSERT INTO `dept_course` (`name`, `course_numb`, `sec`) VALUES
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '90xxxxxx', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506113', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 3', '05502222', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506002', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 4', 'xxxxxxxx', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506004', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506004A', 2),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506xxx', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506008', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506015', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 3', '05506019', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 3', '05501111', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '90644008', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506011', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506014', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', '05506236', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 4', '05506099', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506233', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506233A', 2),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 4', '05506018', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '90641002', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05501111', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506001', 1),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', '05506001A', 2);

-- --------------------------------------------------------

--
-- Table structure for table `exp_dept`
--

CREATE TABLE `exp_dept` (
  `name_id` varchar(255) NOT NULL,
  `meeting_time` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `exp_dept`
--

INSERT INTO `exp_dept` (`name_id`, `meeting_time`) VALUES
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', 3),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', 3),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 1', 6),
('วิทยาการคอมพิวเตอร์ ชั้นปีที่ 2', 6);

-- --------------------------------------------------------

--
-- Table structure for table `instructor`
--

CREATE TABLE `instructor` (
  `number` varchar(3) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `instructor`
--

INSERT INTO `instructor` (`number`, `name`) VALUES
('I1', 'ผศ.ดร.ธีระ ศิริธีรากุล'),
('I10', 'ผศ.ดร.ปัทมา เจริญพร'),
('I11', 'ผศ.กฤษฎา บุศรา'),
('I2', 'ผศ.ดร.วิสันต์ ตั้งวงษ์เจริญ'),
('I3', 'ผศ.ดร.ศรัณย์ อินทโกสุม'),
('I4', 'อ.สันธนะ อู่อุดมยิ่ง'),
('I5', 'รศ.ดร.จีรพร วีระพันธุ์'),
('I6', 'ดร.รุ่งรัตน์ เวียงศรีพนาวัลย์'),
('I7', 'ผศ.ดร.อินทราพร อรัณยะนาค'),
('I8', 'ดร.วิชญะ ต่อวงศ์ไพชยนต์'),
('I9', 'รศ.ธีรวัฒน์ ประกอบผล');

-- --------------------------------------------------------

--
-- Table structure for table `instructor_availability`
--

CREATE TABLE `instructor_availability` (
  `instructor_id` varchar(3) NOT NULL,
  `meeting_time_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `meeting_time`
--

CREATE TABLE `meeting_time` (
  `id` int(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meeting_time`
--

INSERT INTO `meeting_time` (`id`, `name`, `time`) VALUES
(1, 'จันทร์เช้า', 'จ. 09:00-12:00 น.'),
(2, 'จันทร์บ่าย', 'จ. 13:00-16:00 น.'),
(3, 'อังคารเช้า', 'อ. 09:00-12:00 น.'),
(4, 'อังคารบ่าย', 'อ. 13:00-16:00 น.'),
(5, 'พุธเช้า', 'พ. 09:00-12:00 น.'),
(6, 'พุธบ่าย', 'พ. 13:00-16:00 น.'),
(7, 'พฤหัสบดีเช้า', 'พฤ. 09:00-12:00 น.'),
(8, 'พฤหัสบดีบ่าย', 'พฤ. 13:00-16:00 น.'),
(9, 'ศุกร์เช้า', 'ศ. 09:00-12:00 น.'),
(10, 'ศุกร์บ่าย', 'ศ. 13:00-16:00 น.');

-- --------------------------------------------------------

--
-- Table structure for table `multi_sec`
--

CREATE TABLE `multi_sec` (
  `name1` varchar(255) NOT NULL,
  `name2` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `multi_sec`
--

INSERT INTO `multi_sec` (`name1`, `name2`) VALUES
('05506001', '05506004A'),
('05506001A', '05506004');

-- --------------------------------------------------------

--
-- Table structure for table `parallel`
--

CREATE TABLE `parallel` (
  `name1_parallel` varchar(255) NOT NULL,
  `name2_parallel` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parallel`
--

INSERT INTO `parallel` (`name1_parallel`, `name2_parallel`) VALUES
('05506233', '05506233A');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `number` varchar(255) NOT NULL,
  `capacity` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`number`, `capacity`) VALUES
('ห้อง1', 50),
('ห้อง2', 50),
('ห้อง3', 50),
('ห้อง4', 50),
('ห้อง5', 50),
('ห้อง6', 50),
('ห้อง7', 50),
('ห้อง8', 60),
('ห้อง9', 70);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`number`,`name`);

--
-- Indexes for table `course_instructor`
--
ALTER TABLE `course_instructor`
  ADD KEY `course_number` (`course_number`),
  ADD KEY `instructor_number` (`instructor_number`);

--
-- Indexes for table `dept`
--
ALTER TABLE `dept`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `dept_course`
--
ALTER TABLE `dept_course`
  ADD KEY `name` (`name`),
  ADD KEY `course_numb` (`course_numb`);

--
-- Indexes for table `exp_dept`
--
ALTER TABLE `exp_dept`
  ADD KEY `name_id` (`name_id`),
  ADD KEY `meeting_time` (`meeting_time`);

--
-- Indexes for table `instructor`
--
ALTER TABLE `instructor`
  ADD PRIMARY KEY (`number`);

--
-- Indexes for table `instructor_availability`
--
ALTER TABLE `instructor_availability`
  ADD KEY `instructor_id` (`instructor_id`),
  ADD KEY `meeting_time_id` (`meeting_time_id`);

--
-- Indexes for table `meeting_time`
--
ALTER TABLE `meeting_time`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `multi_sec`
--
ALTER TABLE `multi_sec`
  ADD KEY `name1` (`name1`),
  ADD KEY `name2` (`name2`);

--
-- Indexes for table `parallel`
--
ALTER TABLE `parallel`
  ADD KEY `name1_parallel` (`name1_parallel`),
  ADD KEY `name2_parallel` (`name2_parallel`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`number`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course_instructor`
--
ALTER TABLE `course_instructor`
  ADD CONSTRAINT `course_number` FOREIGN KEY (`course_number`) REFERENCES `course` (`number`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `instructor_number` FOREIGN KEY (`instructor_number`) REFERENCES `instructor` (`number`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `dept_course`
--
ALTER TABLE `dept_course`
  ADD CONSTRAINT `course_numb` FOREIGN KEY (`course_numb`) REFERENCES `course` (`number`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `name` FOREIGN KEY (`name`) REFERENCES `dept` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `exp_dept`
--
ALTER TABLE `exp_dept`
  ADD CONSTRAINT `meeting_time` FOREIGN KEY (`meeting_time`) REFERENCES `meeting_time` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `name_id` FOREIGN KEY (`name_id`) REFERENCES `dept` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `instructor_availability`
--
ALTER TABLE `instructor_availability`
  ADD CONSTRAINT `instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`number`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `meeting_time_id` FOREIGN KEY (`meeting_time_id`) REFERENCES `meeting_time` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `multi_sec`
--
ALTER TABLE `multi_sec`
  ADD CONSTRAINT `name1` FOREIGN KEY (`name1`) REFERENCES `course` (`number`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `name2` FOREIGN KEY (`name2`) REFERENCES `course` (`number`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `parallel`
--
ALTER TABLE `parallel`
  ADD CONSTRAINT `name1_parallel` FOREIGN KEY (`name1_parallel`) REFERENCES `course` (`number`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `name2_parallel` FOREIGN KEY (`name2_parallel`) REFERENCES `course` (`number`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
