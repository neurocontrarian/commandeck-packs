# Contribuer un pack de boutons

🇬🇧 *English version: [CONTRIBUTING.md](CONTRIBUTING.md)*

Merci de partager un pack ! Les packs sont **gratuits** et faits par la communauté. Ce
guide explique comment un pack entre dans la **galerie officielle** (le catalogue signé
que l'app parcourt).

> Rien de tout ceci n'est nécessaire juste pour *utiliser* un pack que vous avez exporté —
> partagez le fichier `.cdpack` comme bon vous semble. Ceci ne sert qu'à le faire entrer
> dans la galerie de l'app.

## Comment soumettre (aucune compétence en code requise)

1. **Créez le pack dans l'app.** Sélectionnez les boutons → **Exporter en pack…** —
   remplissez le nom/la description/les tags et enregistrez. Vous obtenez un seul
   fichier **`.cdpack`**.
2. **Ouvrez le formulaire de soumission :**
   [**Nouvelle issue → 📦 Soumettre un pack**](https://github.com/neurocontrarian/commandeck-packs/issues/new?template=submit-pack.yml).
   Remplissez les champs et **glissez-déposez votre fichier `.cdpack`** dans la zone prévue.
   - GitHub bloque les types de fichiers inconnus : s'il refuse votre `.cdpack`,
     **renommez-le en `.zip`** puis redéposez-le — un `.cdpack` *est* un zip, et le
     mainteneur le renommera à l'inverse.
   - Un compte GitHub est requis pour ouvrir une issue.
3. **Un mainteneur l'examine**, puis le **signe** avec la clé officielle et le publie
   (`<pack-id>/pack.toml` + `pack.sig`, listé dans `index.json`). Une fois fusionné, il
   apparaît dans la galerie de tout le monde avec le badge **✓ Vérifié**.

L'app **ne signe jamais les packs** — seul le mainteneur le fait, après examen. Une
soumission est donc toujours un `.cdpack` *non signé* (le bundle ne contient que
`pack.toml`, pas de `pack.sig`).

## Ce qu'un pack valide doit contenir

- Un identifiant (lettres minuscules, chiffres et tirets), un nom et un numéro de version — l'app les remplit pour vous lors de l'export.
- Au moins un `[[button]]` avec un `name` et une `command`.
- **Aucun secret.** Ne mettez jamais de mot de passe / clé d'API / jeton dans une
  commande. Utilisez un **`{{variable}}`** (l'app demande la valeur au moment de
  l'exécution) — ex. `docker restart {{container}}`. Voir la référence des variables dans l'app.
- **Aucun état machine/installation** : `machine_ids`, `profile_id`, `run_as_user`,
  `is_default`, `source_pack`, `position`, `mcp_executable` sont interdits (l'export les
  retire déjà).

## Bonnes manières pour un pack

- Un thème clair par pack (ex. « Jellyfin », « stockage ZFS »), une `description` utile, des `tags` pertinents.
- Ajoutez des `tooltip`s pour que chacun comprenne chaque bouton.
- Préférez des commandes multi-plateformes, ou indiquez l'`os` d'un bouton quand il est spécifique à un OS.
- Courtoisie de marque : nommez un pack *« buttons for X »*, jamais *« official X »* sauf accord du projet concerné.

## Licence

En soumettant un pack, vous **versez son contenu dans le domaine public** sous
[Creative Commons CC0 1.0 Universal](LICENSE) : vous renoncez à tous vos droits d'auteur et
droits voisins, sans condition. N'importe qui — y compris le mainteneur de Commandeck — peut
alors utiliser, modifier, redistribuer ou réutiliser votre pack librement, à toute fin. Le
contenu d'un pack se limite à des noms de boutons, des commandes shell et des métadonnées
(jamais de secrets) : il n'y a rien de personnel à licencier. Si vous ne pouvez pas faire cette
renonciation pour un contenu, ne le soumettez pas.
