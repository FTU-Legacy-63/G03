const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const test = require('node:test');
const assert = require('node:assert/strict');
const htmlPath = process.argv[2] || path.join(__dirname, 'omo_refactored_v64(4).html');
const html = fs.readFileSync(
  path.join(__dirname, 'omo_refactored_v64.html'),
  'utf8'
);

function section(start, end) {
  const a = html.indexOf(start);
  const b = html.indexOf(end, a + start.length);
  if (a < 0 || b < 0) throw new Error(`Could not find section: ${start} -> ${end}`);
  return html.slice(a, b);
}
function makeModal() {
  const classes = new Set();
  return { classes, classList: {
    add: x => classes.add(x),
    remove: x => classes.delete(x),
    contains: x => classes.has(x),
  }};
}
function setupLearningContext() {
  const title = {textContent: ''};
  const content = {innerHTML: ''};
  const learningModal = makeModal();
  const guideModal = makeModal();
  const nodes = {
    'learning-card-title': title,
    'learning-card-content': content,
    'learning-card-modal': learningModal,
    'guide-modal': guideModal,
  };
  let keydownHandler = null;
  const document = {
    getElementById: id => nodes[id] || null,
    addEventListener: (name, fn) => { if (name === 'keydown') keydownHandler = fn; },
  };
  const src = section('const learningCards={', '\n/* =====================================================================\n   PAPER GAME — CANONICAL LOGIC');
  const ctx = {document};
  vm.createContext(ctx);
  vm.runInContext(src + '\nglobalThis.cards = learningCards;', ctx);
  return {ctx, title, content, learningModal, guideModal, getKeydown: () => keydownHandler};
}

const macroFn = section('function pgMacroTrendSVG(history,uptoPhase=pgPhase){', '\nfunction pgOutstandingHTML');
const outcomeFn = section('function pgFinalEconomicOutcome(result){', '\nfunction pgCheckpointEconomicComment');

// Learning Card and Guide behavior
test('learning-card registry: every entry has a title and content', () => {
  const {ctx} = setupLearningContext();
  const cards = ctx.cards;
  assert.ok(Object.keys(cards).length > 0);
  for (const [key, card] of Object.entries(cards)) {
    assert.ok(card.title && card.title.trim(), `${key} title missing`);
    assert.ok(card.content && card.content.trim(), `${key} content missing`);
  }
});

test('opening a known Learning Card populates title/content and opens modal', () => {
  const {ctx, title, content, learningModal} = setupLearningContext();
  ctx.openLearningCard('auction');
  assert.equal(title.textContent, 'Auction method');
  assert.match(content.innerHTML, /Interest-rate auction/);
  assert.equal(learningModal.classList.contains('open'), true);
});

test('unknown Learning Card key does not open or overwrite existing content', () => {
  const {ctx, title, content, learningModal} = setupLearningContext();
  title.textContent = 'Existing'; content.innerHTML = 'Existing content';
  ctx.openLearningCard('not-a-real-card');
  assert.equal(title.textContent, 'Existing');
  assert.equal(content.innerHTML, 'Existing content');
  assert.equal(learningModal.classList.contains('open'), false);
});

test('closing Learning Card removes open state', () => {
  const {ctx, learningModal} = setupLearningContext();
  ctx.openLearningCard('auction');
  ctx.closeLearningCard();
  assert.equal(learningModal.classList.contains('open'), false);
});

test('Guide opens and closes', () => {
  const {ctx, guideModal} = setupLearningContext();
  ctx.openGuideModal();
  assert.equal(guideModal.classList.contains('open'), true);
  ctx.closeGuideModal();
  assert.equal(guideModal.classList.contains('open'), false);
});

test('Escape closes both Guide and Learning Card', () => {
  const {ctx, guideModal, learningModal, getKeydown} = setupLearningContext();
  ctx.openGuideModal(); ctx.openLearningCard('auction');
  getKeydown()({key: 'Escape'});
  assert.equal(guideModal.classList.contains('open'), false);
  assert.equal(learningModal.classList.contains('open'), false);
});

// Macro chart rendering behavior
test('macro chart ignores non-checkpoint phases', () => {
  const ctx = {pgPhase: 2, getPhaseDisplayDate: p => `D${p}`};
  vm.createContext(ctx); vm.runInContext(macroFn, ctx);
  const svg = ctx.pgMacroTrendSVG([{kind:'result', phase:2, gdp:7, inflation:9}], 2);
  assert.equal((svg.match(/<circle\b/g) || []).length, 0);
  assert.match(svg, /GDP growth and inflation/);
});

test('macro chart plots only published checkpoint observations up to requested phase', () => {
  const ctx = {pgPhase: 3, getPhaseDisplayDate: p => `D${p}`};
  vm.createContext(ctx); vm.runInContext(macroFn, ctx);
  const rows = [
    {kind:'initial', phase:1, gdp:6, inflation:4},
    {kind:'result', phase:2, gdp:99, inflation:99},
    {kind:'result', phase:3, gdp:5.5, inflation:4.2},
    {kind:'result', phase:6, gdp:7, inflation:2},
  ];
  const svg = ctx.pgMacroTrendSVG(rows, 3);
  assert.equal((svg.match(/<circle\b/g) || []).length, 4); // GDP + inflation at opening and Phase 3
  assert.match(svg, /PHASE 3/);
  assert.doesNotMatch(svg, /PHASE 6 ·/);
});

test('macro chart ignores null and empty checkpoint values instead of plotting zero', () => {
  const ctx = {pgPhase: 3, getPhaseDisplayDate: p => `D${p}`};
  vm.createContext(ctx); vm.runInContext(macroFn, ctx);
  const svg = ctx.pgMacroTrendSVG([
    {kind:'initial', phase:1, gdp:6, inflation:4},
    {kind:'result', phase:3, gdp:null, inflation:''},
  ], 3);
  assert.equal((svg.match(/<circle\b/g) || []).length, 2);
});

// This is an expected-behavior test: it should expose the null/empty conversion bug if present.
test('final economic outcome treats null/empty macro values as pending', () => {
  const ctx = {}; vm.createContext(ctx); vm.runInContext(outcomeFn, ctx);
  for (const result of [{gdp_growth:null, inflation:null}, {gdp_growth:'', inflation:''}]) {
    assert.equal(ctx.pgFinalEconomicOutcome(result).title, 'Economic outcome pending');
  }
});
