"""
Portfolio Streamlit - Shine Quinn Firdaus
Jalankan:  streamlit run app.py
Gambar    : taruh di folder assets/ (lihat panduan di chat)
"""

from __future__ import annotations

import base64
import json
from io import BytesIO
from pathlib import Path

import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(
    page_title="Shine Quinn Firdaus | Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
IMG_EXTS = ("jpg", "jpeg", "png", "webp")

# True  = kotak placeholder "Photo placeholder" tampil jika foto belum ada
# False = kotak kosong disembunyikan (pakai ini saat portfolio sudah dipublikasi)
SHOW_PLACEHOLDERS = True

# ----------------------------------------------------------------------------
# DATA (edit di sini kalau ada update CV)
# ----------------------------------------------------------------------------
PROFILE = {
    "name": "Shine Quinn Firdaus",
    "first_name": "Quinn",
    "headline": "Information Systems graduate who enjoys turning data, research, and ideas into useful solutions.",
    "location": "Surakarta, Indonesia",
    "email": "quinn.shine@gmail.com",
    "linkedin": "https://linkedin.com/in/shineequinn",
    "phone": "+62 812-2693-7306",
    "whatsapp": "6281226937306",  # format internasional tanpa + / spasi / 0 di depan
    "lead": "I turn raw data into dashboards and insights that teams can act on.",
    "about": (
        "Information Systems fresh graduate with hands-on experience in data analysis, "
        "dashboard development, reporting, and operational support. I analyze data with "
        "Power BI, Looker Studio, Python, and Google Colab to find trends, patterns, and "
        "insights people can act on. My foundation in Data "
        "Visualization comes from internships, research, and international programs. "
        "I'm detail-oriented, analytical, and adaptable, with a strong interest in "
        "supporting data-driven operational decisions and process improvement."
    ),
}

QUICK_FACTS = [
    ("Education", "B.Sc. Information Systems, ITS (GPA 3.47 / 4.00)"),
    ("Based in", "Surakarta, Indonesia"),
    ("Languages", "Indonesian (Native), English (High Intermediate)"),
    ("Open to", "Full-time Roles, Internships, and Collaborations"),
]

CORE_TOOLS = ["Python", "SQL", "Power BI", "Looker Studio", "Pandas", "Google Colab"]

TOOLKIT = {
    "Data & Analytics": ["SQL", "Pandas", "Google Colab", "Looker Studio", "Power BI", "Excel", "Google Sheets"],
    "Programming & Development": ["Python", "Basic Java", "Laravel", "Flutter"],
    "Database & Enterprise Systems": [
        "DBeaver",
        "SQL Server Management Studio",
        "Pentaho (Data Warehouse)",
        "SAP S/4HANA",
        "Odoo",
    ],
    "Design & Office": ["Figma", "Canva", "Word", "Excel", "PowerPoint"],
}

# "photos" = nama file TANPA ekstensi, relatif terhadap folder assets/
# contoh: "experience/iprospect-1" -> assets/experience/iprospect-1.jpg (atau .png/.webp)
EXPERIENCE = [
    {
        "role": "Data Analyst Intern",
        "org": "PT. iProspect Merkle Indonesia",
        "place": "Jakarta, Indonesia",
        "date": "Sep 2025 - Dec 2025",
        "bullets": [
            "Built and maintained Looker Studio dashboards to monitor e-commerce performance and deliver periodic reports across client accounts.",
            "Processed, organized, and analyzed e-commerce datasets to support performance monitoring and reporting.",
            "Used Google Colab and Python for data exploration, trend and pattern discovery, and actionable insights from client datasets.",
            "Validated data and analyzed it to find performance gaps and potential anomalies, supporting data-driven recommendations.",
            "Translated findings into clear reports and insights for cross-functional stakeholders.",
        ],
        "tags": ["Looker Studio", "Python", "Google Colab", "E-commerce"],
        "photos": ["experience/iprospect-1", "experience/iprospect-2", "experience/iprospect-3"],
    },
    {
        "role": "Research Exchange Intern (Data Science Laboratory)",
        "org": "Shibaura Institute of Technology",
        "place": "Tokyo, Japan",
        "date": "Mar 2026",
        "bullets": [
            "IOMS Scholarship awardee for the research exchange program at Shibaura Institute of Technology.",
            "Researched data science and text data analysis, applying Gaussian Mixture Models (GMM) and Sentence-BERT (SBERT) to real-world datasets under faculty supervision.",
            "Supported research activities including data preparation, analysis, and interpretation of findings.",
            "Collaborated in an international laboratory, contributing to cross-cultural research practices and academic discussions.",
        ],
        "tags": ["GMM", "SBERT", "Text Analytics"],
        "photos": ["experience/shibaura-1", "experience/shibaura-2", "experience/shibaura-3"],
    },
    {
        "role": "Hospitality for International Student Division Volunteer",
        "org": "ITS Global Engagement",
        "place": "Surabaya, Indonesia",
        "date": "Dec 2023 - Dec 2024",
        "bullets": [
            "Provided hospitality and support services to international students at ITS.",
            "Person in Charge (PIC) of the International Student Campus Tour, Event Division (Spring 2024).",
            "PIC of the Global Unity Fair, PDD Division (Spring 2024) and Event Division (Fall 2024).",
            "Committee, International Staff Mobility (ISM): managed program agendas and served as Master of Ceremonies for the opening event.",
            "Committee, Social Innovation Project x Singapore Institute of Technology (SIP x SIT): coordinated program agendas and supported participating delegates.",
        ],
        "tags": ["Event Management", "Public Speaking"],
        "photos": ["experience/its-ge-1", "experience/its-ge-2", "experience/its-ge-3"],
    },
]

# Link: isi URL di sini. Yang kosong ("") tampil sebagai tombol abu-abu (nonaktif).
# Urutan list = urutan tampil (terbaru di atas).
PROJECTS = [
    {
        "date": "June 2026",
        "title": "Dengue Fever (DBD) Mitigation Dashboard",
        "category": "Data Analytics & Decision Support System",
        "tech": ["Python", "Streamlit", "Decision Tree"],
        "type": "College Final Project",
        "org": "Institut Teknologi Sepuluh Nopember",
        "summary": "A dashboard that shows which handling measures should be prioritized in each region, based on data from X. It uses a decision tree to turn the data into clear decision recommendations.",
        "links": {
            "Project Link": "https://shinequinnfirdaus-tugas-akhir-streamlitapp-0x42os.streamlit.app/",
            "Presentation Link": "https://canva.link/5osauqtxa83cs5y",
        },
        "image": "projects/dbd-dashboard",
    },
    {
        "date": "March 2026",
        "title": "GPBL Student Behavioral Transition Analysis",
        "category": "Data Analytics & Machine Learning",
        "tech": ["Python", "NLP", "TF-IDF", "BERT", "GMM"],
        "type": "Internship Project",
        "org": "Shibaura Institute of Technology",
        "summary": "Compared TF-IDF and BERT embeddings with Gaussian Mixture Models to cluster about 240 daily student reflections and map behavioral transitions in project-based learning.",
        "links": {"Project Link": "https://drive.google.com/file/d/1gHPRIJCR2lcN2oJbHrtDF7_boddV3oh5/view?usp=sharing"},
        "image": "projects/gpbl-analysis",
    },
    {
        "date": "October 2025",
        "title": "Fermentor Monitoring App",
        "category": "Mobile Application & UX Design",
        "tech": ["Flutter", "UI/UX"],
        "type": "Student Research & Innovation Project",
        "org": "Institut Teknologi Sepuluh Nopember",
        "summary": "A mobile app that monitors pH, temperature, humidity, and alcohol content in real time for white glutinous rice fermentation (Brem Sari Gading, Madiun). Published 2026.",
        "links": {
            "Project Link": "https://shinequinnfirdaus.github.io/fermentorapp/",
            "Paper Link": "https://doi.org/10.12962/j26139960.v10i4.9372",
        },
        "image": "projects/fermentor-app",
    },
    {
        "date": "September 2025",
        "title": "E-Commerce Data Dashboard",
        "category": "Data Analytics Dashboard",
        "tech": ["Google Looker Studio", "Data Analysis"],
        "type": "Internship Project",
        "org": "PT iProspect Merkle",
        "summary": "A Looker Studio dashboard for monitoring e-commerce performance and periodic client reporting.",
        "links": {"Project Link": "https://datastudio.google.com/reporting/d4566105-4d15-4056-8e91-fdfd43361c03"},
        "image": "projects/ecommerce-dashboard",
    },
    {
        "date": "December 2024",
        "title": "ITS Park",
        "category": "UX Design",
        "tech": ["Figma"],
        "type": "College Project",
        "org": "Institut Teknologi Sepuluh Nopember",
        "summary": "A UX design for an app that makes parking at ITS easier. It also works as a community lost-and-found, where users can chat to post news about items they lost or found.",
        "links": {
            "Project Link": "https://www.figma.com/design/3BrI340mv7p5SSA4J1fh9P/ITS-Park?t=5jErTI7W4tJZUw0G-1",
            "Project Video": "https://youtu.be/HNAMLyXxmH8?si=m1Q2Nibt9eudorkc",
        },
        "image": "projects/its-park",
    },
    {
        "date": "December 2024",
        "title": "University Admission Dashboard",
        "category": "Data Analytics Dashboard",
        "tech": ["Power BI", "Pentaho"],
        "type": "College Project",
        "org": "Institut Teknologi Sepuluh Nopember",
        "summary": "A dashboard for monitoring students applying to a university, covering test scores, region of origin, parents’ data, and selection status.",
        "links": {"Project Link": "https://drive.google.com/file/d/1V8dYLExzxrj_8-bqkKqM_Pq31hcxZ3Ti/view?usp=sharing"},
        "image": "projects/class-dashboard",
    },
]

EDUCATION = [
    {
        "role": "B.Sc. in Information Systems",
        "org": "Institut Teknologi Sepuluh Nopember (ITS)",
        "place": "Surabaya, Indonesia",
        "date": "2022 - 2026",
        "bullets": ["GPA 3.47 / 4.00"],
        "tags": [],
        "photos": [],  # isi mis. ["education/its-1"] kalau ingin ada foto
    }
]

ORGANIZATION = [
    {
        "role": "Staff, Social Community Department",
        "org": "Badan Eksekutif Mahasiswa (BEM) FTEIC ITS",
        "place": "Surabaya, Indonesia",
        "date": "May 2024 - Feb 2025",
        "bullets": [
            "Led the PDD (Publication, Documentation & Design) Division for the Bakti Electics community service event.",
            "Person in Charge (PIC) of the department's Instagram presence.",
        ],
        "tags": [],
    },
    {
        "role": "Intern Staff, Research and Development",
        "org": "Himpunan Mahasiswa Sistem Informasi ITS",
        "place": "Surabaya, Indonesia",
        "date": "Jul 2023 - Oct 2023",
        "bullets": [
            "Organized PKTI-TD training activities for incoming students.",
            "Evaluated post-training assignments to measure learning outcomes.",
        ],
        "tags": [],
    },
]

GLOBAL_LEARNING = [
    {
        "role": "Study Excursion (Short Program)",
        "org": "Saga University",
        "place": "Saga, Japan",
        "date": "Nov 2024",
        "bullets": [
            "Explored Japanese culture, tourism management, and urban and regional planning through a short study program at Saga University.",
            "Learned the Japanese language during the program.",
            "Learned about community and local culture, including how people in Japan interact and communicate with each other.",
            "Built cross-cultural communication skills by interacting with people from different cultural backgrounds, which helps me collaborate with diverse teams and stakeholders.",
            "Improved public speaking and communication skills through discussions and group activities, which supports presenting findings and ideas clearly to non-technical audiences.",
        ],
        "tags": [],
        "photos": ["experience/saga-1", "experience/saga-2", "experience/saga-3"],
    }
]

CERTIFICATIONS = ["SAP Certified Application Associate - SAP S/4HANA", "Google Analytics 4 (GA4)"]
ACHIEVEMENTS = ["2nd Winner, ISCOM (Information Systems Competition), Smart City Category"]
LANGUAGES = [("Indonesian", "Native"), ("English", "High intermediate")]

NAV = [
    ("home", "Home"),
    ("about", "About"),
    ("tools", "Tools"),
    ("experience", "Experience"),
    ("projects", "Projects"),
    ("education", "Education"),
    ("organization", "Organization"),
    ("global", "Global"),
    ("more", "More"),
    ("contact", "Contact"),
]

# ----------------------------------------------------------------------------
# STYLE  (palet: charcoal #1E1E1C, off-white #F4F4F1, sand #EAE9E3, muted sakura #E3B8C2)
# ----------------------------------------------------------------------------
CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root{
  --ink:#1E1E1C; --muted:#6A6A64; --indigo:#2A2A27; --indigo-soft:#EAE9E3;
  --sakura:#E3B8C2; --sakura-soft:#F6ECEE; --rose:#8C4F5E; --mist:#F4F4F1; --line:#E1E1DA; --card:#FBFBF9;
  --pad:clamp(1.1rem,4vw,4rem);
}
html{scroll-behavior:smooth;}
#MainMenu, footer, header[data-testid="stHeader"]{visibility:hidden;height:0;}
.stApp{background:var(--mist);}
.block-container, [data-testid="stMainBlockContainer"]{
  max-width:100%!important;padding:5.5rem var(--pad) 3rem!important;}

.pf, .pf *{font-family:'Plus Jakarta Sans',system-ui,sans-serif;box-sizing:border-box;}
.pf h1,.pf h2,.pf .serif{font-family:'DM Serif Display',Georgia,serif;font-weight:400;color:var(--ink);margin:0;}
.pf h3{font-weight:700;color:var(--ink);margin:0;line-height:1.3;}
.pf p{color:var(--muted);line-height:1.75;margin:0;}
.pf a{text-decoration:none;}

/* Navbar */
.pf-nav{position:fixed;top:0;left:0;right:0;z-index:999;background:rgba(244,244,241,.9);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--line);}
.pf-nav-inner{padding:.85rem var(--pad);display:flex;align-items:center;justify-content:space-between;gap:1rem;}
.pf-brand{font-family:'DM Serif Display',serif!important;font-size:1.3rem;color:var(--ink);}
.pf-brand small{font-family:'Plus Jakarta Sans',sans-serif!important;font-size:.85rem;color:var(--muted);margin-left:.4rem;}
.pf-links{display:flex;gap:1.3rem;flex-wrap:wrap;justify-content:flex-end;}
.pf-links a{font-size:.86rem;font-weight:500;color:var(--muted);transition:color .15s;}
.pf-links a:hover{color:var(--indigo);}

/* Hero */
.pf-hero{display:grid;grid-template-columns:1.5fr 1fr;gap:3rem;align-items:center;min-height:78vh;padding:1.5rem 0 2.5rem;}
.pf-avail{display:inline-flex;align-items:center;gap:.55rem;background:#fff;border:1px solid var(--line);
  font-weight:600;font-size:.82rem;color:var(--ink);padding:.4rem .9rem;border-radius:999px;margin-bottom:1.4rem;}
.pf-dot{width:9px;height:9px;border-radius:50%;background:#22A56B;animation:pulse 2s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(34,165,107,.5);}70%{box-shadow:0 0 0 9px rgba(34,165,107,0);}100%{box-shadow:0 0 0 0 rgba(34,165,107,0);}}
.pf-hero h1{font-size:clamp(3.4rem,9vw,8rem);line-height:.98;letter-spacing:-.015em;}
.pf-role{font-size:1.4rem;font-weight:600;color:var(--indigo);margin:1.2rem 0 .8rem;}
.pf-headline{font-size:1.1rem;max-width:36rem;}
.pf-cta{display:flex;gap:.7rem;margin-top:1.8rem;flex-wrap:wrap;}
.btn{display:inline-block;padding:.75rem 1.4rem;border-radius:10px;font-weight:600;font-size:.92rem;
  transition:transform .15s, box-shadow .15s, border-color .15s;}
.btn-primary{background:var(--indigo);color:#fff!important;}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(30,30,28,.22);}
.btn-ghost{background:#fff;color:var(--ink)!important;border:1px solid var(--line);}
.btn-ghost:hover{border-color:var(--indigo);}
.pf-scroll{margin-top:2.2rem;font-size:.82rem;color:var(--muted);}

.pf-photo-wrap{position:relative;justify-self:center;width:min(420px,100%);}
.pf-photo-wrap::before{content:"";position:absolute;inset:16px -16px -16px 16px;border-radius:999px 999px 32px 32px;
  background:var(--sakura);opacity:.55;}
.pf-photo{position:relative;width:100%;aspect-ratio:4/5;border-radius:999px 999px 32px 32px;overflow:hidden;
  background:linear-gradient(160deg,var(--indigo-soft),#fff);display:flex;align-items:center;justify-content:center;
  border:1px solid var(--line);}
.pf-photo img{width:100%;height:100%;object-fit:cover;display:block;}
.pf-initials{font-family:'DM Serif Display',serif!important;font-size:5rem;color:var(--indigo);}

/* Section */
.pf-section{padding:4rem 0 1.2rem;scroll-margin-top:4.5rem;}
.pf-section h2{font-size:clamp(2.2rem,4.5vw,3.6rem);line-height:1.05;}
.pf-sub{margin-top:.6rem;font-size:1rem;}
.pf-bar{width:48px;height:4px;border-radius:4px;background:var(--sakura);margin-top:1.1rem;}

/* About */
.pf-about{display:grid;grid-template-columns:1.6fr 1fr;gap:3rem;align-items:start;}
.pf-lead{font-family:'DM Serif Display',serif!important;font-size:clamp(1.7rem,3vw,2.6rem);line-height:1.2;color:var(--ink);margin-bottom:1.3rem;}
.pf-about p{font-size:1.02rem;max-width:46rem;}
.pf-facts{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.5rem 1.6rem;
  display:flex;flex-direction:column;gap:1rem;}
.pf-fact b{display:block;font-size:.8rem;color:var(--indigo);margin-bottom:.1rem;}
.pf-fact span{font-size:.95rem;color:var(--ink);}

/* Chips */
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem;}
.chip{background:var(--indigo-soft);color:var(--indigo);font-size:.78rem;font-weight:600;padding:.3rem .7rem;border-radius:8px;}
.chip-core{background:var(--indigo);color:#fff;font-size:.95rem;padding:.55rem 1.1rem;border-radius:10px;}
.chip-plain{background:#fff;color:var(--ink);border:1px solid var(--line);font-weight:500;font-size:.84rem;}
.core-label{font-size:.95rem;font-weight:600;color:var(--ink);}
.core-row{margin-bottom:1.6rem;}
.core-row .chips{margin-top:.6rem;}
.tool-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;}
.tool-card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.3rem 1.4rem;}
.tool-card h3{font-size:1rem;}

/* Kartu experience (teks + foto) */
.xlist{display:flex;flex-direction:column;gap:1.4rem;}
.xcard{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:2rem;
  display:grid;grid-template-columns:1.1fr 1fr;gap:2.2rem;align-items:center;}
.xtext{min-width:0;}
.xcard.solo{grid-template-columns:1fr;}
.pf .xcard,.pf .pcard{margin-bottom:.4rem;}
.xgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.4rem;}
.xmeta{display:flex;gap:.8rem;align-items:center;flex-wrap:wrap;font-size:.85rem;color:var(--muted);margin-bottom:.9rem;}
.tl-date{font-size:.8rem;font-weight:600;color:var(--rose);background:var(--sakura-soft);padding:.3rem .75rem;border-radius:999px;white-space:nowrap;}
.pf .xcard h3{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(1.5rem,2.2vw,2rem);line-height:1.15;}
.tl-org{font-size:.98rem;font-weight:600;color:var(--indigo);margin-top:.5rem;}
.xcard ul{margin:1rem 0 0;padding-left:1.1rem;}
.xcard li{color:var(--muted);line-height:1.7;font-size:.94rem;margin-bottom:.35rem;}
.xcard li::marker,.more-card li::marker{color:var(--sakura);}

/* Galeri foto */
.gallery{display:grid;gap:8px;width:100%;aspect-ratio:4/3;}
.gallery.g1{grid-template-columns:1fr;grid-template-rows:minmax(0,1fr);}
.gallery.g2{grid-template-columns:1fr;grid-template-rows:repeat(2,minmax(0,1fr));}
.gallery.g3{grid-template-columns:1fr 1fr;grid-template-rows:minmax(0,1.5fr) minmax(0,1fr);}
.gallery.g3 .tile:first-child{grid-column:1/-1;}
.ph{width:100%;height:100%;min-height:0;object-fit:cover;object-position:center;border:0;border-radius:12px;display:block;background:var(--indigo-soft);}
.ph-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.25rem;text-align:center;
  background:repeating-linear-gradient(135deg,#EEEEE9,#EEEEE9 10px,#F4F4F1 10px,#F4F4F1 20px);
  border:1.5px dashed #CBCBC2;color:var(--muted);font-size:.82rem;font-weight:600;padding:.5rem;}
.ph-empty small{font-weight:400;font-size:.72rem;word-break:break-all;}

/* Projects */
.plist{display:flex;flex-direction:column;gap:1.6rem;}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:1.6rem;
  display:grid;grid-template-columns:1.15fr 1fr;gap:2.4rem;align-items:center;}
.pbody{min-width:0;}
.pcard.rev .pimg{order:2;}
.pmeta{display:flex;gap:.8rem;align-items:center;flex-wrap:wrap;font-size:.85rem;color:var(--muted);margin-bottom:.9rem;}
.pf .pcard h3{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(1.7rem,2.8vw,2.5rem);line-height:1.1;}
.pcat{font-size:1rem;font-weight:600;color:var(--indigo);margin-top:.6rem;}
.pcard p{margin-top:.9rem;font-size:.95rem;}
.porg{margin-top:.9rem;font-size:.88rem;color:var(--ink);font-weight:500;}
.links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.3rem;}
.lnk{display:inline-block;font-size:.85rem;font-weight:600;padding:.55rem 1.05rem;border-radius:9px;
  background:var(--ink);color:#fff!important;transition:transform .15s;}
.lnk:hover{transform:translateY(-1px);}
.lnk.off{background:#fff;color:#A3A39B!important;border:1px dashed #CBCBC2;cursor:not-allowed;}
.lnk.off:hover{transform:none;}

/* More */
.more-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;}
.more-card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.4rem 1.5rem;}
.more-card h3{margin-bottom:.7rem;font-size:1.02rem;}
.more-card li{color:var(--muted);font-size:.92rem;line-height:1.6;margin-bottom:.4rem;}
.more-card ul{padding-left:1.1rem;margin:0;}

/* Contact */
.pf-contact{background:var(--ink);border-radius:28px;padding:clamp(2.2rem,5vw,3.6rem) clamp(1.2rem,4vw,3rem);margin-top:.5rem;text-align:center;}
.pf-contact h2{color:#fff!important;font-size:clamp(2rem,4vw,3rem);line-height:1.1;}
.pf-contact p{color:#C9C9C1;margin:.9rem auto 1.8rem;max-width:34rem;font-size:1rem;}
.pf-contact .btn-ghost{background:transparent;color:#fff!important;border:1px solid #55554F;}
.pf-contact .btn-ghost:hover{border-color:var(--sakura);}
.pf-contact .btn-primary{background:var(--sakura);color:var(--ink)!important;}
.ct-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:.4rem 2.2rem;margin-top:.2rem;}
.ct-card{display:inline-block;padding:.35rem 0;border:0;background:none;}
a.ct-card:hover span{color:var(--sakura);text-decoration:underline;text-underline-offset:6px;}
.ct-card span{display:block;font-size:1.05rem;font-weight:600;color:#fff;transition:color .2s;}
.pf-foot{text-align:center;color:var(--muted);font-size:.82rem;padding:2rem 0 0;}

.stDownloadButton button{border-radius:10px;border:1px solid var(--line);background:#fff;font-weight:600;}
.stDownloadButton button:hover{border-color:var(--indigo);color:var(--indigo);}

/* Pop up saat scroll (aktif hanya jika JS di bawah berhasil jalan) */
.pimg{position:relative;overflow:hidden;width:100%;aspect-ratio:16/10;border-radius:16px;background:var(--indigo-soft);}
.tile{position:relative;overflow:hidden;min-height:0;border-radius:12px;background:var(--indigo-soft);}
/* Foto mengisi frame penuh dan di-crop (seperti frame di Canva), apa pun ukuran aslinya */
.pimg .ph,.tile .ph{position:absolute!important;inset:0!important;width:100%!important;height:100%!important;
  max-width:none!important;max-height:none!important;aspect-ratio:auto!important;
  object-fit:cover!important;object-position:center;border:0;border-radius:0!important;margin:0;}
.pimg .ph{border-radius:0;}
/* Bouncy pop-up: diputar ulang setiap kali elemen masuk layar.
   Pakai keyframes (bukan transition) agar posisi asli elemen tidak bergeser -> tidak berkedip. */
@keyframes pop{
  from{opacity:0;transform:translateY(26px) scale(.98);}
  to{opacity:1;transform:none;}
}
@media (prefers-reduced-motion:no-preference){
  .reveal-on .rv:not(.in){opacity:0;}
  .reveal-on .rv.in{opacity:1;animation:pop .65s cubic-bezier(.25,.9,.35,1.06) backwards;}
  /* kartu bersebelahan muncul berurutan */
  .reveal-on .tool-card.in:nth-child(2),.reveal-on .more-card.in:nth-child(2),.reveal-on .xgrid .xcard.in:nth-child(2){animation-delay:.06s;}
  .reveal-on .tool-card.in:nth-child(3),.reveal-on .more-card.in:nth-child(3){animation-delay:.12s;}
  .reveal-on .tool-card.in:nth-child(4){animation-delay:.18s;}
}

a:focus-visible,button:focus-visible{outline:3px solid var(--sakura);outline-offset:2px;}

@media (max-width:1100px){ .tool-grid{grid-template-columns:repeat(2,1fr);} }
@media (max-width:900px){
  .pf-hero{grid-template-columns:1fr;gap:2rem;min-height:auto;}
  .pf-photo-wrap{order:-1;width:min(260px,70%);}
  .pf-about,.xcard,.pcard,.xgrid,.more-grid,.tool-grid{grid-template-columns:1fr;}
  .pcard.rev .pimg{order:0;}
  .pf-links{display:none;}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto;} .pf-dot{animation:none;} *{transition:none!important;}
}
"""

# ----------------------------------------------------------------------------
# HELPER
# ----------------------------------------------------------------------------
def flat(html: str) -> str:
    """Rapatkan HTML agar Markdown Streamlit tidak menganggapnya blok kode."""
    return " ".join(line.strip() for line in html.splitlines() if line.strip())


def render(html: str) -> None:
    st.markdown(flat(html), unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def _read_image(path_str: str, mtime: float, max_w: int) -> str:
    """Perkecil & kompres foto (jadi WebP) lalu jadikan data URI.
    Foto 5 MB dari kamera/HP -> sekitar 80-200 KB, jadi halaman jauh lebih ringan."""
    path = Path(path_str)
    try:
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im)  # hormati rotasi dari HP
            im.thumbnail((max_w, max_w))
            im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
            buf = BytesIO()
            im.save(buf, "WEBP", quality=78, method=4)
        return f"data:image/webp;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except Exception:  # file aneh: pakai apa adanya
        mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}.get(
            path.suffix.lower().lstrip("."), "image/png"
        )
        return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


@st.cache_data(show_spinner=False)
def _cv_bytes(mtime: float) -> bytes:
    return (ASSETS / "CV.pdf").read_bytes()


def find_image(stem: str, max_w: int = 1200) -> str | None:
    """Cari assets/<stem>.(jpg|jpeg|png|webp), huruf besar/kecil sama saja."""
    for ext in IMG_EXTS + tuple(e.upper() for e in IMG_EXTS):
        p = ASSETS / f"{stem}.{ext}"
        if p.exists():
            return _read_image(str(p), p.stat().st_mtime, max_w)
    return None


def chips(items, css="chip") -> str:
    return "".join(f'<span class="{css}">{i}</span>' for i in items)


def section(anchor: str, title: str, sub: str = "") -> None:
    sub_html = f'<p class="pf-sub">{sub}</p>' if sub else ""
    render(f'<div class="pf pf-section rv" id="{anchor}"><h2>{title}</h2>{sub_html}<div class="pf-bar"></div></div>')


def gallery(stems, alt: str) -> str:
    tiles = []
    for s in stems:
        uri = find_image(s)
        if uri:
            tiles.append(f'<div class="tile"><img class="ph" src="{uri}" alt="{alt}" loading="lazy" decoding="async"/></div>')
        elif SHOW_PLACEHOLDERS:
            tiles.append(f'<div class="tile"><div class="ph ph-empty"><span>Photo placeholder</span><small>assets/{s}.jpg</small></div></div>')
    return f'<div class="gallery g{min(len(tiles), 3)}">{"".join(tiles[:3])}</div>' if tiles else ""


def xcard(it) -> str:
    bullets = "".join(f"<li>{b}</li>" for b in it["bullets"])
    tags = f'<div class="chips">{chips(it["tags"])}</div>' if it.get("tags") else ""
    gal = gallery(it.get("photos", []), it["org"])
    solo = "" if gal else " solo"
    return f"""
    <div class="xcard rv{solo}">
      <div class="xtext">
        <div class="xmeta"><span class="tl-date">{it['date']}</span><span>{it['place']}</span></div>
        <h3>{it['role']}</h3>
        <div class="tl-org">{it['org']}</div>
        <ul>{bullets}</ul>
        {tags}
      </div>
      {gal}
    </div>"""


def render_cards(items, grid=False) -> None:
    if grid:  # kartu tanpa foto: ringan, satu blok
        render(f'<div class="pf xgrid">{"".join(xcard(i) for i in items)}</div>')
    else:  # kartu berfoto: satu elemen per kartu agar tampil bertahap
        for i in items:
            render(f'<div class="pf">{xcard(i)}</div>')


def pcard(p, idx: int) -> str:
    uri = find_image(p["image"]) if p.get("image") else None
    if uri:
        img = f'<img class="ph" src="{uri}" alt="{p["title"]}" loading="lazy" decoding="async"/>'
    elif SHOW_PLACEHOLDERS:
        img = f'<div class="ph ph-empty"><span>Project screenshot</span><small>assets/{p["image"]}.png</small></div>'
    else:
        img = ""
    links = "".join(
        f'<a class="lnk" href="{url}" target="_blank" rel="noopener">{name}</a>'
        if url
        else f'<span class="lnk off" title="Link belum diisi">{name}</span>'
        for name, url in p["links"].items()
    )
    summary = f"<p>{p['summary']}</p>" if p.get("summary") else ""
    rev = " rev" if idx % 2 else ""
    return f"""
    <article class="pcard rv{rev}">
      <div class="pimg">{img}</div>
      <div class="pbody">
        <div class="pmeta"><span class="tl-date">{p['date']}</span><span>{p['type']}</span></div>
        <h3>{p['title']}</h3>
        <div class="pcat">{p['category']}</div>
        {summary}
        <div class="porg">{p['org']}</div>
        <div class="chips">{chips(p['tech'])}</div>
        <div class="links">{links}</div>
      </div>
    </article>"""


def ul(items) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ----------------------------------------------------------------------------
# RENDER HALAMAN
# ----------------------------------------------------------------------------
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

nav_links = "".join(f'<a href="#{a}">{label}</a>' for a, label in NAV)
render(
    f"""
    <div class="pf pf-nav"><div class="pf-nav-inner">
      <span class="pf-brand">{PROFILE['first_name']}<small>/ Portfolio</small></span>
      <nav class="pf-links">{nav_links}</nav>
    </div></div>
    """
)

# Hero
photo_uri = find_image("profile", 900)
photo_html = (
    f'<img src="{photo_uri}" alt="Foto {PROFILE["name"]}"/>' if photo_uri else '<span class="pf-initials">SQ</span>'
)
render(
    f"""
    <div class="pf pf-hero" id="home">
      <div>
        <span class="pf-avail"><span class="pf-dot"></span>Available for work</span>
        <h1>Hi, I'm {PROFILE['first_name']}.</h1>
        <div class="pf-role">{PROFILE['name']}</div>
        <p class="pf-headline">{PROFILE['headline']}</p>
        <div class="pf-cta">
          <a class="btn btn-primary" href="#projects">View projects</a>
          <a class="btn btn-ghost" href="#contact">Get in touch</a>
        </div>
        <div class="pf-scroll">Scroll down to see more</div>
      </div>
      <div class="pf-photo-wrap"><div class="pf-photo">{photo_html}</div></div>
    </div>
    """
)

cv_path = ASSETS / "CV.pdf"
if cv_path.exists():
    st.download_button("Download CV (PDF)", data=_cv_bytes(cv_path.stat().st_mtime), file_name="Shine_Quinn_Firdaus_CV.pdf", mime="application/pdf")

# About
section("about", "About me")
facts = "".join(f'<div class="pf-fact"><b>{k}</b><span>{v}</span></div>' for k, v in QUICK_FACTS)
render(
    f"""
    <div class="pf pf-about">
      <div><div class="pf-lead rv">{PROFILE['lead']}</div><p>{PROFILE['about']}</p></div>
      <div class="pf-facts rv">{facts}</div>
    </div>
    """
)

# Tools
section("tools", "Tools I work with", "What I reach for to clean, analyze, and present data.")
cards = "".join(
    f'<div class="tool-card rv"><h3>{cat}</h3><div class="chips">{chips(tools, "chip chip-plain")}</div></div>'
    for cat, tools in TOOLKIT.items()
)
render(
    f"""
    <div class="pf">
      <div class="core-row"><div class="core-label">Daily drivers</div>
        <div class="chips">{chips(CORE_TOOLS, "chip chip-core")}</div></div>
      <div class="tool-grid">{cards}</div>
    </div>
    """
)

# Professional experience
section("experience", "Professional experience", "Internships and programs where I worked.")
render_cards(EXPERIENCE)

# Projects
section("projects", "Selected projects", "Dashboards, analyses, and apps from internships and college.")
for i, p in enumerate(PROJECTS):
    render(f'<div class="pf">{pcard(p, i)}</div>')

# Education
section("education", "Education")
render_cards(EDUCATION)

# Organizational (tanpa foto)
section("organization", "Organizational experience")
render_cards(ORGANIZATION, grid=True)

# Global learning
section("global", "Global learning experience")
render_cards(GLOBAL_LEARNING)

# Additional info
section("more", "Additional information")
langs = [f"<b>{l}</b>: {lv}" for l, lv in LANGUAGES]
render(
    f"""
    <div class="pf more-grid">
      <div class="more-card rv"><h3>Certifications and training</h3>{ul(CERTIFICATIONS)}</div>
      <div class="more-card rv"><h3>Achievement</h3>{ul(ACHIEVEMENTS)}</div>
      <div class="more-card rv"><h3>Languages</h3>{ul(langs)}</div>
    </div>
    """
)

# Contact
section("contact", "Contact")
# Email: buka compose Gmail langsung ke alamat kamu (lebih andal daripada mailto: di Streamlit)
gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}"
wa_url = f"https://wa.me/{PROFILE['whatsapp']}"
render(
    f"""
    <div class="pf pf-contact rv">
      <h2>Let's connect.</h2>
      <p>I'm open to new opportunities, collaborations, and conversations. Reach me through any of the channels below.</p>
      <div class="ct-grid">
        <a class="ct-card" href="{gmail_url}" target="_blank" rel="noopener"><span>Email</span></a>
        <a class="ct-card" href="{wa_url}" target="_blank" rel="noopener"><span>WhatsApp</span></a>
        <a class="ct-card" href="{PROFILE['linkedin']}" target="_blank" rel="noopener"><span>LinkedIn</span></a>
      </div>
    </div>
    <div class="pf pf-foot">Built with Streamlit</div>
    """
)

# ----------------------------------------------------------------------------
# SCROLL REVEAL: elemen ber-kelas "rv" muncul (pop up) saat masuk layar.
# Script disuntik ke halaman induk supaya tetap hidup walau Streamlit rerun.
# ----------------------------------------------------------------------------
REVEAL_JS = """
if (!window.__rvInit) {
  window.__rvInit = true;
  // Tambah 'in' saat >=12% terlihat; cabut saat sepenuhnya keluar layar -> animasi main lagi tiap scroll
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.intersectionRatio >= 0.12) e.target.classList.add('in');
      else if (!e.isIntersecting) e.target.classList.remove('in');
    });
  }, { threshold: [0, 0.12], rootMargin: '0px 0px -6% 0px' });
  const scan = () => document.querySelectorAll('.rv:not(.in):not([data-rv])').forEach((el) => {
    el.setAttribute('data-rv', '1');
    io.observe(el);
  });
  scan();
  let queued = false;
  new MutationObserver(() => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; scan(); });
  }).observe(document.body, { childList: true, subtree: true });
  document.documentElement.classList.add('reveal-on');
}
"""

_reveal_html = f"""<script>
try {{
  const d = window.parent.document;
  const s = d.createElement('script');
  s.textContent = {json.dumps(REVEAL_JS)};
  d.head.appendChild(s);
}} catch (e) {{ console.warn('Scroll reveal dinonaktifkan:', e); }}
</script>"""

# st.iframe ada di Streamlit versi baru; components.html untuk versi lama
if hasattr(st, "iframe"):
    st.iframe(_reveal_html, height=1)
else:
    import streamlit.components.v1 as components

    components.html(_reveal_html, height=0)