-- phpMyAdmin SQL Dump
-- version 3.3.7
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2024 年 05 月 29 日 06:07
-- 服务器版本: 8.0.37
-- PHP 版本: 5.2.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `honor_of_kings`
--

-- --------------------------------------------------------

--
-- 表的结构 `abyss_game`
--

CREATE TABLE IF NOT EXISTS `abyss_game` (
  `session` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `champion_team` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `player_mvp` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `password1` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`session`) USING BTREE,
  KEY `champion_team` (`champion_team`) USING BTREE,
  KEY `player_mvp` (`player_mvp`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `abyss_game`
--

INSERT INTO `abyss_game` (`session`, `champion_team`, `player_mvp`, `password1`) VALUES
('2022王者荣耀挑战者杯', '广州TTG', '广州TTG.帆帆', '2022TZZ'),
('2023KPL职业联赛夏季赛', NULL, NULL, '2023KPL'),
('2023王者荣耀挑战者杯', '成都AG超玩会', '成都AG超玩会.长生', '2023TZZ');

--
-- 触发器 `abyss_game`
--
DROP TRIGGER IF EXISTS `abyss_game_insert`;
DELIMITER //
CREATE TRIGGER `abyss_game_insert` BEFORE INSERT ON `abyss_game`
 FOR EACH ROW BEGIN
    DECLARE team_exists INT DEFAULT 0;
    DECLARE player_exists INT DEFAULT 0;
    
    SELECT COUNT(*) INTO team_exists FROM `team` WHERE `team_name` = NEW.`champion_team`;
    SELECT COUNT(*) INTO player_exists FROM `player` WHERE `player_name` = NEW.`player_mvp` AND `team_name` = NEW.`champion_team`;
    
    IF player_exists = 0 AND team_exists = 1 THEN
        INSERT INTO `player` (`player_name`, `team_name`) VALUES (NEW.`player_mvp`, NEW.`champion_team`);
    ELSEIF player_exists = 0 AND team_exists = 0 THEN
        INSERT INTO `team` (`team_name`) VALUES (NEW.`champion_team`);
        INSERT INTO `player` (`player_name`, `team_name`) VALUES (NEW.`player_mvp`, NEW.`champion_team`);
    END IF;
END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- 表的结构 `player`
--

CREATE TABLE IF NOT EXISTS `player` (
  `player_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `player_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `common_role1` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `common_role2` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `team_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`player_name`) USING BTREE,
  KEY `team_name` (`team_name`) USING BTREE,
  KEY `player_name` (`player_name`) USING BTREE,
  KEY `player_ibfk_1` (`common_role1`) USING BTREE,
  KEY `player_ibfk_2` (`common_role2`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `player`
--

INSERT INTO `player` (`player_name`, `player_id`, `common_role1`, `common_role2`, `team_name`) VALUES
('BOA.小伟', 'Lis', '沈梦溪', '王昭君', 'BOA'),
('BOA.小朱', 'Kucao', '达摩', '姬小满', 'BOA'),
('BOA.小瞳', 'NAN', '狄仁杰', '孙尚香', 'BOA'),
('BOA.昊然', 'huahua', '夏侯惇', '杨玉环', 'BOA'),
('BOA.梦溪', 'Czai', '朵莉亚', '张飞', 'BOA'),
('eStarPro.奶茶', 'heart', '明世隐', '张飞', '武汉eStarPro'),
('KSG.一天', 'Fox', '镜', '铠', '苏州KSG'),
('佛山DRG.小度', 'Sxy', '姬小满', '达摩', 'GK'),
('佛山DRG.皖皖', 'Yeyv', '镜', '铠', 'GK'),
('佛山DRG.阿豆', 'MK', '张飞', '太乙真人', 'GK'),
('佛山DRG.青枫', 'Long', '沈梦溪', '王昭君', 'GK'),
('佛山DRG.鹏鹏', 'AnYi', '哪吒', '镜', 'GK'),
('北京WB.乔兮', 'Maom', '公孙离', '敖隐', 'Ts'),
('北京WB.星宇', 'ppz', '张飞', '朵莉亚', 'Ts'),
('北京WB.暖阳', 'Drop', '铠', '裴擒虎', 'Ts'),
('北京WB.梓墨', 'ppxia', '达摩', '姬小满', 'Ts'),
('北京WB.花卷', 'silverzhi', '弈星', '不知火舞', 'Ts'),
('广州TTG.仙语', 'Huan', '项羽', '花木兰', '广州TTG'),
('广州TTG.小爱', 'ZYJ', '孙悟空', '镜', '广州TTG'),
('广州TTG.帆帆', 'Jelly', '张飞', '鲁班大师', '广州TTG'),
('广州TTG.清清', 'iron', '姬小满', '亚连', '广州TTG'),
('广州TTG.雨空', 'SuperRich', '孙尚香', '狄仁杰', '广州TTG'),
('成都AG超玩会.Cat', 'YiHua', '孙尚香', '黄忠', '成都AG超玩会'),
('成都AG超玩会.一诺', 'SanS', '敖隐', '孙尚香', '成都AG超玩会'),
('成都AG超玩会.轩染', 'DongX', '姬小满', '曹操', '成都AG超玩会'),
('成都AG超玩会.钟意', 'D', '夏侯惇', '杨玉环', '成都AG超玩会'),
('成都AG超玩会.长生', '487', '王昭君', '沈梦溪', '成都AG超玩会'),
('武汉eStarPro.清融', 'XingChen', '沈梦溪', '王昭君', '武汉eStarPro'),
('武汉eStarPro.绝意', 'shadow', '公孙离', '孙尚香', '武汉eStarPro'),
('武汉eStarPro.花海', 'Ymm', '杨玉环', '铠', '武汉eStarPro'),
('武汉eStarPro.黎明', 'xawm', '沈梦溪', '弈星', '武汉eStarPro'),
('苏州KSG.久酷', 'Alex', '牛魔', '张飞', '苏州KSG'),
('苏州KSG.今屿', 'QingQ', '杨玉环', '夏侯惇', '苏州KSG'),
('苏州KSG.小玖', 'lion', '公孙离', '孙尚香', '苏州KSG'),
('苏州KSG.轻语', 'dis', '狂铁', '达摩', '苏州KSG'),
('重庆狼队.小暄', 'AK', '庄周', '苏烈', 'QGhappy'),
('重庆狼队.小胖', 'Yue', '夏侯惇', '兰陵王', 'QGhappy'),
('重庆狼队.明崽', '18', '王昭君', '海月', 'QGhappy'),
('重庆狼队.道崽', 'JiaXin', '戈娅', '狄仁杰', 'QGhappy'),
('重庆狼队.郁上', 'Huiyi', '夏侯惇', '赵怀真', 'QGhappy'),
('长沙TES.A乐乐', 'Libao', '张飞', '朵莉亚', '长沙TES.A'),
('长沙TES.A幕色', 'ZiBi', '弈星', '沈梦溪', '长沙TES.A'),
('长沙TES.A蓝桉', 'Xen', '公孙离', '戈娅', '长沙TES.A'),
('长沙TES.A迷神', 'YinL', '镜', '孙悟空', '长沙TES.A'),
('长沙TES.A雨辰', 'Tx', '达摩', '夏洛特', '长沙TES.A');

--
-- 触发器 `player`
--
DROP TRIGGER IF EXISTS `check_player_team`;
DELIMITER //
CREATE TRIGGER `check_player_team` BEFORE INSERT ON `player`
 FOR EACH ROW BEGIN
    IF NOT EXISTS (
        SELECT *
        FROM team
        WHERE team_name = NEW.team_name
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'team_name does not exist in team table.';
    END IF;
    IF EXISTS (
        SELECT *
        FROM player
        WHERE player_name = NEW.player_name
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'player_name already exists in player table.';
    END IF;
END
//
DELIMITER ;
DROP TRIGGER IF EXISTS `update_player_in_game`;
DELIMITER //
CREATE TRIGGER `update_player_in_game` AFTER UPDATE ON `player`
 FOR EACH ROW UPDATE abyss_game 
  SET player_mvp = NEW.player_name 
  WHERE player_mvp = OLD.player_name
//
DELIMITER ;
DROP TRIGGER IF EXISTS `delete_player`;
DELIMITER //
CREATE TRIGGER `delete_player` BEFORE DELETE ON `player`
 FOR EACH ROW BEGIN
    DECLARE count INT;
    SELECT COUNT(*) INTO count FROM abyss_game WHERE champion_team = OLD.team_name OR player_mvp = OLD.player_name;
    IF count > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Cannot delete player as there are related records in abyss_game table';
    END IF;
END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- 替换视图以便查看 `player_common_role_definition`
--
CREATE TABLE IF NOT EXISTS `player_common_role_definition` (
`player_name` varchar(255)
,`common_role1` varchar(255)
,`role_def1_1` varchar(255)
,`role_def2_1` varchar(255)
,`common_role2` varchar(255)
,`role_def1_2` varchar(255)
,`role_def2_2` varchar(255)
);
-- --------------------------------------------------------

--
-- 表的结构 `role`
--

CREATE TABLE IF NOT EXISTS `role` (
  `role_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '角色名',
  `camp` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `role_definition1` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `role_definition2` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`role_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `role`
--

INSERT INTO `role` (`role_name`, `camp`, `role_definition1`, `role_definition2`) VALUES
('上官婉儿', '法师', '中路', NULL),
('不知火舞', '法师', '中路', '打野'),
('亚连', '战士', '对抗路', NULL),
('伽罗', '射手', '发育路', NULL),
('公孙离', '射手', '发育路', NULL),
('兰陵王', '刺客', '打野', '辅助'),
('关羽', '战士', '对抗路', NULL),
('后羿', '射手', '发育路', NULL),
('周瑜', '法师', '中路', NULL),
('哪吒', '战士', '对抗路', '辅助'),
('夏侯惇', '战士', '对抗路', NULL),
('夏洛特', '战士', '对抗路', NULL),
('大乔', '坦克', '辅助', NULL),
('太乙真人', '坦克', '辅助', NULL),
('姬小满', '战士', '对抗路', NULL),
('嬴政', '法师', '中路', '辅助'),
('孙尚香', '射手', '发育路', '对抗路'),
('孙悟空', '刺客', '打野', NULL),
('孙策', '战士', '对抗路', NULL),
('孙膑', '坦克', '辅助', NULL),
('安琪拉', '法师', '中路', NULL),
('宫本武藏', '刺客', '打野', NULL),
('干将莫邪', '法师', '中路', '打野'),
('庄周', '坦克', '辅助', '中路'),
('廉颇', '战士', '对抗路', '辅助'),
('弈星', '法师', '中路', '辅助'),
('张飞', '坦克', '辅助', '对抗路'),
('戈娅', '射手', '发育路', NULL),
('敖隐', '射手', '发育路', '中路'),
('明世隐', '坦克', '辅助', NULL),
('暃', '刺客', '打野', '对抗路'),
('曜', '战士', '对抗路', '打野'),
('曹操', '战士', '对抗路', NULL),
('朵莉亚', '战士', '对抗路', '辅助'),
('杨玉环', '法师', '中路', NULL),
('桑启', '坦克', '辅助', NULL),
('橘右京', '刺客', '打野', '对抗路'),
('沈梦溪', '法师', '中路', NULL),
('海月', '法师', '中路', NULL),
('海诺', '战士', '中路', '对抗路'),
('牛魔', '坦克', '对抗路', '辅助'),
('狂铁', '战士', '对抗路', NULL),
('狄仁杰', '射手', '发育路', NULL),
('猪八戒', '战士', '对抗路', NULL),
('王昭君', '法师', '中路', NULL),
('甄姬', '法师', '中路', NULL),
('老夫子', '战士', '对抗路', '打野'),
('花木兰', '战士', '对抗路', NULL),
('苏烈', '战士', '辅助', NULL),
('蔡文姬', '坦克', '辅助', '对抗路'),
('虞姬', '射手', '发育路', NULL),
('裴擒虎', '刺客', '打野', NULL),
('西施', '法师', '中路', '对抗路'),
('赵怀真', '战士', '对抗路', NULL),
('达摩', '战士', '对抗路', '打野'),
('铠', '战士', '对抗路', NULL),
('镜', '刺客', '打野', NULL),
('阿古朵', '坦克', '辅助', NULL),
('露娜', '战士', '打野', NULL),
('项羽', '战士', '对抗路', NULL),
('马可波罗', '射手', '发育路', NULL),
('马超', '战士', '对抗路', NULL),
('鲁班七号', '射手', '发育路', '打野'),
('鲁班大师', '坦克', '对抗路', '辅助'),
('黄忠', '射手', '发育路', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `team`
--

CREATE TABLE IF NOT EXISTS `team` (
  `team_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `coach` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `team_leader` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`team_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `team`
--

INSERT INTO `team` (`team_name`, `coach`, `team_leader`) VALUES
('BOA', 'Chz', 'BOA.小瞳'),
('GK', 'TY', NULL),
('QGhappy', 'Billy', NULL),
('Ts', 'tiger', '北京WB.花卷'),
('广州TTG', 'BH', '广州TTG.清清'),
('成都AG超玩会', 'LZX', '成都AG超玩会.Cat'),
('武汉eStarPro', 'blue', '武汉eStarPro.黎明'),
('苏州KSG', 'Ysir', '苏州KSG.小玖'),
('长沙TES.A', 'XW', NULL);

--
-- 触发器 `team`
--
DROP TRIGGER IF EXISTS `update_team_name_in_game`;
DELIMITER //
CREATE TRIGGER `update_team_name_in_game` AFTER UPDATE ON `team`
 FOR EACH ROW UPDATE abyss_game 
  SET champion_team = NEW.team_name 
  WHERE champion_team = OLD.team_name
//
DELIMITER ;
DROP TRIGGER IF EXISTS `update_team_name_in_player`;
DELIMITER //
CREATE TRIGGER `update_team_name_in_player` AFTER UPDATE ON `team`
 FOR EACH ROW UPDATE player 
  SET team_name = NEW.team_name
  WHERE team_name = OLD.team_name
//
DELIMITER ;
DROP TRIGGER IF EXISTS `del_player_on_delete_team`;
DELIMITER //
CREATE TRIGGER `del_player_on_delete_team` BEFORE DELETE ON `team`
 FOR EACH ROW BEGIN
  DECLARE team_count INT;
  SET team_count = (SELECT COUNT(*) FROM abyss_game WHERE champion_team = OLD.team_name);
  IF team_count = 0 THEN
    DELETE FROM player WHERE team_name = OLD.team_name;
  ELSE
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'team_name already exists in abyss_game table.';
  END IF;
END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- 替换视图以便查看 `team_rescue_assist`
--
CREATE TABLE IF NOT EXISTS `team_rescue_assist` (
`player_name` varchar(255)
,`common_role1` varchar(255)
,`common_role2` varchar(255)
,`team_name` varchar(255)
);
-- --------------------------------------------------------

--
-- 视图结构 `player_common_role_definition`
--
DROP TABLE IF EXISTS `player_common_role_definition`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `player_common_role_definition` AS select `p`.`player_name` AS `player_name`,`p`.`common_role1` AS `common_role1`,`r1`.`role_definition1` AS `role_def1_1`,`r1`.`role_definition2` AS `role_def2_1`,`p`.`common_role2` AS `common_role2`,`r2`.`role_definition1` AS `role_def1_2`,`r2`.`role_definition2` AS `role_def2_2` from ((`player` `p` join `role` `r1` on((`p`.`common_role1` = `r1`.`role_name`))) join `role` `r2` on((`p`.`common_role2` = `r2`.`role_name`))) where ((`r1`.`role_definition1` is not null) and (`r2`.`role_definition1` is not null));

-- --------------------------------------------------------

--
-- 视图结构 `team_rescue_assist`
--
DROP TABLE IF EXISTS `team_rescue_assist`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `team_rescue_assist` AS select `p`.`player_name` AS `player_name`,`p`.`common_role1` AS `common_role1`,`p`.`common_role2` AS `common_role2`,`p`.`team_name` AS `team_name` from ((`player` `p` join `role` `r1` on((`p`.`common_role1` = `r1`.`role_name`))) join `role` `r2` on((`p`.`common_role2` = `r2`.`role_name`))) where (((`r1`.`role_definition1` = '辅助') and (`r2`.`role_definition1` = '对抗路')) or ((`r1`.`role_definition2` = '辅助') and (`r2`.`role_definition1` = '对抗路')) or ((`r1`.`role_definition1` = '辅助') and (`r2`.`role_definition2` = '对抗路')) or ((`r1`.`role_definition2` = '辅助') and (`r2`.`role_definition2` = '对抗路')) or ((`r1`.`role_definition1` = '对抗路') and (`r2`.`role_definition1` = '辅助')) or ((`r1`.`role_definition2` = '对抗路') and (`r2`.`role_definition1` = '辅助')) or ((`r1`.`role_definition1` = '对抗路') and (`r2`.`role_definition2` = '辅助')) or ((`r1`.`role_definition2` = '对抗路') and (`r2`.`role_definition2` = '辅助')));

--
-- 限制导出的表
--

--
-- 限制表 `abyss_game`
--
ALTER TABLE `abyss_game`
  ADD CONSTRAINT `champion_team` FOREIGN KEY (`champion_team`) REFERENCES `team` (`team_name`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `player_mvp` FOREIGN KEY (`player_mvp`) REFERENCES `player` (`player_name`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- 限制表 `player`
--
ALTER TABLE `player`
  ADD CONSTRAINT `player_ibfk_1` FOREIGN KEY (`common_role1`) REFERENCES `role` (`role_name`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `player_ibfk_2` FOREIGN KEY (`common_role2`) REFERENCES `role` (`role_name`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `team_name` FOREIGN KEY (`team_name`) REFERENCES `team` (`team_name`) ON DELETE SET NULL ON UPDATE CASCADE;
