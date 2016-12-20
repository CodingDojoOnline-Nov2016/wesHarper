SELECT name, percentage, language FROM countries c
	JOIN languages ON c.id = languages.country_id
    WHERE language LIKE "Slovene"
    ORDER BY percentage DESC;

SELECT countries.name, COUNT(cities.id) AS city_num FROM countries
	JOIN cities ON countries.id = cities.country_id
    GROUP BY countries.id
	ORDER BY city_num DESC;

SELECT cities.name, cities.population FROM cities
	WHERE cities.population > 500000 AND country_id = 
		(SELECT id from countries WHERE name = "Mexico");

SELECT countries.name, languages.language, languages.percentage FROM countries
	JOIN languages ON countries.id = languages.country_id
    WHERE languages.percentage > 89
    ORDER BY percentage DESC;
  
SELECT name FROM countries
	WHERE surface_area < 501
    AND population > 100000;

SELECT name FROM countries
	WHERE government_form = "Constitutional Monarchy"
    AND life_expectancy > 75
    AND capital > 200;
  
SELECT countries.name, cities.name, district, cities.population FROM cities
	JOIN countries ON countries.id = cities.country_id
    WHERE countries.name = "Argentina"
    AND district = "Buenos Aires"
    AND cities.population > 500000;
    
SELECT countries.region, COUNT(countries.id) AS num_countries FROM countries
	GROUP BY countries.region
    ORDER BY num_countries DESC;