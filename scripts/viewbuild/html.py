"""Generate product B: a single self-contained interactive HTML file.

Data is inlined as JSON (no runtime fetch, so it works from file://).
Rendering is hand-written SVG + vanilla JS — zero third-party deps.
Tabs: worldline tree, timeline, factions, characters. Pan/zoom + click.
"""
import json

_HTML = r"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ · 世界观视图</title>
<style>
  :root{--bg:#0e1116;--panel:#161b22;--ink:#e6edf3;--mut:#8b949e;
        --line:#30363d;--accent:#7c9cff;--warm:#e3b341;--rival:#f7768e;}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
       font:14px/1.5 -apple-system,Segoe UI,Roboto,"PingFang SC",sans-serif}
  header{padding:14px 18px;border-bottom:1px solid var(--line)}
  header h1{margin:0;font-size:16px}
  header .sub{color:var(--mut);font-size:12px;margin-top:2px}
  .tabs{display:flex;gap:4px;padding:8px 12px;border-bottom:1px solid var(--line);flex-wrap:wrap}
  .tab{padding:6px 12px;border-radius:8px;cursor:pointer;color:var(--mut);user-select:none}
  .tab:hover{background:var(--panel)}
  .tab.on{background:var(--panel);color:var(--ink);border:1px solid var(--line)}
  .stage{position:relative;height:calc(100vh - 150px);overflow:hidden}
  svg{width:100%;height:100%;cursor:grab}
  svg.drag{cursor:grabbing}
  .node{cursor:pointer}
  .nlabel{fill:var(--ink);font-size:13px}
  .edge{stroke:var(--line);stroke-width:1.6}
  .edge.rival{stroke:var(--rival);stroke-dasharray:0}
  .edge.dash{stroke-dasharray:5 4}
  .elabel{fill:var(--mut);font-size:11px}
  .hint{position:absolute;right:12px;bottom:10px;color:var(--mut);font-size:11px}
  #detail{position:absolute;left:12px;top:12px;max-width:300px;background:var(--panel);
          border:1px solid var(--line);border-radius:10px;padding:10px 12px;display:none}
  #detail h3{margin:0 0 6px;font-size:14px}
  #detail div{color:var(--mut);font-size:12px;margin:2px 0}
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <div class="sub">自动生成的世界观视图 · 拖拽平移 · 滚轮缩放 · 点击查看 · 改 codex 后重跑脚本同步</div>
</header>
<div class="tabs" id="tabs"></div>
<div class="stage">
  <svg id="svg"><g id="root"></g></svg>
  <div id="detail"></div>
  <div class="hint">拖拽平移 · 滚轮缩放</div>
</div>
<script>
const DATA = __DATA__;
const svg=document.getElementById('svg'), root=document.getElementById('root'),
      detail=document.getElementById('detail'), tabsEl=document.getElementById('tabs');
let view={x:40,y:40,k:1};
function apply(){root.setAttribute('transform',`translate(${view.x},${view.y}) scale(${view.k})`);}
function SVG(tag,attr){const e=document.createElementNS('http://www.w3.org/2000/svg',tag);
  for(const k in attr)e.setAttribute(k,attr[k]);return e;}
function clear(){root.innerHTML='';detail.style.display='none';}
function showDetail(title,rows){detail.innerHTML='<h3>'+title+'</h3>'+
  rows.map(r=>'<div>'+r+'</div>').join('');detail.style.display='block';}

function drawNode(x,y,label,kind,onClick){
  const g=SVG('g',{class:'node',transform:`translate(${x},${y})`});
  const w=Math.max(60,label.length*9+24);
  let shape;
  if(kind==='era'){shape=SVG('rect',{x:-w/2,y:-16,width:w,height:32,rx:8,
     fill:'#1f2937',stroke:'#3b4a63'});}
  else if(kind==='faction'){shape=SVG('rect',{x:-w/2,y:-18,width:w,height:36,rx:4,
     fill:'#2a2118',stroke:'#5a4a30'});}
  else if(kind==='ext'){shape=SVG('rect',{x:-w/2,y:-15,width:w,height:30,rx:15,
     fill:'#181d24',stroke:'#30363d'});}
  else if(kind==='wl'){shape=SVG('rect',{x:-w/2,y:-17,width:w,height:34,rx:17,
     fill:'#15223b',stroke:'#3a5a9a'});}
  else{shape=SVG('rect',{x:-w/2,y:-17,width:w,height:34,rx:17,
     fill:'#15223b',stroke:'#3a5a9a'});}
  g.appendChild(shape);
  const t=SVG('text',{class:'nlabel','text-anchor':'middle',dy:'0.35em'});t.textContent=label;
  g.appendChild(t);
  if(onClick)g.addEventListener('click',e=>{e.stopPropagation();onClick();});
  root.appendChild(g);return g;
}
function drawEdge(x1,y1,x2,y2,label,cls){
  const e=SVG('line',{x1,y1,x2,y2,class:'edge '+(cls||'')});root.appendChild(e);
  if(label){const t=SVG('text',{class:'elabel','text-anchor':'middle',
     x:(x1+x2)/2,y:(y1+y2)/2-4});t.textContent=label;root.appendChild(t);}
}

const RENDER={
  worldline(){clear();const ws=DATA.worldline;
    const trunk=ws.find(w=>w.status==='trunk')||{name:'α',id:'trunk'};
    const branches=ws.filter(w=>w.status!=='trunk');
    const cx=120, top=70, gap=150;
    let ty=top+gap*Math.max(0,branches.length-1)/2;
    drawNode(cx,ty,trunk.name,'wl',()=>showDetail(trunk.name,
      ['主干 trunk','不动点: '+((trunk.fixed_points||[]).join('、')||'—')]));
    const bx=cx+360, convx=cx+720;
    branches.forEach((w,i)=>{const y=top+gap*i;
      drawEdge(cx,ty,bx,y,'@'+(w.diverge_at||'?'),'dash');
      drawNode(bx,y,w.name,'wl',()=>showDetail(w.name,
        ['分叉: '+(w.diverge_at||'?'),'成因: '+(w.diverge_trigger||'—'),
         '收束于: '+(w.converges||'—'),'状态: '+(w.status||'—')]));
      if(w.converges){drawEdge(bx,y,convx,ty,'收束: '+w.converges,'');}
    });
    if(branches.some(w=>w.converges))
      drawNode(convx,ty,'第一次回声','era',()=>showDetail('收束点',['所有线在此重合']));
  },
  era(){clear();const es=DATA.era.slice().sort((a,b)=>(a.order||0)-(b.order||0));
    let x=40;const y=120;
    es.forEach((e,i)=>{const label=e.name+' ('+(e.span_start||'?')+'–'+(e.span_end||'?')+')';
      if(i>0)drawEdge(x-90,y,x,y,'','');
      drawNode(x,y,label,'era',()=>showDetail(e.name,
        ['时段: '+(e.span_start||'?')+'–'+(e.span_end||'?'),
         '质变点: '+((e.tipping_points||[]).join('、')||'—')]));
      (e.tipping_points||[]).forEach((tp,j)=>{
        drawEdge(x,y,x,y+70+j*44,'','dash');
        drawNode(x,y+95+j*44,tp,'ext',null);});
      x+=Math.max(180,label.length*11+80);});
  },
  faction(){clear();const fs=DATA.faction;const cx=320,cy=80,r=140;
    const pos={};fs.forEach((f,i)=>{const a=-Math.PI/2+i*2*Math.PI/Math.max(1,fs.length);
      pos[f.id]={x:cx+Math.cos(a)*r,y:cy+220+Math.sin(a)*r};});
    const drawn={};
    fs.forEach(f=>{(f.rivals||[]).forEach(rv=>{const key=[f.id,rv].sort().join('|');
      if(pos[rv]&&!drawn[key]){drawEdge(pos[f.id].x,pos[f.id].y,pos[rv].x,pos[rv].y,'宿敌','rival');drawn[key]=1;}});});
    fs.forEach(f=>{if(f.sponsor){const sx=pos[f.id].x,sy=pos[f.id].y-90;
      drawEdge(sx,sy,pos[f.id].x,pos[f.id].y,'赞助','dash');
      drawNode(sx,sy,f.sponsor,'ext',null);}});
    fs.forEach(f=>drawNode(pos[f.id].x,pos[f.id].y,f.name,'faction',()=>showDetail(f.name,
      ['生于: '+(f.born_from||'—'),'宿敌: '+((f.rivals||[]).join('、')||'—'),
       '赞助/绑定: '+(f.sponsor||'—'),'分裂风险: '+(f.splits_risk||'—')])));
  },
  character(){clear();const cs=DATA.character;const cx=340,cy=300,r=160;
    const pos={};cs.forEach((c,i)=>{const a=i*2*Math.PI/Math.max(1,cs.length);
      pos[c.id]={x:cx+Math.cos(a)*r,y:cy+Math.sin(a)*r};});
    const ext={};let ei=0;const dpair={};
    cs.forEach(c=>{(c.relations||[]).forEach(rel=>{
      let tx,ty;if(pos[rel.to]){const key=[c.id,rel.to].sort().join('|');
        if(dpair[key])return;dpair[key]=1;
        tx=pos[rel.to].x;ty=pos[rel.to].y;
        drawEdge(pos[c.id].x,pos[c.id].y,tx,ty,rel.type,'');}
      else{if(!ext[rel.to]){ext[rel.to]={x:60,y:80+ei*70};ei++;}
        drawEdge(pos[c.id].x,pos[c.id].y,ext[rel.to].x,ext[rel.to].y,rel.type,'dash');}});});
    for(const name in ext)drawNode(ext[name].x,ext[name].y,name,'ext',null);
    cs.forEach(c=>drawNode(pos[c.id].x,pos[c.id].y,c.name,'char',()=>showDetail(c.name,
      ['所属: '+((c.affiliation||[]).join('、')||'—'),
       '线: '+((c.lines||[]).join('、')||'—'),
       '关系: '+((c.relations||[]).map(r=>r.type+'→'+r.to).join('；')||'—')])));
  }
};

const TABS=[['worldline','世界线树'],['era','时代主轴'],['faction','派系关系'],['character','人物关系']];
let active=null;
function selectTab(key){active=key;
  [...tabsEl.children].forEach(c=>c.classList.toggle('on',c.dataset.k===key));
  view={x:40,y:40,k:1};apply();RENDER[key]();}
TABS.forEach(([k,label])=>{if((DATA[k]||[]).length===0)return;
  const d=document.createElement('div');d.className='tab';d.dataset.k=k;d.textContent=label;
  d.onclick=()=>selectTab(k);tabsEl.appendChild(d);});

// pan & zoom
let drag=null;
svg.addEventListener('mousedown',e=>{drag={x:e.clientX,y:e.clientY};svg.classList.add('drag');});
window.addEventListener('mouseup',()=>{drag=null;svg.classList.remove('drag');});
window.addEventListener('mousemove',e=>{if(!drag)return;
  view.x+=e.clientX-drag.x;view.y+=e.clientY-drag.y;drag={x:e.clientX,y:e.clientY};apply();});
svg.addEventListener('wheel',e=>{e.preventDefault();
  const f=e.deltaY<0?1.1:0.9;view.k=Math.max(0.3,Math.min(3,view.k*f));apply();},{passive:false});
svg.addEventListener('click',()=>detail.style.display='none');

const first=TABS.find(([k])=>(DATA[k]||[]).length>0);
if(first)selectTab(first[0]);
apply();
</script>
</body>
</html>"""


def build_html(model, title):
    data = {
        "worldline": model.get("worldline", []),
        "era": model.get("era", []),
        "faction": model.get("faction", []),
        "character": model.get("character", []),
    }
    payload = json.dumps(data, ensure_ascii=False)
    return _HTML.replace("__DATA__", payload).replace("__TITLE__", title)
