-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: easily_store
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Stock`
--

DROP TABLE IF EXISTS `Stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stock` (
  `id` int NOT NULL AUTO_INCREMENT,
  `producto` varchar(50) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `talle` varchar(50) DEFAULT NULL,
  `colores` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stock`
--

LOCK TABLES `Stock` WRITE;
/*!40000 ALTER TABLE `Stock` DISABLE KEYS */;
INSERT INTO `Stock` VALUES (1,'Remera boxy fit blanca',NULL,NULL,NULL,NULL),(2,'Remera boxy fit negra',NULL,NULL,NULL,NULL),(3,'Remera boxy fit verde',NULL,NULL,NULL,NULL),(4,'Remera lila',NULL,NULL,NULL,NULL),(5,'Remera azul',NULL,NULL,NULL,NULL),(6,'Remera top gris',NULL,NULL,NULL,NULL),(7,'Remera top negro',NULL,NULL,NULL,NULL),(8,'Remera top blanco',NULL,NULL,NULL,NULL),(9,'Remera top azul',NULL,NULL,NULL,NULL),(10,'Remera top rojo',NULL,NULL,NULL,NULL),(11,'Remera musculosa verde',NULL,NULL,NULL,NULL),(12,'Remera musculosa gris',NULL,NULL,NULL,NULL),(13,'Remera musculosa roja',NULL,NULL,NULL,NULL),(14,'Remera musculosa negra',NULL,NULL,NULL,NULL),(15,'Remera naranja',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-31 18:48:46
