from pathlib import Path

p = Path("widget.js")
s = p.read_text(encoding="utf-8")

# Sauvegarde de sécurité
Path("widget.js.original-before-service-demandeur").write_text(
    s, encoding="utf-8"
)

# ============================================================
# LISTE SERVICE DEMANDEUR
# ============================================================

services = [
    "SGA",
    "SAJ",
    "SAE",
    "SAAS",
    "RH",
    "Pôle1d44",
    "PACTE 1D PU",
    "PACTE 1D PR",
    "MED PREV",
    "EFIV442D",
    "EFIV441D",
    "DSI – ANT 44",
    "DSI",
    "DSDEN49 - DRH",
    "DSDEN49",
    "DSDEN 85 / DRH",
    "DSDEN 72 / PERS. ENS. 1DPUB",
    "DSDEN 53 / GRHAG",
    "DSDEN 53 / CPDEPS",
    "DSDEN 49 – ASH",
    "DRANE",
    "DIPE",
    "DIPATE",
    "DEC",
    "DBF2",
    "DBF1",
    "DAPSI",
    "DAPP / DRH49",
    "DAPP",
    "DAEP",
    "CDOEA - SDEI 85"
]

# ============================================================
# 1. MAPPING DU CHAMP
# ============================================================

s = s.replace(
    "category: 'Category',",
    "serviceDemandeur: 'SERVICE DEMANDEUR',"
)

s = s.replace(
    "fieldCategory: 'Catégorie'",
    "fieldServiceDemandeur: 'SERVICE DEMANDEUR'"
)

s = s.replace(
    "fieldCategory: 'Category'",
    "fieldServiceDemandeur: 'SERVICE DEMANDEUR'"
)

# ============================================================
# 2. COLONNE CRÉÉE DANS PM_Tasks
# ============================================================

s = s.replace(
    "{ id: 'Category', type: 'Text' }",
    "{ id: 'SERVICE DEMANDEUR', type: 'Text' }"
)

# ============================================================
# 3. CONFIGURATION PM_Config
# ============================================================

s = s.replace(
    "['task_category', TASKS_TABLE, 'Category', 'Catégorie', false, 'Category']",
    "['task_service_demandeur', TASKS_TABLE, 'SERVICE DEMANDEUR', 'SERVICE DEMANDEUR', false, 'SERVICE DEMANDEUR']"
)

# ============================================================
# 4. CHARGEMENT DES TÂCHES
# ============================================================

s = s.replace(
    "var categoryCol = getColumnName('tasks', 'category');",
    "var serviceDemandeurCol = getColumnName('tasks', 'serviceDemandeur');"
)

s = s.replace(
    "task.Category = taskData[categoryCol] ? taskData[categoryCol][i] : '';",
    "task.SERVICE_DEMANDEUR = taskData[serviceDemandeurCol] ? taskData[serviceDemandeurCol][i] : '';"
)

# ============================================================
# 5. TEMPLATES
# ============================================================

s = s.replace(
    "Category: tplData.Category ? tplData.Category[i] : '',",
    "SERVICE_DEMANDEUR: tplData['SERVICE DEMANDEUR'] ? tplData['SERVICE DEMANDEUR'][i] : '',"
)

# ============================================================
# 6. FILTRE
# ============================================================

s = s.replace(
    "var currentFilterCategory = null;",
    "var currentFilterServiceDemandeur = null;"
)

s = s.replace(
    "currentFilterCategory",
    "currentFilterServiceDemandeur"
)

s = s.replace(
    "filterByCategory",
    "filterByServiceDemandeur"
)

# ============================================================
# 7. DONNÉES DU FILTRE
# ============================================================

s = s.replace(
    "t.Category && allCategories.indexOf(t.Category) === -1",
    "t.SERVICE_DEMANDEUR && allServiceDemandeurs.indexOf(t.SERVICE_DEMANDEUR) === -1"
)

s = s.replace(
    "allCategories.push(t.Category)",
    "allServiceDemandeurs.push(t.SERVICE_DEMANDEUR)"
)

s = s.replace(
    "String(t.Category || '')",
    "String(t.SERVICE_DEMANDEUR || '')"
)

# ============================================================
# 8. OBJETS TASK
# ============================================================

s = s.replace(
    "task.Category",
    "task.SERVICE_DEMANDEUR"
)

# ============================================================
# 9. TEMPLATES
# ============================================================

s = s.replace(
    "tpl.Category",
    "tpl.SERVICE_DEMANDEUR"
)

# ============================================================
# 10. ÉCRITURE DU CHAMP DANS GRIST
# ============================================================

s = s.replace(
    "setField(record, 'tasks', 'category',",
    "setField(record, 'tasks', 'serviceDemandeur',"
)

# ============================================================
# 11. IDENTIFIANTS HTML
# ============================================================

s = s.replace(
    "id=\"task-category\"",
    "id=\"task-service-demandeur\""
)

s = s.replace(
    "id='task-category'",
    "id='task-service-demandeur'"
)

# ============================================================
# 12. COMBOBOX SERVICE DEMANDEUR
# ============================================================

service_js = ",\n".join(
    "    " + repr(x).replace("'", '"')
    for x in services
)

block = f"""
// ============================================================
// SERVICE DEMANDEUR - LISTE
// ============================================================

var SERVICE_DEMANDEUR_OPTIONS = [
{service_js}
];

function buildServiceDemandeurOptions(currentValue) {{
  var html = '<option value="">--</option>';

  SERVICE_DEMANDEUR_OPTIONS.forEach(function(service) {{
    var selected = service === (currentValue || '') ? ' selected' : '';

    html += '<option value="' +
      sanitize(service) +
      '"' + selected + '>' +
      sanitize(service) +
      '</option>';
  }});

  // Une ancienne valeur est conservée si elle existe
  // déjà dans Grist mais n'est pas dans la nouvelle liste.
  if (
    currentValue &&
    SERVICE_DEMANDEUR_OPTIONS.indexOf(currentValue) === -1
  ) {{
    html += '<option value="' +
      sanitize(currentValue) +
      '" selected>' +
      sanitize(currentValue) +
      '</option>';
  }}

  return html;
}}

"""

if "var SERVICE_DEMANDEUR_OPTIONS = [" not in s:
    marker = "// =============================================================================\n// UTILS"
    if marker in s:
        s = s.replace(marker, block + "\n" + marker, 1)

# ============================================================
# 13. CRÉATION D'UNE TÂCHE
# ============================================================

old_start = """var newCategoryOptions = '<option value="">--</option>';
  for (var nci = 0; nci < categories.length; nci++) {
    newCategoryOptions += '<option value="' + sanitize(categories[nci].Name) + '">' + sanitize(categories[nci].Name) + '</option>';
  }
  html += '<span class="detail-field-label">' + t('fieldCategory') + '</span>';
  html += '<div class="detail-field-value"><select id="task-service-demandeur">' + newCategoryOptions + '</select></div>';"""

new_start = """var newServiceDemandeurOptions = buildServiceDemandeurOptions('');
  html += '<span class="detail-field-label">SERVICE DEMANDEUR</span>';
  html += '<div class="detail-field-value"><select id="task-service-demandeur">' + newServiceDemandeurOptions + '</select></div>';"""

s = s.replace(old_start, new_start)

# ============================================================
# 14. MODIFICATION D'UNE TÂCHE
# ============================================================

old_edit = """var categoryOptions = '<option value="">--</option>';
  for (var ci = 0; ci < categories.length; ci++) {
    var catSel = categories[ci].Name === task.SERVICE_DEMANDEUR ? ' selected' : '';
    categoryOptions += '<option value="' + sanitize(categories[ci].Name) + '"' + catSel + '>' + sanitize(categories[ci].Name) + '</option>';
  }
  html += '<span class="detail-field-label">' + t('fieldCategory') + '</span>';
  html += '<div class="detail-field-value"><select id="task-service-demandeur">' + categoryOptions + '</select></div>';"""

new_edit = """var serviceDemandeurOptions = buildServiceDemandeurOptions(task.SERVICE_DEMANDEUR || '');
  html += '<span class="detail-field-label">SERVICE DEMANDEUR</span>';
  html += '<div class="detail-field-value"><select id="task-service-demandeur">' + serviceDemandeurOptions + '</select></div>';"""

s = s.replace(old_edit, new_edit)

# ============================================================
# 15. PREFILL
# ============================================================

s = s.replace(
    "if (prefill.category) setField(record, 'tasks', 'serviceDemandeur', prefill.category);",
    "if (prefill.serviceDemandeur) setField(record, 'tasks', 'serviceDemandeur', prefill.serviceDemandeur);"
)

# ============================================================
# 16. TEMPLATE FORM
# ============================================================

s = s.replace(
    "var category = editing ? (tpl.SERVICE_DEMANDEUR || '') : '';",
    "var serviceDemandeur = editing ? (tpl.SERVICE_DEMANDEUR || '') : '';"
)

s = s.replace(
    "var tplCatOptions = '<option value=\"\"' + (!category ? ' selected' : '') + '>--</option>';",
    "var tplServiceDemandeurOptions = buildServiceDemandeurOptions(serviceDemandeur);"
)

# Remplacement du bloc de génération des options de template
import re

s = re.sub(
    r"""var tplCatOptions = '<option value=""' \+ \(!category \? ' selected' : ''\) \+ '>--</option>';\s*
  for \(var tci = 0; tci < categories\.length; tci\+\+\) \{\s*
    var catName = categories\[tci\]\.Name;\s*
    tplCatOptions \+= '<option value="' \+ sanitize\(catName\) \+ '"' \+ \(catName === category \? ' selected' : ''\) \+ '>' \+ sanitize\(catName\) \+ '</option>';\s*
  \}""",
    "var tplServiceDemandeurOptions = buildServiceDemandeurOptions(serviceDemandeur);",
    s
)

s = s.replace(
    "t('fieldCategory')",
    "'SERVICE DEMANDEUR'"
)

s = s.replace(
    "tplCatOptions",
    "tplServiceDemandeurOptions"
)

s = s.replace(
    "tpl-category",
    "tpl-service-demandeur"
)

s = s.replace(
    "document.getElementById('tpl-service-demandeur').value.trim()",
    "document.getElementById('tpl-service-demandeur').value.trim()"
)

s = s.replace(
    "Category: document.getElementById('tpl-service-demandeur').value.trim(),",
    "SERVICE_DEMANDEUR: document.getElementById('tpl-service-demandeur').value.trim(),"
)

# ============================================================
# 17. CARTES
# ============================================================

s = s.replace(
    "cd.category && task.SERVICE_DEMANDEUR",
    "cd.serviceDemandeur && task.SERVICE_DEMANDEUR"
)

# ============================================================
# 18. STATISTIQUES
# ============================================================

s = s.replace(
    "chart-category",
    "chart-service-demandeur"
)

# ============================================================
# 19. RECHERCHE
# ============================================================

s = s.replace(
    "t.Category && t.Category.toLowerCase()",
    "t.SERVICE_DEMANDEUR && t.SERVICE_DEMANDEUR.toLowerCase()"
)

# ============================================================
# 20. CSV
# ============================================================

s = s.replace(
    "Priorité,Catégorie,Assigné",
    "Priorité,SERVICE DEMANDEUR,Assigné"
)

# ============================================================
# 21. FIELDS EXPORT / CONFIG
# ============================================================

s = s.replace(
    "'category', 'tag'",
    "'serviceDemandeur', 'tag'"
)

# ============================================================
# 22. TEXTES D'INTERFACE
# ============================================================

s = s.replace(
    "— Catégorie —",
    "— SERVICE DEMANDEUR —"
)

# ============================================================
# 23. SAUVEGARDE
# ============================================================

p.write_text(s, encoding="utf-8")

print("")
print("==============================================")
print(" MIGRATION SERVICE DEMANDEUR TERMINEE")
print("==============================================")
print("")
print("31 services configurés.")
print("")
print("Sauvegarde : widget.js.original-before-service-demandeur")
print("")
