-- Count heart disease cases
SELECT target, COUNT(*)
FROM dataset
GROUP BY target;

-- Average cholesterol
SELECT AVG(cholesterol)
FROM dataset;

-- Age distribution
SELECT age, COUNT(*)
FROM dataset
GROUP BY age;

-- Chest pain types
SELECT cp, COUNT(*)
FROM dataset
GROUP BY cp;
