# ShopSphere - Full-Stack E-commerce Application

ShopSphere is a modern, full-stack e-commerce platform built with cutting-edge technologies, featuring an intelligent product recommendation system.

## 🚀 Features

- **Modern Frontend**: React with TypeScript, Redux for state management, Tailwind CSS for styling, and Swiper for carousels
- **Robust Backend**: Spring Boot with JWT authentication, Keycloak integration, and Spring JPA
- **Intelligent Recommendations**: Product recommendation system that suggests complementary items (e.g., phone → phone cover + data cable)
- **Caching**: Redis integration for improved performance
- **Containerized**: Docker support for easy deployment
- **Database**: MySQL for persistent data storage

## 🛠️ Technology Stack

### Frontend
- React 19 with TypeScript
- Redux Toolkit for state management
- Tailwind CSS for styling
- Swiper for carousel components
- React Router for navigation
- Axios for API calls

### Backend
- Spring Boot 3.2.0
- Spring Security with JWT
- Keycloak for identity management
- Spring Data JPA
- MySQL Database
- Redis for caching

### Infrastructure
- Docker & Docker Compose
- MySQL 8.0
- Redis 7
- Keycloak 23.0

## 📁 Project Structure

```
Ecommerce_project/
├── shopsphere-frontend/     # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── store/          # Redux store and slices
│   │   └── hooks/          # Custom hooks
│   └── package.json
│
├── shopsphere-backend/      # Spring Boot backend
│   ├── src/main/java/com/shopsphere/
│   │   ├── controller/     # REST controllers
│   │   ├── service/        # Business logic
│   │   ├── repository/     # Data access layer
│   │   ├── model/          # Entity models
│   │   └── config/         # Configuration classes
│   └── pom.xml
│
└── docker-compose.yml       # Docker orchestration
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm
- Java 17+
- Maven 3.9+
- Docker and Docker Compose (optional, for containerized setup)

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Start Infrastructure Services (Docker)**

   ```bash
   docker-compose up -d mysql redis keycloak
   ```

   This will start:
   - MySQL on port 3306
   - Redis on port 6379
   - Keycloak on port 8081

3. **Backend Setup**

   ```bash
   cd shopsphere-backend
   mvn clean install
   mvn spring-boot:run
   ```

   The backend will run on `http://localhost:8080`

4. **Frontend Setup**

   ```bash
   cd shopsphere-frontend
   npm install
   npm start
   ```

   The frontend will run on `http://localhost:3000`

### Using Docker (Full Stack)

To run everything with Docker:

```bash
docker-compose up --build
```

This will start all services including the backend and frontend.

## 🎯 Key Features

### Product Recommendation System

The recommendation system works by:

1. **Product Associations**: Products can be associated with complementary items
2. **Association Strength**: Each association has a strength value indicating relevance
3. **Smart Recommendations**: When viewing a product, related items are suggested
4. **Cart Recommendations**: Based on items in cart, additional products are recommended
5. **Category-Aware Recommendations**: For clothing, beauty, home & kitchen, and sports categories, the system intelligently suggests same-category items (e.g., t-shirt → jeans, hair treatment → shampoo)

Example: When a customer views a phone, the system automatically recommends:
- Phone covers
- Data cables
- Screen protectors
- Other complementary accessories

### Product Search

- **Full-Text Search**: Search across product names, descriptions, and categories
- **Case-Insensitive**: Search works regardless of letter case
- **Real-Time Results**: Search results update instantly
- **Error Handling**: User-friendly error messages and loading states

### Product Images

- **High-Quality Images**: All products feature high-quality images from Unsplash
- **Multiple Views**: Product detail pages show 5 different images per product
- **Optimized Loading**: Images are optimized for fast loading with proper caching

### Pricing & Discounts

- **INR Currency**: All prices displayed in Indian Rupees (₹)
- **Dynamic Discounts**: Discounts range from 5% to 50% for variety
- **Clear Pricing**: Original and discounted prices clearly displayed

### API Endpoints

#### Products
- `GET /api/products` - Get all products
- `GET /api/products/{id}` - Get product by ID
- `GET /api/products/{id}/recommendations` - Get product recommendations
- `GET /api/products/{id}/frequently-bought-together` - Get frequently bought together items
- `GET /api/products/search?q={query}` - Search products (searches name, description, and category)
- `GET /api/products/category/{category}` - Get products by category
- `GET /api/products/top-rated` - Get top-rated products

#### Cart
- `GET /api/cart/{userId}` - Get user's cart
- `POST /api/cart/{userId}/add` - Add item to cart
- `DELETE /api/cart/{userId}/remove/{productId}` - Remove item from cart
- `GET /api/cart/{userId}/recommendations` - Get cart-based recommendations

## 🔧 Configuration

### Backend Configuration

Edit `shopsphere-backend/src/main/resources/application.yml`:

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/shopsphere_db
    username: root
    password: rootpassword
  data:
    redis:
      host: localhost
      port: 6379
```

### Frontend Configuration

API URL is configured in Redux slices. Update `API_URL` in:
- `src/store/slices/productSlice.ts`
- `src/store/slices/cartSlice.ts`

## 📝 Database Schema

- **users**: User accounts and authentication
- **products**: Product catalog (67 products with updated images)
- **product_associations**: Product recommendation relationships
- **cart**: Shopping cart items
- **orders**: Order history
- **order_items**: Order line items
- **wishlist**: User wishlist items

## 📋 Recent Updates

### Product Management
- ✅ Updated all product images with high-quality Unsplash photos
- ✅ Removed products without updated images (60 products removed)
- ✅ Each product now has 5 different images on detail pages
- ✅ Product tiles display updated images on homepage and product listing pages

### Search Functionality
- ✅ Implemented full-text search across product names, descriptions, and categories
- ✅ Added search result count and query display
- ✅ Added clear search button and error handling
- ✅ Search results update in real-time with loading states

### UI/UX Improvements
- ✅ Changed currency from USD ($) to INR (₹)
- ✅ Implemented dynamic discounts (5% to 50% range)
- ✅ Enhanced product detail pages with Flipkart-style design
- ✅ Improved product recommendation logic for better relevance

### Backend Enhancements
- ✅ Enhanced search query to search across multiple fields
- ✅ Improved product recommendation algorithm
- ✅ Added proper error handling for all endpoints
- ✅ Optimized database queries for better performance

## 🧪 Testing

### Backend Tests
```bash
cd shopsphere-backend
mvn test
```

### Frontend Tests
```bash
cd shopsphere-frontend
npm test
```

## 🚢 Deployment

### Production Build

**Frontend:**
```bash
cd shopsphere-frontend
npm run build
```

**Backend:**
```bash
cd shopsphere-backend
mvn clean package
java -jar target/shopsphere-backend-1.0.0.jar
```

### Docker Production
```bash
docker-compose -f docker-compose.prod.yml up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- ShopSphere Development Team

## 🙏 Acknowledgments

- Design inspiration from Figma community templates
- Spring Boot and React communities for excellent documentation

---

**ShopSphere** - Your one-stop shopping destination! 🛒✨











