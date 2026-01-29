#!/usr/bin/env python3
"""
🚀 Mapeador de Habilidades Pessoais - Gustavo Henrique
📊 Descobre superpoderes em 5 perguntas + ranking visual
💾 Exporta CSV profissional para portfólio

Execute: python mapeador.py
"""

import csv
from datetime import datetime

# 🌟 Perguntas otimizadas
perguntas = [
    "😊 O que as pessoas costumam elogiar em você?",
    "💪 Em que tipo de tarefa você se sente mais confiante?",
    "🤝 Que tipo de ajuda você costuma oferecer para amigos/familiares?",
    "⚡ Quais atividades você faz com facilidade (enquanto outros sofrem)?",
    "📚 Que tipo de conteúdo você consome com frequência?"
]

def coletar_respostas():
    print("🚀 INICIANDO MAPEAMENTO DE HABILIDADES")
    print("=" * 60)
    respostas = []
    
    for i, p in enumerate(perguntas, 1):
        print(f"\n📝 PERGUNTA {i}/5")
        print("-" * 40)
        print(p)
        
        texto = input("\nSua resposta: ").strip()
        while not texto:
            print("⚠️  Digite algo!")
            texto = input("Sua resposta: ").strip()
            
        nota = None
        while nota is None:
            try:
                n = input("⭐ Nota de confiança (1-5): ")
                nota = int(n)
                if not 1 <= nota <= 5:
                    nota = None
                    print("❌ Use 1 a 5")
            except:
                print("❌ Número inválido!")
        
        tags_input = input("🏷️  Tags (vírgula): ").strip()
        tags_list = [t.strip().lower() for t in tags_input.split(",") if t.strip()]
        
        respostas.append({
            "pergunta": p, "resposta": texto, "nota": nota, "tags": tags_list
        })
        print("✅ OK!")
    
    return respostas

def gerar_mapa(respostas):
    mapa = {}
    for r in respostas:
        for tag in r.get("tags", ["geral"]):
            if tag not in mapa:
                mapa[tag] = {"total": 0, "count": 0}
            mapa[tag]["total"] += r["nota"]
            mapa[tag]["count"] += 1
    
    resumo = {tag: round(v["total"]/v["count"], 1) for tag, v in mapa.items()}
    top = sorted(resumo.items(), key=lambda x: x[1], reverse=True)
    return top

def exibir_resultados(top):
    print("\n" + "="*70)
    print("🏆 SEUS SUPERPODEDORES!")
    print("="*70)
    
    print("\n📊 TOP HABILIDADES:")
    for i, (tag, media) in enumerate(top[:5], 1):
        estrelas = "⭐" * int(media)
        print(f"{i}. {tag.capitalize():20} {media:4.1f} {estrelas}")
    
    print(f"\n📈 Total: {len(top)} habilidades mapeadas")

def salvar_csv(respostas, top):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    fname = f"mapa_habilidades_gustavo_{timestamp}.csv"
    
    with open(fname, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Pergunta", "Resposta", "Nota", "Tags"])
        for r in respostas:
            writer.writerow([r["pergunta"][:50]+"...", r["resposta"], r["nota"], ", ".join(r["tags"])])
    
    print(f"\n💾 Salvo: {fname}")
    return fname

def main():
    print("🌟 MAPEADOR HABILIDADES - Gustavo Henrique")
    print("Portfolio Data Analyst Júnior | Salvador/BA\n")
    
    respostas = coletar_respostas()
    top_habilidades = gerar_mapa(respostas)
    
    exibir_resultados(top_habilidades)
    
    if input("\n💾 Salvar CSV? (s/N): ").lower().startswith('s'):
        salvar_csv(respostas, top_habilidades)
    
    print("\n🎉 Copie seu TOP 3 para LinkedIn!")
    print("📂 Adicione este CSV no GitHub!")

if __name__ == "__main__":
    main()
