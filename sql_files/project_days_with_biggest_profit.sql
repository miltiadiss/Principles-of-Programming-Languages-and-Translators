CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `days_with_biggest_profit`
--

DROP TABLE IF EXISTS `days_with_biggest_profit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `days_with_biggest_profit` (
  `Commodity` varchar(255) DEFAULT NULL,
  `Weekday` varchar(255) DEFAULT NULL,
  `Profit` bigint DEFAULT NULL,
  `Measure` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `days_with_biggest_profit`
--

LOCK TABLES `days_with_biggest_profit` WRITE;
/*!40000 ALTER TABLE `days_with_biggest_profit` DISABLE KEYS */;
INSERT INTO `days_with_biggest_profit` VALUES ('All','26/11/2021',2227000000,'$'),('Electrical machinery and equip','06/11/2020',96000000,'$'),('Fish, crustaceans, and molluscs','25/09/2017',21000000,'$'),('Fruit','03/05/2020',63000000,'$'),('Logs, wood, and wood articles','30/07/2021',97000000,'$'),('Meat and edible offal','21/05/2017',99000000,'$'),('Mechanical machinery and equip','02/10/2018',143000000,'$'),('Milk powder, butter, and cheese','04/12/2019',419000000,'$'),('Non-food manufactured goods','26/06/2020',565000000,'$'),('Fish, crustaceans, and molluscs','05/02/2019',4000,'Tonnes'),('Logs, wood, and wood articles','03/02/2020',476000,'Tonnes'),('Meat and edible offal','02/03/2015',14000,'Tonnes'),('Milk powder, butter, and cheese','04/12/2019',87000,'Tonnes');
/*!40000 ALTER TABLE `days_with_biggest_profit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-04 23:45:58
