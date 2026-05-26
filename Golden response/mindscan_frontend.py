FRONTEND_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MindScan</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    :root {
      --primary: #4A90D9;
      --green:   #5BAD8F;
      --bg:      #F4F6FB;
      --card:    #FFFFFF;
      --text:    #2D2D2D;
      --muted:   #7A7A8C;
      --border:  #E0E4EF;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Poppins', sans-serif; background: var(--bg); color: var(--text); }

    nav {
      display: none; justify-content: space-between; align-items: center;
      padding: 1rem 2rem; background: var(--card);
      border-bottom: 1px solid var(--border);
    }
    nav .brand { font-weight: 600; color: var(--primary); font-size: 1.2rem; }
    nav .nav-links a {
      margin-left: 1.5rem; cursor: pointer; color: var(--muted);
      text-decoration: none; font-size: 0.9rem; font-weight: 500;
      transition: color 0.2s;
    }
    nav .nav-links a:hover { color: var(--primary); }

    .view { display: none; min-height: calc(100vh - 60px); padding: 2rem; }
    .view.active { display: block; }

    .card {
      background: var(--card); border-radius: 16px;
      padding: 2rem; box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      margin-bottom: 1.5rem;
    }
    .card h2 { color: var(--primary); margin-bottom: 1rem; font-size: 1.4rem; }

    .container { max-width: 480px; margin: 3rem auto; }
    .input {
      width: 100%; padding: 12px 16px; margin: 8px 0 16px;
      border: 1.5px solid var(--border); border-radius: 10px;
      font-family: 'Poppins', sans-serif; font-size: 0.95rem;
      transition: border-color 0.2s; outline: none;
    }
    .input:focus { border-color: var(--primary); }
    .btn {
      width: 100%; padding: 13px; border: none; border-radius: 10px;
      background: var(--primary); color: white; font-family: 'Poppins', sans-serif;
      font-size: 0.95rem; font-weight: 500; cursor: pointer; transition: opacity 0.2s;
    }
    .btn:hover:not(:disabled) { opacity: 0.88; }
    .btn:disabled { background: #ccc; cursor: not-allowed; }
    .btn-outline {
      background: transparent; color: var(--primary);
      border: 1.5px solid var(--primary); margin-top: 0.75rem;
    }

    .progress-wrap { background: var(--border); height: 8px; border-radius: 4px; margin-bottom: 1.5rem; overflow: hidden; }
    .progress-bar  { background: var(--primary); height: 100%; width: 0%; transition: width 0.4s ease; }
    .question-text { font-size: 1.1rem; font-weight: 500; margin-bottom: 1.2rem; line-height: 1.5; }
    .option {
      padding: 14px 18px; border: 2px solid var(--border); border-radius: 10px;
      margin-bottom: 10px; cursor: pointer; transition: border-color 0.2s, background 0.2s;
      font-size: 0.95rem;
    }
    .option:hover   { border-color: var(--primary); }
    .option.selected { border-color: var(--primary); background: rgba(74,144,217,0.08); font-weight: 500; }

    .wellness-score {
      text-align: center; padding: 1.5rem;
      background: linear-gradient(135deg, #4A90D9, #5BAD8F);
      border-radius: 16px; color: white; margin-bottom: 1.5rem;
    }
    .wellness-score .score-num { font-size: 3.5rem; font-weight: 600; }
    .result-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; }
    .result-card  { background: var(--card); border-radius: 12px; padding: 1.2rem; border: 1px solid var(--border); text-align: center; }
    .badge {
      display: inline-block; padding: 4px 14px; border-radius: 20px;
      font-size: 0.8rem; font-weight: 600; margin-bottom: 0.5rem;
    }
    .badge-Minimal  { background: #e6f7ee; color: #1a7a40; }
    .badge-Mild     { background: #fff8e1; color: #8a6d00; }
    .badge-Moderate { background: #fff0e0; color: #a35200; }
    .badge-Severe   { background: #fde8e8; color: #9b1c1c; }
    .crisis-alert {
      background: #fde8e8; border: 1.5px solid #f87171;
      border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1.5rem; color: #7f1d1d;
    }

    .dash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
    .stat-card  {
      background: var(--card); border-radius: 12px; padding: 1.2rem;
      border: 1px solid var(--border); text-align: center;
    }
    .stat-card .stat-val { font-size: 2rem; font-weight: 600; color: var(--primary); }
    .stat-card .stat-label { font-size: 0.8rem; color: var(--muted); margin-top: 4px; }

    .toast {
      position: fixed; bottom: 24px; right: 24px; padding: 12px 20px;
      border-radius: 10px; background: #2D2D2D; color: white;
      font-size: 0.9rem; z-index: 9999; animation: slideUp 0.3s ease;
      max-width: 320px;
    }
    .toast.success { background: #1a7a40; }
    .toast.error   { background: #9b1c1c; }

    .toggle-link { text-align: center; margin-top: 1rem; color: var(--primary); cursor: pointer; font-size: 0.9rem; }
    .disclaimer  { background: #f0f4ff; border-radius: 10px; padding: 1rem 1.5rem; font-size: 0.88rem; color: var(--muted); margin-top: 1.5rem; }

    @keyframes slideUp   { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    @keyframes fadeInUp  { from { transform: translateY(12px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    .fade-in { animation: fadeInUp 0.5s ease both; }
  </style>
</head>
<body>

<nav id="navbar">
  <span class="brand">MindScan</span>
  <div class="nav-links">
    <a onclick="showView('dashboard-view')">Dashboard</a>
    <a onclick="showView('screening-view')">Screening</a>
    <a onclick="showView('journal-view')">Journal</a>
    <a onclick="logout()">Logout</a>
  </div>
</nav>

<!-- AUTH VIEW -->
<div id="auth-view" class="view active">
  <div class="container">
    <div class="card">
      <h2 id="auth-title">Welcome Back</h2>
      <input id="auth-name"     class="input" placeholder="Your name"       style="display:none;">
      <input id="auth-email"    class="input" placeholder="Email address"   type="email">
      <input id="auth-password" class="input" placeholder="Password"        type="password">
      <button class="btn" onclick="handleAuth()" id="auth-btn">Login</button>
      <p class="toggle-link" onclick="toggleAuth()" id="auth-toggle">Don't have an account? Sign up</p>
    </div>
  </div>
</div>

<!-- DASHBOARD VIEW -->
<div id="dashboard-view" class="view">
  <div class="dash-grid">
    <div class="stat-card"><div class="stat-val" id="dash-wellness">--</div><div class="stat-label">Wellness Score</div></div>
    <div class="stat-card"><div class="stat-val" id="dash-streak">--</div><div class="stat-label">Day Streak</div></div>
    <div class="stat-card"><div class="stat-val" id="dash-screenings">--</div><div class="stat-label">Screenings Done</div></div>
  </div>
  <div class="card">
    <h2>Mood Trend (last 30 days)</h2>
    <div style="position:relative; height:260px;">
      <canvas id="moodChart" role="img" aria-label="Line chart showing mood scores over the last 30 days"></canvas>
    </div>
  </div>
  <div class="card">
    <h2>Motivational Quote</h2>
    <p id="dash-quote" style="font-style:italic; color:var(--muted); line-height:1.8;"></p>
  </div>
</div>

<!-- SCREENING VIEW -->
<div id="screening-view" class="view">
  <div style="max-width:640px; margin:0 auto;">
    <div id="disclaimer-card" class="card">
      <h2>Mental Wellness Screening</h2>
      <p style="color:var(--muted); line-height:1.8; margin-bottom:1.5rem;">
        This tool uses the DASS-21 questionnaire to screen for patterns of depression, anxiety, and stress.
        It is not a clinical diagnosis. Please speak to a licensed mental health professional for real support.
      </p>
      <button class="btn" onclick="startScreening()">I understand, let's start</button>
    </div>

    <div id="quiz-card" class="card" style="display:none;">
      <div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
      <p style="font-size:0.8rem; color:var(--muted); margin-bottom:1rem;" id="q-counter">Question 1 of 21</p>
      <div id="q-content"></div>
      <div style="display:flex; gap:1rem; margin-top:1.5rem;">
        <button class="btn btn-outline" id="prev-btn" onclick="prevQuestion()" style="display:none;">Back</button>
        <button class="btn" id="next-btn" onclick="nextQuestion()" disabled>Next</button>
      </div>
    </div>

    <div id="results-card" class="card" style="display:none;">
      <div id="crisis-alert" class="crisis-alert" style="display:none;">
        ⚠️ If you are in crisis, please call iCall: <strong>9152987821</strong> or visit <a href="https://findahelpline.com" target="_blank">findahelpline.com</a>
      </div>
      <div class="wellness-score fade-in">
        <p style="font-size:0.9rem; opacity:0.85; margin-bottom:4px;">Your Wellness Score</p>
        <div class="score-num" id="res-score">--</div>
        <p style="font-size:0.8rem; opacity:0.7;">out of 100</p>
      </div>
      <div class="result-cards" id="result-cards"></div>
      <div style="display:flex; gap:1rem; margin-top:1.5rem; flex-wrap:wrap;">
        <button class="btn" onclick="saveScreening()">Save to History</button>
        <button class="btn btn-outline" onclick="restartScreening()">Retake Screening</button>
      </div>
      <div class="disclaimer">This is a wellness screening tool, not a medical diagnosis. Always consult a licensed professional for clinical advice.</div>
    </div>
  </div>
</div>

<!-- JOURNAL VIEW -->
<div id="journal-view" class="view">
  <div style="max-width:680px; margin:0 auto;">
    <div class="card">
      <h2>Today's Entry</h2>
      <div style="display:flex; gap:12px; margin-bottom:1rem; flex-wrap:wrap;" id="mood-buttons">
        <button class="mood-btn" data-mood="Very Happy" data-score="5" onclick="selectMood(this)" style="font-size:1.6rem; background:none; border:2px solid var(--border); border-radius:10px; padding:8px 14px; cursor:pointer;">😄</button>
        <button class="mood-btn" data-mood="Happy"      data-score="4" onclick="selectMood(this)" style="font-size:1.6rem; background:none; border:2px solid var(--border); border-radius:10px; padding:8px 14px; cursor:pointer;">🙂</button>
        <button class="mood-btn" data-mood="Neutral"    data-score="3" onclick="selectMood(this)" style="font-size:1.6rem; background:none; border:2px solid var(--border); border-radius:10px; padding:8px 14px; cursor:pointer;">😐</button>
        <button class="mood-btn" data-mood="Sad"        data-score="2" onclick="selectMood(this)" style="font-size:1.6rem; background:none; border:2px solid var(--border); border-radius:10px; padding:8px 14px; cursor:pointer;">😔</button>
        <button class="mood-btn" data-mood="Very Sad"   data-score="1" onclick="selectMood(this)" style="font-size:1.6rem; background:none; border:2px solid var(--border); border-radius:10px; padding:8px 14px; cursor:pointer;">😢</button>
      </div>
      <textarea id="journal-text" class="input" rows="5" maxlength="2000"
        placeholder="Write how you're feeling today..." style="resize:vertical;"></textarea>
      <p style="font-size:0.78rem; color:var(--muted); text-align:right;" id="char-count">0 / 2000</p>
      <input id="journal-tags-input" class="input" placeholder="Add a tag and press Enter (e.g. anxious, productive)">
      <div id="tags-container" style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:1rem;"></div>
      <button class="btn" onclick="saveJournal()">Save Entry</button>
    </div>
    <div class="card">
      <h2>Past Entries</h2>
      <input id="journal-search" class="input" placeholder="Search by keyword or tag..." oninput="filterEntries()">
      <div id="entries-list"></div>
    </div>
  </div>
</div>

<script>
const API      = "";
let isLogin    = true;
let currentQ   = 0;
let answers    = [];
let lastResult = null;
let journalTags      = [];
let selectedMood     = null;
let selectedMoodScore = null;
let allEntries   = [];
let chartInstance = null;

const QUESTIONS = [
  "I found it hard to wind down",
  "I was aware of dryness of my mouth",
  "I couldn't seem to experience any positive feeling at all",
  "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)",
  "I found it difficult to work up the initiative to do things",
  "I tended to over-react to situations",
  "I experienced trembling (e.g. in the hands)",
  "I felt that I was using a lot of nervous energy",
  "I was worried about situations in which I might panic and make a fool of myself",
  "I felt that I had nothing to look forward to",
  "I found myself getting agitated",
  "I found it difficult to relax",
  "I felt down-hearted and blue",
  "I was intolerant of anything that kept me from getting on with what I was doing",
  "I felt I was close to panic",
  "I was unable to become enthusiastic about anything",
  "I felt I wasn't worth much as a person",
  "I felt that I was rather touchy",
  "I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, irregular heartbeat)",
  "I felt scared without any good reason",
  "I felt that life was meaningless"
];

const QUOTES = [
  "You don't have to control your thoughts. You just have to stop letting them control you.",
  "Mental health is not a destination, but a process. It's about how you drive, not where you're going.",
  "There is hope, even when your brain tells you there isn't.",
  "Self-care is how you take your power back.",
  "You are not your illness. You have an individual story to tell.",
  "It's okay to not be okay — as long as you are not giving up.",
  "Healing is not linear. Some days will feel harder than others, and that's okay.",
  "Your present circumstances don't determine where you can go; they merely determine where you start.",
  "Recovery is not a race. You don't have to feel guilty if it takes you longer than you thought.",
  "Be patient with yourself. Nothing in nature blooms all year."
];

function showView(id) {
  document.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
  document.getElementById(id).classList.add("active");
  if (id === "dashboard-view") loadDashboard();
  if (id === "journal-view")   loadJournal();
  if (id === "screening-view") resetScreeningUI();
}

function toast(msg, type = "") {
  const t = document.createElement("div");
  t.className = `toast ${type}`;
  t.innerText = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3500);
}

async function api(endpoint, method = "GET", body = null) {
  const headers = { "Content-Type": "application/json" };
  const token   = localStorage.getItem("token");
  if (token) headers["Authorization"] = `Bearer ${token}`;
  const res = await fetch(API + endpoint, {
    method, headers, body: body ? JSON.stringify(body) : null
  });
  if (res.status === 401) { logout(); return null; }
  const data = await res.json();
  if (!res.ok) throw new Error(data.message || "Request failed");
  return data;
}

function init() {
  const token = localStorage.getItem("token");
  if (token) {
    document.getElementById("navbar").style.display = "flex";
    showView("dashboard-view");
  } else {
    showView("auth-view");
  }
}

function toggleAuth() {
  isLogin = !isLogin;
  document.getElementById("auth-title").innerText    = isLogin ? "Welcome Back" : "Create Account";
  document.getElementById("auth-btn").innerText      = isLogin ? "Login" : "Sign Up";
  document.getElementById("auth-toggle").innerText   = isLogin ? "Don't have an account? Sign up" : "Already have an account? Login";
  document.getElementById("auth-name").style.display = isLogin ? "none" : "block";
}

async function handleAuth() {
  const email    = document.getElementById("auth-email").value.trim();
  const password = document.getElementById("auth-password").value.trim();
  const name     = document.getElementById("auth-name").value.trim();
  if (!email || !password) return toast("Email and password are required", "error");
  try {
    if (isLogin) {
      const res = await api("/api/auth/login", "POST", { email, password });
      if (!res) return;
      localStorage.setItem("token", res.token);
      localStorage.setItem("name",  res.name);
      toast("Logged in successfully", "success");
      document.getElementById("navbar").style.display = "flex";
      showView("dashboard-view");
    } else {
      if (!name) return toast("Name is required", "error");
      await api("/api/auth/signup", "POST", { name, email, password });
      toast("Account created! Please log in.", "success");
      toggleAuth();
    }
  } catch (e) { toast(e.message, "error"); }
}

function logout() {
  localStorage.clear();
  document.getElementById("navbar").style.display = "none";
  showView("auth-view");
}

async function loadDashboard() {
  document.getElementById("dash-quote").innerText = QUOTES[Math.floor(Math.random() * QUOTES.length)];
  try {
    const [screenings, entries] = await Promise.all([
      api("/api/screening/history"),
      api("/api/journal/entries")
    ]);
    if (!screenings || !entries) return;

    document.getElementById("dash-wellness").innerText =
      screenings.length ? screenings[0].wellnessScore : "N/A";
    document.getElementById("dash-screenings").innerText = screenings.length;

    const dates = entries.map(e => e.date ? e.date.slice(0, 10) : "").filter(Boolean);
    document.getElementById("dash-streak").innerText = calcStreak(dates);

    const moodMap = {};
    entries.forEach(e => {
      const d = e.date ? e.date.slice(0, 10) : "";
      if (d) moodMap[d] = e.moodScore || 3;
    });
    const labels = [], dataPoints = [];
    for (let i = 29; i >= 0; i--) {
      const d = new Date();
      d.setDate(d.getDate() - i);
      const key = d.toISOString().slice(0, 10);
      labels.push(key.slice(5));
      dataPoints.push(moodMap[key] || null);
    }
    if (chartInstance) chartInstance.destroy();
    chartInstance = new Chart(document.getElementById("moodChart"), {
      type: "line",
      data: {
        labels,
        datasets: [{
          label: "Mood Score", data: dataPoints,
          borderColor: "#4A90D9", backgroundColor: "rgba(74,144,217,0.08)",
          tension: 0.3, fill: true, pointRadius: 3, spanGaps: true
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: { min: 1, max: 5, ticks: { stepSize: 1 }, grid: { color: "rgba(0,0,0,0.05)" } },
          x: { ticks: { autoSkip: true, maxTicksLimit: 10 }, grid: { display: false } }
        }
      }
    });
  } catch(e) { toast("Could not load dashboard data", "error"); }
}

function calcStreak(dates) {
  if (!dates.length) return 0;
  const unique = [...new Set(dates)].sort().reverse();
  let streak = 0;
  for (let i = 0; i < unique.length; i++) {
    const expected = new Date();
    expected.setDate(expected.getDate() - i);
    if (unique[i] === expected.toISOString().slice(0, 10)) streak++;
    else break;
  }
  return streak;
}

function resetScreeningUI() {
  document.getElementById("disclaimer-card").style.display = "block";
  document.getElementById("quiz-card").style.display       = "none";
  document.getElementById("results-card").style.display    = "none";
}

function startScreening() {
  answers    = new Array(21).fill(null);
  currentQ   = 0;
  lastResult = null;
  document.getElementById("disclaimer-card").style.display = "none";
  document.getElementById("quiz-card").style.display       = "block";
  renderQuestion();
}

function restartScreening() {
  resetScreeningUI();
  startScreening();
}

function renderQuestion() {
  const pct = ((currentQ) / QUESTIONS.length) * 100;
  document.getElementById("progress-bar").style.width = pct + "%";
  document.getElementById("q-counter").innerText      = `Question ${currentQ + 1} of ${QUESTIONS.length}`;

  const opts = ["Not at all", "Several days", "More than half the days", "Nearly every day"];
  document.getElementById("q-content").innerHTML = `
    <p class="question-text">${currentQ + 1}. ${QUESTIONS[currentQ]}</p>
    ${opts.map((o, i) => `
      <div class="option ${answers[currentQ] === i ? "selected" : ""}" onclick="pickAnswer(${i})">${o}</div>
    `).join("")}
  `;

  const nextBtn = document.getElementById("next-btn");
  nextBtn.innerText = currentQ === QUESTIONS.length - 1 ? "Submit" : "Next";
  nextBtn.disabled  = answers[currentQ] === null;
  document.getElementById("prev-btn").style.display = currentQ > 0 ? "block" : "none";
}

function pickAnswer(val) {
  answers[currentQ] = val;
  renderQuestion();
}

function prevQuestion() {
  if (currentQ > 0) { currentQ--; renderQuestion(); }
}

async function nextQuestion() {
  if (currentQ < QUESTIONS.length - 1) {
    currentQ++; renderQuestion(); return;
  }
  const nextBtn = document.getElementById("next-btn");
  nextBtn.innerText = "Processing..."; nextBtn.disabled = true;
  try {
    const res = await api("/api/screening/submit", "POST", { answers });
    if (!res) return;
    lastResult = res;
    showResults(res);
  } catch(e) {
    toast(e.message, "error");
    nextBtn.innerText = "Submit"; nextBtn.disabled = false;
  }
}

function showResults(res) {
  document.getElementById("quiz-card").style.display    = "none";
  document.getElementById("results-card").style.display = "block";
  document.getElementById("res-score").innerText        = res.wellnessScore;

  const { depression, anxiety, stress } = res.prediction;
  const severe = [depression, anxiety, stress].some(l => l === "Moderate" || l === "Severe");
  document.getElementById("crisis-alert").style.display = severe ? "block" : "none";

  const descriptions = {
    Minimal:  "You're doing well in this area. Keep up your healthy habits.",
    Mild:     "Some signs present. Try mindfulness or journaling to support yourself.",
    Moderate: "Noticeable impact on daily life. Consider speaking to a counsellor.",
    Severe:   "Significant impact. Please reach out to a mental health professional."
  };

  document.getElementById("result-cards").innerHTML = [
    { label: "Depression", level: depression },
    { label: "Anxiety",    level: anxiety    },
    { label: "Stress",     level: stress     }
  ].map((c, i) => `
    <div class="result-card fade-in" style="animation-delay:${i * 0.15}s">
      <p style="font-weight:500; margin-bottom:8px;">${c.label}</p>
      <span class="badge badge-${c.level}">${c.level}</span>
      <p style="font-size:0.82rem; color:var(--muted); margin-top:8px; line-height:1.5;">${descriptions[c.level]}</p>
    </div>
  `).join("");
}

async function saveScreening() {
  toast("Result already saved to your history.", "success");
}

function selectMood(btn) {
  document.querySelectorAll(".mood-btn").forEach(b => b.style.borderColor = "var(--border)");
  btn.style.borderColor = "var(--primary)";
  selectedMood      = btn.dataset.mood;
  selectedMoodScore = parseInt(btn.dataset.score);
}

document.getElementById("journal-text").addEventListener("input", function() {
  document.getElementById("char-count").innerText = this.value.length + " / 2000";
});

document.getElementById("journal-tags-input").addEventListener("keydown", function(e) {
  if (e.key === "Enter" && this.value.trim()) {
    e.preventDefault();
    addTag(this.value.trim()); this.value = "";
  }
});

function addTag(tag) {
  if (journalTags.includes(tag)) return;
  journalTags.push(tag);
  renderTags();
}

function removeTag(tag) {
  journalTags = journalTags.filter(t => t !== tag);
  renderTags();
}

function renderTags() {
  document.getElementById("tags-container").innerHTML = journalTags.map(t =>
    `<span style="background:#e8f0fe; color:#1a56db; padding:4px 12px; border-radius:20px; font-size:0.82rem; display:flex; align-items:center; gap:6px;">
      ${t} <span onclick="removeTag('${t}')" style="cursor:pointer; font-weight:600;">x</span>
    </span>`
  ).join("");
}

async function saveJournal() {
  if (!selectedMood) return toast("Please select a mood first", "error");
  const text = document.getElementById("journal-text").value.trim();
  try {
    await api("/api/journal/add", "POST", {
      mood:      selectedMood,
      moodScore: selectedMoodScore,
      entryText: text,
      tags:      journalTags,
      date:      new Date().toISOString()
    });
    toast("Journal entry saved!", "success");
    document.getElementById("journal-text").value = "";
    document.getElementById("char-count").innerText = "0 / 2000";
    journalTags = []; renderTags();
    selectedMood = null; selectedMoodScore = null;
    document.querySelectorAll(".mood-btn").forEach(b => b.style.borderColor = "var(--border)");
    loadJournal();
  } catch(e) { toast(e.message, "error"); }
}

async function loadJournal() {
  try {
    allEntries = await api("/api/journal/entries") || [];
    renderEntries(allEntries);
  } catch(e) { toast("Could not load journal entries", "error"); }
}

function filterEntries() {
  const q = document.getElementById("journal-search").value.toLowerCase();
  const filtered = allEntries.filter(e =>
    (e.entryText || "").toLowerCase().includes(q) ||
    (e.tags || []).some(t => t.toLowerCase().includes(q))
  );
  renderEntries(filtered);
}

function renderEntries(entries) {
  const moodEmoji = { "Very Happy": "😄", "Happy": "🙂", "Neutral": "😐", "Sad": "😔", "Very Sad": "😢" };
  document.getElementById("entries-list").innerHTML = entries.length
    ? entries.map(e => `
        <div class="card" style="cursor:pointer;" onclick="this.querySelector('.full-text').style.display = this.querySelector('.full-text').style.display === 'none' ? 'block' : 'none'">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span style="font-size:1.3rem;">${moodEmoji[e.mood] || "😐"}</span>
            <span style="font-size:0.8rem; color:var(--muted);">${(e.date || "").slice(0,10)}</span>
          </div>
          <p style="font-size:0.9rem; color:var(--muted);">${(e.entryText || "").slice(0,120)}${(e.entryText || "").length > 120 ? "..." : ""}</p>
          <div class="full-text" style="display:none; margin-top:10px; font-size:0.9rem; line-height:1.6;">${e.entryText || ""}</div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:10px;">
            ${(e.tags || []).map(t => `<span style="background:#e8f0fe; color:#1a56db; padding:2px 10px; border-radius:20px; font-size:0.78rem;">${t}</span>`).join("")}
          </div>
          <div style="display:flex; gap:10px; margin-top:10px;">
            <button onclick="event.stopPropagation(); deleteEntry('${e._id}')" style="font-size:0.8rem; color:#9b1c1c; background:none; border:none; cursor:pointer;">Delete</button>
          </div>
        </div>
      `).join("")
    : `<p style="color:var(--muted); text-align:center; padding:2rem;">No entries yet. Write your first one above.</p>`;
}

async function deleteEntry(id) {
  if (!confirm("Delete this entry?")) return;
  try {
    await api(`/api/journal/${id}`, "DELETE");
    toast("Entry deleted", "success");
    loadJournal();
  } catch(e) { toast(e.message, "error"); }
}

init();
</script>
</body>
</html>
"""
