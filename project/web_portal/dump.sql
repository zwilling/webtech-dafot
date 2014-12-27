--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO code_admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO code_admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO code_admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO code_admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO code_admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO code_admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO code_admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO code_admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO code_admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO code_admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO code_admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO code_admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: courses_assignment; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE courses_assignment (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    template_code text,
    verification_code text,
    course_id integer NOT NULL
);


ALTER TABLE public.courses_assignment OWNER TO code_admin;

--
-- Name: courses_assignment_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE courses_assignment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_assignment_id_seq OWNER TO code_admin;

--
-- Name: courses_assignment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE courses_assignment_id_seq OWNED BY courses_assignment.id;


--
-- Name: courses_attendee; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE courses_attendee (
    id integer NOT NULL,
    user_id integer NOT NULL,
    course_id integer NOT NULL
);


ALTER TABLE public.courses_attendee OWNER TO code_admin;

--
-- Name: courses_attendee_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE courses_attendee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_attendee_id_seq OWNER TO code_admin;

--
-- Name: courses_attendee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE courses_attendee_id_seq OWNED BY courses_attendee.id;


--
-- Name: courses_course; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE courses_course (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    organizer_id integer NOT NULL
);


ALTER TABLE public.courses_course OWNER TO code_admin;

--
-- Name: courses_course_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE courses_course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_course_id_seq OWNER TO code_admin;

--
-- Name: courses_course_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE courses_course_id_seq OWNED BY courses_course.id;


--
-- Name: courses_solution; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE courses_solution (
    id integer NOT NULL,
    code text,
    exceptions text,
    grade double precision NOT NULL,
    assignment_id integer NOT NULL
);


ALTER TABLE public.courses_solution OWNER TO code_admin;

--
-- Name: courses_solution_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE courses_solution_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_solution_id_seq OWNER TO code_admin;

--
-- Name: courses_solution_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE courses_solution_id_seq OWNED BY courses_solution.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO code_admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO code_admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO code_admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO code_admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO code_admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO code_admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO code_admin;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO code_admin;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO code_admin;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: registration_registrationprofile; Type: TABLE; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE TABLE registration_registrationprofile (
    id integer NOT NULL,
    user_id integer NOT NULL,
    activation_key character varying(40) NOT NULL
);


ALTER TABLE public.registration_registrationprofile OWNER TO code_admin;

--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: code_admin
--

CREATE SEQUENCE registration_registrationprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.registration_registrationprofile_id_seq OWNER TO code_admin;

--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: code_admin
--

ALTER SEQUENCE registration_registrationprofile_id_seq OWNED BY registration_registrationprofile.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_assignment ALTER COLUMN id SET DEFAULT nextval('courses_assignment_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_attendee ALTER COLUMN id SET DEFAULT nextval('courses_attendee_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_course ALTER COLUMN id SET DEFAULT nextval('courses_course_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_solution ALTER COLUMN id SET DEFAULT nextval('courses_solution_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY registration_registrationprofile ALTER COLUMN id SET DEFAULT nextval('registration_registrationprofile_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add registration profile	8	add_registrationprofile
23	Can change registration profile	8	change_registrationprofile
24	Can delete registration profile	8	delete_registrationprofile
25	Can add course	9	add_course
26	Can change course	9	change_course
27	Can delete course	9	delete_course
28	Can add assignment	10	add_assignment
29	Can change assignment	10	change_assignment
30	Can delete assignment	10	delete_assignment
31	Can add solution	11	add_solution
32	Can change solution	11	change_solution
33	Can delete solution	11	delete_solution
34	Can add attendee	12	add_attendee
35	Can change attendee	12	change_attendee
36	Can delete attendee	12	delete_attendee
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$12000$3IhYBZNmAsfa$vqS9TawjLvAsesizmrX+hm+6PZEeojr7ogEwvuDtU8Q=	2014-12-23 22:39:08.898048+01	f	werttanya			werttanya@mail.ru	f	f	2014-12-23 22:39:08.898048+01
1	pbkdf2_sha256$12000$aWLQXQAZn4Lw$u64peM687OZ2q7GHKnVfJC6f0UkDXJdwW8xDs5U0FIY=	2014-12-23 22:38:16.382319+01	t	admin			dafot.webtech@gmail.com	t	t	2014-12-23 17:23:18.21373+01
4	pbkdf2_sha256$12000$nJoZ2xZxCaOp$1MVEgp/w+Wm8k4tfDKIvGfv3dNJ83CM0+uauviWminQ=	2014-12-26 14:30:58.526473+01	f	user1			user1@test.com	f	f	2014-12-26 14:30:58.526473+01
5	pbkdf2_sha256$12000$IcL5bvioOlnK$wvytjY5NacjNqe15q2p154PiLB+QNfkKA8VFn1+dS8c=	2014-12-26 17:11:45.890682+01	f	user2			user2@test.com	f	f	2014-12-26 17:11:45.890682+01
6	pbkdf2_sha256$12000$2pgbIwmkAUmi$pUZyaxlz/RZ/vZjaRwl82mLqnfXaCS7wUMqA2gDH7Uk=	2014-12-27 16:49:36.214999+01	f	user3	User3	User3	werttanya@yandex.ru	f	t	2014-12-26 17:16:52.319306+01
3	pbkdf2_sha256$12000$0BT4ODgEzGir$E1bJ/zwJzYWTDVLLRP8DSHlUjiF5b1SQ1SM6MElQ10s=	2014-12-27 17:39:38.83124+01	f	werttanya2			werttanya@gmail.com	f	t	2014-12-23 22:46:05.471868+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_user_id_seq', 6, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: courses_assignment; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY courses_assignment (id, name, description, template_code, verification_code, course_id) FROM stdin;
\.


--
-- Name: courses_assignment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('courses_assignment_id_seq', 1, false);


--
-- Data for Name: courses_attendee; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY courses_attendee (id, user_id, course_id) FROM stdin;
\.


--
-- Name: courses_attendee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('courses_attendee_id_seq', 1, false);


--
-- Data for Name: courses_course; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY courses_course (id, name, description, organizer_id) FROM stdin;
1	dive in to python	This course is specifically designed to be a first programming course using the popular Python programming language.  The pace of the course is designed to lead to mastery of each of the topics in the class.  We will use simple data analysis as the programming exercises through the course.    Understanding how to process data is valuable for everyone regardless of your career.  This course might kindle an interest in more advanced programming courses or courses in web design and development or just provide skills when you are faced with a bunch of data that you need to analyze. You can do the programming assignments for the class using a web browser or using your personal computer.   All required software for the course is free. 	6
2	Python language	A computer program is a set of instructions for a computer to follow, just as a recipe is a set of instructions for a chef. Laptops, kitchen appliances, MP3 players, and many other electronic devices all run computer programs. Programs have been written to manipulate sound and video, write poetry, run banking systems, predict the weather, and analyze athletic performance. This course is intended for people who have never seen a computer program. It will give you a better understanding of how computer applications work and teach you how to write your own applications. More importantly, you’ll start to learn computational thinking, which is a fundamental approach to solving real-world problems. Computer programming languages share common fundamental concepts, and this course will introduce you to those concepts using the Python programming language. By the end of this course, you will be able to write your own programs to process data from the web and create interactive text-based games.	3
3	python2	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
4	python3	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
5	python4	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
6	python5	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
7	python2	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
8	python2	This course aims to teach everyone to learn the basics of programming computers using Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course.	3
\.


--
-- Name: courses_course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('courses_course_id_seq', 8, true);


--
-- Data for Name: courses_solution; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY courses_solution (id, code, exceptions, grade, assignment_id) FROM stdin;
\.


--
-- Name: courses_solution_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('courses_solution_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	registration profile	registration	registrationprofile
9	course	courses	course
10	assignment	courses	assignment
11	solution	courses	solution
12	attendee	courses	attendee
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('django_content_type_id_seq', 12, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2014-12-23 17:12:37.263395+01
2	auth	0001_initial	2014-12-23 17:12:38.0916+01
3	admin	0001_initial	2014-12-23 17:12:38.344947+01
4	sessions	0001_initial	2014-12-23 17:12:38.511803+01
5	sites	0001_initial	2014-12-23 21:53:33.759982+01
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('django_migrations_id_seq', 5, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
31m1ly2mg6outme9uu1msx3zxk2p86j4	NDY2ZjE2Y2QyMGMzODQ1ZWRhOWExZTRiZWI5Yjg2NWViNDlhMTBhOTp7fQ==	2015-01-09 17:33:19.055153+01
lxdlcdq4kw9fbkm747jztsg5oilimdqi	ZDVmZmJmYjM2NTcwYTc4NzFlYzNjZDcxOGM1MTY5OGViY2UwMzg1MTp7Il9hdXRoX3VzZXJfaGFzaCI6ImUxMTg5YjU2MmQwZDFlNWU5MmEyZTc1MTJiNzExYzkyMjI0Y2I0MzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjN9	2015-01-10 17:39:38.841969+01
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: registration_registrationprofile; Type: TABLE DATA; Schema: public; Owner: code_admin
--

COPY registration_registrationprofile (id, user_id, activation_key) FROM stdin;
1	2	7368a9afca42503831eb76ccd8c24838da6bc51c
2	3	ALREADY_ACTIVATED
3	4	b69f31bf6b146a4b21fe963226cc4e21f53a5778
4	5	f025f7115bd686beabaf0227aee9c75bf7dde716
5	6	ALREADY_ACTIVATED
\.


--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: code_admin
--

SELECT pg_catalog.setval('registration_registrationprofile_id_seq', 5, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: courses_assignment_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY courses_assignment
    ADD CONSTRAINT courses_assignment_pkey PRIMARY KEY (id);


--
-- Name: courses_attendee_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY courses_attendee
    ADD CONSTRAINT courses_attendee_pkey PRIMARY KEY (id);


--
-- Name: courses_attendee_user_id_course_id_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY courses_attendee
    ADD CONSTRAINT courses_attendee_user_id_course_id_key UNIQUE (user_id, course_id);


--
-- Name: courses_course_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_pkey PRIMARY KEY (id);


--
-- Name: courses_solution_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY courses_solution
    ADD CONSTRAINT courses_solution_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: registration_registrationprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY registration_registrationprofile
    ADD CONSTRAINT registration_registrationprofile_pkey PRIMARY KEY (id);


--
-- Name: registration_registrationprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: code_admin; Tablespace: 
--

ALTER TABLE ONLY registration_registrationprofile
    ADD CONSTRAINT registration_registrationprofile_user_id_key UNIQUE (user_id);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: courses_assignment_course_id; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX courses_assignment_course_id ON courses_assignment USING btree (course_id);


--
-- Name: courses_attendee_course_id; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX courses_attendee_course_id ON courses_attendee USING btree (course_id);


--
-- Name: courses_attendee_user_id; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX courses_attendee_user_id ON courses_attendee USING btree (user_id);


--
-- Name: courses_course_organizer_id; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX courses_course_organizer_id ON courses_course USING btree (organizer_id);


--
-- Name: courses_solution_assignment_id; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX courses_solution_assignment_id ON courses_solution USING btree (assignment_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: code_admin; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_assignment_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_assignment
    ADD CONSTRAINT courses_assignment_course_id_fkey FOREIGN KEY (course_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_attendee_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_attendee
    ADD CONSTRAINT courses_attendee_course_id_fkey FOREIGN KEY (course_id) REFERENCES courses_course(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_attendee_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_attendee
    ADD CONSTRAINT courses_attendee_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_course_organizer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_course
    ADD CONSTRAINT courses_course_organizer_id_fkey FOREIGN KEY (organizer_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: courses_solution_assignment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY courses_solution
    ADD CONSTRAINT courses_solution_assignment_id_fkey FOREIGN KEY (assignment_id) REFERENCES courses_assignment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_registrationprofile_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: code_admin
--

ALTER TABLE ONLY registration_registrationprofile
    ADD CONSTRAINT registration_registrationprofile_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: code_admin
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM code_admin;
GRANT ALL ON SCHEMA public TO code_admin;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- code_adminQL database dump complete
--

