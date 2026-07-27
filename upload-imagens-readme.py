#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sobe as imagens locais (anexos/imagens/...) para o CDN do ReadMe e reescreve
as referências nos .md para a URL retornada.

Como usar (PowerShell):
    $env:README_API_KEY = "SUA_CHAVE_DO_README"      # a chave NUNCA fica no script
    pip install requests
    python upload-imagens-readme.py "C:\\Users\\anna.brandao\\Downloads\\Doc-Readme\\docs"

- Passe como argumento a pasta a processar (ex.: o docs/ do Doc-Readme). Sem argumento, usa a pasta atual.
- Cada imagem é enviada UMA vez (mesmo que apareça em várias páginas).
- Use --dry-run para só listar o que seria feito, sem enviar nem alterar nada.
- Depois de rodar, faça: git add -A && git commit -m "imagens no CDN do ReadMe" && git push
"""
import os, re, sys, mimetypes, pathlib

DRY = "--dry-run" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("-")]
BASE = pathlib.Path(args[0] if args else ".").resolve()

try:
    import requests
except ImportError:
    print("Falta a lib 'requests'. Rode:  pip install requests"); sys.exit(1)

KEY = os.environ.get("README_API_KEY")
if not KEY and not DRY:
    print("Defina a variável de ambiente README_API_KEY com sua API key do ReadMe.")
    print('PowerShell:  $env:README_API_KEY = "sua_chave"')
    sys.exit(1)

API = "https://api.readme.com/v2/images"
IMG_RE = re.compile(r'(?:!\[[^\]]*\]\(|\]:\s*)([^)\s]+\.(?:png|jpe?g|gif|svg))', re.I)

cache = {}   # caminho absoluto -> url no CDN
def upload(path: pathlib.Path):
    if path in cache: return cache[path]
    if DRY:
        cache[path] = f"<url-do-cdn:{path.name}>"; return cache[path]
    mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    with open(path, "rb") as f:
        r = requests.post(API, headers={"Authorization": f"Bearer {KEY}"},
                          files={"file": (path.name, f, mime)})
    if r.status_code != 201:
        print(f"   ERRO {r.status_code} ao enviar {path.name}: {r.text[:200]}"); return None
    url = r.json().get("data", {}).get("url")
    if not url:
        print(f"   ERRO: resposta sem data.url para {path.name}: {r.text[:200]}"); return None
    cache[path] = url
    print(f"   enviada: {path.name} -> {url}")
    return url

paginas = 0; erros = 0; nao_encontradas = 0
for md in sorted(BASE.rglob("*.md")):
    text = md.read_text(encoding="utf-8"); orig = text
    refs = {m.group(1) for m in IMG_RE.finditer(text)}
    for ref in refs:
        if ref.startswith(("http://", "https://")): continue
        img = (md.parent / ref).resolve()
        if not img.is_file():
            print(f" ! imagem não encontrada: {ref}  (em {md.relative_to(BASE)})"); nao_encontradas += 1; continue
        url = upload(img)
        if not url: erros += 1; continue
        text = text.replace(ref, url)
    if text != orig:
        if not DRY: md.write_text(text, encoding="utf-8")
        paginas += 1
        print(f" {'[dry] ' if DRY else ''}atualizado: {md.relative_to(BASE)}")

print("\n===== RESUMO =====")
print(f"Modo: {'DRY-RUN (nada enviado/alterado)' if DRY else 'EXECUÇÃO'}")
print(f"Imagens únicas: {len(cache)} | Páginas atualizadas: {paginas} | Erros: {erros} | Não encontradas: {nao_encontradas}")
if not DRY and paginas:
    print("\nAgora rode:  git add -A && git commit -m \"imagens no CDN do ReadMe\" && git push")
