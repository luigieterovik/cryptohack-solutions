<h1>🧠 CryptoHack Solutions</h1>

<blockquote>
  <strong>SPOILER WARNING:</strong> These are <em>my</em> scripts for solving CryptoHack puzzles.
  <br><strong>DO NOT OPEN</strong> if you haven't solved the puzzles yet. You were warned.
</blockquote>

<h2>What this is</h2>
<p>Collection of scripts I wrote to solve CryptoHack (CTF-style) puzzles. Each folder = course/module. Each file = a script named after the puzzle it solves. Purpose: clear, reproducible code you can study after you've solved the challenge.</p>

<h2>Repo layout</h2>
<pre><code>
├─ README.md
├─ module-crypto-1/
│  ├─ requirements.txt
│  ├─ puzzle-name-1.py
│  └─ puzzle-name-2.py
├─ module-crypto-2/
│  ├─ requirements.txt
│  ├─ another-puzzle.py
│  └─ ...
└─ other-challenges.py

</code></pre>

<h2>Rules — read this now</h2>
<ul>
  <li><strong>Spoilers live here.</strong> Don't blame the repo if you ruin the puzzle.</li>
  <li><strong>Use:</strong> educational — learn crypto techniques and CTF tricks.</li>
  <li><strong>Do not</strong> use these solutions to cheat in active competitions. Be ethical.</li>
</ul>

<h2>Quick run (zero drama)</h2>
<ol>
  <li>Install Python 3.8+.</li>
</ol>
<ol start="2">
  <li>Install deps (if provided):</li>
</ol>
<pre><code>pip install -r requirements.txt
</code></pre>
<ol start="3">
  <li>Run a script:</li>
</ol>
<pre><code>python module-crypto-1/puzzle-name-1.py
</code></pre>
<p>Some scripts include a top comment explaining expected inputs and how to feed them.</p>

<h2>Typical dependencies</h2>
<pre><code>pwntools
pycryptodome
</code></pre>
</code></pre>
