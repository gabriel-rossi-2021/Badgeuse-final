-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- HÃ´te : localhost:3306
-- GÃ©nÃ©rÃ© le : lun. 16 aoÃ»t 2021 Ã  06:38
-- Version du serveur :  5.7.24
-- Version de PHP : 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de donnÃ©es : `rossi_gabriel_info1c_timbrage_bd_104`
--

-- --------------------------------------------------------
DROP DATABASE IF EXISTS rossi_gabriel_info1c_timbrage_bd_104;

-- CrÃƒÂ©ation d'un nouvelle base de donnÃƒÂ©e

CREATE DATABASE IF NOT EXISTS rossi_gabriel_info1c_timbrage_bd_104;

-- Utilisation de cette base de donnÃƒÂ©e

USE rossi_gabriel_info1c_timbrage_bd_104;
--
-- Structure de la table `t_collaborateur`
--

CREATE TABLE `t_collaborateur` (
  `id_collaborateur` int(11) NOT NULL,
  `nom_famille` varchar(42) NOT NULL,
  `prenom` varchar(42) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_collaborateur`
--

INSERT INTO `t_collaborateur` (`id_collaborateur`, `nom_famille`, `prenom`) VALUES
(14, 'Rossi', 'Gabriel'),
(15, 'Skaloud', 'Matej'),
(16, 'Taillens', 'Kevin'),
(17, 'Urbano', 'Fabian'),
(18, 'Admin', 'Admin'),
(19, 'Preselet', 'Elvis'),
(20, 'Pilet', 'Kelly'),
(21, 'Ryser', 'Lorien');

-- --------------------------------------------------------

--
-- Structure de la table `t_collaborateur_details_collaborateur`
--

CREATE TABLE `t_collaborateur_details_collaborateur` (
  `id_collaborateur_details_collaborateur` int(11) NOT NULL,
  `FK_collaborateur` int(11) NOT NULL,
  `FK_details_collaborateur` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_collaborateur_details_collaborateur`
--

INSERT INTO `t_collaborateur_details_collaborateur` (`id_collaborateur_details_collaborateur`, `FK_collaborateur`, `FK_details_collaborateur`) VALUES
(17, 14, 10),
(9, 15, 11),
(10, 16, 12),
(11, 17, 13),
(13, 18, 14),
(14, 19, 15),
(15, 20, 16),
(16, 21, 17);

-- --------------------------------------------------------

--
-- Structure de la table `t_collaborateur_horaires`
--

CREATE TABLE `t_collaborateur_horaires` (
  `id_collaborateur_horaires` int(11) NOT NULL,
  `FK_collaborateur` int(11) NOT NULL,
  `FK_horaires` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_collaborateur_horaires`
--

INSERT INTO `t_collaborateur_horaires` (`id_collaborateur_horaires`, `FK_collaborateur`, `FK_horaires`) VALUES
(3, 14, 3),
(4, 15, 4),
(5, 16, 5),
(6, 17, 6);

-- --------------------------------------------------------

--
-- Structure de la table `t_collaborateur_identification`
--

CREATE TABLE `t_collaborateur_identification` (
  `id_collaborateur_identification` int(11) NOT NULL,
  `FK_collaborateur` int(11) NOT NULL,
  `FK_identification` int(11) NOT NULL,
  `date_et_heure_arrivee` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `date_et_heure_depart` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_collaborateur_identification`
--

INSERT INTO `t_collaborateur_identification` (`id_collaborateur_identification`, `FK_collaborateur`, `FK_identification`, `date_et_heure_arrivee`, `date_et_heure_depart`) VALUES
(10, 14, 14, '2021-05-21 06:42:15', '2021-05-21 06:42:15'),
(11, 15, 15, '2021-05-21 06:47:14', '2021-05-21 06:47:14'),
(12, 16, 16, '2021-05-21 06:55:38', '2021-05-21 06:55:38'),
(13, 17, 17, '2021-05-21 07:02:07', '2021-05-21 07:02:07'),
(14, 19, 19, '2021-05-21 11:30:53', '2021-05-21 11:30:53'),
(15, 20, 20, '2021-05-21 11:30:53', '2021-05-21 11:30:53'),
(16, 21, 21, '2021-05-21 11:30:59', '2021-05-21 11:30:59');

-- --------------------------------------------------------

--
-- Structure de la table `t_collaborateur_origine`
--

CREATE TABLE `t_collaborateur_origine` (
  `id_collaborateur_origine` int(11) NOT NULL,
  `FK_collaborateur` int(11) NOT NULL,
  `FK_origine` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_collaborateur_origine`
--

INSERT INTO `t_collaborateur_origine` (`id_collaborateur_origine`, `FK_collaborateur`, `FK_origine`) VALUES
(5, 14, 108),
(6, 14, 181),
(7, 15, 57),
(8, 16, 181),
(10, 17, 7),
(9, 17, 181),
(11, 18, 181),
(13, 19, 127),
(12, 19, 181),
(14, 20, 181),
(15, 21, 181);

-- --------------------------------------------------------

--
-- Structure de la table `t_collaborateur_specificite`
--

CREATE TABLE `t_collaborateur_specificite` (
  `id_collaborateur_specificite` int(11) NOT NULL,
  `FK_collaborateur` int(11) NOT NULL,
  `FK_specificite` int(11) NOT NULL,
  `date_et_heure` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_details_collaborateur`
--

CREATE TABLE `t_details_collaborateur` (
  `id_details_collaborateur` int(11) NOT NULL,
  `sexe` varchar(5) NOT NULL,
  `rue` varchar(50) NOT NULL,
  `numero_rue` int(11) NOT NULL,
  `npa` int(11) NOT NULL,
  `ville` varchar(20) NOT NULL,
  `pays` varchar(20) NOT NULL,
  `telephone` int(50) NOT NULL,
  `date_entree_entreprise` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_details_collaborateur`
--

INSERT INTO `t_details_collaborateur` (`id_details_collaborateur`, `sexe`, `rue`, `numero_rue`, `npa`, `ville`, `pays`, `telephone`, `date_entree_entreprise`) VALUES
(10, 'Homme', 'Chemin de Rente', 4, 1030, 'Bussigny', 'Suisse', 788237818, '2020-04-29'),
(11, 'Homme', 'Rue Montelieu', 48, 1030, 'Bussigny', 'Suisse', 786788392, '2020-05-29'),
(12, 'Homme', 'Chemin de Primerose ', 35, 1007, 'Lausanne', 'Suisse', 796547638, '2020-06-29'),
(13, 'Homme', 'Chemin de Cocagne', 15, 1030, 'Bussigny ', 'Suisse', 796599759, '2020-07-29'),
(14, 'Homme', 'Chemin du fleuve', 3, 1004, 'Lausanne', 'Suisse', 782362636, '2020-08-29'),
(15, 'Homme', 'Route du singe ', 4, 1020, 'Renens', 'Suisse', 782532525, '2020-09-29'),
(16, 'Femme', 'Rue de la femme ', 34, 1010, 'Lausanne', 'Suisse', 772837236, '2020-10-29'),
(17, 'Homme', 'Chemin des pleine', 4, 1004, 'Lausanne', 'Suisse', 763452443, '2020-11-29');

-- --------------------------------------------------------

--
-- Structure de la table `t_horaires`
--

CREATE TABLE `t_horaires` (
  `id_horaires` int(11) NOT NULL,
  `date_et_heure_horaires` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `est_un_timbrage` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_horaires`
--

INSERT INTO `t_horaires` (`id_horaires`, `date_et_heure_horaires`, `est_un_timbrage`) VALUES
(3, '2021-05-21 06:50:01', 1),
(4, '2021-05-21 07:01:22', 1),
(5, '2021-05-21 07:02:25', 1),
(6, '2021-05-21 07:02:28', 1),
(7, '2021-05-21 07:02:31', 1);

-- --------------------------------------------------------

--
-- Structure de la table `t_identification`
--

CREATE TABLE `t_identification` (
  `id_identification` int(11) NOT NULL,
  `nom_utilisateur` varchar(30) NOT NULL,
  `mot_de_passe` varchar(128) NOT NULL,
  `courriel` varchar(100) NOT NULL,
  `fk_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_identification`
--

INSERT INTO `t_identification` (`id_identification`, `nom_utilisateur`, `mot_de_passe`, `courriel`, `fk_role`) VALUES
(14, 'Rossig', 'pbkdf2:sha256:150000$r6O4b7kw$be74aebe10619fd6ad33e15c1a6c13a66f7e4d51a21862f7047801c3c9a92ea6', 'rossig@gmail.ch', 5),
(15, 'Skaloudm', 'pbkdf2:sha256:150000$HnbdWCCu$04b32dd252f3f3df595ff455cf0517ef12c8417a57a77a3005d7404d67ac22c0', 'skaloudm@gmail.com', 3),
(16, 'taillensk', 'pbkdf2:sha256:150000$3a8PEg1f$bf2ae856874c2072647131c032de4b949df1c46ed27403a0f2fbd5a982f9fff8', 'taillensk@gmail.com', 3),
(17, 'urbanof', 'pbkdf2:sha256:150000$iQx5vZxk$92cf116bea44acec9fd052d011f66025be3bf09a09e3657e3ad1b477ca1cfecf', 'urbanof@gmai.com', 3),
(18, 'admin', 'pbkdf2:sha256:150000$6qUo2bAL$b7f72b09afb702c82ccdcab798aac72d319ec0f9c2a9ced582a93ab5e5cc2ea2', 'admin@admin.com', 4),
(19, 'preselete', 'pbkdf2:sha256:150000$hvbyDTDM$96488beba9c23d544b13493ccbf5e667d93059f27405d00b8692691f9b7db65a', 'preselete@gmail.com', 3),
(20, 'Piletk', 'pbkdf2:sha256:150000$iaQX0XJZ$e77b9b210c93f59890c319b9a221205fe21cd323bd470fdc4d62e0a49876d4a6', 'piletk@gmail.com', 3),
(21, 'Ryserl', 'pbkdf2:sha256:150000$17IDen1O$08b6f27f96f9007b3164d7ff831d451c3da2edcb2ab2fece20825134c482ce28', 'ryserl@gmal.com', 3),
(22, 'test', 'pbkdf2:sha256:150000$4VHqLGIO$0c36bebbfcfdbb2644dc9ee04b60f7e8cee5e809a93ced14867aaf77acf37158', 'test@test.com', 3);

-- --------------------------------------------------------

--
-- Structure de la table `t_origine`
--

CREATE TABLE `t_origine` (
  `id_origine` int(11) NOT NULL,
  `origine` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_origine`
--

INSERT INTO `t_origine` (`id_origine`, `origine`) VALUES
(1, 'Afghan-(e)'),
(2, 'Albanais-(e)'),
(3, 'Allemand-(e)'),
(4, 'Andorran-(e)'),
(5, 'Angolais-(e)'),
(6, 'Saoudien-(ne)'),
(7, 'Argentin-(e)'),
(8, 'ArmÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nien-(ne)'),
(9, 'Arubain-(ne)'),
(10, 'Australien-(ne)'),
(11, 'Autrichien-(ne)'),
(12, 'AzerbaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯djanais-(e)'),
(13, 'Bahamien-(ne)'),
(14, 'bahreÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯nien-(ne)'),
(15, 'Bangladais-(e)'),
(16, 'bahreÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯nien-(ne)'),
(17, 'BiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©lorusse'),
(18, 'Birman-(e)'),
(19, 'Belge'),
(20, 'BÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©lizien-(ne)'),
(21, 'BÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ninois-(e)'),
(22, 'Bermudien-(ne)'),
(23, 'Bhoutanais-(e)'),
(24, 'Bolivien-(ne)'),
(25, 'aque'),
(50, 'tswanais-(e)'),
(51, 'ilien-(ne)'),
(52, 'unÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ien-(ne)'),
(53, 'lgare'),
(54, 'BurkinabÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©-(e)'),
(55, 'Burundais-(e)'),
(56, 'Camerounais-(e)'),
(57, 'Canadien-(ne)'),
(58, 'Cap-Verdien-(ne)'),
(59, 'Centrafricain-(e)'),
(60, 'Chilien-(ne)'),
(61, 'Chinois-(e)'),
(62, 'Chypriote'),
(63, 'Colombien-(ne)'),
(64, 'Comorien-(ne)'),
(65, 'Congolais-(e)'),
(66, 'Nord-CorÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(67, 'Sud-CorÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(68, 'Costaricain-(e)'),
(69, 'Ivoirien-(ne)'),
(70, 'Croate'),
(71, 'Cubain-(e)'),
(72, 'Danois-(e)'),
(73, 'Djiboutien-(ne)'),
(74, 'Dominiquais-(e)'),
(75, 'Egyptien-(ne)'),
(76, 'Emirien-(ne)'),
(77, 'Equatorien-(ne)'),
(78, 'ErythrÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(79, 'Espagnol-(e)'),
(80, 'Estonien-(ne)'),
(81, 'AmÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ricain-(e)'),
(82, 'Ethiopien-(ne)'),
(83, 'Fidjien-(ne)'),
(84, 'Finlandais-(e)'),
(85, 'FranÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ais-(e)'),
(86, 'Gabonais-(e)'),
(87, 'Gambien-(ne)'),
(88, 'GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©orgien-(ne)'),
(89, 'GhanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(90, 'Gibraltarien-(ne)'),
(91, 'Grec - Grecque'),
(92, 'Grenadien-(ne)'),
(93, 'GuatÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©maltÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨que'),
(94, 'GuinÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(95, 'Bissau-GuinÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(96, 'Equato-GuinÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(97, 'Guyanais-(e)'),
(98, 'HaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯tien-(ne)'),
(99, 'Hondurien-(ne)'),
(100, 'Hongrois-(e)'),
(101, 'Indien-(ne)'),
(102, 'IonÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©sien-(ne)'),
(103, 'Iranien-(ne)'),
(104, 'Irakien-(ne'),
(105, 'Irlandais-(e)'),
(106, 'Islandais-(e)'),
(107, 'IsraÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©lien-(ne)'),
(108, 'Italien-(ne)'),
(109, 'JamaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯cain-(e)'),
(110, 'Japonais-(e)'),
(111, 'Jordanien-(ne)'),
(112, 'Kazakh-(e)'),
(113, 'Kenyan-(e)'),
(114, 'Kirighiz'),
(115, 'Kiribatien-(ne)'),
(116, 'KoweÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯tien-(ne)'),
(117, 'Kosovar-(e)'),
(118, 'Laotien-(ne)'),
(119, 'Lesothan-(e)'),
(120, 'Letton-(ne)'),
(121, 'Libanais-(e)'),
(122, 'LibÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©rien-(ne)'),
(123, 'Libyen-(ne)'),
(124, 'Liechtensteinois-(e)'),
(125, 'Lituanien-(ne)'),
(126, 'Luxembourgeois-(e)'),
(127, 'MacÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©donien-(ne)'),
(128, 'Malgache'),
(129, 'Malaisien-(ne)'),
(130, 'Malawite'),
(131, 'Maldivien-(ne)'),
(132, 'Malien-(ne)'),
(133, 'Maltias-(e)'),
(134, 'Marocain-(e)'),
(135, 'Mauricien-(ne)'),
(136, 'Mauritanien-(ne)'),
(137, 'Mexicain-(e)'),
(138, 'MonÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©gasque'),
(139, 'Mongol-(e)'),
(140, 'MontÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©grin-(e)'),
(141, 'Mozambicain-(e)'),
(142, 'Namibien-(ne)'),
(143, 'NÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©palais-(e)'),
(144, 'Nicaraguayen-(ne)'),
(145, 'NigÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©rien-(ne)'),
(146, 'NigÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©rian-(e)'),
(147, 'NorvÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©gien-(ne)'),
(148, 'NÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©o-ZÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©landais-(e)'),
(149, 'Omanais-(e)'),
(150, 'Ougandais-(e)'),
(151, 'Ouzbek'),
(152, 'Pakistanais-(e)'),
(153, 'PanamÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)'),
(154, 'Papouasien-(ne)'),
(155, 'Paraguayen-(ne)'),
(156, 'NÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©erlandais-(e)'),
(157, 'PÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©ruvien-(ne)'),
(158, 'Philippin-(e)'),
(159, 'Polonais-(e)'),
(160, 'Portoricain-(e)'),
(161, 'Portugais-(e)'),
(162, 'Qatari-(e)'),
(163, 'Dominicain-(e)'),
(164, 'TchÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨que'),
(165, 'Roumain-(e)'),
(166, 'Britannique'),
(167, 'Russe'),
(168, 'Rwandais-(e)'),
(169, 'Saint-Vincentais-(e)'),
(170, 'Salvadorien-(ne)'),
(171, 'SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©galais-(e)'),
(172, 'Serbe'),
(173, 'Sierra-LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©onais-(e)'),
(174, 'Singapourien-(ne)'),
(175, 'Slovaque'),
(176, 'SlovÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨ne'),
(177, 'Somalien-(ne)'),
(178, 'Soudanais-(e)'),
(179, 'Sri-Lankais-(e)'),
(180, 'SuÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©dois-(e)'),
(181, 'Suisse'),
(182, 'Surinamien-(ne)'),
(183, 'Swazi-(e)'),
(184, 'Syrien-(ne)'),
(185, 'Tadjik'),
(186, 'TaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯wanais-(e)'),
(187, 'Tanzanien-(ne)'),
(188, 'Tchadien-(ne)'),
(189, 'ThaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¯landais-(e)'),
(190, 'Togolais-(e)'),
(191, 'Tunisien-(ne)'),
(192, 'TurkmÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨ne'),
(193, 'Turc - Turque'),
(194, 'Tuvaluan-(e)'),
(195, 'Ukrainien-(ne)'),
(196, 'Uruguayen-(ne)'),
(197, 'VÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©zuÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©lien-(ne)'),
(198, 'Vietnamien-(ne)'),
(199, 'YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©nite'),
(200, 'Zambien-(ne)'),
(201, 'ZimbabwÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©en-(ne)');

-- --------------------------------------------------------

--
-- Structure de la table `t_role`
--

CREATE TABLE `t_role` (
  `id_role` int(11) NOT NULL,
  `role_name` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- DÃ©chargement des donnÃ©es de la table `t_role`
--

INSERT INTO `t_role` (`id_role`, `role_name`) VALUES
(3, 'user'),
(4, 'admin'),
(5, 'moderateur');

-- --------------------------------------------------------

--
-- Structure de la table `t_specificite`
--

CREATE TABLE `t_specificite` (
  `id_specificite` int(11) NOT NULL,
  `nb_heures_par_semaine` double NOT NULL,
  `nb_jours_vacance_par_an` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Index pour les tables dÃ©chargÃ©es
--

--
-- Index pour la table `t_collaborateur`
--
ALTER TABLE `t_collaborateur`
  ADD PRIMARY KEY (`id_collaborateur`);

--
-- Index pour la table `t_collaborateur_details_collaborateur`
--
ALTER TABLE `t_collaborateur_details_collaborateur`
  ADD PRIMARY KEY (`id_collaborateur_details_collaborateur`),
  ADD KEY `FK_collaborateur` (`FK_collaborateur`,`FK_details_collaborateur`),
  ADD KEY `FK_details_collaborateur` (`FK_details_collaborateur`);

--
-- Index pour la table `t_collaborateur_horaires`
--
ALTER TABLE `t_collaborateur_horaires`
  ADD PRIMARY KEY (`id_collaborateur_horaires`),
  ADD KEY `FK_collaborateur` (`FK_collaborateur`),
  ADD KEY `FK_horaires` (`FK_horaires`);

--
-- Index pour la table `t_collaborateur_identification`
--
ALTER TABLE `t_collaborateur_identification`
  ADD PRIMARY KEY (`id_collaborateur_identification`),
  ADD KEY `FK_collaborateur` (`FK_collaborateur`),
  ADD KEY `FK_identification` (`FK_identification`);

--
-- Index pour la table `t_collaborateur_origine`
--
ALTER TABLE `t_collaborateur_origine`
  ADD PRIMARY KEY (`id_collaborateur_origine`),
  ADD KEY `FK_collaborateur` (`FK_collaborateur`,`FK_origine`),
  ADD KEY `FK_origine` (`FK_origine`);

--
-- Index pour la table `t_collaborateur_specificite`
--
ALTER TABLE `t_collaborateur_specificite`
  ADD PRIMARY KEY (`id_collaborateur_specificite`),
  ADD KEY `FK_collaborateur` (`FK_collaborateur`,`FK_specificite`),
  ADD KEY `FK_specificite` (`FK_specificite`);

--
-- Index pour la table `t_details_collaborateur`
--
ALTER TABLE `t_details_collaborateur`
  ADD PRIMARY KEY (`id_details_collaborateur`);

--
-- Index pour la table `t_horaires`
--
ALTER TABLE `t_horaires`
  ADD PRIMARY KEY (`id_horaires`);

--
-- Index pour la table `t_identification`
--
ALTER TABLE `t_identification`
  ADD PRIMARY KEY (`id_identification`),
  ADD KEY `fk_role` (`fk_role`);

--
-- Index pour la table `t_origine`
--
ALTER TABLE `t_origine`
  ADD PRIMARY KEY (`id_origine`);

--
-- Index pour la table `t_role`
--
ALTER TABLE `t_role`
  ADD PRIMARY KEY (`id_role`);

--
-- Index pour la table `t_specificite`
--
ALTER TABLE `t_specificite`
  ADD PRIMARY KEY (`id_specificite`);

--
-- AUTO_INCREMENT pour les tables dÃ©chargÃ©es
--

--
-- AUTO_INCREMENT pour la table `t_collaborateur`
--
ALTER TABLE `t_collaborateur`
  MODIFY `id_collaborateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `t_collaborateur_details_collaborateur`
--
ALTER TABLE `t_collaborateur_details_collaborateur`
  MODIFY `id_collaborateur_details_collaborateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `t_collaborateur_horaires`
--
ALTER TABLE `t_collaborateur_horaires`
  MODIFY `id_collaborateur_horaires` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `t_collaborateur_identification`
--
ALTER TABLE `t_collaborateur_identification`
  MODIFY `id_collaborateur_identification` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `t_collaborateur_origine`
--
ALTER TABLE `t_collaborateur_origine`
  MODIFY `id_collaborateur_origine` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `t_collaborateur_specificite`
--
ALTER TABLE `t_collaborateur_specificite`
  MODIFY `id_collaborateur_specificite` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_details_collaborateur`
--
ALTER TABLE `t_details_collaborateur`
  MODIFY `id_details_collaborateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `t_horaires`
--
ALTER TABLE `t_horaires`
  MODIFY `id_horaires` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `t_identification`
--
ALTER TABLE `t_identification`
  MODIFY `id_identification` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT pour la table `t_origine`
--
ALTER TABLE `t_origine`
  MODIFY `id_origine` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202;

--
-- AUTO_INCREMENT pour la table `t_role`
--
ALTER TABLE `t_role`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `t_specificite`
--
ALTER TABLE `t_specificite`
  MODIFY `id_specificite` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables dÃ©chargÃ©es
--

--
-- Contraintes pour la table `t_collaborateur_details_collaborateur`
--
ALTER TABLE `t_collaborateur_details_collaborateur`
  ADD CONSTRAINT `t_collaborateur_details_collaborateur_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_details_collaborateur_ibfk_2` FOREIGN KEY (`FK_details_collaborateur`) REFERENCES `t_details_collaborateur` (`id_details_collaborateur`);

--
-- Contraintes pour la table `t_collaborateur_horaires`
--
ALTER TABLE `t_collaborateur_horaires`
  ADD CONSTRAINT `t_collaborateur_horaires_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_horaires_ibfk_2` FOREIGN KEY (`FK_horaires`) REFERENCES `t_horaires` (`id_horaires`);

--
-- Contraintes pour la table `t_collaborateur_identification`
--
ALTER TABLE `t_collaborateur_identification`
  ADD CONSTRAINT `t_collaborateur_identification_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_identification_ibfk_2` FOREIGN KEY (`FK_identification`) REFERENCES `t_identification` (`id_identification`);

--
-- Contraintes pour la table `t_collaborateur_origine`
--
ALTER TABLE `t_collaborateur_origine`
  ADD CONSTRAINT `t_collaborateur_origine_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_origine_ibfk_2` FOREIGN KEY (`FK_origine`) REFERENCES `t_origine` (`id_origine`);

--
-- Contraintes pour la table `t_collaborateur_specificite`
--
ALTER TABLE `t_collaborateur_specificite`
  ADD CONSTRAINT `t_collaborateur_specificite_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_specificite_ibfk_1` FOREIGN KEY (`FK_collaborateur`) REFERENCES `t_collaborateur` (`id_collaborateur`),
  ADD CONSTRAINT `t_collaborateur_specificite_ibfk_2` FOREIGN KEY (`FK_specificite`) REFERENCES `t_specificite` (`id_specificite`);

--
-- Contraintes pour la table `t_identification`
--
ALTER TABLE `t_identification`
  ADD CONSTRAINT `t_identification_ibfk_1` FOREIGN KEY (`fk_role`) REFERENCES `t_role` (`id_role`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;