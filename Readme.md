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
  - [Örnek Kullanım](#örnek-kullanım)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## API Endpoints

Bu API aşağıdaki endpoint'leri sağlar:

### Todo Endpoints:
| Method | URL                                             | Açıklama                     |
|--------|-------------------------------------------------|------------------------------|
| GET    | `https://umit8101.pythonanywhere.com/todo/`     | Tüm todo'ları listele        |
| POST   | `POST https://umit8101.pythonanywhere.com/todo/`| Yeni bir todo oluştur        |
| GET    | `https://umit8101.pythonanywhere.com/todo/26/`  | Belirli bir todo'yu görüntüle|
| PUT    | `https://umit8101.pythonanywhere.com/todo/26/`  | Bir todo'yu güncelle         |
| DELETE | `https://umit8101.pythonanywhere.com/todo/26/`  | Bir todo'yu sil              |

## API Testing

Postman Collection, API'nizin her bir endpoint'ini test etmek için gerekli istekleri içerir. API'nin işlevselliğini hızlı bir şekilde anlamak için kullanabilirsiniz.

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-2f319feb-d1dd-4e25-8774-b3f1f5589e7d?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Blog App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-2f319feb-d1dd-4e25-8774-b3f1f5589e7d?action=share&creator=17531143)


## Overview

Bu Django Rest Framework ile oluşturulmuş bir Todo API uygulamasıdır. Kullanıcıların yapılacaklar listesini oluşturmasına, güncellemesine, görüntülemesine ve silmesine olanak tanır. Bu API aşağıdaki özellikleri sunar:
- CRUD işlemleri (Create, Read, Update, Delete)
- Priorite bazlı sıralama
- Kullanıcı dostu bir web tarayıcı arayüzü

- Web browsable API
<!-- ![screenshot](project_screenshot/ToDo_App-2.gif) -->
<img src="project_screenshot/ToDo_App-2.gif" alt="Web browsable API" width="400"/>
➡ *Django Rest Framework'ün sağladığı web arayüzünde API'yi test etme süreci.*

---

- Todo CRUD Testi
<!-- ![screenshot](project_screenshot/ToDo_App.gif) -->
<img src="project_screenshot/ToDo_App.gif" alt="Todo CRUD Testi" width="400"/>
➡ *Postman ile CRUD işlemlerini test ederken alınan ekran görüntüsü.*


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->
Bu proje aşağıdaki teknolojiler kullanılarak geliştirilmiştir:
- [Django Rest Framework](https://www.django-rest-framework.org/) - Güçlü bir REST API framework'ü.


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

### Örnek Kullanım

1. **Todo Listeleme:**
   - URL: `https://umit8101.pythonanywhere.com/todo/`
   - Method: `GET`

2. **Todo Oluşturma:**
   - URL: `https://umit8101.pythonanywhere.com/todo/`
   - Method: `POST`
   - Body (JSON):

```json
  {
    "task": "study english",
    "description": "test create",
    "priority": 1
  }
```

## About This Project

This project is a Todo API implementation that aims to make it easier for users to organize their daily tasks. Users:
- Can create, view, update and delete tasks.
- Can assign priority to tasks.
- Can test the API with a user-friendly web interface or tools like Postman.

<hr>

Bu proje, kullanıcıların günlük görevlerini organize etmelerini kolaylaştırmayı hedefleyen bir Todo API uygulamasıdır. Kullanıcılar:
- Görev oluşturabilir, görüntüleyebilir, güncelleyebilir ve silebilir.
- Görevlerine öncelik atayabilir.
- Kullanıcı dostu bir web arayüzü veya Postman gibi araçlarla API'yi test edebilir.


## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/) - REST API oluşturmak için kullanılan framework.


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- **GitHub**: [@Umit8098](https://github.com/Umit8098)

- **LinkedIn**: [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
