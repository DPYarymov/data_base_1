--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-04-22 14:09:04

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16422)
-- Name: table_1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_1 (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    password character varying(65) NOT NULL
);


ALTER TABLE public.table_1 OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16421)
-- Name: table_1_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.table_1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.table_1_id_seq OWNER TO postgres;

--
-- TOC entry 4850 (class 0 OID 0)
-- Dependencies: 217
-- Name: table_1_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.table_1_id_seq OWNED BY public.table_1.id;


--
-- TOC entry 4695 (class 2604 OID 16425)
-- Name: table_1 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.table_1 ALTER COLUMN id SET DEFAULT nextval('public.table_1_id_seq'::regclass);


--
-- TOC entry 4844 (class 0 OID 16422)
-- Dependencies: 218
-- Data for Name: table_1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_1 (id, first_name, last_name, password) FROM stdin;
\.


--
-- TOC entry 4851 (class 0 OID 0)
-- Dependencies: 217
-- Name: table_1_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.table_1_id_seq', 1, false);


--
-- TOC entry 4697 (class 2606 OID 16427)
-- Name: table_1 table_1_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.table_1
    ADD CONSTRAINT table_1_pkey PRIMARY KEY (id);


-- Completed on 2025-04-22 14:09:04

--
-- PostgreSQL database dump complete
--

