package com.shopsphere.service;

import com.shopsphere.model.Product;
import com.shopsphere.model.ProductAssociation;
import com.shopsphere.repository.ProductAssociationRepository;
import com.shopsphere.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import java.util.stream.Collectors;

@Service
@Transactional
public class RecommendationService {
    
    @Autowired
    private ProductAssociationRepository associationRepository;
    
    @Autowired
    private ProductRepository productRepository;
    
    /**
     * Get recommended products for a given product
     * Example: If buying a phone, recommend phone cover and data cable
     */
    @Cacheable(value = "recommendations", key = "#productId")
    public List<Product> getRecommendations(Long productId) {
        List<ProductAssociation> associations = 
            associationRepository.findTopAssociationsByProductIdOrderByAssociationStrengthDesc(productId);
        
        List<Product> recommended = associations.stream()
            .map(ProductAssociation::getAssociatedProduct)
            .filter(p -> p.getStock() > 0) // Only recommend in-stock products
            .limit(8) // Limit to top 8 recommendations
            .collect(Collectors.toList());
        
        // If not enough recommendations, add products from same category
        if (recommended.size() < 4) {
            Product product = productRepository.findById(productId).orElse(null);
            if (product != null) {
                List<Product> sameCategory = productRepository.findByCategory(product.getCategory())
                    .stream()
                    .filter(p -> !p.getId().equals(productId) && p.getStock() > 0)
                    .filter(p -> recommended.stream().noneMatch(r -> r.getId().equals(p.getId())))
                    .limit(4 - recommended.size())
                    .collect(Collectors.toList());
                recommended.addAll(sameCategory);
            }
        }
        
        return recommended;
    }
    
    /**
     * Get recommendations based on cart items
     */
    public List<Product> getCartRecommendations(List<Long> productIds) {
        return productIds.stream()
            .flatMap(id -> associationRepository.findTopAssociationsByProductId(id).stream())
            .collect(Collectors.groupingBy(
                ProductAssociation::getAssociatedProduct,
                Collectors.summingDouble(pa -> pa.getAssociationStrength())
            ))
            .entrySet().stream()
            .sorted((e1, e2) -> Double.compare(e2.getValue(), e1.getValue()))
            .map(e -> e.getKey())
            .filter(p -> !productIds.contains(p.getId()) && p.getStock() > 0)
            .limit(5)
            .collect(Collectors.toList());
    }
    
    /**
     * Create or update product association
     */
    public void createAssociation(Long productId, Long associatedProductId, 
                                  ProductAssociation.AssociationType type, 
                                  Double strength) {
        Product product = productRepository.findById(productId)
            .orElseThrow(() -> new RuntimeException("Product not found"));
        Product associatedProduct = productRepository.findById(associatedProductId)
            .orElseThrow(() -> new RuntimeException("Associated product not found"));
        
        ProductAssociation association = new ProductAssociation();
        association.setProduct(product);
        association.setAssociatedProduct(associatedProduct);
        association.setType(type);
        association.setAssociationStrength(strength);
        
        associationRepository.save(association);
    }
}

