# 🏍️ Misha's Bikes - Premium Motorbike Rental Website

> **WOW Hero Section** with dynamic backgrounds optimized for iPad and all devices

## ✨ Features

### 🎯 **Hero Section**
- **Dynamic wallpaper backgrounds** from `images/wp/` folder
- **iPad-optimized** for both portrait and landscape
- **Modern animations** with word reveals and parallax effects
- **Mobile typing animations** at human reading speed
- **Conversion-optimized** design with CTAs

### 📱 **Responsive Design**
- **iPad Pro support** with specific optimizations
- **Mobile-first** approach with 2025 best practices
- **Dynamic viewport height** (`100dvh`) for mobile
- **Touch-friendly** buttons (48px minimum)

### 🚀 **Integrated Categories**
Instead of separate sections, all bike category info is integrated into the rental section:

- **Light Scooters** - Honda Click, Scoopy, Yamaha Fino
- **Sport Scooters** - Yamaha NMAX, Aerox, GPX Drone  
- **Big Bikes** - Yamaha XSR, Honda CB300R

Each category shows:
- Description and use cases
- Technical specs (cc, transmission)
- Model examples
- Horizontal bike slider

### 🔐 **Admin Panel**
Full bike management system with real-time updates.

**Access:** Add `#admin` to URL  
**Login:** `admin`  
**Password:** `misha2025`

**Features:**
- Enable/disable bikes
- Set rental/sale status
- Update prices (daily/monthly/sale)
- Export/import configuration
- Real-time preview

### 🖼️ **Image Structure**
```
images/
├── 1.jpg - 23.jpg     # Bike photos (by ID)
├── wp/                # Hero wallpapers
│   ├── wp1.jpeg       # Primary background
│   └── wp2.jpeg       # Secondary background
├── category1-3.jpg    # Category images
└── hero-koh-phangan.jpg
```

## 🚀 Quick Start

1. **Clone & Open**
   ```bash
   git clone [your-repo-url]
   cd "08-06 Mishas Bike"
   open index.html
   ```

2. **Admin Access**
   - Go to `yoursite.com#admin`
   - Login: `admin` / `misha2025`
   - Manage bikes, prices, availability

3. **Deploy**
   - Upload to any web server
   - Works as static site
   - No backend required

## 📸 Image Optimization

Hero backgrounds are optimized:
- **wp1.jpeg**: 1280x959, 228KB ✅
- **wp2.jpeg**: 1280x854, 148KB ✅

Perfect for fast loading on iPad and mobile!

## 🎨 Design Highlights

- **Orbitron font** for futuristic headings
- **Gradient overlays** for better text readability
- **Smooth animations** with proper timing
- **WhatsApp integration** for instant bookings
- **5-star rating display** for social proof

## 📱 Mobile Optimization

Following 2025 best practices:
- Dynamic viewport units (`dvh`)
- Proper touch targets (48px+)
- Optimized animations
- Performance-focused rendering
- Accessibility compliance

## 🔧 Configuration

Bikes are configured in `bikes-config.js`:
```javascript
{
  "id": 1,              // Links to images/1.jpg
  "number": "08761",    // Display number
  "model": "Yamaha Fino Red",
  "price_day": 250,
  "price_month": 5000,
  "for_rent": true,
  "active": true
}
```

## 🌟 Technologies

- **Vanilla JavaScript** - No frameworks needed
- **Tailwind CSS** - Utility-first styling
- **Font Awesome** - Icon library
- **Google Fonts** - Typography
- **LocalStorage** - Admin data persistence

## 📞 Contact Integration

- **WhatsApp**: Automatic message generation
- **Phone**: Click-to-call functionality
- **Location**: Koh Phangan, Thailand
- **Social**: Instagram, Telegram links

---

**Made with ❤️ for Misha's bike rental business in Koh Phangan**

*Ready to explore paradise on two wheels!* 🏍️🏝️