# 🌐 Social Media Platform

A modern **full-stack social media web application** developed as part of the **CodeAlpha Internship Program**.

This project enables users to create accounts, share posts, interact with other users, and engage through a dynamic social networking experience.

---

## 🚀 Features

### 👤 User Authentication

* User Registration
* Secure Login & Logout
* Password Encryption
* Session/JWT Authentication

### 📝 Create & Manage Posts

* Create new posts
* Edit existing posts
* Delete posts
* View all user posts

### ❤️ Social Interactions

* Like posts
* Comment on posts
* Real-time engagement tracking

### 👥 User Profiles

* Personalized user profiles
* Profile picture support
* Bio and account details
* View user activity

### 📰 News Feed

* Dynamic feed displaying recent posts
* Chronological content updates
* User-generated content display

### 🔍 Search Functionality

* Search users
* Search posts
* Discover new connections

### 💾 Database Integration

* User data storage
* Posts management
* Comments and likes persistence
* Secure authentication records

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap / Tailwind CSS

### Backend

* Node.js
* Express.js

### Database

* MongoDB

### Authentication

* JWT (JSON Web Token)
* bcrypt.js

---

## 📂 Project Structure

```text
CodeAlpha_SocialMedia/
│
├── backend/
│   ├── models/
│   │   ├── User.js
│   │   ├── Post.js
│   │   └── Comment.js
│   │
│   ├── routes/
│   │   ├── auth.js
│   │   ├── posts.js
│   │   └── users.js
│   │
│   ├── middleware/
│   └── server.js
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── feed.html
│   ├── css/
│   └── js/
│
├── .env
├── package.json
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Utkarsh01245/CodeAlpha_SocialMedia.git
cd CodeAlpha_SocialMedia
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
PORT=5000
```

### 4️⃣ Start the Application

```bash
npm start
```

or

```bash
npm run dev
```

### 5️⃣ Open in Browser

```text
http://localhost:5000
```

---

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| POST   | `/api/auth/register` | Register a new user |
| POST   | `/api/auth/login`    | Login user          |
| POST   | `/api/auth/logout`   | Logout user         |

---

### 📝 Posts

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| GET    | `/api/posts`     | Get all posts |
| POST   | `/api/posts`     | Create a post |
| PUT    | `/api/posts/:id` | Update a post |
| DELETE | `/api/posts/:id` | Delete a post |

---

### 💬 Comments

| Method | Endpoint                | Description  |
| ------ | ----------------------- | ------------ |
| POST   | `/api/comments/:postId` | Add comment  |
| GET    | `/api/comments/:postId` | Get comments |

---

### ❤️ Likes

| Method | Endpoint              | Description |
| ------ | --------------------- | ----------- |
| POST   | `/api/posts/:id/like` | Like a post |
| DELETE | `/api/posts/:id/like` | Remove like |

---

## 🔒 Security Features

* Password Hashing using bcrypt
* JWT Authentication
* Protected Routes
* Environment Variable Management
* Input Validation & Sanitization

---

## 🎯 Learning Outcomes

This project demonstrates:

* Full-Stack Web Development
* REST API Design
* User Authentication & Authorization
* Database Management
* CRUD Operations
* Social Media Architecture
* Backend Development with Node.js & Express
* MongoDB Integration

---

## 📸 Screenshots

Add screenshots of:

* Login Page
* Registration Page
* User Profile
* News Feed
* Post Creation Interface

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project was developed for educational purposes as part of the **CodeAlpha Internship Program**.

---

### ⭐ If you found this project useful, please consider giving it a star on GitHub!
