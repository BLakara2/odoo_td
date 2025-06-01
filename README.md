# 🏥 Odoo Hospital Management - TP

Ce projet est un ensemble de modules Odoo personnalisés développés dans le cadre d’un TP. Il simule la gestion d’un hôpital, en exploitant le framework Odoo 17.  

## 📁 Modules disponibles

- `hospital` : module principal pour la gestion des patients.
- `hospital_disease` : gestion des maladies liées aux patients.
- `hospital_doctor` : gestion des docteurs et leur spécialité.
- `hospital_nurse` : gestion des infirmiers et des rondes.

---

## 🚀 Installation

### 1. Pré-requis

- Python 3.10+
- PostgreSQL (v13 ou plus recommandé)
- wkhtmltopdf installé (pour les rapports PDF)
- Odoo 17 installé et fonctionnel

### 2. Cloner ce dépôt

```bash
git clone https://github.com/BLakara2/odoo_td.git
cd odoo_td
```

### 3. Copier les modules dans le répertoire `custom_addons`

Exemple :

```bash
cp -r hospital* /chemin/vers/odoo/custom_addons/
```

### 4. Lancer Odoo

Dans le dossier principal de Odoo :

```bash
./odoo-bin -d td_hospital -i hospital,hospital_disease,hospital_doctor,hospital_nurse --http-port=8070 -c odoo.conf
```

---

## 🧪 Données de démonstration

Chaque module contient un fichier `demo_data.xml` pour peupler automatiquement la base avec des patients, docteurs, infirmiers, etc.

---

## 📦 Structure

```
hospital/
├── __init__.py
├── __manifest__.py
├── models/
│   └── patient.py
├── views/
│   └── hospital_views.xml
└── data/
    └── demo_patient.xml
```

---

## 📸 Capture d’écran

![Menu principal](screenshots/menu.png)

---

## ✍️ Auteur

- **Lakara B.**  
TP de développement Odoo E-TECH - 2025 

---

## 📄 Licence

Ce projet est à usage pédagogique uniquement. Non destiné à un usage en production.