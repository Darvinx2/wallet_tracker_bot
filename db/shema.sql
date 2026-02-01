CREATE TABLE public.farm_wallets (
    id integer NOT NULL,
    farm_id integer NOT NULL,
    chain character varying(12) NOT NULL,
    wallet character varying(255) NOT NULL,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT farm_wallets_chain_check CHECK (((chain)::text = ANY ((ARRAY['solana'::character varying, 'evm'::character varying, 'abstract'::character varying])::text[])))
);

CREATE TABLE public.farms (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    chain character varying(12) NOT NULL,
    total real NOT NULL,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT farms_chain_check CHECK (((chain)::text = ANY ((ARRAY['solana'::character varying, 'evm'::character varying, 'abstract'::character varying])::text[])))
);