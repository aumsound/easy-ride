# 🏍️ Misha's Bikes - Setup Instructions

## 📁 File Structure
```
/
├── index.html          (main website)
├── bikes-config.js     (bikes configuration)
└── images/            (bike photos folder)
    ├── 1.jpg          (Click bike #1)
    ├── 2.jpg          (Click bike #2)
    ├── ...
    ├── 11.jpg         (NMAX bike #11)
    ├── ...
    └── 23.jpg         (XMAX bike #23)
```

## 🚀 Quick Start

### 1. **Deploy Files**
- Upload `index.html` and `bikes-config.js` to your server/GitHub
- Create `images/` folder

### 2. **Add Bike Photos**
Name photos by bike number: `1.jpg`, `2.jpg`, etc.

**Photo Requirements:**
- Size: 800x600px recommended
- Format: JPG
- Quality: 85% compression
- File size: ~100-200KB each

### 3. **Admin Access**
- Go to: `yoursite.com#admin` or `yoursite.com/admin`
- Username: `admin`
- Password: `misha2025`

## 📸 Image Optimization

### Option 1: Online Tools (Easiest)
1. Go to [tinypng.com](https://tinypng.com)
2. Upload all photos
3. Download optimized versions

### Option 2: Command Line (Mac/Linux)
```bash
# Install ImageMagick
brew install imagemagick  # Mac
apt-get install imagemagick  # Linux

# Optimize all images
for f in *.jpg; do 
  convert "$f" -resize 800x600 -quality 85 "$f"
done
```

### Option 3: Python Script
```python
from PIL import Image
import os

for filename in os.listdir('images'):
    if filename.endswith('.jpg'):
        img = Image.open(f'images/{filename}')
        img.thumbnail((800, 600))
        img.save(f'images/{filename}', quality=85, optimize=True)
        print(f'Optimized {filename}')
```

## 🎨 Admin Panel Features

### Bike Management
- **Active**: Show/hide bike on website
- **For Rent**: Show in rental section
- **For Sale**: Show in sale section
- **Prices**: Daily, monthly, sale prices
- **Details**: Year, mileage

### Config Management
- **Save Changes**: Saves to browser localStorage
- **Export Config**: Downloads `bikes-config.js`
- **Import Config**: Upload modified config file

## 🔧 Configuration

### Editing Directly in bikes-config.js
```javascript
{
  "id": 1,              // Unique ID
  "number": "1",        // Bike number (matches image: 1.jpg)
  "price_day": 250,     // Daily rental price
  "price_month": 5000,  // Monthly rental price
  "sale_price": 45000,  // Sale price
  "year": 2023,         // Manufacturing year
  "mileage": 5000,      // Kilometers
  "for_rent": true,     // Available for rent
  "for_sale": false,    // Available for sale
  "active": true        // Show on website
}
```

### Bike Categories
- **click**: Honda Click bikes (IDs 1-10)
- **nmax**: Yamaha NMAX bikes (IDs 11-20)
- **xmax**: Yamaha XMAX bikes (IDs 21-23)

## 📱 WhatsApp Integration

Current number: `+7 917 555 6789`

To change:
1. Open `index.html`
2. Find & replace: `79175556789`
3. Replace with new number (no spaces or symbols)

## 🌐 Deployment Options

### GitHub Pages (Free)
1. Create GitHub repository
2. Upload all files
3. Enable Pages in Settings
4. Access at: `username.github.io/repo-name`

### Vercel (Free)
1. Connect GitHub repo
2. Deploy automatically
3. Custom domain available

### Railway
1. Push to GitHub
2. Connect Railway to repo
3. Auto-deploy on push

## ⚠️ Important Notes

1. **Browser Storage**: Admin changes save to browser localStorage
   - Data persists on same device/browser
   - Clear cache = reset to bikes-config.js
   - Always export config for backup!

2. **Images**: Currently using placeholder images
   - Replace with real bike photos
   - Keep consistent naming: 1.jpg, 2.jpg, etc.

3. **Mobile First**: Site optimized for mobile devices
   - Test on phone before launch
   - WhatsApp links work best on mobile

## 🆘 Troubleshooting

**Admin panel not working?**
- Check URL: Must include `#admin`
- Clear browser cache
- Check console for errors

**Images not showing?**
- Verify file names match bike numbers
- Check images folder path
- Ensure .jpg extension (lowercase)

**Config not saving?**
- Browser localStorage might be disabled
- Try different browser
- Export/import config file instead

## 📞 Support

For issues with the site, contact the developer with:
- Browser type and version
- Screenshot of error
- Steps to reproduce issue

---

**Ready to launch!** 🚀 Just add photos and update WhatsApp number.