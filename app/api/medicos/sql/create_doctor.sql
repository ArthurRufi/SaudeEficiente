INSERT INTO doctors (
    nome,
    crm_numero,
    crm_uf,
    specialty,
    email,
    phone,
    is_active,
    create_at,
    update_at
)
VALUES (
    :name,
    :crm_numero,
    :crm_uf,
    :specialty,
    :email,
    :phone,
    true,
    NOW(),
    NOW()
)
RETURNING *;