# Founder skill — installation

Source : https://github.com/Jakeschincariol/founder-skill (MIT, commit fd9385b), 11 skills.

## Claude Code
Déjà installé dans ce dépôt : `.claude/skills/founder-*`. Ouvre le projet dans Claude Code
et tape `/founder-board`, `/founder-cfo`, etc.

Pour l'avoir dans tous tes projets (sur ta machine) :

```bash
cp -r .claude/skills/founder-* ~/.claude/skills/
```

Ou en plugin : `/plugin marketplace add Jakeschincariol/founder-skill` puis
`/plugin install founder-skill@founder-skill`.

## Cowork / claude.ai
Dans claude.ai : Paramètres → Capacités → Skills → « Importer un skill »,
puis importe chaque fichier `founder-*.zip` de ce dossier (un par skill).

Remarque : `founder-plan` appelle le script de `founder-cfo` ; importe les deux.

Ordre conseillé : board → competitors → consumer → pricing → offer → cfo →
marketing → brand → ops → launch → plan. Les outils Python demandent Python 3.8+,
rien à installer.
