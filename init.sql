/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 正在导出表  aoi.tb_menu 的数据：~23 rows (大约)
DELETE FROM `tb_menu`;
/*!40000 ALTER TABLE `tb_menu` DISABLE KEYS */;
INSERT INTO `tb_menu` (`id`, `parent_id`, `name`, `url`, `icon`, `component`, `type`, `is_active`, `sort`, `create_id`, `create_name`, `create_time`, `updater_id`, `updater_name`, `update_time`, `is_delete`, `require_login`) VALUES
	(1, -1, '根菜单', '/', 'fas bars', '/', 'catalogue', 1, 1, 1, 'admin', '2022-01-14 17:41:44.000000', 1, 'admin', '2022-01-14 17:41:54.000000', 0, 0),
	(2, 1, '视频前台', '/', 'fas globe', '/Index.vue', 'catalogue', 1, 1, 1, 'admin', '2022-01-15 09:12:53.000000', 1, 'admin', '2022-01-15 20:14:34.647521', 0, 0),
	(3, 1, '管理后台', '/backend', 'fas dharmachakra', '/Backend/Index.vue', 'catalogue', 1, 1, 1, 'admin', '2022-01-15 09:45:11.000000', 1, 'admin', '2022-01-15 20:14:04.385799', 0, 0),
	(4, 3, '运营数据', '', 'fas globe', '/Backend/Summary.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 20:13:10.000000', 1, 'admin', '2022-01-15 20:25:12.523077', 0, 0),
	(5, 3, '用户管理', 'user', 'fas user', '/Backend/User.vue', 'router', 1, 100, 1, 'admin', '2022-01-15 20:20:21.113447', 1, 'admin', '2022-01-15 20:20:21.113447', 1, 0),
	(6, 3, '视频管理', '', 'fas video', '/', 'catalogue', 1, 2, 1, 'admin', '2022-01-15 20:23:10.000000', 1, 'admin', '2022-01-15 20:26:06.314073', 0, 0),
	(7, 3, '用户管理', '', 'fas  user', '/', 'catalogue', 1, 3, 1, 'admin', '2022-01-15 20:24:42.000000', 1, 'admin', '2022-01-15 20:30:46.075396', 0, 0),
	(8, 3, '页面管理', '', 'fas leaf', '/', 'catalogue', 1, 4, 1, 'admin', '2022-01-15 20:27:00.385464', 1, 'admin', '2022-01-15 20:27:00.385464', 0, 0),
	(9, 3, '系统管理', '', 'fas car', '/', 'catalogue', 1, 5, 1, 'admin', '2022-01-15 20:27:44.000000', 1, 'admin', '2022-01-15 20:28:44.048437', 0, 0),
	(10, 7, '用户列表', 'user', 'fas list', '/Backend/User.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 20:30:27.418618', 1, 'admin', '2022-01-15 20:30:27.418618', 0, 0),
	(11, 7, '组别列表', 'group', 'fas list', '/Backend/Group.vue', 'router', 1, 2, 1, 'admin', '2022-01-15 20:31:43.696333', 1, 'admin', '2022-01-15 20:31:43.696333', 0, 0),
	(12, 6, '视频列表', 'video', 'fas list', '/Backend/Video.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 20:33:01.215810', 1, 'admin', '2022-01-15 20:33:01.215810', 0, 0),
	(13, 6, '分类列表', 'category', 'fas list', '/Backend/Category.vue', 'router', 1, 2, 1, 'admin', '2022-01-15 20:33:53.744056', 1, 'admin', '2022-01-15 20:33:53.744056', 0, 0),
	(14, 6, '标签列表', 'tag', 'fas list', '/Backend/Tag.vue', 'router', 1, 3, 1, 'admin', '2022-01-15 20:34:24.433932', 1, 'admin', '2022-01-15 20:34:24.433932', 0, 0),
	(15, 6, '标签列表', 'comment', 'fas list', '/Backend/Comment.vue', 'router', 1, 4, 1, 'admin', '2022-01-15 20:34:55.911908', 1, 'admin', '2022-01-15 20:34:55.911908', 0, 0),
	(16, 8, '菜单管理', 'menu', 'fas list', '/Backend/Menu.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 20:36:13.943315', 1, 'admin', '2022-01-15 20:36:13.943315', 0, 0),
	(17, 9, '常量配置', 'config', 'fas list', '/Backend/Config.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 20:36:50.641712', 1, 'admin', '2022-01-15 20:36:50.641712', 0, 0),
	(18, 2, '主页', '', 'fas home', '/Home/Index.vue', 'router', 1, 1, 1, 'admin', '2022-01-15 21:13:36.570758', 1, 'admin', '2022-01-15 21:13:36.570758', 0, 0),
	(19, 2, '分类', 'category', 'fas list', '/Home/Category.vue', 'router', 1, 2, 1, 'admin', '2022-01-15 21:17:06.000000', 1, 'admin', '2022-01-15 21:18:24.298719', 0, 0),
	(20, 2, '会员', 'member', 'fas list', '/Home/Member.vue', 'router', 1, 3, 1, 'admin', '2022-01-15 21:19:41.000000', 1, 'admin', '2022-01-15 21:19:54.917914', 0, 0),
	(21, 2, '关于', 'about', 'fas  list', '/Home/About.vue', 'router', 1, 4, 1, 'admin', '2022-01-15 21:22:03.473734', 1, 'admin', '2022-01-15 21:22:03.473734', 0, 0),
	(22, 2, '我的', 'personal', 'fas list', '/Home/Personal.vue', 'router', 1, 5, 1, 'admin', '2022-01-15 21:23:41.220305', 1, 'admin', '2022-01-15 21:23:41.220305', 0, 0),
	(23, 2, '视频详情', 'details', 'fas list', '/Home/Details.vue', 'router', 1, 6, 1, 'admin', '2022-01-15 21:24:59.524511', 1, 'admin', '2022-01-15 21:24:59.524511', 0, 0);
/*!40000 ALTER TABLE `tb_menu` ENABLE KEYS */;