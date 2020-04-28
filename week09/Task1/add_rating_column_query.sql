ALTER TABLE Languages
ADD COLUMN rating INTEGER CHECK(rating > 0 AND rating < 10)