/* Detta är ett exempel på substraktion */
CREATE FUNCTION subtract_numbers(a INT, b INT) RETURNS INT AS $$
BEGIN
    RETURN a - b;
END;
$$ LANGUAGE plpgsql;
