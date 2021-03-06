-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema projetoSQL
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projetoSQL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projetoSQL` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `projetoSQL` ;

-- -----------------------------------------------------
-- Table `projetoSQL`.`Disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projetoSQL`.`Disciplina` (
  `nome` VARCHAR(45) NOT NULL,
  `professor` VARCHAR(45) NULL DEFAULT NULL,
  `comentario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`nome`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `projetoSQL`.`Nota`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projetoSQL`.`Nota` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_disciplina` VARCHAR(45) NOT NULL,
  `nota` FLOAT NOT NULL,
  PRIMARY KEY (`nota_id`),
  INDEX `fk_nome_idx` (`disc_nome` ASC) VISIBLE,
  CONSTRAINT `fk_nome`
    FOREIGN KEY (`disc_nome`)
    REFERENCES `projetoSQL`.`Disciplina` (`nome`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;