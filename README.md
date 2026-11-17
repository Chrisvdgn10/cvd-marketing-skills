# CVD Marketing — bibliothèque de skills

Marketplace de plug-ins Claude de CVD Digital.

## Installer

Dans Claude : **Plug-ins → Ajouter → Ajouter une marketplace**, puis indiquer ce repo (`Chrisvdgn10/cvd-marketing-skills`). Installer ensuite le plug-in **cvd-marketing-skills**.

Dans Claude Code :

```
/plugin marketplace add Chrisvdgn10/cvd-marketing-skills
/plugin install cvd-marketing-skills@cvd-marketing
```

## Contenu

| Skill | Rôle | Source |
|---|---|---|
| product-marketing | Fiche contexte client | coreyhaines31/marketingskills |
| marketing-strategy-pmm | Positionnement et go-to-market | alirezarezvani/claude-skills |
| wasted-spend-finder | Budget ads gaspillé (Google, Meta) | thatrebeccarae/claude-marketing |
| ai-seo | Visibilité dans les moteurs IA (GEO) | coreyhaines31/marketingskills |
| cro | Optimisation de la conversion | coreyhaines31/marketingskills |
| copywriting | Textes de pages et d'ads | coreyhaines31/marketingskills |
| content-creator | Calendrier éditorial et réseaux sociaux | thatrebeccarae/claude-marketing |
| retention-churn-prevention | Rétention et reconquête | thatrebeccarae/claude-marketing |
| utm-attribution-strategy | UTM, attribution, GA4 | thatrebeccarae/claude-marketing |
| shopify | Funnel et tracking Shopify | thatrebeccarae/claude-marketing |
| social | Contenu organique : posts, calendrier, scripts vidéo courts, recyclage | coreyhaines31/marketingskills |
| ad-creative | Créations publicitaires : accroches, variantes, formats Meta/Google/TikTok/LinkedIn | coreyhaines31/marketingskills |
| facebook-ads | Meta Ads : audit, audiences, stratégie créative, pixel, CAPI | thatrebeccarae/claude-marketing |
| tiktok-ads | TikTok Ads : campagnes, créa, Spark Ads, mesure | thatrebeccarae/claude-marketing |
| claude-video-edit | Montage FFmpeg : couper, assembler, recadrer, vitesse, overlays, étalonnage | AgriciDaniel/claude-video |
| claude-video-caption | Transcription et sous-titres animés (SRT, karaoké, incrustation) | AgriciDaniel/claude-video |
| cvd-find-skills | Trouve, évalue et ajoute de nouveaux skills à cette bibliothèque (skill maison, adapté de vercel-labs/skills) | CVD Digital |

Tous les skills sont sous licence MIT (voir `plugins/cvd-marketing-skills/LICENSE-*`).

## Mises à jour

Le 1er de chaque mois, l'action GitHub « Mise à jour des skills » récupère les dernières versions depuis les repos d'origine. Si quelque chose a changé, elle ouvre une pull request « Mise à jour mensuelle des skills ».

1. Relire la pull request (liste des skills modifiés).
2. Cliquer sur **Merge** pour accepter. Rien ne change dans Claude tant que ce n'est pas fait.
3. Dans Claude, mettre à jour le plug-in depuis la page Plug-ins.

Pour lancer une mise à jour à la main : onglet **Actions → Mise à jour des skills → Run workflow**.

## Ajouter ou retirer un skill

- Ajouter : une ligne dans `scripts/sources.txt` (`nom|compte/repo|chemin/du/skill`), puis lancer l'action.
- Skill maison : créer `plugins/cvd-marketing-skills/skills/<nom>/SKILL.md` sans l'ajouter à `sources.txt` ; la synchronisation n'y touche pas.
- Retirer : supprimer le dossier du skill et sa ligne dans `sources.txt`.
