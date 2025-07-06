<h1 align="center">🧠 Django REST Framework - Learning Repository</h1>

<p align="center">
  <em>A hands-on project to learn and implement various features of Django REST Framework (DRF) including views, serializers, filtering, pagination and more!</em>
</p>

---

## 🚀 Overview

This repository is a **learning-focused** implementation of the Django REST Framework. It demonstrates how to build REST APIs using different approaches:

- ✅ Function-Based Views (FBV)
- ✅ Class-Based Views (CBV)
- ✅ Mixins
- ✅ Generic Views
- ✅ ViewSets & ModelViewSets
- ✅ Serializers (`Serializer`, `ModelSerializer`, Nested, Custom)
- ✅ Filters & Search
- ✅ Pagination

---



## 🧪 Features Breakdown
  
| Feature                         |  Description
                                              
---------------------------------------------------
| 🔧 **FBV/CBV**                 |  Step-by-step manual control over logic using Django's views    
| 🧩 **Mixins/Generics**         | Reusable view components for rapid development                 
| 🚀 **ViewSet / ModelViewSet**  | Powerful abstraction using routers and actions                 
| 📦 **Serializers**             | Data validation, transformation, and nesting                   
| 🔍 **Filtering/Search**        | Query filtering, ordering, and full-text search                
| 📄 **Pagination**              | Page number, limit-offset, and customizable pagination classes   
-----------------------------------------------------------------


## 🔧 Setup Instructions
---
1️⃣ Clone the Repository
git clone https://github.com/Swarajsolanke/DRF.git
cd DR
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Run the Server
python manage.py migrate
python manage.py runserver

---

## 📌 Pagination Types
1.PageNumberPagination

2.LimitOffsetPagination

3.CustomPagination

----

## 🔍 Filtering & Searching

mplemented using:

1.django-filter for query param-based filtering.

2.SearchFilter for full-text search.

3.OrderingFilter to sort by fields.

----
## 🧰 Tech Stack

🐍 Python 3.10+

⚙️ Django 4.x

🧱 Django REST Framework

🔎 django-filter




## 📚 Learning Goals
This repository was created for educational purposes to:

Understand different DRF view types.

Practice building REST APIs from scratch.

Learn how pagination, filtering, and routing work.

Explore reusable DRF components.
