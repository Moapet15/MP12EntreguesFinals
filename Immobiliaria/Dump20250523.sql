-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: immobiliaria
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `consultes`
--

DROP TABLE IF EXISTS `consultes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consultes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `telefon` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tipus` varchar(50) NOT NULL,
  `missatge` text NOT NULL,
  `data_creacio` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultes`
--

LOCK TABLES `consultes` WRITE;
/*!40000 ALTER TABLE `consultes` DISABLE KEYS */;
INSERT INTO `consultes` VALUES (1,'689927124','franquetandreu@gmail.com','venda','Vull valorar el meu pis!','2025-05-19 18:26:21'),(2,'689927124','franquetandreu@gmail.com','lloguer','Vull assessorament per a llogar el meu local.','2025-05-20 15:21:37');
/*!40000 ALTER TABLE `consultes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `immobles`
--

DROP TABLE IF EXISTS `immobles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `immobles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `referencia` varchar(50) NOT NULL,
  `tipusFinca` varchar(50) NOT NULL DEFAULT '',
  `tipusHabitatge` varchar(50) NOT NULL,
  `provincia` varchar(50) NOT NULL,
  `municipi` varchar(50) NOT NULL,
  `poblacio` varchar(50) NOT NULL,
  `barri` varchar(50) NOT NULL,
  `estatConservacio` varchar(50) NOT NULL,
  `habitacions` int NOT NULL,
  `superficieUtil` int NOT NULL,
  `superficieConstruida` int NOT NULL,
  `superficieTerreny` int NOT NULL,
  `preu` int NOT NULL,
  `pisos` int NOT NULL,
  `descripcio` text,
  `lavabos` int NOT NULL,
  `terrassa` tinyint(1) NOT NULL DEFAULT '0',
  `traster` tinyint(1) NOT NULL DEFAULT '0',
  `garatge` tinyint(1) NOT NULL DEFAULT '0',
  `jardi` tinyint(1) NOT NULL DEFAULT '0',
  `qualificacioEnergetica` int NOT NULL,
  `ruta_carpeta` text NOT NULL,
  `destacat` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `immobles`
--

LOCK TABLES `immobles` WRITE;
/*!40000 ALTER TABLE `immobles` DISABLE KEYS */;
INSERT INTO `immobles` VALUES (11,'123456','Urbana','Casa','Tarragona','Priorat','Falset','Casc antic','Nou',4,150,200,200,120000,4,'Informació inventada només per a plenar...',4,1,0,1,0,430,'finques/Ref_123456/Foto1.webp, finques/Ref_123456/Foto2.webp, finques/Ref_123456/Foto3.webp',1),(13,'U-638','Urbana','Casa','Tarragona','Els Guiamets','Els Guiamets','Casc antic','En bon estat',4,185,185,185,165000,2,'Ref. U-638 - GRAN OPORTUNITAT ELS GUIAMETS - PROMOCIÓ LIMITADA\r\nPREU ACTUALITZAT A: 165.000\'00.-€!\r\n\r\nUna casa amb ànima, perfecta tant com a residència habitual com per escapades de cap de setmana.\r\n\r\nPreu promocional vàlid fins al 20 de juliol de 2025 (abans: 175.000\'00.-€)\r\nEs ven encantadora casa d\'estil rústic de 185m², totalment llesta per entrar a viure, al cor d\'Els Guiamets. Ideal per als amants de la tranquil·litat i l\'autenticitat, amb acabats que transmeten calidesa i caràcter.\r\nDistribució:\r\nPlanta baixa: àmplia sala d\'estar, cuina office, pas i escala interior que connecta amb les plantes superiors.\r\nPrimera planta: distribuïdor/saleta, 2 habitacions dobles i bany amb hidromassatge.\r\nSegona planta: 2 habitacions més (una amb sostre inclinat), i un bany complet.\r\nTerrat amb vistes ideals per gaudir del bon temps.\r\nPlanta soterrani: espai ideal com a bodega o celler.\r\nCaracterístiques destacades:\r\nFaçana en molt bon estat, amb detalls decoratius de totxo vist a finestres i balcons.\r\nAcabats rústics amb pedra vista, bigues de fusta als sostres i sòl de gres.\r\nTancaments, portes i finestres en bon estat de conservació.',2,1,1,0,0,245,'finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01a6a.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01a6b.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01a6d.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01a69.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01a70.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-000012d01eec.jpg.webp, finques/Ref_U-638/ID770d7a01-0000-0500-0000-0000154949fb.jpg.webp',1),(14,'U-704','Urbana','Casa','Tarragona','Poboleda','Poboleda','Casc antic','Per reformar',5,620,400,634,158000,4,'Ref. U-704. A POBOLEDA (PRIORAT) ES VEN CASA CANTONERA AMB UNA SUPERFÍCIE DE 400 m² AMB MAGATZEM/GARATGE AMB POSSIBILITAT D\'AMPLIAR 220 m2 MÉS o TRANSFORMAR EN JARDÍ.\r\n\r\nDescobreix aquesta casa de 400 m², distribuïda en dues plantes d\'habitatge, magatzem i garatge. Situada al bell mig del poble, aquesta propietat ofereix fàcil accés. Amb una superfície de planta de 108 m², la planta baixa i la primera planta estan dedicades a ús residencial, proporcionant un espai ampli i còmode per a tota la família.\r\n\r\nLa casa compta amb cinc dormitoris, dos banys complets, una terrassa i un balcó amb vistes.\r\n\r\nEl magatzem de 108 m² i el garatge de 90 m² ofereixen espai addicional per a emmagatzematge i aparcament,\r\n\r\nIdeal per a múltiples usos, aquesta finca urbana solar es troba en una ubicació privilegiada amb fàcil accés\r\n\r\nAmb possibilitat d\'ampliar 220 m2 més per a aquells que busquen un projecte de reforma amb infinites possibilitats.\r\n\r\nTotal de superfície 634 m2.\r\n\r\nPREU: 158.000\'00.-€',2,1,0,1,1,450,'finques/Ref_U-704/IDc8168201-0000-0500-0000-000013bf414e.jpg.webp, finques/Ref_U-704/IDc8168201-0000-0500-0000-000013bf414f.jpg.webp, finques/Ref_U-704/IDc8168201-0000-0500-0000-000013bf4150.jpg.webp, finques/Ref_U-704/IDc8168201-0000-0500-0000-000013bf4151.jpg.webp, finques/Ref_U-704/IDc8168201-0000-0500-0000-000013bf4153.jpg.webp',1),(15,'R-572','Rustica','Finca rústica','Tarragona','Gratallops','Gratallops','.','Bon estat',1,16000,30,16000,50000,0,'R-572. A GRATALLOPS ES VEN FINCA RÚSTICA DE 1\'60 HA\r\nCaracterístiques:\r\n\r\nFinca situada al terme municipal de Gratallops, al cor del Priorat.\r\n\r\nSuperfície total de 16.300 m² distribuïts en diverses zones de cultiu i terreny natural.\r\n\r\nAltres zones de matollar i vegetació natural\r\n\r\nAccés per camí rural\r\n\r\nEntorn tranquil, ideal per a usos agrícoles, de lleure o inversió en terreny al Priorat\r\n\r\nAmb una caseta de 30 m²\r\n\r\nCultius:\r\n\r\no Oliveres\r\n\r\no Ametllers\r\n\r\no Zona de matoll i bosc\r\n\r\n\r\nPreu: 50.000 €',1,0,0,0,1,350,'finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6be.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6c2.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6c6.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6ca.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6cd.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6cf.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6d0.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6d2.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6d4.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6d9.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c6e6.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c713.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c714.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c715.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c716.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c717.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c718.jpg.webp, finques/Ref_R-572/ID19369b01-0000-0500-0000-00001590c719.jpg.webp',1),(16,'R-567','Rustica','Finca rústica','Tarragona','Falset','Falset','.','Bon estat',0,40000,10,40000,18000,0,'R-567. ES VEN FINCA RÚSTICA AL TERME DE FALSET AMB CASETA\r\n\r\nDescobreix aquest magnífic terreny rústic de 4 Ha, situat en un entorn muntanyós. Aquest espai ofereix una oportunitat única per aquells que busquen un refugi natural lluny de l\'estrès de la ciutat.\r\n\r\nEl terreny compta amb cultius d\'avellaners, matorral i un bosc sense conrear que afegeix un encant especial a la finca, és una inversió ideal per a aquells que volen connectar-se amb la natura i gaudir d\'un estil de vida més sostenible. No deixis passar aquesta oportunitat única de fer-te amb un trosset de paradís!\r\n\r\nPREU: 18.000\'00.-€',0,0,0,0,1,0,'finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0c5.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0c8.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0ca.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0ce.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0d0.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0d2.jpg.webp, finques/Ref_R-567/IDf84b9901-0000-0500-0000-00001562d0d3.jpg.webp',1),(17,'R-533','Rustica','Finca rústica','Tarragona','Miravet','Miravet','.','Bon estat',2,130,142,230000,420000,2,'Aquesta propietat compta amb un embarcador propi i està ubicada al costat del riu, cosa que la fa ideal per a activitats esportives i aquàtiques, com la pesca. L\'habitatge principal, construït de fusta nòrdica, té un perfecte estat de conservació i ofereix una terrassa amb impressionants vistes al riu.\r\n\r\nAmb una distribució en 2 plantes, a la planta primera hi trobem una sala diàfana, un saló amb accés a la terrassa i barbacoa, un dormitori principal i un bany. A la segona planta hi ha una sala d´estar o dormitori addicional. A més, aquesta propietat compta amb un altre habitatge o refugi pendent d\'acabats interiors. Disposa d\'aigua de pou, electricitat i cultius en una extensió d\'aproximadament 2 ha de regadiu.\r\n\r\nAmb 142 m² construïts i 130 m² útils, aquesta casa rural compta amb 2 dormitoris, 1 bany, terrassa, armaris de paret, traster, llar de foc i jardí.\r\n\r\nAny de construcció: 2000. Orientació est/oest. Parcel·la de 230.000 m².',1,1,0,1,1,0,'finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba1a.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba1b.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba1c.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba15.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba16.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba17.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba18.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba19.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba21.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba23.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba24.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba26.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-000012f1ba28.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f24a.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f24b.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f24e.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f25a.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f241.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f242.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f243.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f244.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f245.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f248.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f252.jpg.webp, finques/Ref_R-533/ID8c997601-0000-0500-0000-00001267f253.jpg.webp',1),(18,'LOC-498','Lloguer','Local en lloguer','Tarragona','Falset','Falset','Casc antic','En bon estat',0,45,50,50,400,1,'Ref. LU-498. A FALSET ES LLOGA LOCAL COMERCIAL UBICAT A LA PLANTA BAIXA, AL CARRER PRINCIPAL. LOCAL PER A MÚLTIPLES OPCIONS OFICINA, DESPATX, COMERÇ. PREU: 400.- € / MENSUALS!!\r\n\r\nCaracterístiques:\r\n- Local d\'uns 35 m², situat en planta baixa.\r\n- Molt ben situat amb aparador al carrer principal.\r\n- Ideal per a instal·lar-hi oficina.\r\n- Servei.\r\n- Sòl de parquet.\r\n- Porta exterior amb reixa.\r\n\r\nPREU: 400\'00.- €',1,0,1,0,0,0,'finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdb.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdc.jpg_1.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdc.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdd.jpg_1.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdd.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fde.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fdf.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fe1.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fe3.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fe4.jpg.webp, finques/Ref_LOC-498/ID0fc77201-0000-0500-0000-000014453fe5.jpg.webp',1),(19,'Loc-527','Lloguer','Complex en Lloguer','Tarragona','Gratallops','Gratallops','.','En bon estat',6,1000,1000,14000,14000,3,'Ref. LU-527 - Un Paradís per a l\'Agroturisme al Priorat! Lloga Aquest Complex Amb Tot Inclòs!\r\nEn un dels racons més bells del Priorat, en un entorn natural privilegiat, es troba aquest espectacular complex en lloguer, ideal per a un negoci d\'agroturisme o restauració amb allotjament una joia per als amants del turisme rural i la gastronomia.\r\nAquesta propietat compta amb un restaurant amb cuina equipada, foc de llenya i diverses sales per oferir una experiència única als clients. A l\'exterior, trobaràs amplis espais amb terrasses panoràmiques, perfectes per gaudir de la tranquil·litat del Montsant.\r\nEl complex també disposa de 6 habitacions per a hostes, completament moblades i adaptades per a una estada còmoda i autèntica, oferint una experiència autèntica. La zona d\'esbarjo inclou un jardí espectacular, parc infantil i piscina, convertint-lo en un destí ideal per a turisme familiar.\r\nEl complex també inclou diverses finques rústiques per la qual cosa aporta un gran valor afegit a aquesta propietat. En plena producció dedicades al cultiu de vinya i oliveres, equipada amb bodega pròpia, premsa i molí d\'oli com instal·lacions pròpies per elaborar i comercialitzar vi i oli d\'alta qualitat. Oferint un gran potencial de negoci.\r\nSi busques una inversió segura i amb possibilitats de creixement, aquest complex ho té tot per triomfar. Contacta ara per conèixer-ne tots els detalls!',8,1,1,1,1,0,'finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e3.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e4.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e5.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e7.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e8.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033e9.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033ea.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033eb.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033ec.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033ed.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033ee.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033ef.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f0.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f1.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f2.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f3.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f4.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f5.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f7.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f8.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033f9.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033fa.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033fb.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033fc.jpg.webp, finques/Ref_Loc-527/IDed648d01-0000-0500-0000-0000149033fd.jpg.webp',1),(20,'LOC-424','Lloguer','Local en lloguer','Tarragona','Falset','Falset','Casc antic','En bon estat',0,64,68,68,400,0,'Ref. Lu-424. A falset es lloga local cantoner de 64 m² amb aparador al centre de la població! sol.\r\nLiciti més informació!\r\ncaracterístiques:\r\nes lloga local comercial cantoner.\r\nsuperfície: 64 m².\r\ndisposa d\'aparador frontal i lateral.\r\nubicat al centre de la població.\r\n\r\nPreu: 400 € / mes.',1,0,1,0,0,0,'finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa1f.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa20.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa21.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa22.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa23.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa24.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa25.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa26.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa27.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001213fa28.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f07b.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f07d.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f07f.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f067.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f075.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f077.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f079.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f083.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f085.jpg.webp, finques/Ref_LOC-424/ID92c67201-0000-0500-0000-00001440f086.jpg.webp',1);
/*!40000 ALTER TABLE `immobles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `missatges`
--

DROP TABLE IF EXISTS `missatges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `missatges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuari_email` varchar(255) NOT NULL,
  `finca_referencia` varchar(50) DEFAULT NULL,
  `emissor` enum('usuari','admin') NOT NULL,
  `contingut` text NOT NULL,
  `data_enviament` datetime DEFAULT CURRENT_TIMESTAMP,
  `llegit` tinyint(1) DEFAULT '0',
  `idAssociat` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `missatges`
--

LOCK TABLES `missatges` WRITE;
/*!40000 ALTER TABLE `missatges` DISABLE KEYS */;
INSERT INTO `missatges` VALUES (1,'franquetandreu@gmail.com','123456','usuari','<div class=\"missatgeria\" alt=\"missatgeria\"> <p>Hola, estic interessat en aquest immoble!</p> </div>','2025-05-18 19:01:40',0,NULL),(5,'alfonbeltran@gmail.com','123456','usuari','M\'interessa aquest domicili!','2025-05-19 16:14:34',0,NULL),(7,'alfonbeltran@gmail.com','123456','admin','Responem al missatge amb comptes diferents\r\n','2025-05-19 17:20:53',0,5),(9,'alfonbeltran@gmail.com','123456','usuari','Tornem a respondre per a comprovar que s\'asocia bé el id','2025-05-19 17:27:32',0,7);
/*!40000 ALTER TABLE `missatges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuaris`
--

DROP TABLE IF EXISTS `usuaris`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuaris` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `rebreOfertes` tinyint(1) DEFAULT '0',
  `finquesPreferides` text,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuaris`
--

LOCK TABLES `usuaris` WRITE;
/*!40000 ALTER TABLE `usuaris` DISABLE KEYS */;
INSERT INTO `usuaris` VALUES (1,'Andreu','franquetandreu@gmail.com','Moapet15',0,'123456, 16, R-567',1),(2,'Alfonso','alfonbeltran@gmail.com','Moapet15',0,NULL,0);
/*!40000 ALTER TABLE `usuaris` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-23 15:55:51
