INSERT INTO doctors (
    name,
    crm,
    specialty,
    email,
    phone,
    is_active,
    created_at,
    updated_at
)
VALUES (
    :name,
    :crm,
    :specialty,
    :email,
    :phone,
    true,
    NOW(),
    NOW()
)
RETURNING *;