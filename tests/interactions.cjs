const {test,before,after}=require('node:test');
const assert=require('node:assert/strict');
const {spawn}=require('node:child_process');
const path=require('node:path');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
let browser,server,base;const errors=[];
before(async()=>{base=process.env.PRODES_BASE;if(!base){const port=18765;server=spawn('python3',['-m','http.server',String(port),'--bind','127.0.0.1'],{cwd:path.resolve(__dirname,'..'),stdio:'ignore'});base=`http://127.0.0.1:${port}/`;for(let i=0;i<50;i++){try{if((await fetch(base,{method:'HEAD'})).ok)break;}catch{}await new Promise(r=>setTimeout(r,100));}}
 browser=await chromium.launch();});
after(async()=>{await browser?.close();server?.kill();assert.deepEqual(errors,[],'Erros de JavaScript no navegador');});
async function page(query){const p=await browser.newPage({viewport:{width:1600,height:1000}});p.on('pageerror',e=>errors.push(e.message));await p.goto(base+query);await p.waitForSelector('#g .it');return p;}
const ready=p=>p.waitForFunction(()=>!agendado);
const near=(a,b)=>assert.ok(Math.abs(a-b)<.02,`${a} != ${b}`);
async function focus(p,names){await p.evaluate(ns=>{ns.forEach(n=>foco.add(n));aplicaFoco()},names);}

test('Combinações dependentes permanecem disponíveis e podem ser escolhidas por comparação',async()=>{
 const p=await page('?modo=det&e=territorial:sep,sobrep_imovel:sep&g=barra');await focus(p,['UC Estadual + US','Imóvel com sobreposição ínfima']);await p.locator('[data-filtra-foco]').click();
 assert.equal(await p.locator('[data-grupo-combo]').count(),2);near(await p.evaluate(()=>escolhaFiltro.atual),17925188.71359);
 await p.locator('[data-grupo-combo="1"]').uncheck();near(await p.evaluate(()=>escolhaFiltro.atual),5495090.923);
 await p.locator('[data-grupo-combo="1"]').check();await p.locator('[data-grupo-combo="0"]').uncheck();near(await p.evaluate(()=>escolhaFiltro.atual),0);
 await p.locator('[data-grupo-combo="0"]').check();await p.locator('[data-como="opcoes"]').click();await ready(p);near(await p.evaluate(()=>window.__ult.area),17925188.71359);await p.close();
});

test('Categorias da mesma comparação usam OU; CAR sem ambiguidade não entra na pergunta',async()=>{
 const p=await page('?modo=det&e=car:sep,fundiario:agr,app_rl:agr&g=sank');await focus(p,['Em CAR','CAR adere ao SIGEF (≥90%)','Reserva Legal','APP']);await p.locator('[data-filtra-foco]').click();
 assert.ok(!await p.evaluate(()=>escolhaFiltro.nomes.includes('Em CAR')));assert.equal(await p.locator('[data-grupo-combo]').count(),2);assert.match(await p.locator('.fopcaoGrupo').last().innerText(),/ ou /);
 const total=await p.evaluate(()=>escolhaFiltro.atual);await p.locator('[data-como="opcoes"]').click();await ready(p);near(await p.evaluate(()=>window.__ult.area),total);await p.close();
 const car=await page('?modo=det&e=car:sep&g=barra');await focus(car,['Em CAR']);await car.locator('[data-filtra-foco]').click();await ready(car);assert.equal(await car.locator('.fescolha').count(),0);near(await car.evaluate(()=>window.__ult.area),487672102.27316);await car.close();
});

test('Todas as seções da tabela expandem categorias pequenas pelo teclado',async()=>{
 for(const e of ['prodes:sep,territorial:sep','prodes:sep,car:sep,territorial:sep','territorial:sep,prodes:sep']){
  const p=await page('?modo=det&u=recorte&a=2025&e='+e+'&g=sank');const j=e.startsWith('territorial')?0:e.split(',').length-1;const toggle=p.locator(`[data-miudas="${j}"]`);assert.ok(await toggle.isVisible());
  const before=await p.locator('#tab [data-nome]').count();await toggle.focus();await p.keyboard.press('Enter');assert.equal(await p.locator(`[data-miudas="${j}"]`).getAttribute('aria-expanded'),'true');assert.ok(await p.locator('#tab [data-nome]').count()>before);
  const target='CAR + UC Municipal + PI';const row=p.locator('#tab tr[data-nome]').filter({has:p.locator('td',{hasText:'Imóvel no CAR + UC municipal — proteção integral'})});assert.ok(await row.count()>0);
  const actual=p.locator('#tab tr[data-nome]').filter({has:p.locator('td',{hasText:/^Imóvel no CAR \+ UC municipal — proteção integral$/})});await actual.focus();await p.keyboard.press('Enter');assert.ok(await p.evaluate(n=>foco.has(n),target));
  await p.locator(`[data-miudas="${j}"]`).click();assert.equal(await p.locator(`[data-miudas="${j}"]`).getAttribute('aria-expanded'),'false');assert.ok(await p.locator(`tr[data-nome="${target}"]`).isVisible());await p.close();
 }
});

test('Uma limpeza global inclui seleção, filtros e UF e mantém universo e anos',async()=>{
 const p=await page('?modo=det&e=territorial:sep&g=barra');assert.equal(await p.locator('#limpar').count(),0);await focus(p,['CAR']);assert.ok(await p.locator('.filtroLimpaTudo').isVisible());await p.locator('.filtroLimpaTudo').click();await ready(p);assert.equal(await p.evaluate(()=>foco.size),0);assert.equal(await p.locator('.filtroLimpaTudo').count(),0);
 await p.locator('#uRecorte').click();await ready(p);await p.locator('#selAnos [data-ano="2024"]').click();await ready(p);const years=await p.evaluate(()=>[...anosSel]);await p.locator('#selUF').selectOption('15');await ready(p);await p.evaluate(()=>{estado[9]=1;classesNeg.add(15);sincChips();agenda()});await ready(p);await p.locator('.filtroLimpaTudo').click();await ready(p);
 assert.deepEqual(await p.evaluate(()=>({uf:ufSel,e:Object.keys(estado),fg:filtrosG.length,cs:classesSel.size,cn:classesNeg.size,f:foco.size,p:pilhaFG.length,u:universo,a:[...anosSel]})),{uf:0,e:[],fg:0,cs:0,cn:0,f:0,p:0,u:'recorte',a:years});await p.close();
});

test('Barras são priorizadas; gráficos proporcionais informam a normalização',async()=>{
 const p=await page('?modo=det&e=territorial:som&g=tree');assert.match(await p.locator('#gNota').innerText(),/normalizados pela soma/);assert.match(await p.locator('#g').textContent(),/56,1%/);const area=await p.evaluate(()=>window.__ult.area);await p.locator('.verBarras').click();assert.equal(await p.evaluate(()=>vis),'barra');near(await p.evaluate(()=>window.__ult.area),area);
 await p.locator('#vSun').click();await ready(p);assert.match(await p.locator('#g').textContent(),/869.814.416/);const mode=p.locator('#eixos select.modo').first();await mode.selectOption('sep');await ready(p);await mode.selectOption('som');await ready(p);assert.equal(await p.evaluate(()=>vis),'barra');await p.close();
 const q=await page('?modo=det&e=car:sep,territorial:som&g=barra');assert.ok(await q.evaluate(()=>window.__ult.sobrepoeSegundo));assert.match(await q.locator('#gNota').innerText(),/segmentos são normalizados/);assert.match(await q.locator('#g .bar').first().textContent(),/100%/);await q.close();
});

test('Celular e modos mantêm limpeza e controles acessíveis sem transbordamento',async()=>{
 const p=await page('?modo=det&u=recorte&a=2025&e=prodes:sep,territorial:sep&g=sank');for(const mode of ['simples','det']){await p.locator(`[data-modo="${mode}"]`).click();await ready(p);for(const width of [1600,768,390,320]){await p.setViewportSize({width,height:900});await p.waitForFunction(()=>!!document.querySelector('.exportMobile')===matchMedia('(max-width:700px)').matches);assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);assert.ok(await p.locator('#frase').isVisible());}}
 await p.close();
});

test('Áreas das opções conferem com cálculo direto após filtros e uma troca de contexto cancela a pergunta',async()=>{
 const p=await page('?modo=det&e=territorial:sep,sobrep_imovel:sep&g=barra');await p.evaluate(()=>{estado[7]=2;fonteEstado='det';classesNeg.add(15);ufSel=13;sincChips();agenda()});await ready(p);
 const checks=await p.evaluate(()=>{const names=['UC Estadual + US','Imóvel com sobreposição ínfima'];const itens=names.map((nome,i)=>({nome,r:{i,d:i?'sobrep_imovel':'territorial',m:'sep',labs:[nome]}}));pedeFiltro(itens,()=>names.join(' e '),null);if(!escolhaFiltro)throw Error('Era esperada uma pergunta');const e=escolhaFiltro,out=[];for(let mask=0;mask<(1<<e.grupos.length);mask++){e.grupos.forEach((_,i)=>e.altera(i,!!(mask&(1<<i))));const inc=new Set(e.grupos.flatMap((g,i)=>(mask&(1<<i))?g.itens:[]));const esperado=areaFiltrada(itens.map(x=>({d:x.r.d,m:inc.has(x)?'som':'sep',labs:x.r.labs,nome:x.nome,q:modo,p:1})),null);out.push([e.atual,esperado]);}return out;});for(const [a,b] of checks)near(a,b);
 assert.ok(await p.locator('.fescolha').isVisible());await p.locator('#uRecorte').click();await ready(p);assert.equal(await p.locator('.fescolha').count(),0);await p.close();
});

test('Autoconferência independente dos dados permanece aprovada',async()=>{
 const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message));await p.goto(base+'?modo=det&validar',{timeout:120000});const v=await p.locator('#painelValidacao').innerText({timeout:120000});assert.match(v,/Autoconferência aprovada/);for(const total of ['472/472','60/60','78/78'])assert.ok(v.includes(total));await p.close();
});

test('Sankey com o total de cada categoria: combinações à esquerda, totais à direita',async()=>{
 const p=await page('?modo=simples&e=territorial:som&g=sank');
 assert.deepEqual(await p.evaluate(()=>[vis,eixos[0].m]),['sank','som']);
 assert.match(await p.locator('#gNota').innerText(),/contados mais de uma vez/);
 const [esq,dir,area]=await p.evaluate(()=>[[...document.querySelectorAll('#g rect[data-c="0"]')].reduce((s,r)=>s+ +r.dataset.v,0),[...document.querySelectorAll('#g rect[data-c="1"]')].reduce((s,r)=>s+ +r.dataset.v,0),window.__ult.area]);
 assert.ok(Math.abs(esq-area)<1,'as combinações somam a área'); assert.ok(dir>area,'os totais passam da área');
 await p.close();
 const q=await page('?modo=det&e=car:sep,territorial:sep&g=sank');
 assert.equal(await q.locator('#eixos select.modo').first().locator('option[value="som"]').isDisabled(),true);
 await q.close();
});
