CREATE INDEX IF NOT EXISTS p_vis_id ON Posts(visibility, id DESC);
CREATE INDEX IF NOT EXISTS p_vis_uid ON Posts(user_id, visibility);

CREATE INDEX IF NOT EXISTS l_likes ON Likes(post_id);

CREATE INDEX IF NOT EXISTS f_friend ON Friends(user_id, friend_id);

CREATE INDEX IF NOT EXISTS t_tag ON Tags(post_id, tag);
CREATE INDEX IF NOT EXISTS cat_post ON PostCategories(post_id, category, choice);

DELETE FROM Categories;

INSERT INTO Categories (category, choice) 
VALUES ("Sömntyp", "(annan)");
INSERT INTO Categories (category, choice) 
VALUES ("Sömntyp", "huvudsömn");
INSERT INTO Categories (category, choice) 
VALUES ("Sömntyp", "tupplur");
INSERT INTO Categories (category, choice) 
VALUES ("Sömntyp", "fantasi");
INSERT INTO Categories (category, choice) 
VALUES ("Sömntyp", "vila");