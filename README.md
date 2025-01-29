# desafio_verificacao_hash
Verificação de Integridade de Arquivos com Hashes
# Verificador de Integridade de Arquivos

## 📌 Descrição
Você foi encarregado de criar um sistema simples que verifica a integridade de arquivos, comparando o hash fornecido pelo usuário com o hash real do arquivo.  

A função `verificar_hashes` recebe uma lista de hashes e os compara com os valores esperados para cada arquivo. O objetivo é verificar se o hash calculado é igual ao hash esperado.

---

## 📥 Entrada
- Uma lista de pares de hashes (**hash calculado** e **hash esperado**), separados por vírgulas.
- Cada par é separado por ponto e vírgula (`;`).

---

## 📤 Saída
Para cada par de hashes fornecido, o código imprime o resultado:  
- `"Correto"` → Se o hash calculado for igual ao esperado.  
- `"Inválido"` → Se os hashes forem diferentes.  

---

## 📌 Exemplos

| Entrada | Saída |
|---------|-------|
| `abc123, abc123` | `Correto` |
| `def456, def789` | `Inválido` |
| `123abc, 123abc; 456def,456def` | `Correto`<br>`Correto` |

---

## 🚀 Como Usar
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/verificador-hashes.git
