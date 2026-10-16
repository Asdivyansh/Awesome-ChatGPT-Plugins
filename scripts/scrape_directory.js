/*
 * Snapshot the public ChatGPT Plugin Directory.
 *
 * The directory sits behind bot protection, so this runs in your own browser:
 *   1. Open https://chatgpt.com/plugins (you don't need to be signed in).
 *   2. Open DevTools → Console, paste this file, and press Enter.
 *   3. Wait a few minutes. It downloads `directory-snapshot.json` when it's done.
 *   4. python3 scripts/normalize_snapshot.py ~/Downloads/directory-snapshot.json
 *      python3 scripts/build_catalog.py
 *
 * It sends about one request per plugin from a few workers, with a short pause
 * between requests, so the directory isn't hammered.
 */
(async () => {
  const CATEGORIES = [
    "featured", "new-and-noteworthy", "small-business", "productivity", "creativity",
    "developer-tools", "business-and-operations", "data-and-analytics", "communication",
    "education-and-research", "scientific-research", "security", "finance", "healthcare",
    "travel", "other",
  ];
  const WORKERS = 5;
  const PAUSE_MS = 150;
  const HTML = { headers: { Accept: "text/html,application/xhtml+xml" } };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const parseHTML = (html) => new DOMParser().parseFromString(html, "text/html");

  // 1. Category listings (each page embeds its full plugin list as JSON).
  const stats = {};
  const plugins = {};
  const order = {};
  for (const c of CATEGORIES) {
    const doc = parseHTML(await (await fetch(`/plugins?category=${c}`, HTML)).text());
    const raw = [...doc.querySelectorAll("script")].map((s) => s.textContent).find((t) => t.startsWith('{"url"'));
    const dir = JSON.parse(raw).view.directory;
    order[c] = [];
    for (const sec of dir.sections) {
      for (const p of sec.plugins) {
        order[c].push(p.id);
        plugins[p.id] ??= { n: p.name, d: p.description, c: [] };
        if (!plugins[p.id].c.includes(c)) plugins[p.id].c.push(c);
        if (p.desktop) plugins[p.id].desk = true;
      }
    }
    stats[c] = { n: order[c].length, title: dir.title, desc: dir.description };
    console.log(`[snapshot] ${c}: ${order[c].length}`);
  }

  // 2. Detail pages: developer, website, version, skills, apps, starter prompts.
  const parseDetail = (html) => {
    const a = parseHTML(html).querySelector("article");
    if (!a) return null;
    const o = { sec: {} };
    o.prompts = [...a.querySelectorAll('[data-testid="plugin-starter-prompt"]')].map((e) => e.getAttribute("aria-label")).slice(0, 3);
    o.long = ([...a.children].find((e) => e.tagName === "P")?.textContent || "").trim().slice(0, 700);
    a.querySelectorAll("section").forEach((s) => {
      const h = s.querySelector("h2")?.textContent.trim();
      if (!h || h === "Information") return;
      o.sec[h] = [...s.querySelectorAll("h2 ~ div > *")].map((e) => e.textContent.trim()).filter(Boolean).slice(0, 20);
    });
    a.querySelectorAll("dl > div").forEach((d) => {
      const k = d.querySelector("dt")?.textContent.trim();
      const dd = d.querySelector("dd");
      if (!k || !dd || k === "Privacy Policy" || k === "Terms of Service") return;
      const link = dd.querySelector("a");
      o[k] = link ? link.getAttribute("href") : dd.textContent.trim();
    });
    return o;
  };

  const details = {};
  const queue = Object.keys(plugins);
  let done = 0;
  const worker = async () => {
    while (queue.length) {
      const id = queue.shift();
      for (let attempt = 0; attempt < 3; attempt++) {
        try {
          const r = await fetch(`/plugins/${id}`, HTML);
          if (r.status === 429) { await sleep(5000 * (attempt + 1)); continue; }
          const d = parseDetail(await r.text());
          if (d) { details[id] = d; break; }
        } catch { await sleep(2000); }
      }
      if (++done % 250 === 0) console.log(`[snapshot] details ${done}/${Object.keys(plugins).length}`);
      await sleep(PAUSE_MS);
    }
  };
  await Promise.all(Array.from({ length: WORKERS }, worker));

  // 3. Download.
  const snapshot = { snapshot_date: new Date().toISOString().slice(0, 10), stats, order, plugins, details };
  const url = URL.createObjectURL(new Blob([JSON.stringify(snapshot)], { type: "application/json" }));
  Object.assign(document.createElement("a"), { href: url, download: "directory-snapshot.json" }).click();
  console.log(`[snapshot] done: ${Object.keys(plugins).length} plugins, ${Object.keys(details).length} with details`);
})();
