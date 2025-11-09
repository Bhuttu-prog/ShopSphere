package com.shopsphere.service;

import com.shopsphere.model.Product;
import com.shopsphere.model.ProductAssociation;
import com.shopsphere.repository.ProductRepository;
import com.shopsphere.repository.ProductAssociationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

@Component
public class DataSeederService implements CommandLineRunner {
    
    @Autowired
    private ProductRepository productRepository;
    
    @Autowired
    private ProductAssociationRepository associationRepository;
    
    @Override
    @Transactional
    public void run(String... args) {
        if (productRepository.count() == 0) {
            seedProducts();
        }
    }
    
    private void seedProducts() {
        List<Product> allProducts = new ArrayList<>();
        
        // ========== ELECTRONICS ==========
        // Smartphones
        allProducts.add(createProduct("iPhone 15 Pro", 
            "Latest iPhone with A17 Pro chip, 6.1-inch Super Retina XDR display, Pro camera system with 48MP main camera", 
            new BigDecimal("999.99"), 
            "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&h=500&fit=crop",
            "Electronics", 50, 4.8, 120));
        
        allProducts.add(createProduct("Samsung Galaxy S24 Ultra", 
            "Flagship Android smartphone with 6.8-inch Dynamic AMOLED display, 200MP camera, S Pen support", 
            new BigDecimal("1199.99"), 
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&h=500&fit=crop",
            "Electronics", 40, 4.7, 95));
        
        allProducts.add(createProduct("OnePlus 12", 
            "Premium Android phone with Snapdragon 8 Gen 3, 6.82-inch LTPO display, 50MP triple camera", 
            new BigDecimal("799.99"), 
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&h=500&fit=crop",
            "Electronics", 35, 4.6, 88));
        
        // Laptops
        allProducts.add(createProduct("MacBook Pro 16\" M3", 
            "M3 Pro chip, 16GB RAM, 512GB SSD, Liquid Retina XDR display, 22-hour battery life", 
            new BigDecimal("2499.99"), 
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=500&h=500&fit=crop",
            "Electronics", 30, 4.9, 85));
        
        allProducts.add(createProduct("Dell XPS 15", 
            "Intel i7-13700H, 16GB RAM, 1TB SSD, 15.6-inch 4K OLED touchscreen, NVIDIA RTX 4050", 
            new BigDecimal("1899.99"), 
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop",
            "Electronics", 25, 4.6, 70));
        
        allProducts.add(createProduct("HP Spectre x360", 
            "Intel i7, 16GB RAM, 512GB SSD, 13.5-inch 3K OLED touchscreen, 2-in-1 convertible", 
            new BigDecimal("1399.99"), 
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop",
            "Electronics", 20, 4.5, 65));
        
        // ========== CLOTHING ==========
        // Men's Clothing
        allProducts.add(createProduct("Classic White T-Shirt", 
            "100% cotton, comfortable fit, breathable fabric, perfect for everyday wear", 
            new BigDecimal("19.99"), 
            "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop",
            "Clothing", 150, 4.5, 200));
        
        allProducts.add(createProduct("Denim Jeans - Blue", 
            "Classic fit denim jeans, 98% cotton 2% elastane, stretch comfort, regular fit", 
            new BigDecimal("49.99"), 
            "https://images.unsplash.com/photo-1542272604-787c3835535d?w=500&h=500&fit=crop",
            "Clothing", 100, 4.4, 180));
        
        allProducts.add(createProduct("Leather Jacket", 
            "Genuine leather jacket, classic biker style, quilted lining, multiple pockets", 
            new BigDecimal("199.99"), 
            "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500&h=500&fit=crop",
            "Clothing", 40, 4.7, 95));
        
        allProducts.add(createProduct("Nike Running Shoes", 
            "Lightweight running shoes with cushioned sole, breathable mesh upper, perfect for jogging", 
            new BigDecimal("89.99"), 
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop",
            "Clothing", 80, 4.6, 150));
        
        // Women's Clothing
        allProducts.add(createProduct("Floral Summer Dress", 
            "Beautiful floral print dress, lightweight fabric, perfect for summer occasions", 
            new BigDecimal("39.99"), 
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500&h=500&fit=crop",
            "Clothing", 120, 4.5, 175));
        
        allProducts.add(createProduct("Designer Handbag", 
            "Premium leather handbag, spacious interior, multiple compartments, elegant design", 
            new BigDecimal("149.99"), 
            "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=500&h=500&fit=crop",
            "Clothing", 60, 4.8, 110));
        
        allProducts.add(createProduct("High Heel Sandals", 
            "Elegant high heel sandals, comfortable padding, perfect for parties and events", 
            new BigDecimal("59.99"), 
            "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=500&h=500&fit=crop",
            "Clothing", 90, 4.4, 140));
        
        // ========== HOME & KITCHEN ==========
        allProducts.add(createProduct("Stainless Steel Cookware Set", 
            "10-piece cookware set, non-stick coating, dishwasher safe, induction compatible", 
            new BigDecimal("129.99"), 
            "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=500&h=500&fit=crop",
            "Home & Kitchen", 45, 4.6, 125));
        
        allProducts.add(createProduct("Memory Foam Mattress", 
            "Queen size memory foam mattress, pressure-relieving, hypoallergenic, 10-year warranty", 
            new BigDecimal("499.99"), 
            "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=500&h=500&fit=crop",
            "Home & Kitchen", 25, 4.7, 88));
        
        allProducts.add(createProduct("Coffee Maker", 
            "12-cup programmable coffee maker, auto shut-off, reusable filter, glass carafe", 
            new BigDecimal("79.99"), 
            "https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?w=500&h=500&fit=crop",
            "Home & Kitchen", 70, 4.5, 160));
        
        allProducts.add(createProduct("Smart LED TV 55\"", 
            "55-inch 4K UHD Smart TV, HDR support, Android TV, voice control, multiple HDMI ports", 
            new BigDecimal("599.99"), 
            "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop",
            "Electronics", 35, 4.8, 200));
        
        // ========== ACCESSORIES ==========
        allProducts.add(createProduct("Wireless Bluetooth Earbuds", 
            "True wireless earbuds, noise cancellation, 30-hour battery, water resistant, touch controls", 
            new BigDecimal("79.99"), 
            "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&h=500&fit=crop",
            "Accessories", 200, 4.6, 300));
        
        allProducts.add(createProduct("Smart Watch", 
            "Fitness tracking smartwatch, heart rate monitor, GPS, water resistant, 7-day battery", 
            new BigDecimal("199.99"), 
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&h=500&fit=crop",
            "Accessories", 80, 4.7, 180));
        
        allProducts.add(createProduct("Phone Case - Clear", 
            "Protective clear case, shock absorption, raised edges, wireless charging compatible", 
            new BigDecimal("24.99"), 
            "https://images.unsplash.com/photo-nfWPbwWFTTs?w=500&h=500&fit=crop",
            "Accessories", 300, 4.5, 250));
        
        allProducts.add(createProduct("USB-C Fast Charging Cable", 
            "6ft braided cable, 3A fast charging, data transfer, durable design, multiple device support", 
            new BigDecimal("19.99"), 
            "https://images.unsplash.com/photo-dYocS1QjjvI?w=500&h=500&fit=crop",
            "Accessories", 500, 4.6, 400));
        
        allProducts.add(createProduct("Wireless Charging Pad", 
            "15W fast wireless charger, LED indicator, non-slip surface, compatible with all Qi devices", 
            new BigDecimal("39.99"), 
            "https://images.unsplash.com/photo-r0Do56ntkBs?w=500&h=500&fit=crop",
            "Accessories", 150, 4.7, 220));
        
        allProducts.add(createProduct("Laptop Backpack", 
            "Waterproof laptop backpack, padded compartment for 15\" laptop, USB charging port, multiple pockets", 
            new BigDecimal("79.99"), 
            "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&h=500&fit=crop",
            "Accessories", 100, 4.5, 180));
        
        allProducts.add(createProduct("Wireless Mouse", 
            "Ergonomic wireless mouse, 2.4GHz connectivity, 1600 DPI, long battery life, silent clicks", 
            new BigDecimal("29.99"), 
            "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop",
            "Accessories", 200, 4.4, 250));
        
        allProducts.add(createProduct("Mechanical Keyboard", 
            "RGB mechanical keyboard, Cherry MX switches, customizable backlighting, aluminum frame", 
            new BigDecimal("99.99"), 
            "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500&h=500&fit=crop",
            "Accessories", 80, 4.6, 190));
        
        // ========== BEAUTY & PERSONAL CARE ==========
        allProducts.add(createProduct("Skincare Set", 
            "Complete skincare routine set, cleanser, toner, moisturizer, serum, suitable for all skin types", 
            new BigDecimal("89.99"), 
            "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=500&h=500&fit=crop",
            "Beauty", 60, 4.5, 140));
        
        allProducts.add(createProduct("Perfume - Eau de Parfum", 
            "Luxury fragrance, long-lasting scent, elegant bottle, perfect for special occasions", 
            new BigDecimal("69.99"), 
            "https://images.unsplash.com/photo-1541643600914-78b084683601?w=500&h=500&fit=crop",
            "Beauty", 90, 4.6, 165));
        
        // ========== SPORTS & OUTDOORS ==========
        allProducts.add(createProduct("Yoga Mat", 
            "Premium yoga mat, non-slip surface, extra thick padding, eco-friendly material, carrying strap", 
            new BigDecimal("34.99"), 
            "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&h=500&fit=crop",
            "Sports", 120, 4.5, 180));
        
        allProducts.add(createProduct("Dumbbell Set", 
            "Adjustable dumbbell set, 5-50 lbs per dumbbell, compact design, perfect for home gym", 
            new BigDecimal("149.99"), 
            "https://images.unsplash.com/photo-dhJd3ax1pFs?w=500&h=500&fit=crop",
            "Sports", 40, 4.7, 95));
        
        // Save all products
        List<Product> savedProducts = new ArrayList<>();
        for (Product product : allProducts) {
            savedProducts.add(productRepository.save(product));
        }
        
        // Create associations - Find products by name for reliability
        Product phone1 = savedProducts.stream().filter(p -> p.getName().contains("iPhone")).findFirst().orElse(null);
        Product phone2 = savedProducts.stream().filter(p -> p.getName().contains("Samsung")).findFirst().orElse(null);
        Product phone3 = savedProducts.stream().filter(p -> p.getName().contains("OnePlus")).findFirst().orElse(null);
        
        Product case1 = savedProducts.stream().filter(p -> p.getName().contains("Phone Case")).findFirst().orElse(null);
        Product cable = savedProducts.stream().filter(p -> p.getName().contains("USB-C") || p.getName().contains("Cable")).findFirst().orElse(null);
        Product charger = savedProducts.stream().filter(p -> p.getName().contains("Wireless Charging")).findFirst().orElse(null);
        Product earbuds = savedProducts.stream().filter(p -> p.getName().contains("Earbuds")).findFirst().orElse(null);
        Product watch = savedProducts.stream().filter(p -> p.getName().contains("Smart Watch")).findFirst().orElse(null);
        
        // Phone recommendations
        if (phone1 != null) {
            if (case1 != null) createAssociation(phone1.getId(), case1.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.95);
            if (cable != null) createAssociation(phone1.getId(), cable.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
            if (charger != null) createAssociation(phone1.getId(), charger.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.85);
            if (earbuds != null) createAssociation(phone1.getId(), earbuds.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.80);
            if (watch != null) createAssociation(phone1.getId(), watch.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.75);
        }
        
        if (phone2 != null) {
            if (case1 != null) createAssociation(phone2.getId(), case1.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.95);
            if (cable != null) createAssociation(phone2.getId(), cable.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
            if (charger != null) createAssociation(phone2.getId(), charger.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.85);
            if (earbuds != null) createAssociation(phone2.getId(), earbuds.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.80);
        }
        
        if (phone3 != null) {
            if (case1 != null) createAssociation(phone3.getId(), case1.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.95);
            if (cable != null) createAssociation(phone3.getId(), cable.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
        }
        
        // Laptop accessories
        Product laptop1 = savedProducts.stream().filter(p -> p.getName().contains("MacBook")).findFirst().orElse(null);
        Product laptop2 = savedProducts.stream().filter(p -> p.getName().contains("Dell")).findFirst().orElse(null);
        Product laptop3 = savedProducts.stream().filter(p -> p.getName().contains("HP")).findFirst().orElse(null);
        
        Product backpack = savedProducts.stream().filter(p -> p.getName().contains("Backpack")).findFirst().orElse(null);
        Product mouse = savedProducts.stream().filter(p -> p.getName().contains("Mouse")).findFirst().orElse(null);
        Product keyboard = savedProducts.stream().filter(p -> p.getName().contains("Keyboard")).findFirst().orElse(null);
        
        if (laptop1 != null) {
            if (backpack != null) createAssociation(laptop1.getId(), backpack.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
            if (mouse != null) createAssociation(laptop1.getId(), mouse.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.85);
            if (keyboard != null) createAssociation(laptop1.getId(), keyboard.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.80);
        }
        
        if (laptop2 != null) {
            if (backpack != null) createAssociation(laptop2.getId(), backpack.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
            if (mouse != null) createAssociation(laptop2.getId(), mouse.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.85);
            if (keyboard != null) createAssociation(laptop2.getId(), keyboard.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.80);
        }
        
        if (laptop3 != null) {
            if (backpack != null) createAssociation(laptop3.getId(), backpack.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.90);
            if (mouse != null) createAssociation(laptop3.getId(), mouse.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.85);
        }
        
        // Clothing recommendations - similar items
        Product tshirt = savedProducts.stream().filter(p -> p.getName().contains("T-Shirt")).findFirst().orElse(null);
        Product jeans = savedProducts.stream().filter(p -> p.getName().contains("Jeans")).findFirst().orElse(null);
        Product jacket = savedProducts.stream().filter(p -> p.getName().contains("Jacket")).findFirst().orElse(null);
        Product shoes = savedProducts.stream().filter(p -> p.getName().contains("Shoes")).findFirst().orElse(null);
        
        if (tshirt != null && jeans != null) {
            createAssociation(tshirt.getId(), jeans.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.75);
        }
        if (jeans != null && shoes != null) {
            createAssociation(jeans.getId(), shoes.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.70);
        }
        if (jacket != null && tshirt != null) {
            createAssociation(jacket.getId(), tshirt.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.65);
        }
        
        // Home & Kitchen - complementary items
        Product cookware = savedProducts.stream().filter(p -> p.getName().contains("Cookware")).findFirst().orElse(null);
        Product coffeeMaker = savedProducts.stream().filter(p -> p.getName().contains("Coffee")).findFirst().orElse(null);
        
        if (cookware != null && coffeeMaker != null) {
            createAssociation(cookware.getId(), coffeeMaker.getId(), 
                ProductAssociation.AssociationType.COMPLEMENTARY, 0.60);
        }
    }
    
    private Product createProduct(String name, String description, 
                                 BigDecimal price, String imageUrl, 
                                 String category, Integer stock, 
                                 Double rating, Integer reviewCount) {
        Product product = new Product();
        product.setName(name);
        product.setDescription(description);
        product.setPrice(price);
        product.setImageUrl(imageUrl);
        product.setCategory(category);
        product.setStock(stock);
        product.setRating(rating);
        product.setReviewCount(reviewCount);
        return product;
    }
    
    private void createAssociation(Long productId, Long associatedProductId, 
                                  ProductAssociation.AssociationType type, 
                                  Double strength) {
        Product product = productRepository.findById(productId).orElse(null);
        Product associatedProduct = productRepository.findById(associatedProductId).orElse(null);
        
        if (product != null && associatedProduct != null) {
            ProductAssociation association = new ProductAssociation();
            association.setProduct(product);
            association.setAssociatedProduct(associatedProduct);
            association.setType(type);
            association.setAssociationStrength(strength);
            associationRepository.save(association);
        }
    }
}
