/* Detta är ett exempel på multiplikation */
CREATE FUNCTION multiply_numbers(a INT, b INT) RETURNS INT AS $$
BEGIN
    RETURN a * b;
END;
$$ LANGUAGE plpgsql;
