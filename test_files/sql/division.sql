/* Detta är ett exempel på division */
CREATE FUNCTION divide_numbers(a INT, b INT) RETURNS FLOAT AS $$
BEGIN
    RETURN CASE WHEN b <> 0 THEN a::FLOAT / b ELSE NULL END;
END;
$$ LANGUAGE plpgsql;
