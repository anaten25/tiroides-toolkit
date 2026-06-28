import json

el_id = [0]
def nid(): el_id[0] += 1; return f"e{el_id[0]}"

def rect(x,y,w,h,**kw):
    e={"type":"rectangle","id":nid(),"x":x,"y":y,"width":w,"height":h,"strokeColor":"#1e1e1e","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":2,"roughness":1,"opacity":100,"roundness":{"type":3}}
    e.update(kw); return e

def text(x,y,txt,size=20,**kw):
    e={"type":"text","id":nid(),"x":x,"y":y,"width":len(txt)*size*0.35,"height":size*1.2,"text":txt,"fontSize":size,"fontFamily":1,"strokeColor":"#1e1e1e","originalText":txt,"autoResize":True,"textAlign":"left"}
    e.update(kw); return e

def arrow(x,y,w,h,**kw):
    e={"type":"arrow","id":nid(),"x":x,"y":y,"width":w,"height":h,"points":[[0,0],[w,h]],"endArrowhead":"arrow","strokeColor":"#888888","strokeWidth":1,"roughness":0}
    e.update(kw); return e

def phone(x,y,w=340,h=660):
    it=[rect(x,y,w,h,strokeColor="#555",strokeWidth=3,backgroundColor="#fff",fillStyle="solid",roughness=0)]
    it.append(rect(x,y,w,52,backgroundColor="#1a5276",fillStyle="solid",strokeWidth=0,roughness=0))
    it.append(text(x+12,y+14,"Tiroides Toolkit",20,strokeColor="#fff"))
    it.append(text(x+w-60,y+8,"9:41",14,strokeColor="#fff"))
    # tab bar
    by=y+h-48
    it.append(rect(x,by,w,48,backgroundColor="#f8f9fa",fillStyle="solid",strokeWidth=0,roughness=0))
    tabs=["Evaluacion","Crecim.","Molecular","Seguim."]
    tw=w/4
    for i,l in enumerate(tabs):
        it.append(text(x+i*tw+8,by+12,l,11,strokeColor="#1a5276" if i==0 else "#95a5a6"))
    return it

def card(x,y,w,h,bg="#fff",**kw):
    r={"backgroundColor":bg,"fillStyle":"solid","strokeWidth":0,"roughness":0}
    r.update(kw)
    return rect(x,y,w,h,**r)

# ==================== SCREEN 1: Evaluacion ====================
p1x,p1y=80,200
s1=phone(p1x,p1y)
s1.append(text(p1x+16,p1y+66,"Evaluacion del Nodulo",15,strokeColor="#1a5276"))
s1.append(card(p1x+12,p1y+90,316,28,bg="#ebf5fb"))
s1.append(text(p1x+18,p1y+94,"ACR TI-RADS: 7 pts → TR5 - Alta sospecha",11,strokeColor="#1a5276"))

s1.append(text(p1x+16,p1y+130,"Factores de Riesgo Clinico",13,strokeColor="#2c3e50"))
facts=[("Sexo","Masculino"),("Edad","45 a"),("Hx familiar","Si"),("Radiacion","No"),("Crec. rapido","Si")]
for i,(l,v) in enumerate(facts):
    bg="#e8f8f5" if v=="Si" else "#f8f9fa"
    s1.append(card(p1x+14,p1y+150+i*22,145,20,bg=bg))
    s1.append(text(p1x+18,p1y+152+i*22,f"{l}: {v}",10,strokeColor="#2c3e50"))

s1.append(text(p1x+174,p1y+130,"Crecimiento",13,strokeColor="#2c3e50"))
s1.append(card(p1x+172,p1y+150,156,62,bg="#fff3bf"))
s1.append(text(p1x+178,p1y+154,"Ene 2025: 2.1x1.8x1.5",9,strokeColor="#2c3e50"))
s1.append(text(p1x+178,p1y+168,"Jun 2026: 2.3x2.0x1.7",9,strokeColor="#2c3e50"))
s1.append(text(p1x+178,p1y+184,"Vol: +33% en 12 m",9,strokeColor="#c0392b"))

s1.append(card(p1x+12,p1y+222,316,62,bg="#fdedec"))
s1.append(text(p1x+18,p1y+226,"RIESGO ALTO (Combinado)",14,strokeColor="#c0392b"))
s1.append(text(p1x+18,p1y+246,"TR5 + sexo M + hx familiar + crecimiento activo",9,strokeColor="#2c3e50"))
s1.append(text(p1x+18,p1y+262,"FNA indicado (>=1.0 cm). Molecular si Bethesda III/IV",9,strokeColor="#2c3e50"))

s1.append(text(p1x+16,p1y+298,"Sintomas",13,strokeColor="#2c3e50"))
for i,s in enumerate(["[x] Disfonia","[ ] Disfagia","[x] Compresion"]):
    bg="#fdedec" if "[x]" in s else "#f8f9fa"
    s1.append(card(p1x+14,p1y+318+i*22,180,20,bg=bg))
    s1.append(text(p1x+18,p1y+320+i*22,s,10,strokeColor="#2c3e50"))

s1.append(card(p1x+50,p1y+395,240,34,bg="#27ae60"))
s1.append(text(p1x+60,p1y+402,"Generar Plan de Seguimiento",11,strokeColor="#fff"))

# ==================== SCREEN 2: Growth Tracker ====================
p2x,p2y=545,200
s2=phone(p2x,p2y)
s2.append(text(p2x+16,p2y+66,"Growth Tracker",15,strokeColor="#1a5276"))
s2.append(text(p2x+16,p2y+95,"Nuevo Control (3D)",13,strokeColor="#2c3e50"))
s2.append(card(p2x+12,p2y+112,316,108,bg="#f8f9fa"))
for i,(l,v) in enumerate([("Fecha:","2026-06-22"),("L (cm):","2.3"),("A (cm):","2.0"),("P (cm):","1.7")]):
    s2.append(text(p2x+18,p2y+116+i*24,l,11,strokeColor="#2c3e50"))
    s2.append(card(p2x+95,p2y+114+i*24,80,20,bg="#fff",strokeWidth=1))
    s2.append(text(p2x+99,p2y+116+i*24,v,10,strokeColor="#555"))

s2.append(card(p2x+12,p2y+230,316,50,bg="#ebf5fb"))
s2.append(text(p2x+18,p2y+234,"Volumen: 3.91 cc (elipsoide)",13,strokeColor="#1a5276"))
s2.append(text(p2x+18,p2y+252,"Previo: 2.95 cc → Diferencia: +0.96 cc (+33%)",9,strokeColor="#2c3e50"))

s2.append(card(p2x+12,p2y+290,316,38,bg="#fdedec"))
s2.append(text(p2x+18,p2y+294,"ALERTA: +33% en 12 meses (umbral 50% para re-BAAF)",10,strokeColor="#c0392b"))
s2.append(text(p2x+18,p2y+310,"Tasa: +0.32 cc/semestre -- Repetir US en 6 m",9,strokeColor="#888"))

# mini chart (bars)
s2.append(text(p2x+16,p2y+340,"Crecimiento volumetrico (cc)",12,strokeColor="#2c3e50"))
s2.append(card(p2x+12,p2y+358,310,90,bg="#f8f9fa"))
bars=[(30,"Ene24",2.1),(90,"Jun24",2.5),(150,"Ene25",2.95),(210,"Jun25",3.5),(270,"Ene26",3.91)]
for bx,bl,bv in bars:
    bh=int(bv*12)
    s2.append(card(p2x+14+bx,p2y+440-bh,22,bh,bg="#2980b9"))
    s2.append(text(p2x+12+bx,p2y+443,str(bv),8,strokeColor="#2c3e50"))
    s2.append(text(p2x+8+bx,p2y+452,bl,8,strokeColor="#888"))

s2.append(card(p2x+50,p2y+462,240,32,bg="#2980b9"))
s2.append(text(p2x+60,p2y+469,"Calcular Volumen y Comparar",11,strokeColor="#fff"))

# ==================== SCREEN 3: Molecular ====================
p3x,p3y=80,930
s3=phone(p3x,p3y)
s3.append(text(p3x+16,p3y+66,"Estudio Molecular",15,strokeColor="#1a5276"))
s3.append(text(p3x+16,p3y+95,"Resultado BAAF:",12,strokeColor="#2c3e50"))
s3.append(card(p3x+12,p3y+112,316,30,bg="#fff3bf"))
s3.append(text(p3x+20,p3y+118,"Bethesda III - AUS/FLUS",13,strokeColor="#856404"))

s3.append(card(p3x+12,p3y+150,316,24,bg="#ebf5fb"))
s3.append(text(p3x+18,p3y+154,"2.3 cm | TR4 | Riesgo combinado: Alto",10,strokeColor="#1a5276"))

s3.append(text(p3x+16,p3y+185,"Recomendacion",13,strokeColor="#5f3dc4"))
s3.append(card(p3x+12,p3y+205,316,100,bg="#d0bfff"))
s3.append(text(p3x+18,p3y+210,"Ofrecer Estudio Molecular",14,strokeColor="#5f3dc4"))
s3.append(text(p3x+18,p3y+232,"Nodulo 1-4 cm + Bethesda III + riesgo alto",10,strokeColor="#2c3e50"))
s3.append(text(p3x+18,p3y+248,"Opcion 1: Afirma GSC (RNA)  VPP 51% VPN 96%",10,strokeColor="#2c3e50"))
s3.append(text(p3x+18,p3y+264,"Opcion 2: ThyroSeq v3 (DNA+RNA) VPP 68% VPN 97%",10,strokeColor="#2c3e50"))
s3.append(text(p3x+18,p3y+280,"Opcion 3: RosettaGX (miRNA)  VPP 48% VPN 94%",10,strokeColor="#2c3e50"))
s3.append(text(p3x+18,p3y+296,"Si rechaza o sospecha alta: cirugia directa",9,strokeColor="#888"))

s3.append(card(p3x+12,p3y+318,316,100,bg="#f8f9fa"))
s3.append(text(p3x+18,p3y+324,"Escenario con estudio molecular:",12,strokeColor="#2c3e50"))
s3.append(text(p3x+18,p3y+342,"Si benigno (GSC) → Vigilancia US cada 1-2 a",10,strokeColor="#27ae60"))
s3.append(text(p3x+18,p3y+360,"Si sospechoso (GSC) → Tiroidectomia",10,strokeColor="#c0392b"))
s3.append(text(p3x+18,p3y+378,"Si mutacion BRAF V600E (ThyroSeq) → Cirugia + vaciamiento",10,strokeColor="#c0392b"))
s3.append(text(p3x+18,p3y+396,"Si RAS-like → Lobectomia vs vigilancia (decision compartida)",10,strokeColor="#e67e22"))

s3.append(card(p3x+70,p3y+435,200,32,bg="#5f3dc4"))
s3.append(text(p3x+80,p3y+442,"Generar nota para paciente",11,strokeColor="#fff"))

# ==================== SCREEN 4: Plan Seguimiento ====================
p4x,p4y=545,930
s4=phone(p4x,p4y)
s4.append(text(p4x+16,p4y+66,"Plan de Seguimiento",15,strokeColor="#1a5276"))
s4.append(card(p4x+12,p4y+90,316,36,bg="#ebf5fb"))
s4.append(text(p4x+18,p4y+95,"Paciente: Mujer, 52a | Nodulo 2.3 cm TR4",11,strokeColor="#1a5276"))

s4.append(text(p4x+16,p4y+140,"Linea de Tiempo",13,strokeColor="#2c3e50"))
for i,(d,desc,cl) in enumerate([("Jun 2026","FNA + Molecular","#27ae60"),("Oct 2026","US Control 1","#2980b9"),("Abr 2027","US 2 + Reclasificar","#f39c12"),("Oct 2027","US Control 3","#2980b9"),("Abr 2028","Reevaluacion completa","#f39c12")]):
    ey=158+i*42
    s4.append(card(p4x+12,ey,316,36,bg="#f8f9fa"))
    s4.append(text(p4x+18,ey+2,d,9,strokeColor="#888"))
    s4.append(text(p4x+18,ey+14,desc,11,strokeColor="#2c3e50"))
    s4.append(text(p4x+280,ey+8,"●",14,strokeColor=cl))

# Dynamic reclass box
s4.append(text(p4x+16,p4y+380,"Reclasificacion Dinamica",13,strokeColor="#2c3e50"))
s4.append(card(p4x+12,p4y+400,316,52,bg="#fff3bf"))
s4.append(text(p4x+18,p4y+404,"Riesgo actual:",10,strokeColor="#2c3e50"))
s4.append(text(p4x+100,p4y+404,"Intermedio",10,strokeColor="#856404"))
s4.append(text(p4x+18,p4y+420,"Factores: TR4 | No crecimiento | Estable",10,strokeColor="#2c3e50"))
s4.append(text(p4x+18,p4y+436,"Manejo actual: US c/12 meses, FNA solo si crece",9,strokeColor="#888"))

s4.append(card(p4x+50,p4y+462,240,32,bg="#f39c12"))
s4.append(text(p4x+60,p4y+469,"Recalcular Riesgo Ahora",11,strokeColor="#fff"))

s4.append(card(p4x+50,p4y+505,240,32,bg="#1a5276"))
s4.append(text(p4x+60,p4y+512,"Reporte PDF para Paciente (1 hoja)",11,strokeColor="#fff"))

# ==================== TITLE + LEGEND ====================
titles=[]
titles.append(text(250,40,"Tiroides Toolkit v2 - Mockup de Navegacion",30,strokeColor="#1a5276"))
titles.append(text(250,78,"App expandida para seguimiento integral de nodulos tiroideos",14,strokeColor="#666"))
titles.append(card(80,115,440,50,bg="#f8f9fa",strokeWidth=1))
titles.append(text(90,122,"Flujo tipico del paciente:",11,strokeColor="#2c3e50"))
titles.append(text(90,140,"Pantalla 1 (Evaluacion) → Pantalla 2 (Growth Tracker) → Pantalla 3 (Molecular) → Pantalla 4 (Plan + Reclasificacion)",10,strokeColor="#888"))

# Flow arrows
mid_y1=p1y+330; p1r=p1x+340; p2l=p2x
titles.append(arrow(p1r+5,mid_y1,32,0))
titles.append(text(p1r+12,mid_y1-18,"crecimiento",9,strokeColor="#888"))

mid_y3=p3y+330; p3r=p3x+340; p4l=p4x
titles.append(arrow(p3r+5,mid_y3,32,0))
titles.append(text(p3r+12,mid_y3-18,"plan",9,strokeColor="#888"))

mid_x2=p2x+170; p2b=p2y+660; p3t=p3y
titles.append(arrow(mid_x2,p2b+5,0,25))
titles.append(text(mid_x2-55,p2b+16,"si Bethesda III/IV",9,strokeColor="#888"))

# Build
all_e = titles + s1 + s2 + s3 + s4
doc={"type":"excalidraw","version":2,"source":"hermes-agent","elements":all_e,"appState":{"viewBackgroundColor":"#ffffff","gridSize":None}}

import os
out="/Users/anateniente/Endocrinologia/Tiroides/Tiroides-Toolkit/Tiroides-Toolkit-v2-Mockup.excalidraw"
with open(out,"w",encoding="utf-8") as f:
    json.dump(doc,f,indent=2,ensure_ascii=False)
print(f"OK: {out}")
print(f"Elementos: {len(all_e)}")
print(f"Tamano: {os.path.getsize(out)} bytes")
