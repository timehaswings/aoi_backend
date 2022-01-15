/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 正在导出表  aoi.tb_menu 的数据：~3 rows (大约)
DELETE FROM `tb_menu`;
/*!40000 ALTER TABLE `tb_menu` DISABLE KEYS */;
INSERT INTO `tb_menu` (`id`, `parent_id`, `name`, `url`, `icon`, `component`, `type`, `is_active`, `sort`, `create_id`, `create_name`, `create_time`, `updater_id`, `updater_name`, `update_time`, `is_delete`) VALUES
	(1, -1, '根菜单', '/', 'fas bars', '/', 'catalogue', 1, 1, 1, 'admin', '2022-01-14 17:41:44.000000', 1, 'admin', '2022-01-14 17:41:54.000000', 0),
	(2, 1, '视频前台', '/', 'fas globe', '/', 'catalogue', 1, 1, 5, 'admin', '2022-01-15 09:12:53.221002', 5, 'admin', '2022-01-15 09:12:53.221002', 0),
	(3, 1, '管理后台', '/', 'fas dharmachakra', '/', 'catalogue', 1, 1, 5, 'admin', '2022-01-15 09:45:11.140004', 5, 'admin', '2022-01-15 09:45:11.141001', 0);