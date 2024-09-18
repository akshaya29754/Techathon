-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2022 at 06:45 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `disease`
--

CREATE TABLE `disease` (
  `Name` varchar(50) NOT NULL,
  `Symptom1` varchar(50) NOT NULL,
  `Symptom2` varchar(50) NOT NULL,
  `Symptom3` varchar(50) NOT NULL,
  `Symptom4` varchar(50) NOT NULL,
  `Symptom5` varchar(50) NOT NULL,
  `disease` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disease`
--

INSERT INTO `disease` (`Name`, `Symptom1`, `Symptom2`, `Symptom3`, `Symptom4`, `Symptom5`, `disease`) VALUES
('Ajay Ranabhat', 'itching', 'chills', 'stomach_pain', 'nodal_skin_eruptions', 'burning_micturition', 'Fungal infection'),
('Bishwo Karki', 'extra_marital_contacts', 'weakness_of_one_body_side', 'ulcers_on_tongue', 'irritation_in_anus', 'spotting_ urination', 'Drug Reaction'),
('Chabindra Kunwar', 'extra_marital_contacts', 'muscle_wasting', 'high_fever', 'patches_in_throat', 'muscle_weakness', 'AIDS'),
('Bibek Upreti', 'weakness_in_limbs', 'acidity', 'ulcers_on_tongue', 'polyuria', 'small_dents_in_nails', 'GERD'),
('Bibek Upreti', 'headache', 'stomach_pain', 'blackheads', 'vomiting', 'nausea', '(vertigo) Paroymsal  Positional Vertigo'),
('', 'headache', 'cough', 'tiredness', 'diarrhoea', 'high_fever', 'Gastroenteritis'),
('', 'headache', 'cough', 'loss of taste or smell', 'high_fever', 'diarrhoea', 'Gastroenteritis'),
('', 'tiredness', 'loss of taste or smell', 'headache', 'high_fever', 'diarrhoea', 'covid'),
('Ajay Ranabhat', 'itching', 'tiredness', 'high_fever', 'loss of taste or smell', 'diarrhoea', 'covid'),
('Ajay Ranabhat123', 'high_fever', 'loss of taste or smell', 'diarrhoea', 'tiredness', 'cough', 'covid'),
('Pawan ghimire', 'weight_loss', 'fatigue', 'spotting_ urination', 'visual_disturbances', 'drying_and_tingling_lips', 'Drug Reaction'),
('Rohan sharma', 'nodal_skin_eruptions', 'continuous_sneezing', 'ulcers_on_tongue', 'muscle_wasting', 'burning_micturition', 'Fungal infection'),
('Rohan sharma', 'nodal_skin_eruptions', 'continuous_sneezing', 'ulcers_on_tongue', 'muscle_wasting', 'burning_micturition', 'Fungal infection'),
('Milan Ad', 'itching', 'stomach_pain', 'joint_pain', 'chills', 'burning_micturition', 'Drug Reaction');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `specialization` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `Username`, `email`, `password`, `specialization`) VALUES
(1, 'arb12345', 'ajayranabhat19@gmail.com', 'ajayranabhat', 'heart'),
(2, 'amir', 'amir.ranabhat98@gmail.com', 'dfshgj', 'skin'),
(3, 'ajay12345', 'ajayranabhat21@gmail.com', 'arb12345', 'Gynocologist'),
(5, 'amirranabhat', 'amir.ranabhat100@gmail.com', 'ajay123', 'Eyes'),
(6, 'aman123', 'aman.ranabhat98@gmail.com', 'asdfg', 'Head');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `Disease` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `Username`, `email`, `password`, `contact`, `Disease`) VALUES
(8, 'ajay12345', 'ajayranabhat35@gmail.com', 'ajayrb', '9813510603', ''),
(9, 'arb12345', 'ajayranabhat45@gmail.com', 'ajayranabhat', '9823366570', ''),
(10, 'ajay12345', 'ajayranabhat19@gmail.com', 'dsfsdgfhg', '9823366570', ''),
(11, 'bibek', 'bibek.upreti10@gmail.com', 'bibek123', '9813245678', ''),
(12, 'Amir Ranabhat', 'amir.ranabhat88@gmail.com', 'amir123', '9880396896', ''),
(13, 'arb54321', 'ajayranabhat300@gmail.com', 'ajayrb', '9874561230', ''),
(14, 'roshan', 'roshanranabhat19@gmail.com', 'roshan123', '9852146569', ''),
(15, 'arb12345', 'ajayranabhat109@gmail.com', '123', '9852136569', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
