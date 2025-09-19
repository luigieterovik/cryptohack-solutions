<h1>🧠 CryptoHack Solutions</h1>

<blockquote>
  <strong>SPOILER WARNING:</strong> These are <em>my</em> scripts for solving CryptoHack puzzles.
  <br><strong>DO NOT OPEN</strong> if you haven't solved the puzzles yet. You were warned.
</blockquote>

<h2>What this is</h2>
<p>Collection of scripts I wrote to solve CryptoHack (CTF-style) puzzles. Each folder = course/module. Each file = a script named after the puzzle it solves. Purpose: clear, reproducible code you can study after you've solved the challenge.</p>

<h2>Repo layout (actual)</h2>
<pre><code>/
├─ README.md
├─ requirements.txt
├─ "Introduction to CryptoHack"/
│  ├─ 1. ASCII.py
│  ├─ 2. HEX.py
│  └─ ... (scripts for that module)
├─ "Modular Arithmetic"/
│  ├─ 1. Greatest Common Divisor.py
│  └─ ... (scripts for that module)
├─ "other_challenges.py"
└─ other files
</code></pre>

<h2>Rules — read this now</h2>
<ul>
  <li><strong>Spoilers live here.</strong> Don't blame the repo if you ruin the puzzle.</li>
  <li><strong>Use:</strong> educational — learn crypto techniques and CTF tricks.</li>
  <li><strong>Do not</strong> use these solutions to cheat in active competitions. Be ethical.</li>
</ul>

<h2>Setup — create &amp; use a virtual environment</h2>
<p>One command set per OS. Use the one that matches your machine.</p>

<h3>Windows (PowerShell)</h3>
<pre><code>python -m venv venv
# If PowerShell blocks scripts, run once:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
</code></pre>

<h3>Linux</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
</code></pre>

<h3>macOS</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
</code></pre>

<p>Verify the venv is active:</p>
<pre><code>python -c "import sys; print(sys.executable)"
pip list
</code></pre>

<h2>Quick run (zero drama)</h2>
<ol>
  <li>Install Python 3.8+.</li>
  <li>Create &amp; activate venv (see OS above).</li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run a script:
    <pre><code>python "Modular Arithmetic/1. Greatest Common Divisor.py"</code></pre>
  </li>
</ol>
<p>Some scripts include a top comment explaining expected inputs and how to feed them.</p>

<h2>Typical dependencies</h2>
<pre><code>pwntools
pycryptodome
</code></pre>
