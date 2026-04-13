CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(contact_name VARCHAR, contact_phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT name, phone 
    FROM contacts 
    WHERE name ILIKE '%' || pattern || '%' 
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(contact_name VARCHAR, contact_phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT name, phone 
    FROM contacts 
    ORDER BY name 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;