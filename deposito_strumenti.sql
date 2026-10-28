-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dump della struttura del database deposito_strumenti
CREATE DATABASE IF NOT EXISTS `deposito_strumenti` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `deposito_strumenti`;

-- Dump della struttura di tabella deposito_strumenti.strumento
CREATE TABLE IF NOT EXISTS `strumento` (
    `codice` varchar(50) NOT NULL,
    `tipo` varchar(50) NOT NULL,
    `marca` varchar(50) NOT NULL,
    `anno_acquisto` year NOT NULL,
    `valore` decimal(10,2) NOT NULL,
    `disponibile` bool NOT NULL,
    PRIMARY KEY (`codice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dump dei dati della tabella deposito_strumenti.strumento: 24 rows
DELETE FROM `strumento`;
/*!40000 ALTER TABLE `strumento` DISABLE KEYS */;
INSERT INTO `strumento` (`codice`, `tipo`, `marca`, `anno_acquisto`, `valore`, `disponibile`) VALUES
	('S001', 'Chitarra', 'Yamaha', 2019, 250.00, true),
	('S002', 'Chitarra', 'Fender', 2017, 320.00, true),
	('S003', 'Chitarra', 'Gibson', 2015, 890.00, true),
	('S004', 'Chitarra', 'Taylor', 2022, 650.00, true),
	('S005', 'Violino', 'Stentor', 2020, 180.00, true),
	('S006', 'Violino', 'Yamaha', 2021, 240.00, true),
	('S007', 'Violino', 'Hofner', 2016, 310.00, true),
	('S008', 'Tromba', 'Bach', 2018, 600.00, true),
	('S009', 'Tromba', 'Yamaha', 2020, 480.00, true),
	('S010', 'Pianoforte Digitale', 'Roland', 2021, 900.00, true),
	('S011', 'Pianoforte Digitale', 'Yamaha', 2019, 850.00, true),
	('S012', 'Pianoforte Digitale', 'Casio', 2023, 420.00, true),
	('S013', 'Flauto Traverso', 'Yamaha', 2019, 210.00, true),
	('S014', 'Flauto Traverso', 'Pearl', 2022, 260.00, true),
	('S015', 'Clarinetto', 'Buffet', 2020, 450.00, true),
	('S016', 'Clarinetto', 'Yamaha', 2018, 380.00, true),
	('S017', 'Violoncello', 'Stentor', 2018, 700.00, true),
	('S018', 'Violoncello', 'Yamaha', 2021, 780.00, true),
	('S019', 'Sassofono', 'Selmer', 2022, 850.00, true),
	('S020', 'Sassofono', 'Yamaha', 2017, 620.00, true),
	('S021', 'Batteria', 'Pearl', 2021, 500.00, true),
	('S022', 'Batteria', 'Tama', 2019, 540.00, true),
	('S023', 'Basso Elettrico', 'Fender', 2020, 480.00, true),
	('S024', 'Basso Elettrico', 'Ibanez', 2023, 390.00, true);
/*!40000 ALTER TABLE `strumento` ENABLE KEYS */;

-- Dump della struttura di tabella deposito_strumenti.prestito
CREATE TABLE IF NOT EXISTS `prestito` (
    `codice` varchar(50) NOT NULL,
    `data` date NOT NULL,
    `id_strumento` varchar(50) NOT NULL,
    `allievo` varchar(50) NOT NULL,
    PRIMARY KEY (`codice`),
  KEY `FK_strumento` (`id_strumento`),
  CONSTRAINT `FK_strumento` FOREIGN KEY (`id_strumento`) REFERENCES `strumento` (`codice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dump dei dati della tabella deposito_strumenti.prestito: 6 rows
DELETE FROM `prestito`;
/*!40000 ALTER TABLE `prestito` DISABLE KEYS */;
INSERT INTO `prestito` (`codice`, `data`, `id_strumento`, `allievo`) VALUES
    ('P001', '2025-01-01', 'S001', 'Lorenzo Ferrari'),
    ('P002', '2025-01-01', 'S011', 'Mario Rossi'),
    ('P003', '2025-05-12', 'S019', 'Luisa Bianchi'),
    ('P004', '2025-08-03', 'S016', 'Giovanni Verdi'),
    ('P005', '2025-09-04', 'S006', 'Francesca Neri'),
    ('P006', '2025-10-22', 'S022', 'Maria Costa');
/*!40000 ALTER TABLE `prestito` ENABLE KEYS */;

-- Aggiorna la disponibilità degli strumenti in prestito
UPDATE strumento
SET disponibile = false
WHERE codice IN (SELECT id_strumento FROM prestito);

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
