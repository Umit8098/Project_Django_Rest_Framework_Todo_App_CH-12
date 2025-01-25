<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_ToDo_App</h1>


<!-- <div align="center">
  <h3>
    <a href="https://umit8101.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8101.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Endpoints](#api-endpoints)
  - [Todo Endpoints:](#todo-endpoints)
- [API Testing](#api-testing)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## API Endpoints

Bu API aşağıdaki endpoint'leri sağlar:


### Todo Endpoints:
- `GET https://umit8101.pythonanywhere.com/todo/` - Tüm todo'ları listele
- `POST https://umit8101.pythonanywhere.com/todo/` - Yeni bir todo oluştur
- `GET https://umit8101.pythonanywhere.com/todo/26/` - Belirli bir todo detayları
- `PUT https://umit8101.pythonanywhere.com/todo/26/` - Todo güncelleme
- `DELETE https://umit8101.pythonanywhere.com/todo/26/` - Todo silme

## API Testing

Postman Collection, API'nizin her bir endpoint'ini test etmek için gerekli istekleri içerir. API'nin işlevselliğini hızlı bir şekilde anlamak için kullanabilirsiniz.

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-2f319feb-d1dd-4e25-8774-b3f1f5589e7d?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Blog App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-2f319feb-d1dd-4e25-8774-b3f1f5589e7d?action=share&creator=17531143)


## Overview
- Web browsable API
<!-- ![screenshot](project_screenshot/ToDo_App-2.gif) -->
<img src="project_screenshot/ToDo_App-2.gif" alt="Web browsable API" width="400"/>


---

- Todo CRUD Testi
<!-- ![screenshot](project_screenshot/ToDo_App.gif) -->
<img src="project_screenshot/ToDo_App.gif" alt="Todo CRUD Testi" width="400"/>


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework


## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Todo_App_CH-12.git) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Todo_App_CH-12.git

# Install dependencies
    $ python -m venv env
    $ python -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...
"""

# Run the app
    $ python manage.py runserver
```

## About This Project
- Todo Application API service.

<hr>

- Todo Application API service.

## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/)


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
