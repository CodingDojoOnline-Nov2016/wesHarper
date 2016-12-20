SELECT * FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;


SELECT users.first_name, users.last_name, 
friends.first_name AS friend_first, 
friends.last_name AS friend_last FROM friend_db.users
	LEFT JOIN friendships ON users.id = friendships.user_id
    LEFT JOIN users AS friends ON friends.id = friendships.friend_id;