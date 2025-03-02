# 📦 Collection Ansible ynov.general

## 📚 Table des matières

- [Description](#-description)
- [Rôles Inclus](#-rôles-inclus)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Tests](#-tests)
- [Dépendances](#-dépendances)
- [Contribution](#-contribution)
- [Licence](#-licence)

## 📖 Description

Cette collection Ansible, `ynov.general`, fournit un ensemble de rôles Ansible réutilisables pour automatiser le déploiement et la configuration d'applications web, en particulier WordPress. Elle est conçue pour être utilisée avec AWX, mais peut également être utilisée avec Ansible en ligne de commande.

## ⚙️ Rôles inclus

- **`post_installation`**: Mise à jour du système, configuration de base (utilisateurs, SSH, firewall, etc.).
- **`web_server`**: Installation et configuration d'Apache (ou Nginx) avec PHP.
- **`mariadb`**: Installation et configuration d'un serveur MariaDB, création de la base de données.
- **`wordpress`**: Déploiement de WordPress, configuration de la base de données et du serveur web.

## 🛠️ Prérequis

- Python 3.8+
- Git
- Ansible 2.9+
- Accès SSH aux machines cibles.
- Pour les tests Molecule :
  - Python 3.8+
  - Docker

## 💾 Installation

1.  **Depuis Ansible Galaxy :** (Recommandé pour une utilisation facile)

    ```bash
    ansible-galaxy collection install ynov.general
    ```

2.  **Depuis un dépôt Git :** (Pour le développement ou les versions spécifiques)

    - Clonez le dépôt :

      ```bash
      git clone https://github.com/CalixteManaud/ansible-collection-ynov
      cd ansible-collection-ynov
      ```

    - Installez la collection :

      ```bash
      ansible-galaxy collection build
      ansible-galaxy collection install ynov-general-<version>.tar.gz
      ```

## 🚀 Utilisation

Pour utiliser ces rôles dans votre playbook Ansible, vous pouvez simplement les référencer. Assurez-vous d'avoir correctement configuré votre inventaire Ansible.

```yml
name: Deploy WordPress
hosts: all
become: yes
roles:
  - ynov.general.post_installation
  - ynov.general.web_server
  - ynov.general.mariadb
  - ynov.general.wordpress
```

Dans votre fichier `requirements.yml` :

```yml
collections:
    - name: ynov.general
    source: https://url-de-votre-depot-git-collection.git
    type: git
```
