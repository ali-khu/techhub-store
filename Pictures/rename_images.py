<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iTradehub | Premium Smartphones</title>
    
    <!-- Local Website Icon / Favicon -->
    <link rel="icon" type="image/png" href="assets/favicon.png">

    <!-- Google Fonts & FontAwesome -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Poppins', 'sans-serif'] },
                    colors: { primary: '#3b82f6', whatsapp: '#25D366' }
                }
            }
        }
    </script>

    <style>
        html { scroll-behavior: smooth; }
        .product-card:hover { transform: translateY(-5px); }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 antialiased">

    <!-- Navigation -->
    <nav class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex-shrink-0 flex items-center cursor-pointer">
                    <i class="fa-solid fa-mobile-screen-button text-primary text-2xl mr-2"></i>
                    <span class="font-bold text-xl tracking-tight text-gray-900">iTradehub</span>
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="#home" class="text-gray-600 hover:text-primary font-medium transition">Home</a>
                    <a href="#smartphones" class="text-gray-600 hover:text-primary font-medium transition">Smartphones</a>
                    <a href="#contact" class="text-gray-600 hover:text-primary font-medium transition">Contact</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="bg-gradient-to-r from-gray-900 via-blue-950 to-indigo-950 text-white py-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center">
            <div class="md:w-1/2 mb-10 md:mb-0 text-center md:text-left">
                <h1 class="text-4xl md:text-5xl font-bold leading-tight mb-4">
                    Upgrade to the Best.<br> Experience the Future.
                </h1>
                <p class="text-lg text-gray-300 mb-8">
                    Browse our collection of premium smartphones. Find your perfect match and order instantly via WhatsApp.
                </p>
                <a href="#smartphones" class="bg-blue-600 text-white font-semibold px-6 py-3 rounded-full hover:bg-blue-500 transition shadow-lg">
                    View Phones
                </a>
            </div>
            <div class="md:w-1/2 flex justify-center">
                <img src="assets/cover.avif" alt="iTradehub Store Front" class="rounded-2xl shadow-2xl transform hover:scale-105 transition duration-500 max-h-96 w-full object-cover border border-gray-700">
            </div>
        </div>
    </section>

    <!-- Products Section -->
    <section id="smartphones" class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-900">Featured Smartphones</h2>
                <div class="h-1 w-20 bg-primary mx-auto mt-4 rounded"></div>
                <p class="text-gray-500 mt-4">Check specs, prices, condition, and chat with us to buy!</p>
            </div>

            <div id="product-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Phone cards render here -->
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact" class="bg-gray-900 text-white py-10 text-center">
        <div class="max-w-7xl mx-auto px-4">
            <h3 class="text-2xl font-bold mb-4">iTradehub Mobile Store</h3>
            <p class="text-gray-400 mb-6">Your trusted partner for the latest tech.</p>
            <p class="text-gray-500 text-sm">&copy; 2026 iTradehub. All rights reserved.</p>
        </div>
    </footer>

    <!-- JavaScript Logic -->
    <script>
        const BUSINESS_WHATSAPP_NUMBER = "923393336999"; 

        const phones = [
            {
                id: 1,
                name: "iPhone 16 Pro (256GB)",
                brand: "Apple",
                price: "Rs. 179,000",
                image: "Pictures/iphone_16_pro_256gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 90%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 2,
                name: "iPhone 7 (128GB)",
                brand: "Apple",
                price: "Rs. 16,500",
                image: "Pictures/iphone_7_128gb_pta.jpg",
                specs: ["PTA Approved", "Battery Health: 100%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 3,
                name: "iPhone SE-2 (64GB)",
                brand: "Apple",
                price: "Rs. 27,500",
                image: "Pictures/iphone_se2_64gb_pta_backbreak.jpg",
                specs: ["PTA Approved", "Back-Break", "Battery Health: 85%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 4,
                name: "iPhone XS (64GB)",
                brand: "Apple",
                price: "Rs. 32,500",
                image: "Pictures/iphone_xs_64gb_nonpta.jpg",
                specs: ["NON-PTA", "Battery Health: 83%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 5,
                name: "iPhone 12 Pro (256GB)",
                brand: "Apple",
                price: "Rs. 115,000",
                image: "Pictures/iphone_12_pro_256gb_pta.jpg",
                specs: ["PTA Approved", "Battery Health: 97%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 6,
                name: "iPhone 13 (128GB)",
                brand: "Apple",
                price: "Rs. 109,000",
                image: "Pictures/iphone_13_128gb_pta.jpg",
                specs: ["PTA Approved", "Battery Health: 87%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 7,
                name: "iPhone 11 Pro Max (256GB)",
                brand: "Apple",
                price: "Rs. 67,000",
                image: "Pictures/iphone_11_pro_max_256gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 94%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 8,
                name: "iPhone 13 Pro (256GB)",
                brand: "Apple",
                price: "Rs. 112,000",
                image: "Pictures/iphone_13_pro_256gb_nonpta.jpg",
                specs: ["NON-PTA", "Battery Health: 94%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 9,
                name: "iPhone 14 (128GB)",
                brand: "Apple",
                price: "Rs. 77,000",
                image: "Pictures/iphone_14_128gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 88-94%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 10,
                name: "iPhone 13 Pro Max (128GB)",
                brand: "Apple",
                price: "Rs. 117,000",
                image: "Pictures/iphone_13_pro_max_128gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 11,
                name: "iPhone 13 (128GB)",
                brand: "Apple",
                price: "Rs. 67,000",
                image: "Pictures/iphone_13_128gb_jv_88.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 88-87%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 12,
                name: "iPhone XS Max (64GB)",
                brand: "Apple",
                price: "Rs. 54,000",
                image: "Pictures/iphone_xs_max_64gb_pta.jpg",
                specs: ["PTA Approved", "Battery Health: 88%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 13,
                name: "iPhone 16 (128GB)",
                brand: "Apple",
                price: "Rs. 137,000",
                image: "Pictures/iphone_16_128gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 90%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 14,
                name: "iPhone 12 Pro Max (128GB)",
                brand: "Apple",
                price: "Rs. 70,000",
                image: "Pictures/iphone_12_pro_max_128gb.jpg",
                specs: ["PTA Approved", "Battery Health: 90%", "Condition: 7/10", "3 Days Money Back Warranty"]
            },
            {
                id: 15,
                name: "iPhone 13 Pro Max (128GB)",
                brand: "Apple",
                price: "Rs. 127,000",
                image: "Pictures/iphone_13_pro_max_128gb_nonpta.jpg",
                specs: ["NON-PTA", "Battery Health: 92%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 16,
                name: "iPhone 11 (64GB)",
                brand: "Apple",
                price: "Rs. 39,000",
                image: "Pictures/iphone_11_64gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 17,
                name: "iPhone 11 Pro (256GB)",
                brand: "Apple",
                price: "Rs. 54,000",
                image: "Pictures/iphone_11_pro_256gb_nonpta.jpg",
                specs: ["NON-PTA", "Battery Health: 89%", "Condition: 10/10", "3 Days Money Back Warranty"]
            },
            {
                id: 18,
                name: "iPhone 8 Plus (64GB)",
                brand: "Apple",
                price: "Rs. 27,000",
                image: "Pictures/iphone_8_plus_64gb_pta.jpg",
                specs: ["PTA (JV)", "Battery Health: 100%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 19,
                name: "iPhone SE 2nd Gen (64GB)",
                brand: "Apple",
                price: "Rs. 30,500",
                image: "Pictures/iphone_se2_64gb_pta_mix.jpg",
                specs: ["PTA Approved", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 20,
                name: "iPhone XS Max (64GB)",
                brand: "Apple",
                price: "Rs. 37,500",
                image: "Pictures/iphone_xs_max_64gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 80/88/74%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 21,
                name: "iPhone 13 (128GB)",
                brand: "Apple",
                price: "Rs. 65,000",
                image: "Pictures/iphone_13_128gb_jv_mix.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: Mix%", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 22,
                name: "iPhone XS Max (256GB)",
                brand: "Apple",
                price: "Rs. 39,000",
                image: "Pictures/iphone_xs_max_256gb.jpg",
                specs: ["PTA Approved", "Battery Health: 100% (Changed)", "Condition: 9/10", "3 Days Money Back Warranty"]
            },
            {
                id: 23,
                name: "iPhone 11 Pro Max (64GB)",
                brand: "Apple",
                price: "Rs. 58,000",
                image: "Pictures/iphone_11_pro_max_64gb_jv.jpg",
                specs: ["NON-PTA (JV)", "Battery Health: 91%", "Condition: 10/10", "3 Days Money Back Warranty"]
            }
        ];

        function orderOnWhatsApp(phoneName, phonePrice) {
            const message = `Hello iTradehub! 👋%0A%0AI am interested in purchasing the *${phoneName}* priced at *${phonePrice}*. %0A%0ACan you provide more details about availability and delivery?`;
            const whatsappUrl = `https://wa.me/${BUSINESS_WHATSAPP_NUMBER}?text=${message}`;
            window.open(whatsappUrl, '_blank');
        }

        const container = document.getElementById('product-container');

        phones.forEach(phone => {
            const specsHtml = phone.specs.map(spec => `
                <li class="flex items-start mb-2">
                    <i class="fa-solid fa-check text-green-500 mt-1 mr-2 text-sm"></i>
                    <span class="text-gray-600 text-sm">${spec}</span>
                </li>
            `).join('');

            const card = `
                <div class="bg-white rounded-2xl shadow-lg overflow-hidden transition-all duration-300 product-card flex flex-col">
                    <div class="h-64 overflow-hidden relative bg-gray-100 flex justify-center items-center">
                        <span class="absolute top-4 left-4 bg-gray-900 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide z-10">${phone.brand}</span>
                        <img src="${phone.image}" alt="${phone.name}" class="w-full h-full object-cover" onerror="this.src='https://via.placeholder.com/500x500?text=Image+Missing'">
                    </div>
                    
                    <div class="p-6 flex-grow flex flex-col">
                        <div class="flex justify-between items-start mb-4">
                            <h3 class="text-xl font-bold text-gray-900 leading-tight">${phone.name}</h3>
                            <span class="text-lg font-extrabold text-primary whitespace-nowrap ml-2">${phone.price}</span>
                        </div>
                        
                        <ul class="mb-6 flex-grow">
                            ${specsHtml}
                        </ul>
                        
                        <button 
                            onclick="orderOnWhatsApp('${phone.name}', '${phone.price}')" 
                            class="w-full bg-whatsapp hover:bg-green-600 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition-colors flex items-center justify-center space-x-2">
                            <i class="fa-brands fa-whatsapp text-xl"></i>
                            <span>Order via WhatsApp</span>
                        </button>
                    </div>
                </div>
            `;
            container.innerHTML += card;
        });
    </script>
</body>
</html>