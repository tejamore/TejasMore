# Tejas More — Portfolio / Dynamic Resume Site

A single-page portfolio site built with **Flask** (Python), rendering résumé
content from a structured Python dictionary via Jinja2 templates. Features an
animated SVG "automation pipeline" hero graphic, scroll-triggered reveal
animations, a downloadable résumé PDF, and a call-to-action button that links
to a Google Form for inbound contact requests.

---

## 1. Project structure

```
project/
├── app.py                     # Flask app + all résumé content (CV_DATA dict)
├── requirements.txt           # Python dependencies
├── render.yaml                # Render.com deploy config (Infrastructure as Code)
├── Procfile                   # Fallback start command (gunicorn)
├── templates/
│   └── index.html             # Jinja2 template — all page markup + SVG icons
├── static/
│   ├── css/style.css          # Design tokens, layout, animations
│   ├── js/main.js             # Scroll-reveal animation logic
│   ├── img/profile.webp       # Profile photo
│   └── resume/
│       └── Tejas_More_Resume.pdf   # Downloadable résumé
└── README.md
```

---

## 2. Requirements

- Python 3.10+
- pip

---

## 3. Local installation & setup

```bash
# 1. Clone your repository (after you've pushed this project to GitHub — see step 6)
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app locally
python app.py
```

The site will be available at **http://127.0.0.1:5000**.

To run it the same way a production server (gunicorn) would:

```bash
gunicorn app:app
```

---

## 4. Configuration

All résumé content — name, summary, skills, experience, education — lives in
the `CV_DATA` dictionary at the top of `app.py`. Edit that dictionary to
update the site; no HTML editing required.

### Add your Google Form link

Open `app.py` and find this line near the top of `CV_DATA`:

```python
"contact_form_url": "https://forms.gle/REPLACE-WITH-YOUR-GOOGLE-FORM-ID",
```

Replace the placeholder URL with your real Google Form link (Google Forms →
**Send** → copy the link). Every "Get in touch" / "Start a conversation" /
"Fill the contact form" button on the site uses this one value, so you only
need to update it in this single place.

### Replace the profile photo

Swap the file at `static/img/profile.webp` with your own image (keep the same
filename, or update `"profile_image"` in `CV_DATA` to point to the new file).

### Replace the downloadable résumé

Swap the file at `static/resume/Tejas_More_Resume.pdf` with an updated PDF
(keep the same filename, or update `"resume_file"` in `CV_DATA`).

---

## 5. Push the project to GitHub

```bash
cd <your-repo>
git init                                  # skip if already a git repo
git add .
git commit -m "Initial commit — portfolio site"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

---

## 6. Deploy live on Render

**Option A — using `render.yaml` (recommended, one click after connecting the repo)**

1. Push this project to a GitHub repository (see step 5).
2. Go to [render.com](https://render.com) and sign in / sign up.
3. Click **New +** → **Blueprint**.
4. Connect your GitHub account and select this repository.
5. Render detects `render.yaml` automatically and configures:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
6. Click **Apply** / **Create**. Render will build and deploy automatically.
7. Once deployed, Render gives you a live URL like:
   `https://tejas-more-portfolio.onrender.com`

**Option B — manual Web Service setup**

1. Go to [render.com](https://render.com) → **New +** → **Web Service**.
2. Connect your GitHub repo.
3. Set:
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free (or any paid tier)
4. Click **Create Web Service**. Render builds and deploys automatically on
   every push to your main branch.

### Notes on the free tier

Render's free web services spin down after periods of inactivity and take a
few seconds to "wake up" on the next request — this is normal and not a bug
in the app.

---

## 7. Updating the live site after changes

```bash
git add .
git commit -m "Update résumé content"
git push
```

Render automatically rebuilds and redeploys on every push to the connected
branch — no manual redeploy step needed.

---

## 8. Tech stack

- **Backend:** Flask (Python), Jinja2 templating
- **Frontend:** Hand-written HTML/CSS/JS, inline SVG icon sprite, no build step
- **Animations:** CSS keyframes + `IntersectionObserver` scroll reveals, SVG
  `<animateMotion>` for the live automation-pipeline graphic
- **Fonts:** Space Grotesk (display), Inter (body), JetBrains Mono (utility/labels)
- **Deployment target:** Render.com, via `gunicorn`
