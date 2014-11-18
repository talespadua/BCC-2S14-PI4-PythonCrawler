--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.5
-- Dumped by pg_dump version 9.3.5
-- Started on 2014-11-18 17:38:59

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 188 (class 3079 OID 11750)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2058 (class 0 OID 0)
-- Dependencies: 188
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 16422)
-- Name: Actors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Actors" (
    "ID" integer NOT NULL,
    "Name" text NOT NULL,
    "Country" text
);


ALTER TABLE public."Actors" OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 16420)
-- Name: Actors_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Actors_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actors_ID_seq" OWNER TO postgres;

--
-- TOC entry 2059 (class 0 OID 0)
-- Dependencies: 172
-- Name: Actors_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Actors_ID_seq" OWNED BY "Actors"."ID";


--
-- TOC entry 183 (class 1259 OID 16503)
-- Name: Countries; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Countries" (
    id integer NOT NULL,
    "Name" text
);


ALTER TABLE public."Countries" OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 16501)
-- Name: Countries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Countries_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Countries_id_seq" OWNER TO postgres;

--
-- TOC entry 2060 (class 0 OID 0)
-- Dependencies: 182
-- Name: Countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Countries_id_seq" OWNED BY "Countries".id;


--
-- TOC entry 175 (class 1259 OID 16433)
-- Name: Directors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Directors" (
    "ID" integer NOT NULL,
    "Name" integer NOT NULL,
    "Country" text
);


ALTER TABLE public."Directors" OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16431)
-- Name: Directors_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Directors_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Directors_ID_seq" OWNER TO postgres;

--
-- TOC entry 2061 (class 0 OID 0)
-- Dependencies: 174
-- Name: Directors_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Directors_ID_seq" OWNED BY "Directors"."ID";


--
-- TOC entry 177 (class 1259 OID 16446)
-- Name: Keywords; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Keywords" (
    "Id" integer NOT NULL,
    "Word" text
);


ALTER TABLE public."Keywords" OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 16444)
-- Name: Keywords_Id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Keywords_Id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Keywords_Id_seq" OWNER TO postgres;

--
-- TOC entry 2062 (class 0 OID 0)
-- Dependencies: 176
-- Name: Keywords_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Keywords_Id_seq" OWNED BY "Keywords"."Id";


--
-- TOC entry 185 (class 1259 OID 16515)
-- Name: Movie_Keywords; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Movie_Keywords" (
    id integer NOT NULL,
    id_movie integer,
    id_keywork integer
);


ALTER TABLE public."Movie_Keywords" OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 16513)
-- Name: Movie_Keywords_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Movie_Keywords_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_Keywords_id_seq" OWNER TO postgres;

--
-- TOC entry 2063 (class 0 OID 0)
-- Dependencies: 184
-- Name: Movie_Keywords_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Movie_Keywords_id_seq" OWNED BY "Movie_Keywords".id;


--
-- TOC entry 187 (class 1259 OID 16521)
-- Name: Movie_countries; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Movie_countries" (
    id integer NOT NULL,
    id_movie integer,
    id_country integer
);


ALTER TABLE public."Movie_countries" OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 16519)
-- Name: Movie_countries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Movie_countries_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_countries_id_seq" OWNER TO postgres;

--
-- TOC entry 2064 (class 0 OID 0)
-- Dependencies: 186
-- Name: Movie_countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Movie_countries_id_seq" OWNED BY "Movie_countries".id;


--
-- TOC entry 178 (class 1259 OID 16456)
-- Name: Movies_Actors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Movies_Actors" (
    id integer NOT NULL,
    id_movie integer NOT NULL,
    id_actor integer NOT NULL
);


ALTER TABLE public."Movies_Actors" OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 16459)
-- Name: Movies_Actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Movies_Actors_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movies_Actors_id_seq" OWNER TO postgres;

--
-- TOC entry 2065 (class 0 OID 0)
-- Dependencies: 179
-- Name: Movies_Actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Movies_Actors_id_seq" OWNED BY "Movies_Actors".id;


--
-- TOC entry 181 (class 1259 OID 16481)
-- Name: Movies_Directors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Movies_Directors" (
    id integer NOT NULL,
    id_movie integer,
    id_director integer
);


ALTER TABLE public."Movies_Directors" OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 16479)
-- Name: Movies_Directors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Movies_Directors_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movies_Directors_id_seq" OWNER TO postgres;

--
-- TOC entry 2066 (class 0 OID 0)
-- Dependencies: 180
-- Name: Movies_Directors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Movies_Directors_id_seq" OWNED BY "Movies_Directors".id;


--
-- TOC entry 170 (class 1259 OID 16394)
-- Name: movies; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE movies (
    nome text,
    ano integer,
    id integer NOT NULL
);


ALTER TABLE public.movies OWNER TO postgres;

--
-- TOC entry 171 (class 1259 OID 16400)
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE movies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO postgres;

--
-- TOC entry 2067 (class 0 OID 0)
-- Dependencies: 171
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE movies_id_seq OWNED BY movies.id;


--
-- TOC entry 1877 (class 2604 OID 16425)
-- Name: ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Actors" ALTER COLUMN "ID" SET DEFAULT nextval('"Actors_ID_seq"'::regclass);


--
-- TOC entry 1882 (class 2604 OID 16506)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Countries" ALTER COLUMN id SET DEFAULT nextval('"Countries_id_seq"'::regclass);


--
-- TOC entry 1878 (class 2604 OID 16436)
-- Name: ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Directors" ALTER COLUMN "ID" SET DEFAULT nextval('"Directors_ID_seq"'::regclass);


--
-- TOC entry 1879 (class 2604 OID 16449)
-- Name: Id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Keywords" ALTER COLUMN "Id" SET DEFAULT nextval('"Keywords_Id_seq"'::regclass);


--
-- TOC entry 1883 (class 2604 OID 16518)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_Keywords" ALTER COLUMN id SET DEFAULT nextval('"Movie_Keywords_id_seq"'::regclass);


--
-- TOC entry 1884 (class 2604 OID 16524)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_countries" ALTER COLUMN id SET DEFAULT nextval('"Movie_countries_id_seq"'::regclass);


--
-- TOC entry 1880 (class 2604 OID 16461)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Actors" ALTER COLUMN id SET DEFAULT nextval('"Movies_Actors_id_seq"'::regclass);


--
-- TOC entry 1881 (class 2604 OID 16484)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Directors" ALTER COLUMN id SET DEFAULT nextval('"Movies_Directors_id_seq"'::regclass);


--
-- TOC entry 1876 (class 2604 OID 16402)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY movies ALTER COLUMN id SET DEFAULT nextval('movies_id_seq'::regclass);


--
-- TOC entry 2036 (class 0 OID 16422)
-- Dependencies: 173
-- Data for Name: Actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Actors" ("ID", "Name", "Country") FROM stdin;
\.


--
-- TOC entry 2068 (class 0 OID 0)
-- Dependencies: 172
-- Name: Actors_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Actors_ID_seq"', 1, false);


--
-- TOC entry 2046 (class 0 OID 16503)
-- Dependencies: 183
-- Data for Name: Countries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Countries" (id, "Name") FROM stdin;
\.


--
-- TOC entry 2069 (class 0 OID 0)
-- Dependencies: 182
-- Name: Countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Countries_id_seq"', 1, false);


--
-- TOC entry 2038 (class 0 OID 16433)
-- Dependencies: 175
-- Data for Name: Directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Directors" ("ID", "Name", "Country") FROM stdin;
\.


--
-- TOC entry 2070 (class 0 OID 0)
-- Dependencies: 174
-- Name: Directors_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Directors_ID_seq"', 1, false);


--
-- TOC entry 2040 (class 0 OID 16446)
-- Dependencies: 177
-- Data for Name: Keywords; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Keywords" ("Id", "Word") FROM stdin;
\.


--
-- TOC entry 2071 (class 0 OID 0)
-- Dependencies: 176
-- Name: Keywords_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Keywords_Id_seq"', 1, false);


--
-- TOC entry 2048 (class 0 OID 16515)
-- Dependencies: 185
-- Data for Name: Movie_Keywords; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Movie_Keywords" (id, id_movie, id_keywork) FROM stdin;
\.


--
-- TOC entry 2072 (class 0 OID 0)
-- Dependencies: 184
-- Name: Movie_Keywords_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Movie_Keywords_id_seq"', 1, false);


--
-- TOC entry 2050 (class 0 OID 16521)
-- Dependencies: 187
-- Data for Name: Movie_countries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Movie_countries" (id, id_movie, id_country) FROM stdin;
\.


--
-- TOC entry 2073 (class 0 OID 0)
-- Dependencies: 186
-- Name: Movie_countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Movie_countries_id_seq"', 1, false);


--
-- TOC entry 2041 (class 0 OID 16456)
-- Dependencies: 178
-- Data for Name: Movies_Actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Movies_Actors" (id, id_movie, id_actor) FROM stdin;
\.


--
-- TOC entry 2074 (class 0 OID 0)
-- Dependencies: 179
-- Name: Movies_Actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Movies_Actors_id_seq"', 1, false);


--
-- TOC entry 2044 (class 0 OID 16481)
-- Dependencies: 181
-- Data for Name: Movies_Directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Movies_Directors" (id, id_movie, id_director) FROM stdin;
\.


--
-- TOC entry 2075 (class 0 OID 0)
-- Dependencies: 180
-- Name: Movies_Directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Movies_Directors_id_seq"', 1, false);


--
-- TOC entry 2033 (class 0 OID 16394)
-- Dependencies: 170
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY movies (nome, ano, id) FROM stdin;
\.


--
-- TOC entry 2076 (class 0 OID 0)
-- Dependencies: 171
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('movies_id_seq', 1, false);


--
-- TOC entry 1892 (class 2606 OID 16441)
-- Name: pk_dir_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Directors"
    ADD CONSTRAINT pk_dir_id PRIMARY KEY ("ID");


--
-- TOC entry 1886 (class 2606 OID 16410)
-- Name: pk_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY movies
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- TOC entry 1889 (class 2606 OID 16430)
-- Name: pk_id_actor; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Actors"
    ADD CONSTRAINT pk_id_actor PRIMARY KEY ("ID");


--
-- TOC entry 1907 (class 2606 OID 16512)
-- Name: pk_id_country; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Countries"
    ADD CONSTRAINT pk_id_country PRIMARY KEY (id);


--
-- TOC entry 1900 (class 2606 OID 16466)
-- Name: pk_id_movie_actor; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Movies_Actors"
    ADD CONSTRAINT pk_id_movie_actor PRIMARY KEY (id);


--
-- TOC entry 1905 (class 2606 OID 16486)
-- Name: pk_id_movie_directors; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Movies_Directors"
    ADD CONSTRAINT pk_id_movie_directors PRIMARY KEY (id);


--
-- TOC entry 1917 (class 2606 OID 16526)
-- Name: pk_movie_countries; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Movie_countries"
    ADD CONSTRAINT pk_movie_countries PRIMARY KEY (id);


--
-- TOC entry 1912 (class 2606 OID 16546)
-- Name: pk_movie_keywords; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Movie_Keywords"
    ADD CONSTRAINT pk_movie_keywords PRIMARY KEY (id);


--
-- TOC entry 1895 (class 2606 OID 16454)
-- Name: pk_words; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Keywords"
    ADD CONSTRAINT pk_words PRIMARY KEY ("Id");


--
-- TOC entry 1896 (class 1259 OID 16478)
-- Name: fk_movie_actor_idactor; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_actor_idactor ON "Movies_Actors" USING btree (id_actor);


--
-- TOC entry 1897 (class 1259 OID 16472)
-- Name: fk_movie_actor_idmovie; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_actor_idmovie ON "Movies_Actors" USING btree (id_movie);


--
-- TOC entry 1913 (class 1259 OID 16543)
-- Name: fk_movie_countries_idcountries; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_countries_idcountries ON "Movie_countries" USING btree (id_country);


--
-- TOC entry 1914 (class 1259 OID 16537)
-- Name: fk_movie_countries_idmovies; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_countries_idmovies ON "Movie_countries" USING btree (id_movie);


--
-- TOC entry 1901 (class 1259 OID 16499)
-- Name: fk_movie_director_iddirector; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_director_iddirector ON "Movies_Directors" USING btree (id_director);


--
-- TOC entry 1902 (class 1259 OID 16493)
-- Name: fk_movie_director_idmovie; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fk_movie_director_idmovie ON "Movies_Directors" USING btree (id_movie);


--
-- TOC entry 1908 (class 1259 OID 16563)
-- Name: fki_movie_keywords_id_keywords; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fki_movie_keywords_id_keywords ON "Movie_Keywords" USING btree (id_keywork);


--
-- TOC entry 1909 (class 1259 OID 16557)
-- Name: fki_movie_keywords_idmovie; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fki_movie_keywords_idmovie ON "Movie_Keywords" USING btree (id_movie);


--
-- TOC entry 1898 (class 1259 OID 16487)
-- Name: index_movie_actors; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX index_movie_actors ON "Movies_Actors" USING btree (id);


--
-- TOC entry 1915 (class 1259 OID 16544)
-- Name: index_movie_countries; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX index_movie_countries ON "Movie_countries" USING btree (id);


--
-- TOC entry 1903 (class 1259 OID 16500)
-- Name: index_movie_director; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX index_movie_director ON "Movies_Directors" USING btree (id);


--
-- TOC entry 1910 (class 1259 OID 16564)
-- Name: index_movie_keywords; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX index_movie_keywords ON "Movie_Keywords" USING btree (id);


--
-- TOC entry 1887 (class 1259 OID 16442)
-- Name: indexactor; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX indexactor ON "Actors" USING btree ("ID");


--
-- TOC entry 1890 (class 1259 OID 16443)
-- Name: indexdirector; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX indexdirector ON "Directors" USING btree ("ID");


--
-- TOC entry 1893 (class 1259 OID 16455)
-- Name: indexword; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX indexword ON "Keywords" USING btree ("Id");


--
-- TOC entry 1918 (class 2606 OID 16473)
-- Name: fk_movie_actor_idactor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Actors"
    ADD CONSTRAINT fk_movie_actor_idactor FOREIGN KEY (id_actor) REFERENCES "Actors"("ID");


--
-- TOC entry 1919 (class 2606 OID 16467)
-- Name: fk_movie_actor_idmovie; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Actors"
    ADD CONSTRAINT fk_movie_actor_idmovie FOREIGN KEY (id_movie) REFERENCES movies(id);


--
-- TOC entry 1924 (class 2606 OID 16538)
-- Name: fk_movie_countries_idcountries; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_countries"
    ADD CONSTRAINT fk_movie_countries_idcountries FOREIGN KEY (id_country) REFERENCES "Countries"(id);


--
-- TOC entry 1925 (class 2606 OID 16532)
-- Name: fk_movie_countries_idmovie; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_countries"
    ADD CONSTRAINT fk_movie_countries_idmovie FOREIGN KEY (id_movie) REFERENCES movies(id);


--
-- TOC entry 1921 (class 2606 OID 16494)
-- Name: fk_movie_director_iddirector; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Directors"
    ADD CONSTRAINT fk_movie_director_iddirector FOREIGN KEY (id_director) REFERENCES "Directors"("ID");


--
-- TOC entry 1920 (class 2606 OID 16488)
-- Name: fk_movie_director_idmovie; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movies_Directors"
    ADD CONSTRAINT fk_movie_director_idmovie FOREIGN KEY (id_movie) REFERENCES movies(id);


--
-- TOC entry 1923 (class 2606 OID 16558)
-- Name: fk_movie_keywords_id_keywords; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_Keywords"
    ADD CONSTRAINT fk_movie_keywords_id_keywords FOREIGN KEY (id_keywork) REFERENCES "Keywords"("Id");


--
-- TOC entry 1922 (class 2606 OID 16552)
-- Name: fk_movie_keywords_idmovie; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Movie_Keywords"
    ADD CONSTRAINT fk_movie_keywords_idmovie FOREIGN KEY (id_movie) REFERENCES movies(id);


--
-- TOC entry 2057 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2014-11-18 17:38:59

--
-- PostgreSQL database dump complete
--

