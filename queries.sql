-- Count total heart disease cases
SELECT HeartDisease, COUNT(*) AS TotalCount
FROM dataset
GROUP BY HeartDisease;

-- See average BMI by HeartDisease status
SELECT HeartDisease, ROUND(AVG(BMI), 2) AS AverageBMI
FROM dataset
GROUP BY HeartDisease;

-- Analyze Smoking and Heart Disease Correlation
SELECT Smoking, HeartDisease, COUNT(*) AS Cases
FROM dataset
GROUP BY Smoking, HeartDisease
ORDER BY Smoking, HeartDisease;

-- Age Category distribution for those with Heart Disease
SELECT AgeCategory, COUNT(*) as CaseCount
FROM dataset
WHERE HeartDisease = 'Yes'
GROUP BY AgeCategory
ORDER BY CaseCount DESC;

-- Health conditions grouping (Diabetic, Stroke, KidneyDisease)
SELECT 
    Diabetic, 
    Stroke, 
    KidneyDisease, 
    COUNT(*) AS PatientCount,
    SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) as HeartDiseaseCases
FROM dataset
GROUP BY Diabetic, Stroke, KidneyDisease
ORDER BY HeartDiseaseCases DESC
LIMIT 10;
