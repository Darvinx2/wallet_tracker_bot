CREATE TABLE farms (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    chain VARCHAR(12) NOT NULL CHECK (chain IN ('solana', 'evm', 'abstract')),
    total REAL NOT NULL DEFAULT 0,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE farm_wallets (
    id SERIAL PRIMARY KEY,
    farm_id INTEGER NOT NULL REFERENCES farms(id) ON DELETE CASCADE,
    chain VARCHAR(12) NOT NULL CHECK (chain IN ('solana', 'evm', 'abstract')),
    wallet VARCHAR(255) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);