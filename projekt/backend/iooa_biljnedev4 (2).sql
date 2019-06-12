-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 12, 2019 at 07:26 AM
-- Server version: 5.5.62-0+deb8u1
-- PHP Version: 5.6.40-0+deb8u2

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `iooa_biljnedev4`
--


--
-- Dumping data for table `biljnevrsteapp_biljnavrsta`
--

INSERT INTO `biljnevrsteapp_biljnavrsta` (`ID_biljne_vrste`, `hrvatski_naziv_vrste`, `latinski_naziv`, `sinonim_vrste`, `opis_vrste`, `ID_roda_id`, `ID_sistematicara_id`) VALUES
(2, 'Divlja mrkva', 'Daucus carota', 'Sinonim', 'Divlji oblik mrkve (Daucus carota L. ssp. carota) ima vretenast, bijel i žilav korijen iz kojeg izbija grubo dlakava do 1 metar visoka i razgranjena stabljika. Korijen je najbolji za jelo u prvoj godini, u drugoj godini, kad izraste stabljika, korijen postaje drvenast.', 1, 1),
(3, 'Bijeli sljez', 'Althea officinalis', 'Pitomi sljez', 'Visegodisnja biljka, visoka do 2 m, jakog, mesnatog, racvastog korijena. Meso korijena je bijelo, slatkastog okusa i sadrzi sluz. Listovi su srcasti, krupni, na dugim peteljkama, obrasli gustim dlacicama. Bijeli cvjetovi sastavljeni su od pet latica.', 2, 1),
(4, 'Pitomi bosiljak', 'Ocimum basilicum', 'Bosilj, bazilika, bosiljak sarmaš, krupan bosiljak, bažulek', 'Bosiljak je jednogodisnja biljka koja moze doseci visinu od 80 cm. Stabljika je uspravna, a listovi jajasti s ostrim vrhom. Velicina se listova povecava od vrha stabljike prema njezinom podnozju. Cvjetovi bosiljka su sitni i bijele boje.', 3, 1),
(5, 'Kadulja', 'Salvia officinalis', 'Ljekovita kadulja, žalfija, šalvija', 'Kadulja je visegodisnja biljka, racvastog, drvenastog korijena. Vrlo je otporna na susu. Mladi izdanci su svijetlozeleni do ljubicasti, prekriveni rjedjim ili guscim dlacicama sivobijele boje. Listovi su svijetli, s obje strane obrasli dlacicama. Cvat ja klasast, sastoji se od 2-8 cvjetova, plave, ruzicaste ili bijele boje, vrlo ugodna mirisa koji privlaci pcele.', 4, 1),
(6, 'Prava kamilica', 'Matricaria chamomilla', 'titrica, kamomila, zdravis, bijeli margic', 'Kamilica je jednogodisnja, samonikla biljka rasirena u cijelom svijetu. Stabljika moze biti uspravna ili povijena, visoka od 5–100 cm, sto ovisi o razli?itim ciniocima (tlu, sklopu). Listovi su sjedeci, dvostruko do trostruko perasto razdijeljeni, uski, svijetlozelene boje i bez dlacica. Cvat je sastavljen od jezicastih, bijelih cvjetova koji su poredani oko supljeg cvjetista i cjevastih zutih cvjetova. Plod je sivobijela roska duga 1 do 1,5mm.', 6, 1),
(7, 'Metvica', 'Mentha sp.', 'Menta, Nana', 'Metvicu karakterizira ugodan miris mentola, a jedna je od najvažnijih ljekovitih biljaka za proizvodnju eteri?nog ulja, lijekova i cajeva. Razmnozavanje se vrsi pomocu vrijeza. Ovisno o uvjetima u kojima raste, stabljika moze izrasti od 20-130 cm te je razgranata i grmolika.', 5, 1);

--
-- Dumping data for table `biljnevrsteapp_biljnavrsta_slika`
--

INSERT INTO `biljnevrsteapp_biljnavrsta_slika` (`id`, `biljnavrsta_id`, `slika_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 3, 3),
(4, 3, 4),
(5, 3, 5),
(6, 5, 6),
(7, 5, 7),
(8, 6, 8),
(9, 7, 9);

--
-- Dumping data for table `biljnevrsteapp_biljnavrsta_uporabni_dio`
--

INSERT INTO `biljnevrsteapp_biljnavrsta_uporabni_dio` (`id`, `biljnavrsta_id`, `uporabnidio_id`) VALUES
(5, 2, 1),
(3, 2, 2),
(4, 3, 2),
(10, 3, 5),
(11, 3, 7),
(12, 4, 2),
(13, 5, 2),
(14, 5, 7),
(15, 6, 4),
(16, 7, 4);

--
-- Dumping data for table `biljnevrsteapp_podvrsta`
--

INSERT INTO `biljnevrsteapp_podvrsta` (`ID_podvrste`, `naziv_podvrste`, `ID_bilje_vrste_id`) VALUES
(2, 'azoricus', 2),
(3, 'boissieri', 2),
(8, 'spicata', 7),
(9, 'piperita', 7),
(10, 'cannabina', 3),
(11, 'pratensis', 5),
(12, 'nemorosa ', 5),
(13, 'minimum', 4),
(14, 'tenuiflorum', 4),
(15, 'discoidea', 6),
(16, 'nobile', 6);

--
-- Dumping data for table `biljnevrsteapp_porodica`
--

INSERT INTO `biljnevrsteapp_porodica` (`ID_porodice`, `hrvatski_naziv_porodice`, `latisnki_naziv_porodice`) VALUES
(1, 'stitarke', 'Apiaceae'),
(2, 'usnace', 'Lamiaceae'),
(3, 'glavocike', 'Asteraceae'),
(4, 'sljezovke', 'Malvaceae');

--
-- Dumping data for table `biljnevrsteapp_rod`
--

INSERT INTO `biljnevrsteapp_rod` (`ID_roda`, `naziv_roda`, `ID_porodice_id`) VALUES
(1, 'Daucus', 1),
(2, 'Althaea', 4),
(3, 'Ocimum', 2),
(4, 'Salviae', 2),
(5, 'Mentha', 2),
(6, 'Matricaria', 3);

--
-- Dumping data for table `biljnevrsteapp_sistematicar`
--

INSERT INTO `biljnevrsteapp_sistematicar` (`ID_sistematicara`, `naziv_sistematicara`) VALUES
(1, 'L.'),
(2, 'R.');

--
-- Dumping data for table `biljnevrsteapp_slika`
--

INSERT INTO `biljnevrsteapp_slika` (`ID_Slike`, `naziv_slike`, `opis_slike`, `ID_uporabni_dio_id`) VALUES
(1, 'mrkva1.jpg', 'mrkva korijen', 1),
(2, 'mrkva2_MBgxlOG.jpg', 'mrkva list', 2),
(3, 'bijeli-sljez1_KOm0OIt.jpg', 'bijeli sljez list', 2),
(4, 'bijeli-sljez2_d8HRFKP.jpg', 'bijeli sljez korijen', 1),
(5, 'bijeli-sljez3_gbed48I.jpg', 'bijeli sljez cvijet', 7),
(6, 'kadulja1.jpg', 'kadulja list', 2),
(7, 'kadulja2.jpg', 'kadulja cvijet', 7),
(8, 'kamilica1.jpg', 'kamilica', 4),
(9, 'menta1.jpg', 'menta', 4);

--
-- Dumping data for table `biljnevrsteapp_uporabnidio`
--

INSERT INTO `biljnevrsteapp_uporabnidio` (`ID_Uporabni_Dio`, `naziv`) VALUES
(1, 'Zadebljali korijen'),
(2, 'Mladi listovi'),
(4, 'Herba'),
(5, 'Korijen'),
(6, 'Stabiljka'),
(7, 'Cvijet'),
(8, '-');

--
-- Dumping data for table `biljnevrsteapp_varijet`
--

INSERT INTO `biljnevrsteapp_varijet` (`ID_varijeta`, `naziv_varijeta`, `ID_podvrste_id`) VALUES
(2, 'v', 2),
(3, '222', 2),
(4, 'š', 2),
(5, '11', 2),
(6, 'h.', 2);

SET FOREIGN_KEY_CHECKS=1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
