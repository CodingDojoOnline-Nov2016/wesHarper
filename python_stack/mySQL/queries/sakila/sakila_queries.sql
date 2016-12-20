SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer
	JOIN address ON address.address_id = customer.address_id
    WHERE address.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON category.category_id = film_category.category_id
    WHERE category.name = "Comedy";
    
SELECT film.title, film.description, film.release_year FROM film
	JOIN film_actor ON film_actor.film_id = film.film_id
    JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer
	JOIN address ON address.address_id = customer.address_id
	WHERE customer.store_id = 1 AND address.city_id = 1
	OR customer.store_id = 1 AND address.city_id = 42
	OR customer.store_id = 1 AND address.city_id = 312
	OR customer.store_id = 1 AND address.city_id = 459;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features FROM film
	JOIN film_actor ON film_actor.film_id = film.film_id
    WHERE film.rating = "G" 
		AND film.special_features LIKE "behind the scenes" 
        AND film_actor.actor_id = 15;

SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name FROM actor
	JOIN film_actor ON film_actor.actor_id = actor.actor_id
    JOIN film ON film.film_id = film_actor.film_id
    WHERE film.film_id = 369;
    
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON category.category_id = film_category.category_id
    WHERE category.name = "drama"
		AND film.rental_rate = 2.99;
        
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON category.category_id = film_category.category_id
    JOIN film_actor ON film_actor.film_id = film.film_id
    JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE actor.first_name = "SANDRA"
		AND actor.last_name = "KILMER"
        AND category.name = "action";