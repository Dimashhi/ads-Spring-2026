CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;
CREATE OR REPLACE PROCEDURE delete_contact(p_identifier VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts 
    WHERE name = p_identifier OR phone = p_identifier;
END;
$$;
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[],
    OUT p_invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    current_name VARCHAR;
    current_phone VARCHAR;
BEGIN
    p_invalid_data := '{}';
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        current_name := p_names[i];
        current_phone := p_phones[i];

        IF current_phone ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = current_name) THEN
                UPDATE contacts SET phone = current_phone WHERE name = current_name;
            ELSE
                INSERT INTO contacts(name, phone) VALUES(current_name, current_phone);
            END IF;
        ELSE
            p_invalid_data := array_append(p_invalid_data, current_name || ':' || current_phone);
        END IF;
    END LOOP;
END;
$$;