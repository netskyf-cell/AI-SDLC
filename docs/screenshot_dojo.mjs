import { chromium } from 'playwright-core';
import fs from 'fs';
// Run from the repo root: node docs/screenshot_dojo.mjs (needs playwright-core + Chromium).
import path from 'path';
const SRC = 'file://' + path.resolve('dojo/ai-sdlc.html');
const OUT = path.resolve('docs/dojo/img');
fs.mkdirSync(OUT, { recursive: true });
let browser;
try { browser = await chromium.launch(); } catch { browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); }
const page = await browser.newPage({ viewport: { width: 1200, height: 900 }, deviceScaleFactor: 2 });
const big = await browser.newPage({ viewport: { width: 1200, height: 900 }, deviceScaleFactor: 4 });
await page.goto(SRC);
const ids = await page.$$eval('section.site-page', s => s.map(x => x.id));
const manifest = {};
for (const id of ids) {
  await page.goto(`${SRC}#${id}`); await page.waitForTimeout(150);
  await page.evaluate(() => document.fonts.ready);
  await big.goto(`${SRC}#${id}`); await big.waitForTimeout(150);
  await big.evaluate(() => document.fonts.ready);
  const css = '.reader-panel-zoom{display:none!important}';
  await page.addStyleTag({ content: css }); await big.addStyleTag({ content: css });
  const els = await page.$$(`#${id} main .reader-screen, #${id} main .reader-panel`);
  const bigEls = await big.$$(`#${id} main .reader-screen, #${id} main .reader-panel`);
  manifest[id] = [];
  for (let i = 0; i < els.length; i++) {
    const name = `${id}-${String(i + 1).padStart(2, '0')}.png`;
    const isPanel = await els[i].evaluate(e => e.classList.contains('reader-panel'));
    const el = isPanel ? (await bigEls[i].$('.reader-panel-frame')) : els[i];
    await el.scrollIntoViewIfNeeded();
    await el.screenshot({ path: `${OUT}/${name}` });
    manifest[id].push(name);
  }
  console.log(id, els.length);
}
fs.writeFileSync(`${OUT}/manifest.json`, JSON.stringify(manifest, null, 1));
await browser.close();
