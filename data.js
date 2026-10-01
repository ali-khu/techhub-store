// data.js
const BUSINESS_WHATSAPP_NUMBER = "923393336999"; 

const phones = [
    { id: 31, name: "iPhone Duo (256GB)", brand: "Apple", price: "Rs. 750,000", priceVal: 750000, image: "Pictures/duo.jpg", specs: ["7.6\" Foldable Super Retina XDR OLED", "Apple A20 Pro Chip", "Dual 48MP Fusion Camera System", "3 Days Money Back Warranty"] },
    { id: 7, name: "iPhone 11 Pro Max (256GB)", brand: "Apple", price: "Rs. 67,000", priceVal: 67000, image: "Pictures/iphone_11_pro_max_256gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: 94%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 8, name: "iPhone 13 Pro (256GB)", brand: "Apple", price: "Rs. 112,000", priceVal: 112000, image: "Pictures/iphone_13_pro_256gb_nonpta.jpg", specs: ["NON-PTA", "Battery Health: 94%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 9, name: "iPhone 14 (128GB)", brand: "Apple", price: "Rs. 77,000", priceVal: 77000, image: "Pictures/iphone_14_128gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: 88-94%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 10, name: "iPhone 13 Pro Max (128GB)", brand: "Apple", price: "Rs. 117,000", priceVal: 117000, image: "Pictures/iphone_13_pro_max_128gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 11, name: "iPhone 13 (128GB)", brand: "Apple", price: "Rs. 67,000", priceVal: 67000, image: "Pictures/iphone_13_128gb_jv_88.jpg", specs: ["NON-PTA (JV)", "Battery Health: 88-87%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 12, name: "iPhone XS Max (64GB)", brand: "Apple", price: "Rs. 54,000", priceVal: 54000, image: "Pictures/iphone_xs_max_64gb_pta.jpg", specs: ["PTA Approved", "Battery Health: 88%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 13, name: "iPhone 16 (128GB)", brand: "Apple", price: "Rs. 137,000", priceVal: 137000, image: "Pictures/iphone_16_128gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: 90%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 14, name: "iPhone 12 Pro Max (128GB)", brand: "Apple", price: "Rs. 70,000", priceVal: 70000, image: "Pictures/iphone_12_pro_max_128gb.jpg", specs: ["PTA Approved", "Battery Health: 90%", "Condition: 7/10", "3 Days Money Back Warranty"] },
    { id: 15, name: "iPhone 13 Pro Max (128GB)", brand: "Apple", price: "Rs. 127,000", priceVal: 127000, image: "Pictures/iphone_13_pro_max_128gb_nonpta.jpg", specs: ["NON-PTA", "Battery Health: 92%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 16, name: "iPhone 11 (64GB)", brand: "Apple", price: "Rs. 39,000", priceVal: 39000, image: "Pictures/iphone_11_64gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 17, name: "iPhone 11 Pro (256GB)", brand: "Apple", price: "Rs. 54,000", priceVal: 54000, image: "Pictures/iphone_11_pro_256gb_nonpta.jpg", specs: ["NON-PTA", "Battery Health: 89%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 18, name: "iPhone 8 Plus (64GB)", brand: "Apple", price: "Rs. 27,000", priceVal: 27000, image: "Pictures/iphone_8_plus_64gb_pta.jpg", specs: ["PTA (JV)", "Battery Health: 100%", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 19, name: "iPhone SE 2nd Gen (64GB)", brand: "Apple", price: "Rs. 30,500", priceVal: 30500, image: "Pictures/iphone_se2_64gb_pta_mix.jpg", specs: ["PTA Approved", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 20, name: "iPhone XS Max (64GB)", brand: "Apple", price: "Rs. 37,500", priceVal: 37500, image: "Pictures/iphone_xs_max_64gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: 80/88/74%", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 21, name: "iPhone 13 (128GB)", brand: "Apple", price: "Rs. 65,000", priceVal: 65000, image: "Pictures/iphone_13_128gb_jv_mix.jpg", specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 22, name: "iPhone XS Max (256GB)", brand: "Apple", price: "Rs. 39,000", priceVal: 39000, image: "Pictures/iphone_xs_max_256gb.jpg", specs: ["PTA Approved", "Battery Health: 100% (Changed)", "Condition: 9/10", "3 Days Money Back Warranty"] },
    { id: 23, name: "iPhone 11 Pro Max (64GB)", brand: "Apple", price: "Rs. 58,000", priceVal: 58000, image: "Pictures/iphone_11_pro_max_64gb_jv.jpg", specs: ["NON-PTA (JV)", "Battery Health: 91%", "Condition: 10/10", "3 Days Money Back Warranty"] },
    { id: 24, name: "iPhone 17 (128GB)", brand: "Apple", price: "Rs. 245,000", priceVal: 245000, image: "Pictures/iphone_17_128gb.jpg", specs: ["Official PTA Approved", "A19 Bionic Chip", "Battery Health: 100%", "3 Days Money Back Warranty"] },
    { id: 25, name: "iPhone 17 Air (256GB)", brand: "Apple", price: "Rs. 285,000", priceVal: 285000, image: "Pictures/iphone_17_air_256gb.jpg", specs: ["Official PTA Approved", "Ultra-Slim Design", "Battery Health: 100%", "3 Days Money Back Warranty"] },
    { id: 26, name: "iPhone 17 Pro (256GB)", brand: "Apple", price: "Rs. 335,000", priceVal: 335000, image: "Pictures/iphone_17_pro_256gb.jpg", specs: ["NON-PTA (JV)", "A19 Pro Chip", "Battery Health: 100%", "3 Days Money Back Warranty"] },
    { id: 27, name: "iPhone 17 Pro Max (512GB)", brand: "Apple", price: "Rs. 410,000", priceVal: 410000, image: "Pictures/iphone_17_pro_max_512gb.jpg", specs: ["Official PTA Approved", "Triple 48MP Camera", "Battery Health: 100%", "3 Days Money Back Warranty"] },
    { id: 29, name: "iPhone 18 Pro (256GB)", brand: "Apple", price: "Rs. 495,000", priceVal: 495000, image: "Pictures/iphone_18_pro_256gb.jpg", specs: ["Pre-Order / Import", "A20 Pro Chip", "Under-Display Face ID", "3 Days Money Back Warranty"] },
    { id: 30, name: "iPhone 18 Pro Max (512GB)", brand: "Apple", price: "Rs. 675,000", priceVal: 675000, image: "Pictures/iphone_18_pro_max_512gb.jpg", specs: ["Pre-Order / Import", "A20 Pro Chip", "Variable Aperture Camera", "3 Days Money Back Warranty"] }     
];


const accessories = [
    { id: 101, name: "Apple 20W USB-C Power Adapter", brand: "Apple", price: "Rs. 5,500", image: "https://via.placeholder.com/300x300?text=Charger" },
    { id: 102, name: "AirPods Pro (2nd Gen)", brand: "Apple", price: "Rs. 65,000", image: "https://via.placeholder.com/300x300?text=AirPods" },
    { id: 103, name: "Premium Silicone Case (All Models)", brand: "Accessory", price: "Rs. 1,500", image: "https://via.placeholder.com/300x300?text=Case" },
    { id: 104, name: "9D Glass Screen Protector", brand: "Accessory", price: "Rs. 800", image: "https://via.placeholder.com/300x300?text=Protector" }
];