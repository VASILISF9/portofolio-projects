-- i use data downloaded by the link down below. The data cleaning process involves handling missing values, removing duplicates, correcting data types, detecting outliers, and standardizing data
-- Additionaly, I did an EDA  to show some insights about layoffs per years, country, company and found worst economy year 


-- https://www.kaggle.com/datasets/swaptr/layoffs-2022


-- exploratory data analysis 

SELECT *
FROM layoffs_staging2
WHERE percentage_laid_off = 1
ORDER BY funds_raised DESC;

-- companies that fired most people 

SELECT company, SUM(total_laid_off)
FROM layoffs_staging2
GROUP BY company
ORDER BY 2 DESC ;

-- see the time space that our data is 


SELECT MIN(`date`), MAX(`date`)
FROM layoffs_staging2;

-- idustry that lost more employyes 

SELECT industry, SUM(total_laid_off)
FROM layoffs_staging2
GROUP BY industry
ORDER BY 2 DESC ;

-- country with most laid offs 


SELECT country, SUM(total_laid_off)
FROM layoffs_staging2
GROUP BY country 
ORDER BY 2 DESC ;

-- found the worst year for employees  


SELECT YEAR(`date`), SUM(total_laid_off)
FROM layoffs_staging2
GROUP BY YEAR(`date`) 
ORDER BY 2 DESC ;


SELECT SUBSTRING(`date`,1,7) AS `MONTH`, SUM(total_laid_off) 
FROM layoffs_staging2
WHERE SUBSTRING(`date`,1,7) IS NOT NULL 
GROUP BY `MONTH`
ORDER BY 1 ASC; 

-- progression of laid off by month 


WITH rolling_total AS 
(
SELECT SUBSTRING(`date`,1,7) AS `MONTH`, SUM(total_laid_off) 
FROM layoffs_staging2
WHERE SUBSTRING(`date`,1,7) IS NOT NULL 
GROUP BY `MONTH`
ORDER BY 1 ASC
)
SELECT `MONTH`, 
SUM(total_laid_off),
SUM(total_laid_off) OVER(ORDER BY `MONTH`) AS rolling_total 
FROM rolling_total;

-- rank year with most laid offs 


SELECT company, YEAR(`date`), SUM(total_laid_off)
FROM layoffs_staging2
GROUP BY company, YEAR(`date`)
ORDER BY 3 DESC 

