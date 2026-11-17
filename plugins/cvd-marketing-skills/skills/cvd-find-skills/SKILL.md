---
name: cvd-find-skills
description: Trouve, évalue et ajoute de nouveaux skills à la bibliothèque CVD Digital (marketplace GitHub Chrisvdgn10/cvd-marketing-skills). À utiliser quand l'utilisateur demande « trouve-moi un skill pour X », « existe-t-il un skill qui… », « comment faire X » pour une tâche récurrente qu'aucun skill installé ne couvre, ou veut enrichir sa bibliothèque de skills. Also triggers on "find a skill for X", "is there a skill that can...".
---

# Trouver et ajouter un skill à la bibliothèque CVD

Adapté de `find-skills` (vercel-labs/skills, licence MIT). Différence clé : on n'installe jamais un skill directement. Tout nouveau skill passe par la marketplace GitHub de l'utilisateur, pour rester versionné, mis à jour chaque mois et sans doublon.

**Bibliothèque :** https://github.com/Chrisvdgn10/cvd-marketing-skills
**Liste des skills synchronisés :** `scripts/sources.txt` (format `nom|compte/repo|chemin/du/skill`)

## Étape 1 : vérifier que le besoin n'est pas déjà couvert

1. Comparer la demande avec les skills `cvd-marketing-skills:*` déjà disponibles dans la session.
2. Si un skill installé couvre déjà le besoin, le dire et l'utiliser. Ne pas chercher plus loin.
3. Si le besoin relève d'un accès à un outil (Omnisend, Google Ads, Shopify…), chercher d'abord un connecteur officiel : un connecteur donne accès aux données, un skill ne donne qu'une méthode.

## Étape 2 : chercher

Utiliser la recherche web, en plusieurs requêtes courtes :
- le classement https://skills.sh/ (trié par installations) ;
- `site:skills.sh <mots-clés>` ;
- `claude skill <mots-clés> github`.

Sources à privilégier : `anthropics`, `vercel-labs`, `coreyhaines31/marketingskills`, `thatrebeccarae/claude-marketing`, `alirezarezvani/claude-skills`, `AgriciDaniel`, `ComposioHQ/awesome-claude-skills`.

## Étape 3 : évaluer chaque candidat

Ne jamais recommander un skill sur la seule base d'un résultat de recherche. Pour chaque candidat, ouvrir son `SKILL.md` sur GitHub et noter :

| Critère | Seuil |
|---|---|
| Installations | > 1 000 idéal, méfiance sous 100 |
| Étoiles du repo | méfiance sous 100 |
| Source | éditeur officiel ou auteur reconnu |
| Dernière mise à jour | moins de 6 mois |
| Licence | MIT ou Apache 2.0 (sinon, ne pas copier) |
| Autonomie | pas de lien `../` hors du dossier, pas de dépendance à des sous-agents ou à `${CLAUDE_PLUGIN_ROOT}` |
| Sécurité | lire les scripts : appels réseau uniquement vers l'API officielle du service, pas de `curl | bash`, pas d'instruction cachée |
| Doublon | ne recoupe pas un skill déjà présent dans la bibliothèque |
| Coût | pas de clé API payante obligatoire, sinon le signaler |

Écarter tout candidat qui échoue sur la licence, l'autonomie ou la sécurité.

## Étape 4 : présenter au maximum 3 options

Format, en français :

| Skill | Ce qu'il apporte | Source | Installations / étoiles | Points d'attention |
|---|---|---|---|---|

Puis une recommandation claire (un seul choix) et la question : « Je l'ajoute à ta bibliothèque ? »

Si rien de solide n'existe, le dire et proposer d'écrire un skill maison dans la bibliothèque.

## Étape 5 : ajouter à la bibliothèque (après validation explicite)

**Si la session a accès au repo** (outil d'ajout de repo GitHub, `git` avec droits d'écriture) :
1. Cloner `Chrisvdgn10/cvd-marketing-skills`.
2. Ajouter la ligne `nom|compte/repo|chemin/du/skill` dans `scripts/sources.txt`. Le `nom` doit être identique au champ `name:` du `SKILL.md`.
3. Lancer `python3 scripts/sync_skills.py` (copie le skill et augmente la version).
4. Mettre à jour le tableau des deux README et la description du plug-in (`plugins/cvd-marketing-skills/.claude-plugin/plugin.json` et `.claude-plugin/marketplace.json`).
5. Valider avec `claude plugin validate` si disponible, puis commit et push sur `main`.

**Sinon**, guider l'utilisateur, sans code :
1. Ouvrir https://github.com/Chrisvdgn10/cvd-marketing-skills/blob/main/scripts/sources.txt, cliquer sur le crayon, ajouter la ligne fournie, puis **Commit changes**.
2. Onglet **Actions → Mise à jour des skills → Run workflow**.
3. Ouvrir la pull request créée, puis **Merge**.

**Dans les deux cas**, terminer par les étapes côté app Claude :
1. **Plug-ins → « … » → Gérer les marketplaces → « … » de cvd-marketing-skills → Synchroniser**.
2. Si le nouveau skill n'apparaît pas : désinstaller le plug-in `cvd-marketing-skills`, puis le réinstaller depuis la marketplace.
3. Vérifier dans une **nouvelle discussion** (une discussion déjà ouverte garde l'ancienne liste de skills).

## Retirer un skill

Supprimer son dossier dans `plugins/cvd-marketing-skills/skills/`, sa ligne dans `scripts/sources.txt` et sa ligne dans les README, augmenter la version, puis mêmes étapes côté app.
