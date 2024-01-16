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
-- Table structure for table `top_5_commodities`
--

DROP TABLE IF EXISTS `top_5_commodities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `top_5_commodities` (
  `Country` varchar(255) DEFAULT NULL,
  `Commodity` varchar(255) DEFAULT NULL,
  `Profit` bigint DEFAULT NULL,
  `Measure` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `top_5_commodities`
--

LOCK TABLES `top_5_commodities` WRITE;
/*!40000 ALTER TABLE `top_5_commodities` DISABLE KEYS */;
INSERT INTO `top_5_commodities` VALUES ('All','All',1603472000000,'$'),('All','Non-food manufactured goods',403154000000,'$'),('All','Milk powder, butter, and cheese',98757000000,'$'),('All','Mechanical machinery and equip',57567000000,'$'),('All','Meat and edible offal',51206000000,'$'),('Australia','All',107686000000,'$'),('China','All',182406000000,'$'),('China','Milk powder, butter, and cheese',31216000000,'$'),('China','Logs, wood, and wood articles',17993000000,'$'),('China','Electrical machinery and equip',16478000000,'$'),('China','Meat and edible offal',15463000000,'$'),('East Asia (excluding China)','All',89245000000,'$'),('East Asia (excluding China)','Milk powder, butter, and cheese',27311000000,'$'),('European Union (27)','All',26644000000,'$'),('Japan','All',23155000000,'$'),('Total (excluding China)','All',291991000000,'$'),('United Kingdom','All',21591000000,'$'),('United States','All',40477000000,'$'),('United States','Meat and edible offal',11843000000,'$'),('All','Logs, wood, and wood articles',154650000,'Tonnes'),('All','Milk powder, butter, and cheese',22118000,'Tonnes'),('All','Meat and edible offal',6749000,'Tonnes'),('All','Fish, crustaceans, and molluscs',1832000,'Tonnes'),('China','Logs, wood, and wood articles',109752000,'Tonnes'),('China','Milk powder, butter, and cheese',7536000,'Tonnes'),('China','Meat and edible offal',2285000,'Tonnes'),('East Asia (excluding China)','Milk powder, butter, and cheese',6137000,'Tonnes'),('United States','Meat and edible offal',1338000,'Tonnes');
/*!40000 ALTER TABLE `top_5_commodities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-04 23:45:57
